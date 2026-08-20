# tmp/ — measurements, evidence and scripts

Everything here supports the analysis in the parent directory. Nothing here is a deliverable.

## Derived data (the numbers behind the reports)
| File | Contents |
|---|---|
| `sample_meta.json` | The 17 sampled videos with full yt-dlp metadata |
| `sample_def.json` | Sample selection rules and per-video rationale |
| `scene_analysis.json` | Per-video scene changes, threshold sensitivity, shot-length distributions, time-band breakdowns, appearance stats |
| `transcript_metrics.json` | Per-video WPM, word counts, sentence stats, readability, WPM curves |
| `script_structure.json` | CTA timestamps and verbatim text, first sentences, question cadence, jargon/analogy density, repeated n-grams |
| `frame_metrics.json.gz` | Per-frame brightness, contrast, saturation, colour, edge density, difference metrics (~13,600 frames) |
| `frame_metrics2.json.gz` | Masked-region metrics, letterbox measurement, text-band detection |
| `list_*.json` | Full catalogues of all 5 channels (761 long-form videos) |
| `meta.tar.gz` | Raw yt-dlp JSON for the 17 sampled videos |
| `transcripts.tar.gz` | Raw timestamped caption tracks (~280,000 words) |
| `watch/` | Gemini multimodal shot-lists — **2 videos only**; the tool hit its 15-calls/24h cap |
| `watch_plan.json` | The full 84-window multimodal plan that could not be completed |

## Evidence images
| Path | Contents |
|---|---|
| `evidence/contact_sheets/TL_<id>.jpg` | 24-frame whole-timeline montage for each of the 17 videos |
| `evidence/contact_sheets/<id>_1800.jpg` | Consecutive frames, 30:00–33:00 — used for detector calibration |
| `evidence/contact_sheets/<id>_intro.jpg` | Consecutive frames, 0:00–2:55 |
| `evidence/contact_sheets/<id>_outro.jpg` | Consecutive frames, final 3 minutes |
| `evidence/keyframes/<id>/t*.jpg` | Frames at the brief's target timestamps |

## Scripts
`measure.py` → per-frame metrics · `measure2.py` → masked/letterbox/text metrics · `scenes2.py` → calibrated scene analysis · `tscript.py` → transcript metrics · `tstruct.py` → script structure · `aggregate.py` → builds `../analysis_data.json` · `contact.py` → contact sheets and montages

## Reproducing from scratch
The raw storyboard sheets (~57 MB) were deleted after analysis. To regenerate:

```bash
pip install yt-dlp opencv-python-headless numpy pillow
# 1. fetch sb0 metadata for each sampled video id
yt-dlp --extractor-args "youtube:player_client=mweb" -f sb0 -J \
       "https://www.youtube.com/watch?v=<ID>" > meta/<ID>.json
# 2. pull every storyboard fragment URL from meta/<ID>.json -> formats[format_id==sb0].fragments[].url
#    and download each to sheets/<ID>/NNNN.jpg
# 3. then run, in order:
python3 measure.py && python3 measure2.py && python3 scenes2.py
python3 tscript.py && python3 tstruct.py && python3 aggregate.py
```
Transcripts come from the NexLev MCP tool `get_video_transcript` (one call per video id).
