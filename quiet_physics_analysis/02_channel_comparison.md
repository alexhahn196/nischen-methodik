# 02 — Channel Comparison

**Sample:** 17 videos across 5 channels · **Measured:** 2026-08-20 · All numbers below are measured unless marked ESTIMATE.

---

## 0. How this was measured (read this before trusting any number)

| Layer | Source | Coverage | Status |
|---|---|---|---|
| Metadata | `yt-dlp` (mweb client) | 17/17 videos, plus full catalogues of all 5 channels (761 long-form videos) | **Complete** |
| Visual timeline | YouTube storyboard strip (`sb0`, 320×180 tiles), fetched directly | 17/17 videos, **full runtime**, 1,502 sheets → ~13,600 frames, mean sampling interval **9.95 s** | **Complete** |
| Scene / asset change | OpenCV: per-video temporal-variance mask + HSV 12×6×6 histogram Bhattacharyya distance | 17/17 videos | **Complete, calibrated** |
| Script | YouTube auto-caption tracks, de-overlapped into a timestamped word stream | 17/17 videos (11,950–22,511 words each) | **Complete** |
| Frame-level visual classification | Direct inspection of contact sheets by the analyst | 9 videos inspected in detail, all 17 sampled | **Partial but broad** |
| Multimodal shot lists (ground truth) | Gemini video-understanding (visuals **and** audio) | **2 videos only** — tool capped at 15 calls / 24 h and the cap was hit | **Severely limited** |
| Audio waveform | — | **NONE** | **Not available** |

### The one thing you must know about the audio findings
**Media streams for these videos are authentication-gated and I did not circumvent that.** I never heard a single second of any of these videos. Every audio statement in `04_audio_voice_analysis.md` is derived from *indirect* evidence (caption `[Music]` annotations, caption-derived word timing, viewer comments) or from the two videos the multimodal tool reached before the rate limit. **Pitch, LUFS, RMS, dynamic range, pause length and human-vs-TTS were not measured and are labelled LOW confidence throughout.**

### Detector calibration (why the visual numbers are trustworthy)
The "new visual asset" threshold (Bhattacharyya distance > 0.40) was validated against three independent ground truths before being applied:

| Validation set | Window | Ground truth | Detector | Match |
|---|---|---|---|---|
| Gemini shot list, `tvB659d_oik` | 30:00–33:00 | 13 changes | 13 | **Exact** |
| Manual frame inspection, `YBNfHLlrJkg` | 30:00–33:00 | 5 changes | 5 | **Exact** |
| Manual frame inspection, `gmq4gqCytlY` | 30:00–33:00 | ~11 changes | 10 | Within 1 |

Threshold sensitivity (0.30 / 0.40 / 0.50 / 0.60) is stored per video in `analysis_data.json`.

**Known resolution limit:** 10 s sampling cannot resolve shots shorter than ~10 s. In the **first 60 seconds** of Sleep On Physics, Calm Science and Calm Space the detector saturates (6–7 changes/min = every sample differs), so the opening cut rate is a **lower bound**, not a measurement. Gemini's shot list on `tvB659d_oik` puts the true opening rate at ~7.5 s/asset and on `_nLpB_Ao7zw` at ~6.4 s/asset.

---

## 1. The channels at a glance

| | **Sleep On Physics** | **Calm Science** | **Calm Space** | **Sleepy Science Ch.** | **Cosmo Explains** |
|---|---|---|---|---|---|
| Handle | @SleepOnPhysics | @CalmScienceToSleep | @CalmSpaceToSleep | @SleepyScienceChannel | @CosmoExplainsYT |
| Subscribers | 28,100 | 5,720 | 93,900 | **328,000** | 22,800 |
| Long-form videos | 123 | 29 | 185 | 290 | 134 |
| Total views | 2.92 M | 0.65 M | 12.9 M | **33.4 M** | 1.59 M |
| **Views per video** | 23,762 | 22,296 | 69,837 | **115,140** | **11,833** |
| Uploads / week | **6.1** | 2.9 | 5.8 | 5.0 | **6.8** |
| Median duration | 119 min | 131 min | 129 min | 137 min | 130 min |
| Like rate (sample) | 1.9–3.1 % | 2.3–2.7 % | 1.5–2.8 % | 1.3–1.7 % | **1.0–2.2 %** |
| RPM (NexLev est.) | **$18.21** | **$19.04** | $14.26 | $20.10 | not sampled |

**Views-per-video is the honest performance metric here**, not subscribers — Calm Science has 5× fewer subs than Cosmo Explains but nearly 2× the views per video.

---

## 2. Production fingerprints (all measured)

| Metric | Sleep On Physics | Calm Science | Calm Space | Sleepy Science | Cosmo Explains |
|---|---|---|---|---|---|
| **Seconds per visual asset** | 19.2 | 21.8 | 20.5 | 20.6 | 17.7 |
| **Unique assets per 120 min** | **394** | **331** | **351** | **350** | **408** |
| Visual changes / min | 3.28 | 2.76 | 2.93 | 2.92 | 3.40 |
| **Letterbox** | 0 % (full-bleed 16:9) | **20 % (2.39:1)** | **20 % (2.39:1)** | 0 % (full-bleed) | 0 % (full-bleed) |
| Mean brightness (0–255) | 40.6 | 32.8 | 31.8 | **24.0** | 38.0 |
| Mean saturation | **0.570** | 0.430 | 0.440 | **0.370** | 0.570 |
| Dark pixels (<32/255) | 61.8 % | 65.8 % | 66.7 % | **80.8 %** | 63.3 % |
| Colour bias (B−R) | +2.6 | +5.6 | +6.1 | −0.7 (warm) | +1.4 |
| Edge density (detail/text proxy) | 0.086 | 0.075 | 0.070 | **0.024** | **0.107** |
| **Words per minute** | **143.4** | **120.3** | 118.7 | 125.0 | 130.1 |
| Total words / video | 17,623 | 15,985 | 15,883 | 17,728 | 16,860 |
| Flesch–Kincaid grade | **9.4** | 9.1 | 9.0 | 9.2 | 9.0 |
| Flesch reading ease | 52.2 | 52.5 | 52.2 | 54.1 | 55.9 |
| **Physics jargon / 1,000 w** | **26.3** | **21.3** | 3.4 | 2.4 | 5.2 |
| Questions / hour | 11.8 | 8.3 | 8.5 | **0.3** | 10.5 |
| Analogy markers / hour | 17.9 | 7.9 | 7.2 | 13.7 | 10.4 |
| Mean sentence length (words) | 14.1 | 13.0 | 12.4 | 14.1 | 14.3 |
| "you/your" per 1,000 w | 8.6 | 7.6 | 6.5 | 12.6 | 12.9 |
| **First CTA** | **59–63 s** | **55–75 s** | **47–67 s** | **67–87 s** | **none** |
| Chapters | **0** | **0** | **0** | **0** | **0** |
| `[Music]` caption coverage | 67.7 % | 12.1 % | 13.3 % | **74.7 %** | **0 %** |
| **Front-loading** (cuts/min, 0–10 min → 30–120 min) | **−44 %** | **−37 %** | **−40 %** | −9 % | **+8 %** |

---

## 3. Findings that change the plan

### 3.1 Calm Science and Calm Space are almost certainly the same operator — HIGH confidence
Five independent fingerprints line up:

1. **Channel descriptions are the same template.** Calm Space: *"Welcome to Calm Space to Sleep 🪐 / We make long-form **space** documentaries for those nights when your mind needs somewhere vast and quiet to wander. Our videos move slowly through the cosmos… Everything is carefully researched but never overwhelming. Just gentle narration, slow visuals, and space to unwind."* Calm Science: same sentences, `space` → `science`.
2. **Identical letterbox spec** — both exactly 20 % of frame height (2.39:1); the other three channels are full-bleed.
3. **Identical CTA construction, verbatim within each channel.** Calm Space: *"Before we get started, if you love exploring the depths of space as much as we do, take a second to like the video or subscribe."* Calm Science: *"Before we begin, if you enjoy these topics as much as we do, make sure to like the video or subscribe."*
4. **Identical opener grammar** — 7 of 7 sampled videos across both channels start with "Tonight, we're going to…".
5. **Near-identical colour/pacing stats** — saturation 0.430 vs 0.440, brightness 32.8 vs 31.8, WPM 120.3 vs 118.7, s/asset 21.8 vs 20.5.

**Why this matters to you:** Calm Science *is* the experiment you are proposing — an operator with a proven 93.9k-sub space channel spinning the same production template into physics. It is 29 videos old and already averaging 22,296 views/video, matching Sleep On Physics (123 videos) on views-per-video. That is the single most useful data point in this entire analysis: **the playbook transfers, and it transfers fast.**

### 3.2 The whole category runs at 3–7 uploads/week — MEDIUM-HIGH confidence
Measured from catalogue position vs. upload date: Cosmo Explains 6.8/wk, Sleep On Physics 6.1/wk, Calm Space 5.8/wk, Sleepy Science 5.0/wk, Calm Science 2.9/wk. Your 3/week target is at the **bottom** of the range and matches Calm Science exactly — which is the only channel proving that low cadence still works.

### 3.3 Nobody uses chapters. Nobody uses on-screen text (except the weakest channel) — HIGH confidence
0 chapter markers in 17/17 videos. Sleep On Physics, Calm Science, Calm Space and Sleepy Science have **no burned-in captions, no titles, no equations, no labels, no diagrams** anywhere in the body. Cosmo Explains burns in ALL-CAPS subtitles on every single frame — and has the **lowest views/video (11,833) and lowest like rate (0.96–2.2 %)** in the sample.

### 3.4 The visuals are decoupled from the script on the two priority channels — HIGH confidence
`tvB659d_oik` ("Where Does Light Get Its Speed From?") shows generic nebulae for 121 of its 124 minutes. `-n6HdllViRU` ("The True Scale of a Single Atom") shows only galaxies and nebulae. `Ty6ZMyFagsU` ("What Voyager Detected at The Edge of Our Solar System") shows generic nebulae. Gemini's verdict on `tvB659d_oik`: *"templated AI nebula wallpaper cut on an almost exact 20.0-second grid and entirely decoupled from the script."*

Two viewers said so out loud, unprompted, in the top comments of `BLPBP5BaU-0`:
> *"This documentary is excellent, but it would be even stronger with animations that visually explain the concepts being discussed."*
> *"Great script. I wish you would have had a video to go along with the script."*

The video has 79,844 views in 7 days regardless. **Visual-script coupling is an upside lever, not an entry requirement.**

### 3.5 Sleepy Science Channel already owns the visual identity you described — HIGH confidence
Your stated plan — *near-black backgrounds, one dominant scientific object, deep negative space, no faces, minimal text, warm amber highlights* — is a frame-by-frame description of the 328k-sub market leader. Measured: brightness 24.0 (darkest in sample), 80.8 % dark pixels, saturation 0.370 (lowest), edge density 0.024 (**one third** of everyone else = massive negative space), colour bias warm (B−R = −0.7, the only warm channel). See `03_visual_analysis.md` §7 for what to do about this.

### 3.6 The category's biggest cost lever is already proven safe — HIGH confidence
Sleep On Physics **halved its editing effort mid-catalogue and did not get punished**:

| Video | Upload | s/asset | Assets/120 min | Views/day |
|---|---|---|---|---|
| `_nLpB_Ao7zw` | 2026-04-03 | 15.7 | 459 | 1,637 |
| `tvB659d_oik` | 2026-07-16 | 14.4 | 499 | 4,525 |
| `YBNfHLlrJkg` | 2026-08-04 | 24.3 | 296 | 746 |
| `BLPBP5BaU-0` | 2026-08-13 | 22.4 | 322 | **11,406** |

They went from ~500 assets to ~300 assets per video, and their best-performing recent video on a per-day basis is one of the *cheap* ones. Views/day is inflated for young videos, so this is **not** proof that fewer assets is better — but it is solid evidence that **300 assets is not a competitive handicap**. Confidence: MEDIUM (n=4, age-confounded).

---

## 4. Per-video sample detail

| Channel | Class | Video | Date | Min | Views | V/day | s/asset | Assets/120m | WPM | Q/h | 1st CTA |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Sleep On Physics | Breakout-AllTime | `_nLpB_Ao7zw` | 2026-04-03 | 108.5 | 227,546 | 1,637 | 15.7 | 459 | 158.0 | 21.6 | 61.6 s |
| Sleep On Physics | Breakout-Modern | `tvB659d_oik` | 2026-07-16 | 123.9 | 158,383 | 4,525 | 14.4 | 499 | 143.0 | 7.3 | 59.3 s |
| Sleep On Physics | Recent-Median | `YBNfHLlrJkg` | 2026-08-04 | 130.4 | 11,929 | 746 | 24.3 | 296 | 136.9 | 9.7 | 62.9 s |
| Sleep On Physics | Recent-Strong | `BLPBP5BaU-0` | 2026-08-13 | 130.8 | 79,844 | 11,406 | 22.4 | 322 | 135.9 | 8.7 | 59.4 s |
| Calm Science | Breakout | `Nq-wJpo8Hk4` | 2026-06-29 | 132.9 | 91,004 | 1,750 | 21.3 | 339 | 118.0 | 10.8 | 64.6 s |
| Calm Science | Breakout-Controlled | `LxDfEBostXk` | 2026-07-31 | 134.3 | 80,342 | 4,017 | 22.1 | 325 | 121.8 | 10.7 | 64.4 s |
| Calm Science | Recent-Median | `-n6HdllViRU` | 2026-08-14 | 130.6 | 9,266 | 1,544 | 21.2 | 339 | 120.0 | 2.3 | 75.0 s |
| Calm Science | Recent-Strong | `lqZntA10Q5g` | 2026-08-10 | 133.4 | 63,899 | 6,390 | 22.4 | 322 | 121.6 | 9.4 | 55.3 s |
| Calm Space | Breakout | `Ty6ZMyFagsU` | 2026-02-18 | 142.2 | 1,770,220 | 9,673 | 19.8 | 363 | 112.9 | 13.5 | 66.6 s |
| Calm Space | Median | `Lgu_Oq8_J5I` | 2026-06-23 | 131.9 | 23,812 | 411 | 20.6 | 350 | 122.5 | 9.1 | 66.0 s |
| Calm Space | Recent-Strong | `o2eIwICmo7w` | 2026-08-11 | 127.9 | 100,812 | 11,201 | 21.1 | 341 | 120.7 | 2.8 | 47.1 s |
| Sleepy Science | Breakout | `xg8ieJQIB70` | 2025-07-25 | 120.0 | 2,353,340 | 6,019 | 21.4 | 336 | 99.6 | 0.5 | 87.2 s |
| Sleepy Science | Median | `A0vVW7PWnm4` | 2026-03-17 | 134.7 | 44,875 | 288 | 22.1 | 325 | 139.0 | 0.4 | 81.1 s |
| Sleepy Science | Recent-Strong | `BA59TWIMNG4` | 2026-08-10 | 165.0 | 39,948 | 3,995 | 18.4 | 390 | 136.4 | 0.0 | 66.6 s |
| Cosmo Explains | Breakout | `gmq4gqCytlY` | 2026-05-12 | 126.7 | 198,908 | 1,989 | 16.0 | 449 | 130.2 | 14.7 | none |
| Cosmo Explains | Recent-Median | `WHh8Q-gNZAk` | 2026-08-08 | 129.3 | 4,017 | 335 | 17.9 | 402 | 129.6 | 9.7 | none |
| Cosmo Explains | Recent-Strong | `xXuMfbr0V9o` | 2026-08-10 | 132.7 | 30,325 | 3,033 | 19.3 | 374 | 130.6 | 7.2 | none |

Full selection rationale per video: `01_video_sample.csv`. Every metric per video: `analysis_data.json`.

---

## 5. Caveats you should hold onto

- **Two sampled breakouts are from an older production era.** `Ty6ZMyFagsU` sits at catalogue position 151/185 and `xg8ieJQIB70` at 275/290. Their style may not reflect what those channels do today. They are included because the brief asked for outliers; they are **not** used to define "current category standard".
- **Views/day is age-biased.** YouTube front-loads impressions. A 7-day-old video's views/day is not comparable to a 139-day-old video's. Where I use it, I say so.
- **No retention data exists** for any competitor channel and none is inferred anywhere in this analysis.
- **n = 3–4 videos per channel.** Within-channel correlations between production choices and performance are **not statistically meaningful** and are labelled LOW confidence wherever they appear.
