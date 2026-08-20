# 13 — Quality Control Checklist

Covers brief step 28. Designed to run in **~20 minutes of human time** per episode, with automated checks doing the sweep and the human doing the judgement.

**Rule: any 🔴 item blocks publication. 🟡 items are logged and fixed next episode.**

---

## A. Automated pre-flight (runs unattended — ~5 min machine)

| # | Check | Method | Threshold | Severity |
|---|---|---|---|---|
| A1 | Runtime in band | `ffprobe` duration | 105–135 min | 🔴 |
| A2 | Narration starts on time | first word in `timing.json` | ≤ 1.0 s | 🔴 |
| A3 | Narration coverage | speech seconds ÷ runtime | ≥ 97 % | 🔴 |
| A4 | Words per minute | word count ÷ runtime | 120–132 | 🟡 |
| A5 | WPM drift across the video | per-10-min buckets | max−min ≤ 15 wpm | 🟡 |
| A6 | Reading grade | Flesch–Kincaid on script | 9.0–9.5 | 🟡 |
| A7 | Mean sentence length | script parse | 12–15 words | 🟡 |
| A8 | Jargon density | term list ÷ 1,000 words | 20–26 | 🟡 |
| A9 | Question count | sentences ending `?` | 10–12 per hour | 🟡 |
| A10 | **Verbatim repetition** | any 8-gram repeating > 2× | **0 occurrences** | 🔴 |
| A11 | Near-verbatim repetition | any 6-gram repeating > 4× | ≤ 12 | 🟡 |
| A12 | **The word "sleep"** | literal search | **0 occurrences** | 🔴 |
| A13 | "Tonight" count | literal search | ≤ 1, first sentence only | 🟡 |
| A14 | CTA placement | timestamp of CTA text | 55–65 s | 🔴 |
| A15 | CTA count | pattern match | 1, or 2 with the second in the final 3 min | 🟡 |
| A16 | Asset count | manifest | 300–400 placed | 🟡 |
| A17 | **Max shot length** | manifest | **≤ 45 s** | 🔴 |
| A18 | Min shot length (body) | manifest, after 10:00 | ≥ 14 s | 🟡 |
| A19 | Cut-rate front-loading | 0–10 min vs 30–120 min | first 10 min ≥ 1.4× body | 🟡 |
| A20 | **Duplicate asset proximity** | perceptual hash | no repeat within 15 min | 🔴 |
| A21 | Cross-episode reuse | asset library `last_used_episode` | not used in the last 3 episodes | 🟡 |
| A22 | Mean frame brightness | sampled frames | 28–36 / 255 | 🟡 |
| A23 | **Brightness spike** | any frame | no frame > 120 / 255 mean | 🔴 |
| A24 | Brightness trend | first 10 min vs last 20 min | non-increasing | 🟡 |
| A25 | Saturation | sampled frames | 0.40–0.50 | 🟡 |
| A26 | **Integrated loudness** | `ffmpeg -af ebur128` | −14 LUFS ± 1 | 🔴 |
| A27 | **True peak** | `ffmpeg -af ebur128` | ≤ −1 dBTP | 🔴 |
| A28 | **Loudness spike** | short-term LUFS | no 3 s window > +6 LU over integrated | 🔴 |
| A29 | **Audio dropout** | silence detect on narration | no gap > 3 s before 110:00 | 🔴 |
| A30 | Music bed entry | first music energy | ≥ 55 s | 🟡 |
| A31 | Music-to-voice ratio | RMS of bed vs narration | 16–24 dB below | 🟡 |
| A32 | **On-screen text** | OCR sweep of 200 sampled frames | **0 detections after 1:30** | 🔴 |
| A33 | Chapters in metadata | upload payload | **0** | 🔴 |
| A34 | Encode sanity | `ffprobe` | 1920×1080, 30 fps, ≥ 8 Mbps or CRF ≤ 22 | 🔴 |
| A35 | Grain/dither applied | filter chain present | yes | 🟡 |

---

## B. Human spot-check — 8 timestamps × 30 s (~10 min)

Watch each with **sound on**.

| Timestamp | What you are checking |
|---|---|
| **0:00–0:30** | Narration on frame one · no logo · no music · hard cuts · brightest section · hook is concrete and escalating |
| **0:52–1:20** | The question lands before 0:58 · CTA runs 15–18 s · music enters under it · the seam is not jarring |
| **3:00–3:30** | Template has taken over cleanly · crossfades not hard cuts · pace has settled |
| **10:00–10:30** | Body rate reached (~3 cuts/min) · 20 s holds · zoom perceptible but not distracting |
| **30:00–30:30** | Still coherent · images not repeating · no dead air |
| **60:00–60:30** | Midpoint fatigue check — would *you* still be listening? |
| **90:00–90:30** | Visual simplification present · nothing has re-escalated |
| **end−0:30** | Fade to black over 3–5 s · no end card · no outro animation · not stimulating |

---

## C. Scientific accuracy — 🔴 gate

| # | Check |
|---|---|
| C1 | Every **number** spoken aloud traces to a source in `research.md` |
| C2 | Every **name and date** verified — misattributed discoveries are the most-corrected error in competitor comments |
| C3 | Every **analogy** is followed by its limits. An unqualified analogy reads as a misconception |
| C4 | No **overclaiming**: "scientists believe" ≠ "scientists have proven". Open questions stay open |
| C5 | No invented experiments, papers, institutions or quotations |
| C6 | Units and orders of magnitude are internally consistent throughout |
| C7 | The two-model fact-check report has **zero unresolved flags** |
| C8 | **A human has read all 16,000 words.** No exceptions, ever |

---

## D. Hallucination and LLM-tell sweep

| # | Check | Severity |
|---|---|---|
| D1 | No "In conclusion", "Let's dive in", "buckle up", "It's important to note" | 🟡 |
| D2 | No numbered/bulleted list structures read aloud — this is prose | 🟡 |
| D3 | No self-reference to being an AI, a script, or a video | 🔴 |
| D4 | No stray markdown, headers or stage directions surviving into the TTS text | 🔴 |
| D5 | Sentence-length variance present — uniform length is the strongest LLM tell in narration | 🟡 |
| D6 | No paragraph opens with the same word as the previous paragraph more than twice in a row | 🟡 |
| D7 | Transitions between movements are motivated, not "Now let's talk about…" | 🟡 |

---

## E. Audio and TTS artefacts

| # | Check | Severity |
|---|---|---|
| E1 | Every physics term pronounced correctly (**listen to the specific terms**, do not assume) | 🔴 |
| E2 | No clipped or truncated words at paragraph joins — the classic per-paragraph TTS concatenation failure | 🔴 |
| E3 | No audible level jump at concatenation seams | 🔴 |
| E4 | No robotic artefacts, glitches or stutters | 🔴 |
| E5 | No unnatural emphasis on function words ("the", "of", "and") | 🟡 |
| E6 | Inter-sentence pauses consistent; no accidental long gaps | 🟡 |
| E7 | Music loop point inaudible | 🟡 |
| E8 | Nothing in the audio is startling — no transient could wake a sleeping listener | 🔴 |
| E9 | Add any newly-mangled term to the pronunciation lexicon before the next episode | 🟡 |

---

## F. Visual defects

| # | Check | Severity |
|---|---|---|
| F1 | No malformed AI artefacts (impossible geometry, melted structures, garbled detail) | 🔴 |
| F2 | **No accidental text, letters, numbers or watermarks** in any generated image | 🔴 |
| F3 | No human faces or hands anywhere (unless deliberately used in the intro) | 🔴 |
| F4 | No image visibly repeats within 15 minutes | 🔴 |
| F5 | No image reused from the last 3 episodes | 🟡 |
| F6 | No accidental fast cuts — nothing shorter than 5 s after 3:00 | 🔴 |
| F7 | No banding in dark gradients on the encoded file (**check the encode, not the source**) | 🔴 |
| F8 | Zoom motion smooth, no stepping or jitter | 🔴 |
| F9 | Zoom magnitude perceptible but not distracting (3–5 % over the shot) | 🟡 |
| F10 | Crossfades consistent at ~1.2 s | 🟡 |
| F11 | Particle overlay subtle, never a focal point | 🟡 |
| F12 | Style consistent across all ~350 assets — no image looks like it came from a different channel | 🟡 |
| F13 | Images match the subject being discussed (**our differentiator — do not let this drift**) | 🟡 |

---

## G. Copyright and platform risk — 🔴 gate

| # | Check |
|---|---|
| G1 | Every music track has a documented licence covering monetised YouTube use |
| G2 | Any stock footage licence covers commercial monetised use |
| G3 | No recognisable copyrighted characters, logos, brands or trademarks in generated images |
| G4 | No real identifiable person depicted |
| G5 | Thumbnail contains no third-party imagery |
| G6 | No copyrighted text read aloud beyond fair-use quotation |
| G7 | Content ID check clean after upload, before the video goes public |
| G8 | Metadata does not impersonate another channel or use a competitor's channel name |

---

## H. Packaging

| # | Check | Severity |
|---|---|---|
| H1 | Title follows a measured category formula, no clickbait overclaim | 🟡 |
| H2 | Title has no typos (checked character by character) | 🔴 |
| H3 | Description 1,000–2,600 characters | 🟡 |
| H4 | **No chapters** | 🔴 |
| H5 | Caption track uploaded, **not burned in** | 🔴 |
| H6 | Thumbnail is dark, single-object, readable at 168×94 px | 🟡 |
| H7 | Thumbnail matches the actual content | 🔴 |
| H8 | Correct visibility, schedule and playlist | 🔴 |
| H9 | "Made for kids" set correctly | 🔴 |

---

## I. The five failures that will actually sink this channel

Ranked by evidence from the sample, not by theory.

1. **🔴 A physics error.** The comment sections of these channels are full of physicists, engineers and retired teachers. One confidently wrong mechanism, repeated six times by the spiral structure, is the fastest credibility loss available. *Guard: C1–C8.*
2. **🔴 Script self-repetition.** Directly observed: *"great content but after hearing the same thing three times I couldn't take it any more bummer it's really interesting."* The spiral must **reword**, never repeat. *Guard: A10, A11.*
3. **🔴 Visual repetition.** The one thing you can see happening in competitor videos — near-identical nebulae recurring within minutes. *Guard: A20, A21, F4, F5.*
4. **🔴 An audio transient that wakes the listener.** A loudness spike, a hard music entry, a click at a concatenation seam. The product is sleep-compatible listening; a startle is a total product failure. *Guard: A26–A29, E2, E3, E8.*
5. **🟡 Style drift away from topic-matched imagery.** Your only measured differentiator is that the pictures show the thing being discussed. The path of least resistance is to slide back into generic nebulae — because that is what the prompt library will happily produce. *Guard: F13, reviewed every 5 episodes.*
