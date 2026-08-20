import json,glob,re,statistics as st
import numpy as np
base='/home/user/nischen-methodik/quiet_physics_analysis/tmp'
sd={x['video_id']:x for x in json.load(open(f'{base}/sample_meta.json'))}
CTA=re.compile(r'\b(subscribe|subscribing|like this video|hit the (bell|like)|leave a comment|comment below|share this video|spotify|patreon|link in the description|links? in the description|support the channel|helps the channel)\b',re.I)
SLEEP=re.compile(r'\b(fall asleep|falling asleep|drift off|drifting off|sleep well|good ?night|close your eyes|as you sleep|while you sleep|tonight|bedtime|rest well|sweet dreams|doze off|lull)\b',re.I)
out={}
for p in sorted(glob.glob(f'{base}/transcripts/*.json')):
    d=json.load(open(p)); vid=d['videoId']
    if vid not in sd: continue
    segs=sorted([(int(s['startMs'])/1000,int(s['endMs'])/1000,s['text'].strip()) for s in d['transcript']],key=lambda x:x[0])
    # rebuild word stream with timestamps (de-overlap rolling captions)
    stream=[]
    for a,b,t in segs:
        tw=t.split()
        if not stream: stream.extend((a,w) for w in tw); continue
        acc=[w for _,w in stream]; mx=0
        for k in range(min(len(tw),12),0,-1):
            if acc[-k:]==tw[:k]: mx=k; break
        stream.extend((a,w) for w in tw[mx:])
    text=' '.join(w for _,w in stream)
    times=[a for a,_ in stream]
    dur=sd[vid]['duration_s']
    # sentence split with timestamps
    sents=[];cur=[];curT=times[0] if times else 0
    for (t,w) in stream:
        if not cur: curT=t
        cur.append(w)
        if re.search(r'[.!?]$',w):
            sents.append((curT,' '.join(cur))); cur=[]
    if cur: sents.append((curT,' '.join(cur)))
    # CTA hits with timestamps
    ctas=[(round(t,1),s[:200]) for t,s in sents if CTA.search(s)]
    sleeps=[(round(t,1),s[:160]) for t,s in sents if SLEEP.search(s)]
    # opening
    first5=[s for _,s in sents[:5]]
    # repetition: repeated 6-grams
    ws=[w.lower().strip('.,!?;:"“”') for _,w in stream]
    from collections import Counter
    g6=Counter(tuple(ws[i:i+6]) for i in range(len(ws)-6))
    rep6=[(' '.join(k),v) for k,v in g6.most_common(12) if v>2]
    g10=Counter(tuple(ws[i:i+10]) for i in range(len(ws)-10))
    rep10=[(' '.join(k),v) for k,v in g10.most_common(6) if v>1]
    # question timeline
    qt=[round(t,1) for t,s in sents if s.strip().endswith('?')]
    qgaps=list(np.diff(qt)) if len(qt)>2 else []
    # section/reset markers
    RESET=re.compile(r'^(but|and yet|now|so|here|there|imagine|picture|consider|think|notice|to see|to understand|the answer|this is|that is|what|why|how|if )',re.I)
    resets=sum(1 for _,s in sents if RESET.match(s))
    # you-address density
    you=len(re.findall(r'\byou\b|\byour\b',text,re.I))
    we=len(re.findall(r'\bwe\b|\bour\b|\bus\b',text,re.I))
    I=len(re.findall(r'\bI\b|\bmy\b|\bme\b',text))
    # metaphor / analogy markers
    analog=len(re.findall(r'\blike a\b|\blike the\b|\bas if\b|\bimagine\b|\bpicture\b|\bthink of it as\b|\banalogy\b|\bcompare[ds]? to\b',text,re.I))
    # numbers/jargon density
    jarg=len(re.findall(r'\b(quantum|photon|electron|proton|neutron|quark|boson|relativity|entangle\w*|wavefunction|field|spacetime|space-?time|momentum|amplitude|entropy|singularity|eigen\w*|lagrangian|symmetry|gauge|fermion|lepton|neutrino|hadron|plasma|redshift|parsec|luminosity)\b',text,re.I))
    out[vid]=dict(channel=sd[vid]['channel'],classification=sd[vid]['classification'],title=sd[vid]['title'],
      duration_s=dur,n_words=len(stream),
      first_5_sentences=first5,
      cta_count=len(ctas),cta_hits=ctas[:6],
      first_cta_s=ctas[0][0] if ctas else None, last_cta_s=ctas[-1][0] if ctas else None,
      sleep_mention_count=len(sleeps),sleep_hits=sleeps[:4],
      n_questions=len(qt), question_median_gap_s=round(float(np.median(qgaps)),1) if qgaps else None,
      questions_first_10min=sum(1 for t in qt if t<600), questions_per_hour=round(len(qt)/(dur/3600),1),
      attention_reset_sentences=resets, reset_pct=round(100*resets/max(1,len(sents)),1),
      you_count=you,we_count=we,I_count=I,
      you_per_1000w=round(1000*you/max(1,len(stream)),1),
      analogy_markers=analog, analogy_per_hour=round(analog/(dur/3600),1),
      jargon_terms=jarg, jargon_per_1000w=round(1000*jarg/max(1,len(stream)),1),
      repeated_6grams=rep6[:8], repeated_10grams=rep10[:4])
json.dump(out,open(f'{base}/script_structure.json','w'),indent=1)
order=['Sleep On Physics','Calm Science','Calm Space','Sleepy Science Channel','Cosmo Explains']
print(f"{'channel':22} {'vid':13} {'CTA':>4} {'1stCTA':>8} {'lastCTA':>8} {'sleep':>6} {'Q/h':>5} {'Qgap':>6} {'you/1k':>7} {'anlg/h':>7} {'jarg/1k':>8} {'reset%':>7}")
for v,r in sorted(out.items(),key=lambda kv:(order.index(kv[1]['channel']),kv[1]['classification'])):
    print(f"{r['channel'][:22]:22} {v:13} {r['cta_count']:4} {str(r['first_cta_s']):>8} {str(r['last_cta_s']):>8} {r['sleep_mention_count']:6} {r['questions_per_hour']:5.1f} {str(r['question_median_gap_s']):>6} {r['you_per_1000w']:7.1f} {r['analogy_per_hour']:7.1f} {r['jargon_per_1000w']:8.1f} {r['reset_pct']:7.1f}")
