# 03 — Visual Analysis

Covers brief steps 3–9. Every number is measured from the full-runtime storyboard timeline of all 17 videos unless marked ESTIMATE or LOW confidence.

---

## 1. Visual source mix (Step 3)

Classified by direct inspection of contact sheets (9 videos in detail, all 17 sampled) plus Gemini shot lists for 2 Sleep On Physics videos. Percentages are of **screen time**, not asset count.

| Source type | Sleep On Physics | Calm Science | Calm Space | Sleepy Science | Cosmo Explains |
|---|---|---|---|---|---|
| AI-generated stills (nebulae, galaxies, abstract cosmic) | **~85 %** | **~85 %** | **~85 %** | **~95 %** | ~0 % body |
| CGI renders / motion graphics (particle meshes, warp tunnels, atom models) | ~8 % | ~10 % | ~10 % | ~3 % | ~0 % |
| **Real stock video** (people, hands, labs, cities, interiors) | **~5 %, concentrated in 0:00–3:00** | <1 % | <1 % | 0 % | 0 % |
| Real space footage / NASA public domain | not separable from AI stills — **UNCERTAIN** | UNCERTAIN | UNCERTAIN | ~0 % | ~0 % |
| Diagrams / labelled figures | **0 %** | **0 %** | **0 %** | **0 %** | 0 % |
| Text graphics / cards | ~0.3 % (one subscribe overlay) | 0 % | 0 % | 0 % | **100 % (burned-in captions)** |
| Fixed composited scene (cartoon room + character + window) | 0 % | 0 % | 0 % | 0 % | **~100 %** |
| Particle / dust overlays | present, persistent (Gemini-confirmed on 2 videos) | apparent | apparent | apparent | apparent |
| Static full-black | opening/closing frames | **opens on black** | **opens on black** | no | no |

**Notes and uncertainties**
- **I cannot reliably separate "AI-generated" from "licensed stock space art" from "processed real astrophotography."** Gemini flagged the Sleep On Physics body imagery as AI-generated ("surreal shapes, smooth gradients") on the two videos it reached. For the other 15 the classification is my visual judgement. Treat the AI-vs-stock split as **UNCERTAIN**; what is certain is that it is *2D still imagery with slow motion applied*, which is what matters for your cost model.
- **Cosmo Explains is a completely different format.** A fixed illustrated room with a robot character; only the "window" region changes. This is why a naive whole-frame detector reported ~1 scene change for the entire video and why the analysis needed a per-video dynamic-region mask.
- **Sleep On Physics' first ~3 minutes are a different production from the rest of the video.** Confirmed by inspection of `BLPBP5BaU-0` 0:00–2:55: real night-sky footage, industrial/lab machinery, CGI atom, blue plasma, hands writing, **a man's face at a window**, hallway, living room, fabric macro, lab equipment, coloured wires, person at a desk with books. Then from ~3:00 the video becomes abstract nebula stills for the remaining ~2 hours.

---

## 2. Scene-change frequency (Step 4)

Primary threshold: HSV histogram Bhattacharyya distance > **0.40** on the masked dynamic region (calibrated — see `02_channel_comparison.md` §0).

### Threshold sensitivity — does the answer depend on where you draw the line?

Mean seconds-per-asset across each channel's sample:

| Threshold | Sleep On Physics | Calm Science | Calm Space | Sleepy Science | Cosmo Explains |
|---|---|---|---|---|---|
| 0.30 (loose) | 17.6 | 18.9 | 18.4 | 15.1 | 15.0 |
| **0.40 (validated)** | **19.2** | **21.8** | **20.5** | **20.6** | **17.7** |
| 0.50 | 20.5 | 23.2 | 21.6 | 29.7 | 28.5 |
| 0.60 (tight) | 21.7 | 24.2 | 22.5 | 49.2 | 1373.4 |

**The three full-bleed still-image channels are rock stable: 17.6–24.2 s per asset across the whole threshold band.** That is the finding you can build on.

Two channels destabilise at the tight end and it is worth knowing why:
- **Cosmo Explains collapses to 1373 s** at threshold 0.60 because ~85 % of its frame never changes (fixed illustrated room). Only the masked window region moves, so few pairs ever reach a high distance. Its true rate is the 0.30–0.40 figure (15–18 s), corroborated by manual frame counting.
- **Sleepy Science drifts to 49 s** at 0.60 because its frames are so dark and so desaturated (brightness 24.0, saturation 0.370) that two genuinely different images still produce similar histograms. Its true rate is again the 0.30–0.40 figure, corroborated by manual counting of `BA59TWIMNG4` 30:00–33:00 (~20 s/asset).

Nobody in this category is cutting fast.

### What the thresholds separate
- **Slow zoom on the same image** produces a Bhattacharyya distance of typically 0.05–0.25 — well below 0.40. Measured: on held-image pairs the median masked pixel change is small and the histogram barely moves, because a 3–5 % zoom does not redistribute colour.
- **A genuinely new image** produces 0.5–1.0. In the calibration window the two populations were cleanly separated (same-asset: 0.14–0.25; new asset: 0.62–1.00) with **nothing in between**. The distribution is bimodal, which is why the exact threshold barely matters.
- **Brightness drift and particle motion** do not trigger the detector — they are colour-preserving.

### Headline numbers

| | Sleep On Physics | Calm Science | Calm Space | Sleepy Science | Cosmo Explains |
|---|---|---|---|---|---|
| Total visual changes / video | 322–515 | 358–375 | 363–430 | 336–537 | 413–474 |
| **Changes per minute** | **3.28** | **2.76** | **2.93** | **2.92** | **3.40** |
| **Mean s / asset** | **19.2** | **21.8** | **20.5** | **20.6** | **17.7** |
| Median shot length | 10–30 s | 20 s | 10–20 s | 20 s | 10–20 s |
| p90 shot length | 20–40 s | 30–37 s | 30–40 s | 20–34 s | 30 s |
| % of shots > 30 s | 0–24 % | 9–10 % | 8–11 % | 6–10 % | 2–10 % |
| **% of shots > 60 s** | **0 %** | **0 %** | **0–0.2 %** | **0.2–1.8 %** | **0–0.5 %** |

**Category standard: one image change every 17–22 seconds; roughly 2.8–3.4 changes per minute.** HIGH confidence.

**A hard ceiling worth writing into the template: almost no shot ever exceeds 60 seconds.** Across 6,400+ measured shots, the share running longer than a minute is 0 % on Sleep On Physics and Calm Science and under 2 % everywhere else. Whatever else you do, do not park an image for two minutes.

---

## 3. Unique visual assets — the most important output (Step 5)

> **Question asked: does a competitive 2-hour video need 50, 100, 150, 300, or 500+ assets?**
> **Measured answer: ~300–500, and the working number is ~330–390.**

| Channel | Assets / 10 min | **Assets per 120-min video** | Range across sample |
|---|---|---|---|
| Sleep On Physics | 24.7–41.6 | **394** (mean) | 296 – 499 |
| Calm Science | 26.8–28.3 | **331** (mean) | 322 – 339 |
| Calm Space | 28.4–30.2 | **351** (mean) | 341 – 363 |
| Sleepy Science Channel | 27.1–32.5 | **350** (mean) | 325 – 390 |
| Cosmo Explains | 31.1–37.4 | **408** (mean) | 374 – 449 |
| **Category median** | **~28** | **~350** | **296 – 499** |

### But you do not need 350 *unique generated* assets
Three measured facts cut the generation bill:

1. **Assets are reused within the video.** Gemini on `tvB659d_oik`: *"assets recycling within minutes."* In my own frame inspection of `tvB659d_oik` 30:00–33:00, 18 sampled frames contained only **13 distinct images** — and a near-identical "white eye nebula" appears at both 30:26 and 32:15.
2. **Sleep On Physics' recent videos run at 296–322 assets, down from 459–499 earlier — with no performance penalty visible** (see `02_channel_comparison.md` §3.6).
3. **The imagery is topic-agnostic on 3 of 5 channels.** A nebula library is reusable across every episode you will ever make.

**Practical recommendation:** budget **~350 placed assets** per 120–128 minute episode, of which **~200 newly generated** and the rest drawn from within-episode reuse and a growing library. After 10 episodes your library alone can cover 40–60 % of a new episode. Confidence: MEDIUM-HIGH (the placement count is measured; the reuse ratio is an ESTIMATE informed by observed recycling).

---

## 4. Camera movement on still images (Step 6)

**Now measured across all 17 videos** (previously only 2 had direct observations). Method: take every pair of consecutive storyboard samples 10 s apart that the detector classified as the **same asset**, and measure how much the picture changed. A truly static image would show ~zero change; a moving one shows a clear delta. Because pixel change scales with image contrast, the cross-channel index divides by each video's mean frame contrast.

| Channel | Held pairs measured | **% of held images showing motion** | % fully static | Median pixel change | Contrast-normalised motion index |
|---|---|---|---|---|---|
| Sleep On Physics | 1,364 | **99.7 %** | 0.3 % | 15.77 | **0.458** |
| Calm Science | 1,728 | **99.7 %** | 0.3 % | 15.01 | **0.437** |
| Calm Space | 1,238 | **99.7 %** | 0.3 % | 15.26 | **0.456** |
| **Sleepy Science** | 1,282 | **98.6 %** | 1.4 % | **3.58** | **0.302** |
| Cosmo Explains | 1,017 | **99.9 %** | 0.1 % | 19.53 | 0.465 |

**Result 1 — motion is universal.** Between **98.6 % and 99.9 %** of held images carry measurable movement. Fully static images are **0.1–1.4 %** of the total. *No channel in this category ever parks a still image without motion.* Confidence: **HIGH** (measured on 6,629 held pairs across all 17 videos).

**Result 2 — the market leader moves ~35 % less than everyone else.** Sleepy Science's motion index is **0.302** against a 0.437–0.465 band for the other four. This is not a contrast artefact: their frames *are* lower-contrast (σ 12.1 vs 29–42), which is exactly why the index normalises for it, and the gap survives normalisation. **The largest channel in the sample uses the gentlest camera moves.** Confidence: **MEDIUM-HIGH** (the index is a proxy for geometric motion, not a direct measurement of zoom percentage).

**What Gemini directly reported** (2 Sleep On Physics videos — the only direct observations of zoom *magnitude*):
- `tvB659d_oik`: *"slow zoom or pan, ~3 % magnitude, perceptible"*
- `_nLpB_Ao7zw`: *"one AI-generated space still + a 3–5 % Ken Burns zoom + a 1–1.5 s crossfade"*

| Movement type | Prevalence | Evidence |
|---|---|---|
| **Slow zoom in / out (Ken Burns)** | **Dominant — 98.6–99.9 % of held images carry motion** | Measured on 6,629 held pairs, all 17 videos |
| Horizontal / vertical pan | Present, usually combined with zoom | Gemini direct; visible in contact sheets (`YBNfHLlrJkg` 30:26–31:15 drifts diagonally on one image over 50 s) |
| **Completely static** | **0.1–1.4 %** — used for the black open/close and the CTA card | Measured |
| Parallax / multi-plane | **Not observed** | — |
| Particle / dust / star overlay | **Persistent** on Sleep On Physics; apparent elsewhere | Gemini direct; teal bokeh circles visible at `YBNfHLlrJkg` 31:05 |
| Animated camera / 3D moves | Only in the intro CGI segments | Contact sheets |
| Looped background video | Only Cosmo Explains (the fixed room) | Contact sheets |

**Numbers to build against:**
- **98.6–99.9 % of body shots carry motion** (measured, 6,629 held pairs). Fully static images: 0.1–1.4 %.
- **Zoom magnitude: 3–5 % over the shot** (measured by Gemini on 2 videos; consistent with the residual signature elsewhere). Over a 20 s shot that is **0.15–0.25 % per second** — deliberately just at the edge of perception.
- **Direction alternates** between zoom-in and zoom-out; pans are usually diagonal and slow.

> **Can a simple automated Ken Burns template reproduce most of the effect? YES — HIGH confidence.**
> A single FFmpeg `zoompan` expression with a randomised in/out direction and a randomised 3–5 % end scale reproduces what these channels actually do. There is no parallax, no 3D, no per-image artistry. This is the single biggest automation win available.

---

## 5. Transitions (Step 7)

**Direct observation (Gemini, 2 videos):** crossfade, **~1.5 s** duration on `tvB659d_oik`; **1–1.5 s** on `_nLpB_Ao7zw`.

**Corroborating measurement across all 17:** at 10 s sampling a ~1.5 s crossfade lands inside a sample roughly 15 % of the time. Intermediate blended frames appear at exactly that rate in the storyboard timelines, and the histogram distance for those samples falls between the two clean populations — which is why a bimodal distribution with a small middle tail is what the data shows.

| | Value |
|---|---|
| **Dominant transition** | **Cross dissolve** |
| **Typical duration** | **1.0–1.5 s** |
| Transitions per minute | Identical to scene changes: **~3/min** in the body, **~7–9/min** in the first minute |
| Hard cuts | Used in the **intro only** (Gemini: `tvB659d_oik` intro is "24 cuts", hard-cut) |
| Dip to black | Only at the very start and very end of the video |
| Motion / blur / whip transitions | **Not observed anywhere** |
| Do transitions slow down later? | **Yes indirectly** — the *rate* drops 37–44 % after minute 10; the *duration* of each dissolve appears constant. LOW-MEDIUM confidence on constancy (only 2 videos directly observed). |

> **Simplest system that matches category standard:** one 1.2 s cross dissolve, applied to every cut, plus a 2 s fade-from-black at 0:00 and a 3–5 s fade-to-black at the end. **That is the entire transition design.** Anything more is invisible to this audience.

---

## 6. Brightness and colour (Step 8)

All values are means over the full runtime, on the 0–255 luminance scale.

| Channel | Brightness | Contrast (σ) | Saturation | Dark px (<32) | Near-black (<16) | Colourfulness | R / G / B | B−R |
|---|---|---|---|---|---|---|---|---|
| Sleep On Physics | **40.6** | 44.5 | **0.570** | 61.8 % | 46.4 % | 40.6 | 40.3 / 39.4 / 42.9 | +2.6 |
| Calm Science | 32.8 | 36.5 | 0.430 | 65.8 % | 47.6 % | 28.4 | 31.0 / 32.4 / 36.6 | +5.6 |
| Calm Space | 31.8 | 35.9 | 0.440 | 66.7 % | 49.5 % | 29.4 | 29.9 / 31.5 / 36.0 | +6.1 |
| **Sleepy Science** | **24.0** | 28.6 | **0.370** | **80.8 %** | **65.5 %** | 22.1 | 26.2 / 23.4 / 25.5 | **−0.7** |
| Cosmo Explains | 38.0 | 39.1 | 0.570 | 63.3 % | 47.5 % | 39.2 | 38.6 / 36.9 / 40.0 | +1.4 |

**Category is extremely dark.** Mean frame brightness 24–41 out of 255. **62–81 % of all pixels are below 32/255.** Roughly **half of every frame is essentially black.**

### Does the video get darker or calmer as it progresses?

| Channel | 0–10 min | 10–30 | 30–60 | 60–90 | 90–120 | Verdict |
|---|---|---|---|---|---|---|
| Sleep On Physics | **52.8** | 38.8 | 39.7 | 39.6 | 40.9 | **Bright open, −24 % then flat** |
| Calm Science | 32.5 | 34.3 | 32.1 | 32.4 | 34.6 | **Flat** |
| Calm Space | 31.2 | 30.5 | 34.3 | 30.6 | 32.8 | **Flat** |
| Sleepy Science | 29.2 | 28.1 | 26.3 | 25.3 | **18.7** | **Progressively darker, −36 % by the end** |
| Cosmo Explains | 37.9 | 37.6 | 38.4 | 38.7 | 37.8 | **Flat** |

**Answer: mostly no — with two important exceptions.**
- **Sleep On Physics front-loads brightness**: the first 10 minutes are 24 % brighter than the rest, then it flattens. That is a *hook* device, not a sleep ramp.
- **Sleepy Science Channel is the only channel that genuinely ramps down**: brightness falls monotonically 29.2 → 28.1 → 26.3 → 25.3 → **18.7** (−36 %) and edge density collapses 0.026 → 0.027 → 0.023 → 0.021 → **0.004** (−85 % in the final half-hour — frames become almost featureless). Their images literally get darker and simpler as the listener falls asleep. Given they are the largest channel in the sample, this is worth copying. Confidence: HIGH that it happens, LOW that it *causes* their performance.
- Calm Science / Calm Space / Cosmo hold brightness flat for the entire two hours.

### Palette
- **Cool blue-violet dominates** on four of five channels (B−R between +1.4 and +6.1).
- **Sleepy Science is the outlier and the leader** — the only warm-biased channel (B−R = −0.7), running deep amber/rust over near-black with occasional teal.
- Saturation splits into two clusters: **vivid** (Sleep On Physics 0.570, Cosmo 0.570) and **muted** (Calm Science 0.430, Calm Space 0.440, Sleepy Science 0.370).
- Contrast is low-to-moderate everywhere (σ 28.6–44.5); nobody uses punchy contrast.

---

## 7. Text and graphics (Step 9)

| Element | Sleep On Physics | Calm Science | Calm Space | Sleepy Science | Cosmo Explains |
|---|---|---|---|---|---|
| Burned-in subtitles | **No** | **No** | **No** | **No** | **Yes — every frame, ALL CAPS** |
| Chapter cards | No (0 chapters in metadata) | No | No | No | No |
| Titles / section headers | No | No | No | No | No |
| Equations / formulas | **No** | **No** | No | No | No |
| Diagrams / arrows / labels | **No** | **No** | No | No | No |
| Highlighted terms | No | No | No | No | No |
| Any on-screen text at all | **One subscribe-button overlay at ~1:05** | Not observed | Not observed | Not observed | Constant captions |

**Edge density corroborates this quantitatively.** Text and fine graphics raise edge density. Cosmo Explains measures **0.107** (highest, consistent with permanent captions and a detailed illustrated room). Sleepy Science measures **0.024** — one quarter of Cosmo's — consistent with a single soft object on black and nothing else.

> **The strongest channels avoid text entirely. The only channel that uses text has the worst views-per-video and the worst like rate in the sample.** That is a correlation across n=5 channels, not proof of causation — but it removes any argument that text is *required*. Confidence: HIGH that the convention is "no text"; MEDIUM that adding text would hurt.

### Classification

**ESSENTIAL** (present in every strong channel, do not skip)
- Nothing. There is no text element the category treats as essential.

**NICE TO HAVE** (defensible, low risk, may differentiate)
- One subscribe overlay at ~60 s (Sleep On Physics does this; it is the only text they use).
- A tiny, low-contrast episode title in the first 10 seconds — **untested in this category**, so treat as an experiment, not a default.

**UNNECESSARY / ACTIVELY RISKY**
- Burned-in subtitles (the losing channel's signature; also raises brightness and edge density in a category built on darkness).
- Equations, formulas, labelled diagrams, arrows — **zero** across 17 videos and ~2,200 minutes of runtime.
- Chapter cards and on-screen section headers — **zero** across the sample.
- Lower-thirds, name tags, source citations on screen.

---

## 8. What the visual layer actually is, in one paragraph

A 120-minute episode in this category is **~300–400 still images**, each held **17–22 seconds**, each carrying a **3–5 % Ken Burns zoom** in a randomly chosen direction, joined by a **1.0–1.5 second cross dissolve**, with a **persistent particle/dust overlay** and a **vignette**, graded so that **roughly half of every frame is near-black**, containing **no text, no diagrams, no chapters and no captions**, opening with a **denser, brighter, hand-cut 1–3 minute intro** that on some channels uses **real stock footage of people**, and ending on a **fade to black**. Everything else is variation.
