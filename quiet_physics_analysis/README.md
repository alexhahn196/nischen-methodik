# Quiet Physics / Cosmic Physics — Competitor Production Reverse-Engineering

Reverse-engineering of how the strongest channels in the **quiet physics / cosmic physics** sleep-documentary niche actually construct their videos, so that a repeatable production SOP can be built for a target cost of **$20–50 per 2-hour episode**.

**Analysed:** 5 channels · **17 videos** · ~2,200 minutes of runtime · ~13,600 sampled frames · 6,629 measured image-pairs · ~280,000 transcript words · ~77 viewer comments
**Date:** 2026-08-20

---

## Read in this order

| # | File | What it answers |
|---|---|---|
| — | **`10_final_recommendation.md`** | **Start here.** Which channel to model, and the 15 executive answers |
| 1 | `01_video_sample.csv` | The 17 videos, why each was selected, and their metrics |
| 2 | `02_channel_comparison.md` | Methodology, detector calibration, channel-by-channel comparison, the findings that change the plan |
| 3 | `03_visual_analysis.md` | Visual sources · scene-change frequency · **how many assets a 2-hour video needs** · motion · transitions · brightness/colour · text |
| 4 | `04_audio_voice_analysis.md` | Narration pacing, music, voice — **and an explicit account of what could not be measured** |
| 5 | `05_editing_analysis.md` | Intro patterns · script structure · editing intensity over time · retention proxies · complexity scores · automation · the editing template |
| 6 | `06_production_sop.md` | Must-match / nice-to-have / waste-of-money · differentiation · **the full production specification** |
| 7 | `07_120min_blueprint.md` | Section-by-section timeline blueprint for a 120-minute episode |
| 8 | `08_example_episode.md` | Worked example: *"What Is Empty Space Actually Made Of?"* — first 60 s of narration, first 20 assets with prompts |
| 9 | `09_cost_model.md` | $20 / $35 / $50 builds, human hours, monthly economics |
| 10 | `11_production_stack.md` | Exact tools, and what was deliberately rejected |
| 11 | `12_workflow.md` | Topic idea → published video, with human minutes per stage |
| 12 | `13_quality_control_checklist.md` | Reusable QC gate |
| — | `analysis_data.json` | Every measured metric, per channel and per video, in structured form |
| — | `tmp/` | Raw measurements, evidence images and the analysis scripts |

---

## The five findings that matter most

1. **A competitive 2-hour episode needs ~350 placed visual assets** (measured range 296–499), of which only **~200 need to be newly generated**. Not 50, not 100, not 150.
2. **One image change every ~20 seconds** in the body — and **no shot in the sample exceeds 60 seconds**.
3. **Editing effort collapses by 37–44 % at minute 10** on all three strong still-image channels, and never re-escalates. It is a cliff, not a slope.
4. **Four of five channels show generic nebula wallpaper completely decoupled from the script** — and viewers of the leading physics channel complain about it in the top comments. This is the differentiation opening.
5. **The $50 budget is 2–3× more than the format needs.** Marginal cost is $6–20 fully automated. **The binding constraint is human hours (~3.9 h/episode), not money.**

**Bonus:** all five channels are confirmed monetized and faceless (0.98–0.99 confidence), cohort median RPM **$18.59** — and **Calm Science, the recommended primary reference, carries the highest RPM in the sample at $22.04**.

---

## Evidence standard

- Every quantitative claim is measured from the artefacts, or explicitly labelled ESTIMATE / INFERRED / NOT MEASURED.
- The scene-change detector was **calibrated against three independent ground truths** before use (see `02_channel_comparison.md` §0).
- Catalogue-derived views-per-video were **independently corroborated to within 0.6–3.5 %** by a third-party metrics API on all five channels.
- **No audio was ever heard.** Media streams are authentication-gated and that gate was not circumvented; every audio claim rests on caption-track annotations, caption-derived timing, or viewer comments, and is labelled accordingly.
- **No audience-retention data exists** for competitor channels and none is inferred anywhere.
- Confidence (HIGH / MEDIUM / LOW) is stated for every major conclusion, and `10_final_recommendation.md` Part 4 lists what could not be determined.
