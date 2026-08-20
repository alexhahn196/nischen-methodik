# 12 — Repeatable Workflow: Topic Idea → Published Video

Covers brief step 27. Human minutes are given for the **optimised** state (roughly episode 10 onward); first-episode times run ~2× higher.

---

## Pipeline overview

```
TOPIC → RESEARCH → OUTLINE → SCRIPT → FACT CHECK → TTS → PROMPTS → IMAGES
   → ASSET MATCH → EDIT → AUDIO MIX → THUMBNAIL → QC → EXPORT → UPLOAD
```

**Total human time: ~3.9 h/episode · Total machine time: ~3.5–6.5 h (unattended, overlapping)**

---

## Stage detail

### 1. Topic selection — 5 min human
- Pull competitor catalogues free: `yt-dlp --flat-playlist -J "https://www.youtube.com/channel/<ID>/videos"` gives every title and view count in one call.
- Rank candidate topics by competitor views-per-video, not by subscriber count.
- Check RPM per topic (physics measured at $18–20 vs space at $14).
- **Maintain a 20-topic backlog** so this stage never blocks the week.
- **Content mix:** 55 % fundamental physics · 40 % cosmic physics · 5 % experimental.
- **Title formula that dominates this niche** (measured across the sample): `What Is X Actually Made Of?` · `Where Does X Get Its Y From?` · `Why X Cannot Y` · `No One Knows If X`. Open-question titles carry the category.

### 2. Research — 40 min human / 10 min machine
- LLM with web search produces a source-backed brief: the accepted mechanism, the common misconception, the historical experiment, the open question, the cosmic-scale analogue.
- **Collect the specific numbers you will speak aloud** — magnitudes, dates, names. These are what get fact-checked later.
- **Output:** `research.md` with inline source links.

### 3. Outline — 10 min human / 5 min machine
- Map the brief onto the fixed 9-movement spiral (`07_120min_blueprint.md`).
- Assign a word budget per movement (total 16,000).
- Place the 6–8 core-claim restatements explicitly, each **worded differently**.
- **Output:** `outline.json` — movement, role, word budget, key claims, restatement text.

### 4. Script — 10 min human / 20–40 min machine
- Generate **one movement per LLM call**, not one 16,000-word generation. Single-shot long generation degrades badly.
- Pass the previous movement's last 300 words as context for continuity.
- Enforce per movement: mean sentence 13 words · FK grade 9.0–9.5 · 20–26 jargon terms/1,000 w · 1–2 questions · 1–2 analogies.
- **Never open with "Tonight, we're going to…"** — used by 9 of 17 sampled videos.
- **The word "sleep" appears zero times.**
- **Output:** `script.md` + `script_stats.json` (auto-computed WPM, FK, sentence length, jargon density).

### 5. Fact check — 25 min human / 10 min machine
- Automated pass: a **different** model verifies every numeric claim, name and date against the research brief; flags anything unsupported.
- **Human pass: read the entire script. ~60 min, counted in stage 4's read-through below.**
- Physics errors are the one failure this audience punishes — the comment sections contain working physicists and retired engineers.
- **Output:** `factcheck_report.md`, all flags resolved before proceeding.

### 5b. Human script read-through — 60 min human
- Read all 16,000 words. Non-skippable, non-compressible.
- Check specifically: hallucinated specifics · verbatim repeats (the spiral must reword, never repeat) · the hook lands its question before 0:58 · the CTA sits at 58–62 s.

### 6. TTS — 5 min human / 20–40 min machine
- Apply the pronunciation lexicon before synthesis.
- Generate **per paragraph**, concatenate — a single 128-minute call is fragile and un-resumable.
- Auto-detect anomalies: paragraph duration outside expected WPM ±20 % usually means a mangled term or a dropped segment.
- **Output:** `narration.wav` + `timing.json` (word/paragraph timestamps — this drives asset placement).

### 7. Visual prompt generation — 5 min human / 5 min machine
- For each ~20 s slot, derive a subject from the surrounding script text.
- Append the **fixed style suffix** verbatim (see `08_example_episode.md` §3). The suffix is what makes 350 images look like one channel.
- Query the asset library first: reuse anything semantically matching that has not appeared in the last 3 episodes.
- **Output:** `prompts.json` — slot, timestamp, prompt, model tier (hero vs bulk), reuse-candidate ID.

### 8. Image generation — 5 min human / 40–90 min machine
- ~175 bulk on a fast model, ~25 hero on a higher-quality model.
- Generate at 3840×2160 (needed for jitter-free `zoompan`).
- Auto-retry failures; log every failure.
- **Output:** `assets/` + `assets_index.json`.

### 9. Asset matching and QC — 20 min human
- Auto-build a contact sheet of all ~200 new images.
- **Human scans it once.** Reject malformed anatomy, accidental text, wrong subject, over-bright frames.
- Auto-check: mean luminance in 20–45/255, no near-duplicates by perceptual hash, no duplicate placement within 15 minutes.
- Regenerate rejects in one batch.

### 10. Editing — 5 min human / 10 min machine
- **Body (3:00–end): fully automatic.** Python reads `timing.json` + `prompts.json`, emits an FFmpeg graph — `zoompan` (3–5 %, random direction, ~35 % pan), `xfade` 1.2 s, particle overlay, vignette, grade.
- Duration schedule: 7 s (0–3 min) → 12 s (3–10) → 20 s ±20 % (10–end). Ceiling 45 s.
- **Intro (0:00–3:00): hand-cut in DaVinci Resolve.** ~25 shots, hard cuts, brighter, no music. The only human editing in the whole pipeline.
- **Output:** `body.mp4`, `intro.mp4`.

### 11. Audio mix — 5 min human / 5 min machine
- Music bed enters at ~1:05, ~20 dB under narration, one loop, thinning from ~110:00.
- Light 2:1 slow compression on narration.
- Normalise to −14 LUFS integrated, true peak ≤ −1 dBTP.
- **Output:** `mix.wav`.

### 12. Thumbnail — 10 min human
- Generate 3–4 candidates from the episode's hero image.
- Dark, one object, large negative space, minimal or no text — consistent with the frame identity.
- **Output:** `thumb.jpg` (1280×720).

### 13. Quality control — 20 min human
- Run the automated checks in `13_quality_control_checklist.md`.
- **Watch 8 fixed timestamps** for 30 s each: 0:00, 0:58, 3:00, 10:00, 30:00, 60:00, 90:00, end−0:30.
- Any red-flag item blocks publication.

### 14. Export — 2 min human / 60–150 min machine
- Concatenate intro + body, mux `mix.wav`.
- H.264 CRF 20–22, 1080p30, AAC 192k, **plus light grain/dither** to prevent banding in the dark gradients.
- Generate the caption track with Whisper from your own narration WAV. **Upload it as a track — never burn it in.**
- **Output:** `final.mp4`, `captions.srt`.

### 15. Upload package — 10 min human / 15 min machine
- Title from the measured formulas (stage 1).
- Description: 1,000–2,600 characters (competitor range measured 1,055–2,581).
- **No chapters** — 0 of 17 sampled videos use them.
- Tags from competitor tag sets.
- **Publishing is manual. Always.**

---

## Weekly operating rhythm at 3 uploads/week (~12 h)

| Day | Work | Human time |
|---|---|---|
| **Mon** | Topics + research for all 3 episodes; kick off scripts | 2.5 h |
| **Tue** | Read-through + fact check, episodes 1 & 2 | 3 h |
| **Wed** | Read-through + fact check episode 3; TTS all 3; start image batches | 2.5 h |
| **Thu** | Asset QC all 3; cut the 3 intros | 2 h |
| **Fri** | Assemble, mix, thumbnails, QC, export | 1.5 h |
| **Sat/Sun** | Publish on schedule; monitor comments | 0.5 h |

**Batching is what makes 3/week sustainable.** Running three episodes through each stage together roughly halves per-episode overhead versus running them end-to-end one at a time.

---

## Where the pipeline will break (from what the measurements suggest)

| Failure | Symptom | Guard |
|---|---|---|
| **Visual repetition** | Same nebula twice in 10 minutes | Perceptual-hash duplicate check + `last_used_episode` in the asset library |
| **Script self-repetition** | A viewer literally complained: *"after hearing the same thing three times I couldn't take it any more"* | Auto-flag any 8-gram repeating >2× verbatim; the spiral must reword |
| **Physics errors** | Corrections in the comments | Two-model fact check + full human read |
| **TTS mangling terms** | Mispronounced jargon | Pronunciation lexicon, extended every episode |
| **Zoom jitter** | Visible stepping on slow zooms | Render stills at 2×, then downscale |
| **Banding in dark gradients** | Blocky sky under YouTube's transcode | Add light grain before encode |
| **Single-shot script degradation** | Quality collapses after ~5,000 words | Generate movement by movement |
