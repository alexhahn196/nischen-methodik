# 06 — Production SOP

Covers brief steps 19, 21, 22. This is the document you hand to an editor and an automation operator.

---

## 1. Minimum viable quality (Step 19)

Budget ceiling **$50/video**, target **$20–40**. Sorted by what the evidence actually supports.

### MUST MATCH — from day 1, non-negotiable

| # | Requirement | Measured basis | Confidence |
|---|---|---|---|
| 1 | **Runtime 105–135 min** | Category median 119–137 min; 17/17 sampled videos in range | HIGH |
| 2 | **Narration starts ≤ 1.0 s** | 17/17 videos start at 0.0–0.6 s | HIGH |
| 3 | **Narration covers ~100 % of runtime** | 16/17 videos at 98–100 % | HIGH |
| 4 | **16,000 ± 1,500 words** | Category 15,433–17,845 (excluding one outlier fact-list) | HIGH |
| 5 | **120–132 WPM, flat** | Category 118.7–143.4; no in-video slowdown anywhere | HIGH |
| 6 | **Flesch–Kincaid grade 9.0–9.5** | All 5 channels land in a 0.4-grade band | HIGH |
| 7 | **300–390 placed visual assets, ~20 s each in the body** | Category 296–499, mean ~350; s/asset 17.7–21.8 | HIGH |
| 8 | **No shot longer than 45 s** | 0 % of shots exceed 60 s on both priority channels | HIGH |
| 9 | **Every image carries a 3–5 % Ken Burns move** | **Measured on 6,629 held image-pairs across all 17 videos: 98.6–99.9 % of held images move; only 0.1–1.4 % are fully static** | HIGH |
| 10 | **One 1.0–1.5 s cross dissolve, used everywhere** | Gemini-measured; no other transition observed | HIGH |
| 11 | **Frame is dark — mean luminance 25–40/255, 60–80 % of pixels below 32** | Measured across all 5 channels | HIGH |
| 12 | **Zero on-screen text in the body** — no captions, no titles, no equations, no labels, no diagrams | 4 of 5 channels; the exception is the worst performer | HIGH |
| 13 | **Zero chapter markers** | 0/17 videos | HIGH |
| 14 | **Front-load: first 10 min at ~1.7× the body's cut rate** | −37 % to −44 % on all 3 strong still-image channels | HIGH |
| 15 | **Exactly one spoken CTA at 55–65 s**, 15–20 s long | 13 of 14 CTA-using videos at 47–87 s, median 65 s | HIGH |
| 16 | **No logo animation, no branded sting, no musical runway** | 0/17 videos | HIGH |
| 17 | **Fade to black over the final 3–5 s** | Final storyboard frames near-black on every channel | HIGH |
| 18 | **Scientific accuracy** | The comment sections are full of physicists and retired engineers correcting errors | HIGH |

### NICE TO HAVE — real upside, not required to compete

| Item | Evidence | Why it's optional |
|---|---|---|
| **Topic-matched imagery** | Only Sleepy Science does it; two viewers on Sleep On Physics asked for it unprompted | The channel with decoupled wallpaper got 79,844 views in 7 days anyway. **This is your best differentiation lever precisely because it is optional** — see §3 |
| Ambient drone bed | 4 of 5 channels have one; prominence ranges from 12 % to 75 % `[Music]` coverage | Calm Science runs it nearly inaudibly, carries the **highest RPM in the sample ($22.04)**, and performs fine |
| Progressive darkening over 2 h | Sleepy Science only: brightness −36 %, edge density −85 % | The 328k-sub leader does it; nobody else does. Cheap to add |
| 2.39:1 letterbox | Calm Science + Calm Space (same operator) | Free, but it makes you look like their third channel |
| Subscribe overlay graphic at ~1:05 | Sleep On Physics only | Marginal; the spoken CTA is the part that matters |
| Real stock footage in the first 3 min | Sleep On Physics only | Adds cost and adds human faces, which conflicts with a no-faces identity |
| Second CTA in the final 2 min | 5 of 17 videos | Audience is asleep. Harmless, low value |

### WASTE OF MONEY — competitors do it, evidence does not support it

| Item | Why | Confidence |
|---|---|---|
| **Burned-in subtitles** | Only Cosmo Explains does it. Lowest views/video (11,833) and lowest like rate (0.96–2.2 %) in the sample. Also brightens frames and raises edge density in a category built on darkness. Upload a **caption track** instead — free, invisible, searchable | HIGH that it's unnecessary; MEDIUM that it hurts |
| **Bespoke animated explainers, motion-graphics diagrams** | **Zero across 17 videos and ~2,200 minutes.** The most technical channel in the sample (26.3 jargon/1,000 w) uses none | HIGH |
| **A fixed illustrated character/room set** | Cosmo Explains' signature. Expensive to build and maintain, worst performance in the sample | HIGH |
| **Equations and formula cards** | Zero occurrences | HIGH |
| **Parallax / 2.5D depth passes** | Not observed anywhere. Costs 5–10× a Ken Burns move | HIGH |
| **Per-shot custom transitions** | One crossfade, everywhere. No whips, blurs or motion transitions observed | HIGH |
| **Sound effects** | Gemini: "zero SFX". No evidence of SFX on any channel | MEDIUM |
| **Evolving multi-track music score** | `[Music]` tags distribute evenly across all deciles — one unchanging bed | MEDIUM |
| **Chapter markers** | 0/17 | HIGH |
| **4K delivery** | Nothing in this format resolves beyond 1080p; images are stills with 3 % zooms. Doubles render and storage cost | MEDIUM |
| **Premium TTS at $20+/video** | Zero of 40 top comments mention the voice at all | MEDIUM |
| **500 unique generated images** | Sleep On Physics cut from ~500 to ~300 with no visible penalty; assets are recycled within videos anyway | MEDIUM-HIGH |

---

## 2. Where you must not copy (Step 21)

### 2.1 Conventions to match (they are the genre's grammar — breaking them just looks broken)
Dark frame · ~20 s per image · slow Ken Burns · single crossfade · no text · no chapters · 105–135 min · immediate narration · one CTA at ~60 s · flat pace · wall-to-wall narration · fade to black.

### 2.2 Conventions to deliberately avoid

| Avoid | Who does it | Why avoid |
|---|---|---|
| **"Tonight, we're going to…" as your standard opener** | Calm Science 4/4, Calm Space 3/3, Sleep On Physics 2/4 | It is the single most saturated sentence in the niche. A viewer scrolling three of these in a row hears the same voice-over template three times |
| **Burned-in ALL-CAPS captions** | Cosmo Explains | Worst performer; wrong for a dark format |
| **A cartoon character mascot / fixed room** | Cosmo Explains | Expensive, worst-performing |
| **Explicit sleep language** ("close your eyes", "drift off") | Sleepy Science, Cosmo | Your two priority references *never* use it. It caps you as a sleep-aid channel rather than a physics channel, and it fights the physics-engaged audience visible in the comments |
| **Generic nebula wallpaper decoupled from the topic** | Sleep On Physics, Calm Science, Calm Space | The one thing viewers complain about out loud. See §3 |
| **2.39:1 letterbox** | Calm Science + Calm Space | It is the visual signature of a specific competitor pair operating in your exact niche |
| **A verbal channel-name greeting** | Sleepy Science | Burns your strongest 5 seconds on branding nobody searched for |

### 2.3 Where all five are identical (and therefore where differentiation is cheap)
1. **Nobody's visuals mean anything** except Sleepy Science's.
2. **Nobody uses text, diagrams or equations** — in a category explaining physics.
3. **Nobody uses chapters** — in 2-hour videos.
4. **Everybody is blue-violet** except Sleepy Science (warm amber).
5. **Everybody's images are cosmic** — nebulae and galaxies — even when the topic is an atom, an electron or a wire.

**That fifth point is the opening.** Four of five channels making *physics* content show you *astronomy* pictures. Nobody is showing the actual object under discussion.

### 2.4 Verdict on your proposed visual identity

Your stated plan: *nearly black backgrounds · one dominant scientific object · cross-section / cutaway imagery · thin cyan geometry and measurement lines · visual negative space · slow cinematic movement · no faces · minimal text · deep blue-violet palette · occasional warm amber highlights.*

**Assessment: mostly native, one element already owned, two elements genuinely new. Confidence: HIGH.**

| Element | Verdict | Evidence |
|---|---|---|
| Nearly black backgrounds | ✅ **Native.** Mandatory, in fact | 60–81 % dark pixels category-wide |
| **One dominant object + deep negative space** | ⚠️ **This is Sleepy Science Channel's exact signature** — 328k subs, edge density 0.024 (one quarter of everyone else) | Direct frame inspection of `A0vVW7PWnm4`, `BA59TWIMNG4` |
| Slow cinematic movement | ✅ Native | 3–5 % Ken Burns everywhere |
| No faces | ✅ Native — with one exception: Sleep On Physics uses human faces in its first 3 minutes | Frame inspection of `BLPBP5BaU-0` 0:59 |
| Minimal text | ✅ Native (in fact: *zero* text is the standard) | 4 of 5 channels |
| Deep blue / violet palette | ✅ Native — B−R is +2.6 to +6.1 on four channels | Measured |
| Warm amber highlights | ⚠️ **Also Sleepy Science's** — the only warm-biased channel (B−R = −0.7) | Measured |
| **Cross-section / cutaway imagery** | 🟢 **GENUINELY NEW. Not present on any of the 5 channels.** | 17 videos inspected |
| **Thin cyan geometry / measurement lines** | 🟢 **GENUINELY NEW.** The closest thing observed is Calm Science's blue particle meshes, which are decorative, not measurement-like | Frame inspection of `lqZntA10Q5g` 1:39 |

**What to change:** your palette-and-composition plan collides with the biggest channel in the sample. Your *content* plan — cutaways, cross-sections, thin measurement geometry — collides with nobody.

**So invert the emphasis.** Do not differentiate on darkness and negative space; everyone has that. Differentiate on **what is inside the frame**:

> **"The object under discussion, drawn as if measured."**
> A video about the electron shows an electron-scale render, not a nebula. A video about a wire shows a cutaway of a conductor with the field around it. A video about a neutron star shows a cross-section with a scale bar. Thin cyan construction lines, one dominant object, deep black, no labels, no words.

This is **still native** (dark, one object, slow, no faces, no text) but **immediately recognisable**, and it is the exact thing two viewers publicly asked Sleep On Physics for. It costs the same as generating nebulae — it is a prompt-library decision, not a budget decision.

Keep the blue-violet base and use amber sparingly as an accent only (a hot core, a filament) so you do not read as Sleepy Science's palette. **Skip the letterbox** — it belongs to Calm Science/Calm Space.

---

## 3. THE PRODUCTION SPECIFICATION (Step 22)

**Channel:** Quiet Physics / Cosmic Physics
**Positioning:** "Deep questions about reality and the universe, explained calmly at night."
**Mix:** 55 % fundamental physics · 40 % cosmic physics · 5 % experimental
**Cadence:** 3 videos/week · **Runtime:** 105–135 min · **Budget:** $20–50/video

### VIDEO

| | Specification | Basis |
|---|---|---|
| **Resolution** | **1920 × 1080** (render stills at 3840 × 2160, downscale after `zoompan`) | Nothing in this format resolves past 1080p; 2× source is required to avoid zoom jitter |
| **FPS** | **30** (24 acceptable) | Stills with 0.2 %/s motion; 60 fps is pure waste |
| **Bitrate** | **8–10 Mbps** VBR H.264, or CRF 20–22 · AAC 192 kbps | Dark, low-motion, high-noise-risk content — see banding note below |
| **Aspect** | **16:9 full-bleed. No letterbox.** | Letterbox is Calm Science/Calm Space's signature |
| **Duration** | **125 ± 8 min** (16,000 words ÷ 125 wpm = 128 min) | Category median 119–137; Calm Science ships 131–134 min |
| **Colour** | Rec.709, no HDR | — |
| **Banding** | Add **very light film grain / dither** (≈1–2 % noise) before encode | **Critical.** Dark gradients at 60–80 % near-black pixels band badly under YouTube's VP9 transcode. Every competitor's imagery has grain-like texture that masks this |

### SCRIPT

| | Specification | Basis |
|---|---|---|
| **Words** | **15,500–16,500** (target 16,000 → **128 min** at 125 wpm) | Category 15,433–17,845 |
| **Words / min** | **125** (band 120–132) | Calm Science 120.3, Calm Space 118.7, category top 143.4 |
| **Sections** | **9 movements, unlabelled and invisible to the viewer** | 0 chapters observed; structure is a spiral, not a list |
| **Movement duration** | **12–15 min**, no on-screen marker | Derived from the 9-part blueprint in `07_120min_blueprint.md` |
| **Mean sentence** | **13 words** (median 12, p90 ≤ 25) | Calm Science 13.0 / Sleep On Physics 14.1 |
| **Reading difficulty** | **Flesch–Kincaid 9.0–9.5**, Flesch ease 50–56 | All 5 channels in this band |
| **Jargon density** | **20–26 physics terms / 1,000 words**, each defined in plain language on first use | Sleep On Physics 26.3, Calm Science 21.3 — the physics channels' differentiator |
| **Questions** | **10–12 per hour** (≈1 every 5–6 min) | Sleep On Physics 11.8, Cosmo 10.5, Calm 8.3–8.5 |
| **Analogies** | **12–18 per hour**, each followed by its own limits | Sleep On Physics 17.9 |
| **Attention resets** | **12–15 %** of sentences open with a reset word (≈ one every 40 s) | Sleep On Physics 14.6–21.3 %, Calm Science 9.9–14 % |
| **Core-claim restatements** | **6–8 per video**, always reworded, **never verbatim** | Category 4–12; a viewer complained about 3 identical repeats |
| **Second person** | **7–9 "you/your" per 1,000 words** | Sleep On Physics 8.6, Calm Science 7.6 — *not* Sleepy Science's 12.6 |
| **Tone** | Documentary narrator, calm, first-person-singular ownership ("I", not "we") | Sleep On Physics' outro CTA uses "helps *me* keep making these" |
| **Hook** | **55–60 s**, concrete-image cascade → paradox → explicit question. **Do not open with "Tonight, we're going to…"** | Both hook shapes produce breakouts; "Tonight" is saturated |
| **Sleep language** | **The word "sleep" appears zero times.** One "tonight" maximum, in the first sentence | Sleep On Physics and Calm Science both do exactly this |
| **CTA** | **One, spoken, at 58–62 s, 15–18 s long.** Optional second in the final 2 min | Measured 47–87 s, median 65 s; Sleep On Physics spans only 59.3–62.9 s |

### VOICE

⚠️ **Read `04_audio_voice_analysis.md` §4 first — I never heard these videos.** Gender, age, accent, pitch and pause length are **not measured**; the rows below are marked accordingly.

| | Specification | Basis |
|---|---|---|
| **Words per minute** | **125** (120–132) | **MEASURED** |
| **Pacing curve** | Flat. Optionally 8 % faster for minutes 0–15, then settle | **MEASURED** (Calm Science does this) |
| **Start** | First word within 1.0 s of frame one | **MEASURED**, 17/17 |
| **Gender** | **Weak lean: male.** Listeners address the narrator as "sir" / "Mr" on two different channels, unprompted, in ~77 top comments. Verify by listening before committing | Viewer perception, not acoustics — **MEDIUM** |
| **Apparent age** | **No evidence-based recommendation** | NOT MEASURED |
| **Accent** | Neutral international English — a *market* judgement (English-language faceless channel), not a measurement | NOT MEASURED |
| **Pitch / variation** | **No evidence-based recommendation** | NOT MEASURED |
| **Pause length** | Likely < 1 s between sentences, inferred from WPM × sentence length | **INFERRED, LOW confidence** |
| **Emotion** | Low variation, warm, never dramatic — the register the *scripts* demand | Inferred from measured script register |
| **TTS suitability** | **High.** Zero of 40 top comments on the two priority channels mention the voice at all | MEDIUM |
| **Required** | A **pronunciation lexicon** for physics terms your engine mangles (eigenstate, Cherenkov, de Broglie, Kelvin-Helmholtz, muon, Schwarzschild, quasar) | Auto-captions on these very videos show the ASR mangling "quasar"→"quazar", "positron"→"posetron" — your TTS will mangle them too |

### VISUALS

| | Specification | Basis |
|---|---|---|
| **Placed assets** | **~350** for a 125-min episode (≈28 per 10 min). The front-loaded blueprint in `07` runs ~390 (≈33/10 min) — still inside the measured band | Category 296–499, mean ~350; per-10-min range 24.7–41.6 |
| **Newly generated per episode** | **180–220**; remainder from the reusable library | Assets are recycled within competitor videos |
| **Mean seconds per asset** | **20 s** body · **12 s** minutes 3–10 · **7 s** minutes 0–3 | Measured 17.7–21.8 body; Gemini 6.4–7.5 intro |
| **Max shot length** | **45 s** | 0 % of shots exceed 60 s on the priority channels |
| **Still images** | **~95 %** of runtime | Category ~85–95 % |
| **Video clips** | **≤ 5 %**, intro only, and **no human faces** | Sleep On Physics uses stock video in the intro; you should not use faces |
| **Diagrams** | **0 labelled diagrams.** Cutaways and cross-sections instead — pictures, not figures | 0 diagrams observed; cutaways are your differentiator |
| **Text graphics** | **0** | 4 of 5 channels |
| **Style** | *"The object under discussion, drawn as if measured."* One dominant object, deep black, cutaway/cross-section, thin cyan construction geometry, no labels | §2.4 |
| **Brightness** | Mean **28–36 / 255** · 65–75 % of pixels below 32 | Category 24.0–40.6 |
| **Saturation** | **0.42–0.48** — muted, closer to Calm Science than Sleep On Physics | Measured 0.370–0.570 |
| **Contrast** | σ **32–40** | Measured 28.6–44.5 |
| **Palette** | Base deep blue-violet (**B−R ≈ +4 to +6**) · accent thin cyan (#3FD8E8-ish) · **amber sparingly**, as a hot core only | Four channels are blue-biased; amber is Sleepy Science's territory |
| **Movement** | Ken Burns on **100 %** of shots. Consider the market leader's gentler setting: Sleepy Science's contrast-normalised motion index is **0.302** vs 0.437–0.465 for everyone else — ~35 % less movement | Measured on 6,629 held pairs |
| **Zoom** | **3–5 % over the shot** (≈0.2 %/s), direction alternating 50/50 | Gemini-measured |
| **Pan** | **~35 % of shots**, diagonal, always combined with zoom | Observed, MEDIUM confidence |
| **Parallax** | **None** | Not observed anywhere |
| **Particles** | Persistent, very low opacity dust/star overlay + static vignette | Gemini-confirmed |
| **Progressive simplification** | Reduce brightness ~20 % and asset complexity across minutes 60→115 | Sleepy Science (largest channel) does exactly this |

### EDITING

| | Specification | Basis |
|---|---|---|
| **Transition** | **Cross dissolve, everywhere** | Gemini-measured |
| **Transition duration** | **1.2 s** body · **0 s (hard cut)** in minutes 0–3 | Gemini 1.0–1.5 s; intro is hard-cut |
| **Scene duration** | 7 s → 12 s → 20 s across the three zones, with ±20 % jitter | Measured |
| **Cut frequency** | **~8/min** (0–3 min) → **5/min** (3–10) → **3/min** (10–115) | Measured 5.55 → 3.10 |
| **Visual intensity** | High for 10 min, then flat and low for 105 min. **Never re-escalate** | Measured: no channel re-escalates after minute 10 |
| **Intro complexity** | **The only hand-edited part of the video.** ~25 shots in 3 min, hard cuts, brighter, no music | Gemini: "24 cuts", "two productions bolted together" |
| **Outro complexity** | **Minimal.** No end card, no outro animation, no next-video suggestion. Fade to black over 3–5 s | Final frames near-black on every channel |

### AUDIO

| | Specification | Basis |
|---|---|---|
| **Music type** | One unchanging ambient drone / pad loop | Gemini: "one unchanging ambient drone"; `[Music]` tags evenly spread |
| **Music entry** | **Not before ~60 s.** Let the hook run dry; bring the bed in under or just after the CTA | Measured first-tag times 4.6–458 s; SOP's first tag at 2:20 |
| **Music volume** | **Low — Calm Science-quiet, not Sleepy Science-loud.** Roughly 18–22 dB below narration | `[Music]` coverage 12.1 % vs 74.7 %; both profitable, quiet is safer |
| **Voice volume** | Normalise the mix to **−14 LUFS integrated** (YouTube's target), true peak ≤ −1 dBTP | Platform norm — **not verified against these competitors** (LOW) |
| **Ambient layer** | Optional very-low-level noise floor to prevent digital silence between sentences | Craft recommendation |
| **Sound effects** | **None** | Gemini: "zero SFX" |
| **Silence** | No dead air anywhere; narration is wall-to-wall | Measured 98–100 % coverage |
| **Loudness consistency** | Compress narration lightly (2:1, slow) so no sentence spikes and wakes the listener | Craft recommendation |
| **Captions** | Upload a **caption track**. **Never burn captions into the picture** | 4 of 5 channels have no burned captions; the exception performs worst |
