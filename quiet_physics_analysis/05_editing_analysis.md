# 05 — Editing, Intro, Script Structure and Automation Analysis

Covers brief steps 10, 11, 14, 15, 16, 17, 18.

---

## 1. Intro analysis (Step 10)

### 1.1 Intro-pattern comparison table

| | Sleep On Physics | Calm Science | Calm Space | Sleepy Science | Cosmo Explains |
|---|---|---|---|---|---|
| **Narration starts** | **0.0–0.3 s** | 0.3–0.5 s | 0.6 s | 0.5–0.6 s | 0.1–0.2 s |
| **Logo / branded intro** | **None** | **None** | **None** | None (verbal greeting instead) | **None** |
| **Music before narration** | **No** — first `[Music]` tag 4.6–140 s | No — first tag 158–375 s | No — first tag 133–458 s | Yes, from 0.6 s | No music at all |
| **Opening formula** | "Tonight, we're going to…" (2/4) or cold image cascade (2/4) | **"Tonight, we're going to…" (4/4)** | **"Tonight, we're going to explore…" (3/3)** | **"Hello there and welcome to the Sleepy Science Channel."** then "Tonight we are exploring…" | "So, here's something…" / direct second-person scene-setting |
| **Hook type** | Escalating concrete-image cascade → paradox → question | Familiar-object promise → "and we have almost no idea what it actually is" | Journey/scale promise | Greeting → comfort framing → topic | Conversational surprise opener |
| **"Sleep" said explicitly** | **Never** (only "Tonight") | **Never** (only "Tonight") | Rare | **Yes, in sentence 3** | Yes, "as you settle in tonight" |
| **Video length mentioned** | No | No | No | No | No |
| **First CTA** | **59.3 / 59.4 / 61.6 / 62.9 s** | **55.3 / 64.4 / 64.6 / 75.0 s** | **47.1 / 66.0 / 66.6 s** | 66.6 / 81.1 / 87.2 s | **None, ever** |
| **CTA count per video** | 1–3 | 1 | 1–2 | 1–2 | **0** |
| **Second CTA** | Last ~2 min (2 of 4 videos) | None | Last ~2 min (1 of 3) | Last ~2 min (2 of 3) | — |
| **Subscribe overlay graphic** | **Yes, ~1:05** (only on-screen text in the whole video) | Not observed | Not observed | Not observed | — |
| **Visual density, first 60 s** | ≥7 changes/min (detector saturated); Gemini measured **7.5 s/asset** on `tvB659d_oik`, **6.4 s/asset** on `_nLpB_Ao7zw` | ≥7 changes/min (saturated) | ≥6.7 changes/min (saturated) | 2–4 changes/min | 4–5 changes/min |
| **Intro visual sources** | **Real stock video of people, hands, labs, cities, interiors** + CGI | Space stills + abstract CGI meshes | Space stills + spacecraft/warp CGI | Same as body (AI stills) | Same as body (fixed room) |
| **Opens on black?** | No — opens on picture | **Yes** | **Yes** | No | No |
| **Intro cut style** | **Hard cuts** (Gemini: "24 cuts" in 3 min) | Crossfade | Crossfade | Crossfade | Crossfade |

### 1.2 Verbatim first sentences (the evidence)

**Sleep On Physics**
> *"A candle flame in your kitchen produces light. A distant quasar burning at the edge of the observable universe produces light. A gamma-ray burst from a collapsing star unleashing more energy in seconds than the sun will release in its entire lifetime produces light."* — `tvB659d_oik`, 158k views. Resolves at 0:59 into *"And the question is why?"*
> *"Tonight, we're going to explore something you interact with every single day, but almost certainly misunderstand at a fundamental level. Electricity. You flip a switch, and light fills the room."* — `BLPBP5BaU-0`, 79.8k views
> *"Tonight, we're going to confront a question that sounds almost childishly simple, but has haunted physicists for over a century. What is a photon actually made of?"* — `_nLpB_Ao7zw`, 227k views

**Calm Science** (4 of 4 identical grammar)
> *"Tonight, we're going to answer one of the most fundamental questions in all of physics. Where does energy come from?"*
> *"Tonight, we're going to shrink down to a scale so small that your mind is not built to hold it."*
> *"Tonight we're going to talk about something you interact with every single second of your life… And we have almost no idea what it actually is."*

**Sleepy Science Channel**
> *"Hello there and welcome to the Sleepy Science Channel. I'm so glad you found your way here. Maybe you had a long day or maybe you're the kind of person who likes falling asleep to deep thoughts and cosmic mysteries rather than counting sheep."*

**Cosmo Explains** (weakest performer)
> *"So, here's something that might surprise you."*
> *"So, here's something worth thinking about as you settle in tonight."*

### 1.3 Verbatim CTAs (near-identical within each channel — these are templates)

- **Sleep On Physics @ ~60 s:** *"Before we go any further, if you find this kind of deep exploration fascinating, a quick like or subscribe really helps the channel grow. It's a small thing for you, but it makes a huge difference for me. Also, we're now live on Spotify. The link's in the description if you'd like to listen to us wherever you are. Now, let's begin."*
- **Sleep On Physics @ end:** *"If you found this exploration valuable, a like or subscribe helps me keep making these deep journeys into physics."*
- **Calm Science @ ~60 s (verbatim in all 4):** *"Before we begin, if you enjoy these topics as much as we do, make sure to like the video or subscribe."*
- **Calm Space @ ~60 s (verbatim in all 3):** *"Before we get started, if you love exploring the depths of space as much as we do, take a second to like the video or subscribe."*
- **Sleepy Science @ ~70–87 s:** *"If you enjoy these gentle journeys, I invite you to like, subscribe, or share a thought below."*

### 1.4 Direct answers to the four questions you asked

**How quickly should narration start?**
**Within 1 second. Target 0.0–0.5 s.** Measured across 17/17 videos with zero exceptions (range 0.0–0.6 s). No dead air, no music-only runway. Confidence: **HIGH**.

**Should we have ANY logo intro?**
**No. None. Zero of 17 videos has a logo animation or branded sting.** The only channel that does any branding does it *verbally* ("welcome to the Sleepy Science Channel"), costing zero production. Confidence: **HIGH**.

**Should there be an opening hook?**
**Yes, and it should run ~55–60 seconds before you interrupt it.** Every channel except Cosmo Explains constructs a self-contained hook that lands its central question just before the 60-second mark, then breaks for the CTA. Two hook shapes both produce breakouts:
- *Concrete-image cascade* — three escalating real-world instances of the phenomenon, then the paradox, then "why?" (`tvB659d_oik`, 158k)
- *"Tonight, we're going to…" + familiar object + "and we have almost no idea what it is"* (`_nLpB_Ao7zw` 227k, `Nq-wJpo8Hk4` 91k, `BLPBP5BaU-0` 79.8k)

With n=4 breakouts I **cannot** say which is better. Both clear the bar. Confidence that a hook is needed: **HIGH**. Confidence about which shape: **LOW**.

**Should there be a CTA, and where?**
**Yes: exactly one, at 55–65 seconds, spoken, ~15–20 seconds long. Optionally one more in the final two minutes.**
The evidence is unusually tight — 13 of 14 CTA-using videos place the first CTA between **47 and 87 seconds**, median **65 s**, and the four Sleep On Physics videos land within a **3.6-second window** (59.3–62.9 s). The one channel with **no CTA at all** (Cosmo Explains) has the **lowest views/video and lowest like rate** in the sample. Confidence that the convention is real: **HIGH**. Confidence that the CTA causes the performance gap: **LOW** (Cosmo differs on many axes at once).

**Design implication:** the CTA is not an interruption bolted on — it is the *seam* between the expensive hand-cut intro and the cheap templated body. Sleep On Physics literally cuts to a static starfield with a subscribe graphic for ~20 s, then begins the template. Use that seam the same way.

---

## 2. Script and narrative structure (Step 11)

### 2.1 Measured script metrics

| Metric | Sleep On Physics | Calm Science | Calm Space | Sleepy Science | Cosmo Explains |
|---|---|---|---|---|---|
| Total words | 17,623 | 15,985 | 15,883 | 17,728 | 16,860 |
| Words per minute | 143.4 | 120.3 | 118.7 | 125.0 | 130.1 |
| Sentences per video | ~1,264 | ~1,239 | ~1,291 | ~1,252 | ~1,180 |
| **Mean sentence length** | **14.1 w** | **13.0 w** | 12.4 w | 14.1 w | 14.3 w |
| Median sentence length | 13.0 w | 11.5 w | 12.0 w | 13.0 w | 12.0 w |
| p90 sentence length | 21–27 w | 22–25 w | 19–26 w | 21–23 w | 25–28 w |
| **Flesch reading ease** | 52.2 | 52.5 | 52.2 | 54.1 | 55.9 |
| **Flesch–Kincaid grade** | **9.4** | 9.1 | 9.0 | 9.2 | 9.0 |
| Type–token ratio | 0.117–0.142 | 0.135–0.152 | 0.156–0.170 | 0.124–0.169 | 0.160–0.192 |
| **Questions per hour** | **11.8** | 8.3 | 8.5 | **0.3** | 10.5 |
| Analogy markers / hour | **17.9** | 7.9 | 7.2 | 13.7 | 10.4 |
| **Jargon terms / 1,000 w** | **26.3** | **21.3** | 3.4 | 2.4 | 5.2 |
| Attention-reset sentence openers | 14.6–21.3 % | 9.9–14.0 % | 8.6–11.0 % | 7.5–11.2 % | 13.2–18.9 % |
| "you/your" per 1,000 w | 8.6 | 7.6 | 6.5 | 12.6 | 12.9 |

**The whole category writes at US grade 9.0–9.4.** That is a five-channel band 0.4 grades wide across 280,000 words. It is the tightest convention in this entire analysis. Confidence: **HIGH**.

**Sleep On Physics is 5–11× more technical than the space channels** (26.3 jargon terms/1,000 w vs 2.4–3.4) while keeping the same reading grade. It achieves this by defining terms in plain language rather than by avoiding them. **That is the physics-specific differentiator and it is directly relevant to you.**

### 2.2 The actual narrative pattern

The brief proposed: *Question → Context → Simple explanation → Deeper explanation → Analogy → Cosmic implication → New question.*

**Measured, this is close but not quite right.** What the transcripts show on the two priority channels is a **spiral**, not a chain:

1. **Concrete anchor** — a familiar object or scene (a candle, a light switch, your hands)
2. **The paradox** — state plainly why the familiar thing is impossible/strange
3. **The question**, said explicitly ("And the question is why?")
4. *[CTA break at ~60 s]*
5. **Historical or experimental context** — who found this, what they measured
6. **Simple mechanism** — the textbook answer
7. **Undermine the simple mechanism** — "but that isn't quite what happens"
8. **Deeper mechanism** — the field-theoretic / quantum account
9. **Analogy**, then immediately the analogy's limits
10. **Restate the core claim in new words** ← *this is the load-bearing move*
11. **Escalate scale** — from the lab to the cosmos
12. **New question**, which re-enters at step 5

**Step 10 is what makes these scripts work for sleep.** Measured repeated 6-grams show the central claim restated **4–12 times per video** in varied phrasing:
- `LxDfEBostXk`: "the speed of light is not" × **12**
- `YBNfHLlrJkg`: "the neutrino is its own antiparticle" × **10**, "why the universe is made of matter" × 8
- `tvB659d_oik`: "the speed of light in vacuum" × 9, "is the same for every observer" × 7
- `_nLpB_Ao7zw`: "at exactly the speed of light" × 9, "a quantum excitation of the electromagnetic field" × 6

A listener drifting in and out re-enters the argument every few minutes without being lost. **This is deliberate and it is the core script craft of the category.**

**But it has a measured failure mode.** Top comment on `BLPBP5BaU-0`: *"great content but after hearing the same thing three times I couldn't take it any more bummer it's really interesting."* The line between "reassuring spiral" and "you already said this" is real. Target the observed band — **4–10 restatements per 2-hour video, always in new words, never verbatim.**

### 2.3 Linear, episodic, chapter-based, circular, or progressively deeper?

**Progressively deeper + circular. Not chapter-based, not episodic.** Evidence:
- **0 chapter markers in 17/17 videos.** No channel segments its content for the viewer.
- Question cadence is irregular, not periodic — median inter-question gaps range from 7.6 s to 550 s within the same channel, so questions are not being used as section dividers.
- The same phrases recur across the entire runtime rather than being confined to sections, which is the signature of a spiral, not a chapter list.
- **Exception: Sleepy Science Channel is genuinely episodic** — its "100 Facts" format is a list, with **0.0–0.5 questions/hour** (essentially none) because a fact list does not ask questions. This is a fundamentally different and equally profitable format.

### 2.4 How often does the narrative reset attention?
Measured by counting sentences opening with a reset word (*But, And yet, Now, So, Imagine, Picture, Consider, Notice, What, Why, How, If…*):

- Sleep On Physics: **14.6–21.3 %** of all sentences — at ~9.5 sentences/min that is a **reset every 30–45 seconds**
- Calm Science: 9.9–14.0 % — a reset every **45–70 seconds**
- Calm Space: 8.6–11.0 %
- Sleepy Science: 7.5–11.2 %
- Cosmo Explains: 13.2–18.9 %

**Sleep On Physics resets attention roughly twice as often as the space channels.** Combined with its 11.8 questions/hour and 17.9 analogies/hour, it is the most actively engaging script in the sample — which is the correct trade for a *physics* channel where comprehension is the product.

---

## 3. Editing intensity over time (Step 14)

> **Hypothesis tested: "The first 5–15 minutes are visually richer, while the rest of the video becomes simpler and slower."**
> **Verdict: CONFIRMED for the three strongest still-image channels. Quantified below. Confidence: HIGH.**

### Visual changes per minute, by segment

| Channel | 0–10 min | 10–30 | 30–60 | 60–90 | 90–120 | **Change, first 10 min → 30–120 min** |
|---|---|---|---|---|---|---|
| **Sleep On Physics** | **5.55** | 3.12 | 3.11 | 3.08 | 3.09 | **−44.3 %** |
| **Calm Science** | **4.08** | 2.94 | 2.69 | 2.38 | 2.59 | **−37.4 %** |
| **Calm Space** | **4.53** | 2.78 | 2.74 | 2.67 | 2.77 | **−39.9 %** |
| Sleepy Science | 3.30 | 3.22 | 3.39 | 3.38 | 2.28 | −8.6 % |
| **Cosmo Explains** | 3.17 | 3.35 | 3.43 | 3.44 | 3.43 | **+8.3 %** |

### The drop is a cliff, not a slope — it happens by minute 10 and never recovers

Fine-grained opening measurement (changes/min):

| Channel | 0–60 s | 60–120 s | 120–180 s | 180–300 s | 300–600 s | 600–1200 s |
|---|---|---|---|---|---|---|
| **Sleep On Physics** | **≥7.0** | 5.75 | 6.00 | 5.75 | 5.05 | 3.28 |
| **Calm Science** | **≥7.0** | 5.00 | 3.75 | 3.62 | 3.55 | 3.20 |
| **Calm Space** | **≥6.7** | 5.00 | 4.33 | 4.33 | 4.13 | 2.80 |
| Sleepy Science | 3.00 | 3.67 | 3.67 | 3.50 | 3.13 | 3.13 |
| Cosmo Explains | 4.33 | 3.33 | 2.67 | 3.00 | 3.07 | 3.43 |

*(0–60 s values are detector-saturated lower bounds. Gemini's direct shot lists put Sleep On Physics' true opening rate at 6.4–7.5 s/asset ≈ 8–9 changes/min.)*

Sleep On Physics holds ~6 changes/min all the way to **minute 5**, then steps down to ~3.3 by minute 10 and stays there for 110 minutes. Calm Science and Calm Space step down faster — by minute 2–3.

### Other complexity dimensions by segment

| Channel | Brightness 0–10 → 90–120 | Edge density 0–10 → 90–120 |
|---|---|---|
| Sleep On Physics | 52.8 → 41.0 (**−22 %**, all of it by minute 10) | 0.086 → 0.086 (flat) |
| Calm Science | 32.5 → 34.6 (flat) | 0.075 → 0.077 (flat) |
| Calm Space | 31.2 → 32.8 (flat) | 0.071 → 0.072 (flat) |
| **Sleepy Science** | 29.2 → **18.7** (**−36 %, monotonic**) | 0.026 → **0.004** (**−85 %**) |
| Cosmo Explains | 37.9 → 37.8 (flat) | 0.106 → 0.107 (flat) |

### What this means for your production budget

**Yes — production effort can and should be concentrated in the first 10 minutes.** The measured shape of a competitive 120-minute episode is:

| Segment | Share of runtime | Share of visual assets | Production character |
|---|---|---|---|
| **0–3 min** | 2.5 % | **~7 %** | **Hand-cut.** Hard cuts, stock footage, ~6–8 s per asset, brighter, no music |
| 3–10 min | 5.8 % | ~10 % | Template, but denser (~5 changes/min) |
| **10–120 min** | **91.7 %** | **~83 %** | **Pure template.** ~3 changes/min, one Ken Burns preset, one crossfade, unchanged for 110 minutes |

**The two channels that do NOT front-load are the two you should not copy for this** — Cosmo Explains (weakest performer, +8 %) and Sleepy Science (−9 %, but it compensates with a strong brightness/simplicity ramp instead).

Gemini's independent verdict on `tvB659d_oik` says the same thing in one sentence: *"A hand-cut 3-minute retention intro (24 cuts, ~7.5 s holds, live-action stock, drop-in subscribe module) is bolted onto ~121 minutes of templated AI nebula wallpaper cut on an almost exact 20.0-second grid."*

---

## 4. Retention-proxy structure (Step 15)

**No audience-retention data exists for any competitor channel and none is inferred here.** What follows are *structural devices* that are measurable in the artefacts themselves.

| Proxy | Measured evidence | Present in |
|---|---|---|
| **Front-loaded visual density** | 5.55 vs 3.10 changes/min | SOP, CS, CSp |
| **Front-loaded brightness** | 52.8 → 41.0 on SOP | SOP |
| **Hook resolves into an explicit question before 60 s** | "And the question is why?" at 0:59 | SOP, CS, CSp |
| **CTA as a seam, not an interruption** | 47–87 s, right after the hook lands | 4 of 5 channels |
| **Rhetorical questions as attention resets** | 11.8/h (SOP), 8.3–8.5/h (CS/CSp) | all but Sleepy Science |
| **Reset-word sentence openers** | one every 30–45 s (SOP) | all |
| **Spiral restatement of the core claim** | 4–12 restatements/video | SOP, CS, CSp |
| **Analogy followed by its own limits** | 7.2–17.9 analogy markers/h | all |
| **Escalation of scale** (lab → cosmos) | qualitative, present in all sampled physics scripts | SOP, CS |
| **Progressive visual simplification** | edge density −85 %, brightness −36 % | Sleepy Science only |
| **Narration stops, music continues** | last 30 min of `xg8ieJQIB70` | Sleepy Science (1 old video) |
| Chapter resets | **absent — 0 chapters in 17/17** | none |
| Callbacks to earlier sections | present via spiral restatement | SOP, CS |
| **Curiosity loops** (a question posed, then deliberately deferred and answered minutes later) | qualitative — the spiral opens each turn with an unresolved "but that isn't quite what happens" before delivering the deeper mechanism | SOP, CS |
| Topic escalation (lab scale → cosmic scale) | qualitative, present in all sampled physics scripts | SOP, CS |

### How much of this actually gets heard

A Calm Space viewer, unprompted, in the top comments:
> *"Seems like some people don't get that other people just want to use this to fall asleep easier. **Takes about 3 minutes for me.**"*

Treat that as a single anecdote, not a statistic — but it is consistent with everything else measured here. A meaningful share of the audience is asleep inside the first few minutes, which is **exactly** why every strong channel spends 1.7× the editing effort on minutes 0–10 and then runs an unchanged template for the next 110. The video has to win in the first ten minutes or it does not win at all; after that it only has to avoid waking anyone.

### How the format stays interesting without waking the listener

The mechanism the data supports is **decoupling stimulation from information**:

- **Information density stays constant** (flat WPM, ~3 questions and ~6 restatements per 10 minutes, all the way to minute 120).
- **Sensory stimulation drops by ~40 % after minute 10** and never returns: fewer cuts, no text, no SFX, one unchanging drone, ~50 % of every frame near-black.
- **The images carry no information at all** on 3 of 5 channels — they are wallpaper. A listener who closes their eyes loses nothing. A viewer who keeps them open gets a slow, non-demanding visual field.

That is the trick: **the script is engaging, the picture is not.** Waking stimulus comes from cuts, brightness, text and audio transients — all of which are held low — while interest comes from language, which does not require the eyes.

The tension is real and viewers name it: *"Fascinating. I barely slept."* Confidence in the mechanism: **MEDIUM-HIGH** (structure is measured; its effect on retention is unmeasurable without the competitors' analytics).

---

## 5. Production complexity scores (Step 16)

Scored 1–10 (10 = hardest / highest potential), from the measured artefacts.

| | Sleep On Physics | Calm Science | Calm Space | Sleepy Science | Cosmo Explains |
|---|---|---|---|---|---|
| **Scripting difficulty** | **8** | 7 | 5 | 4 | 6 |
| **Research difficulty** | **9** | 8 | 5 | 3 | 6 |
| **Visual generation difficulty** | 4 | 3 | 3 | **5** | 6 |
| **Editing difficulty** | 4 (3 for the body, 7 for the intro) | 3 | 3 | 3 | 5 |
| **Audio difficulty** | 3 | 2 | 2 | 4 | 2 |
| **Automation potential** | **9** | **10** | **10** | 9 | 7 |

**Why physics scores highest on research and script:** 26.3 jargon terms per 1,000 words at grade 9.4 means every technical term must be introduced in plain language and kept correct across 17,600 words. The space channels run 2.4–3.4 jargon terms/1,000 w — they are telling stories about objects, not explaining mechanisms. **Your niche is the expensive one on the input side and the cheapest one on the output side.**

**Why Cosmo Explains scores worst on automation:** a fixed illustrated room with a character, plus burned-in captions on every frame, is a bespoke compositing setup that must be maintained. It buys nothing measurable — that channel has the lowest views/video in the sample.

### Realistic time budget for a 120-minute episode

Human labour and machine time are separated, as the brief requires.

| Stage | Human (first 5 episodes) | Human (optimised) | Machine (unattended) |
|---|---|---|---|
| Topic selection | 15 min | **5 min** | — |
| Research | 90 min | **40 min** | 10 min |
| Outline | 30 min | **10 min** | 5 min |
| Script generation | 20 min | **10 min** | 20–40 min |
| **Script read-through + edit** | **120 min** | **60 min** | — |
| Fact-check pass | 60 min | **25 min** | 10 min |
| TTS generation | 15 min | **5 min** | 20–40 min |
| Image prompt generation | 30 min | **5 min** | 5 min |
| Image generation | 10 min | **5 min** | **40–90 min** |
| Asset QC (scan ~300 images) | 45 min | **20 min** | — |
| Timeline assembly | 30 min | **5 min** | 10 min |
| Audio mix | 20 min | **5 min** | 5 min |
| Thumbnail | 30 min | **10 min** | 5 min |
| QC spot-checks | 45 min | **20 min** | — |
| **Render / encode** | 5 min | **2 min** | **60–150 min** |
| Metadata + upload | 25 min | **10 min** | 15 min |
| **TOTAL** | **~8.3 h human** | **~3.9 h human** | **~3.5–6.5 h machine** |

Machine time overlaps with human time and with itself; wall-clock per episode is ~6–8 hours, of which under 4 hours needs a person.

**The script read-through is the irreducible cost.** 16,000 words at a careful 250 wpm is 64 minutes of reading, minimum, and you cannot skip it without shipping hallucinated physics. Everything else compresses; this does not.

---

## 6. Automation analysis (Step 17)

| Step | Classification | Notes |
|---|---|---|
| Topic research / idea generation | **PARTIALLY AUTOMATABLE** | Competitor title mining and gap analysis automate well; final pick is judgement |
| Outline | **FULLY AUTOMATABLE** | The spiral structure (§2.2) is a fixed template |
| First script draft | **FULLY AUTOMATABLE** | 16,000 words from a validated outline |
| **Fact-checking** | **HUMAN REVIEW REQUIRED** | Non-negotiable. Physics at 26 jargon terms/1,000 w is exactly where LLMs produce confident errors. A separate model pass helps but does not discharge the requirement |
| **Final script approval** | **SHOULD NOT BE AUTOMATED** | You publish it; you read it |
| TTS generation | **FULLY AUTOMATABLE** | Batch by paragraph, concatenate |
| **Pronunciation exceptions** | **HUMAN REVIEW REQUIRED** | A per-channel lexicon for terms your TTS mangles. Build it once, extend per episode |
| Image prompt generation | **FULLY AUTOMATABLE** | Prompts come from the script's section themes plus a fixed style suffix |
| Image generation | **FULLY AUTOMATABLE** | Batch generation, ~300 assets |
| **Broken-image screening** | **HUMAN REVIEW REQUIRED** | Fastest as a contact-sheet scan — ~20 min for 300 images |
| Ken Burns motion | **FULLY AUTOMATABLE** | One FFmpeg `zoompan` expression, randomised direction and 3–5 % magnitude |
| Scene placement / durations | **FULLY AUTOMATABLE** | Randomised 16–24 s with a jitter seed, denser for the first 10 min |
| Transitions | **FULLY AUTOMATABLE** | One 1.2 s crossfade, everywhere |
| Background music | **FULLY AUTOMATABLE** | One loop, ducked under narration |
| Subtitles | **SHOULD NOT BE AUTOMATED — SHOULD NOT BE DONE** | Zero of the four strong channels burn in captions; the one that does performs worst. Upload a caption *track* instead — free, invisible, good for search |
| Audio mix / loudness normalisation | **FULLY AUTOMATABLE** | FFmpeg `loudnorm` |
| Export / encode | **FULLY AUTOMATABLE** | — |
| Thumbnail | **PARTIALLY AUTOMATABLE** | Generate candidates, pick by eye |
| Metadata (title, description, tags) | **PARTIALLY AUTOMATABLE** | Draft automatically, approve manually |
| **Final QC watch-through** | **HUMAN REVIEW REQUIRED** | Spot-checks at fixed timestamps — see `13_quality_control_checklist.md` |
| **Publishing** | **SHOULD NOT BE AUTOMATED** | — |

### The line that keeps this from becoming obvious low-effort AI content

Three human gates, roughly **2 hours per episode**, and they are the only things separating you from the bottom of this niche:

1. **Read the whole script.** Physics errors are the one failure this audience punishes — the comments are full of physicists and retired engineers.
2. **Scan every generated image once.** Malformed AI artefacts are the visual tell.
3. **Watch 6–8 timestamps end-to-end.** Catches audio dropouts, duplicate assets, and cut-rate glitches.

Everything else on this list can run unattended.

---

## 7. Template reverse-engineering (Step 18)

> **Can competitor videos realistically be generated from a reusable template? For minutes 3–120: yes, almost entirely.** Gemini, unprompted, described `_nLpB_Ao7zw` as *"two productions bolted together: a bespoke hand-cut 3-minute hook … followed by ~105 minutes of a single rigid template — one AI-generated space still + a 3–5 % Ken Burns zoom + a 1–1.5 s crossfade."*

### The template, with measured values

```
TRACK 1  Narration            single continuous WAV, 0.0 s → end,  ~120 min
TRACK 2  Ambient bed          one loop, enters at 60–90 s, runs to end
TRACK 3  Visual assets        ~300 stills, Ken Burns, 1.2 s crossfades
TRACK 4  Particle/dust overlay  screen blend, persistent, very low opacity
TRACK 5  Vignette + grade     static adjustment layer
TRACK 6  (intro only) text    one subscribe overlay at ~62 s — the ONLY text
```

### Standard scene parameters

| Parameter | Value | Basis |
|---|---|---|
| **Image duration, body (10–120 min)** | **20 s ± 4 s** (uniform 16–24 s) | Measured mean 19.2–21.8 s; median 20 s; p90 30–40 s |
| **Image duration, 3–10 min** | **12 s ± 3 s** | Measured 4.1–5.1 changes/min in this band |
| **Image duration, 0–3 min** | **7 s ± 2 s** | Gemini-measured 6.4–7.5 s/asset |
| **Hard ceiling on any shot** | **≤ 45 s** | Measured: 0 % of shots exceed 60 s on the two priority channels |
| **Crossfade** | **1.2 s** | Gemini-measured 1.0–1.5 s |
| **Intro cuts (0–3 min)** | **hard cut, 0 s** | Gemini: "24 cuts", hard-cut on `tvB659d_oik` |
| **Zoom magnitude** | **3–5 % over the shot** (≈0.2 %/s) | Gemini-measured; "perceptible but barely" |
| **Zoom direction** | **50 % in / 50 % out**, alternating with jitter | Observed alternation |
| **Pan probability** | **~35 %**, always combined with zoom, always diagonal and slow | Contact-sheet observation, MEDIUM confidence |
| **Overlay probability** | **100 %** — persistent, not per-scene | Gemini: "persistent star/dust particles, subtle vignette" |
| **Fade from black** | 2 s at 0:00 (Calm Science/Space) or none (Sleep On Physics) | Measured: first frame is pure black on CS/CSp |
| **Fade to black** | **3–5 s** at end | Measured: final storyboard sheets are near-black (mean luminance 1.2–9.7/255) on every channel |
| **Aspect** | **Full-bleed 16:9** or **2.39:1 letterbox (20 % of height)** | Measured; both work (see §7.1) |

### 7.1 The letterbox decision
Calm Science and Calm Space (same operator) crop to **2.39:1** by black-barring exactly 20 % of frame height. Sleep On Physics, Sleepy Science and Cosmo Explains are full-bleed 16:9.

- **Cost:** free. It is two black rectangles.
- **Benefit:** instantly reads as "cinema", and it darkens the average frame — measured brightness 32.8/31.8 for the letterboxed channels vs 40.6/38.0 for the full-bleed physics channels.
- **Risk:** you throw away 20 % of the screen, and it makes you look like Calm Space's sibling — which is exactly the channel you would be competing with.

### 7.2 Which tool to build the template in

**Recommendation: FFmpeg driven by Python, with DaVinci Resolve (free) kept only for the intro.** Reasoning:

| Tool | Verdict |
|---|---|
| **FFmpeg + Python** | **Choose this for the body.** `zoompan` does Ken Burns natively; `xfade` does the crossfade; `loudnorm` does the mix. Fully headless, scriptable, zero licence cost, runs on any box. Assembling 300 clips is a loop, not a timeline. |
| **DaVinci Resolve (free)** | **Choose this for the 0–3 min intro only.** Hand-cutting 24 shots with real footage is faster on a timeline than in code. Free tier is sufficient. |
| Remotion | Excellent tool, wrong job — React/Canvas rendering of 300 photographic stills for 2 hours is far slower than FFmpeg's filter graph and buys you nothing this format needs. |
| Python/MoviePy | Works, but wraps FFmpeg and is markedly slower on long timelines. Use FFmpeg directly. |
| Premiere Pro | £/$ per month for a timeline you will not open. No. |
| CapCut | Not viable at 300 assets × 120 min; weak automation. No. |

**One caution about `zoompan`:** it is an integer-position filter and produces visible jitter on very slow zooms unless you upscale first. Render each still at 2× (3840×2160), apply `zoompan` with a high `d` value, then downscale to 1920×1080. This is the single most common failure mode in automated Ken Burns and it will make your video look cheap if you skip it.
