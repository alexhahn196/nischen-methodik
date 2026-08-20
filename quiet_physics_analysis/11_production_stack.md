# 11 — Production Stack

Covers brief step 26. Chosen for cost, reliability, automation potential, quality and speed — in that order of weight, given a $20–50/video ceiling and a 3/week cadence.

> ⚠️ Prices are ESTIMATES with a knowledge cutoff — verify before committing. Tool availability also changes; the *role* each tool plays matters more than the specific brand.

---

## The stack

| Stage | Tool | Cost | Why this one |
|---|---|---|---|
| **Topic research** | **NexLev MCP** (`youtube_channel_videos`, `youtube_channel_outliers`, `get_similar_channels`, `search_videos`) + `yt-dlp` for free catalogue pulls | subscription / free | This is exactly how the present analysis was built. `yt-dlp --flat-playlist -J` gives you a competitor's entire catalogue with view counts in one call, free |
| **Topic validation** | NexLev `get_video_rpm`, `faceless_outliers_videos` | subscription | RPM per topic before you write. Physics measured at $18–20 vs space at $14 — worth checking per idea |
| **Deep research** | **Claude (Sonnet-class) with web search** | ~$2–4/episode | Long-context synthesis of sources into an outline |
| **Script** | **Claude (Sonnet-class), section by section** | ~$2–3/episode | Write 9 movements as separate calls against a fixed structural template, not one 16,000-word generation — quality collapses in single-shot long generation |
| **Fact checking** | **A second, separate model pass** (different provider if possible) + **human read-through** | ~$1/episode + 60 min | The human read is non-negotiable. Physics errors are the one failure this audience punishes; the comment sections are full of physicists |
| **Voice** | **ElevenLabs Turbo/Flash** (Scale tier, amortised) — **or** Azure/Google Neural2 at 1/6 the price | $1.50–8.50/episode | **A/B these on your first 3 episodes.** No evidence in this sample that premium voice buys anything: zero of 40 top comments mention the voice |
| **Pronunciation** | A hand-maintained lexicon / SSML `<phoneme>` dictionary | free, ~10 min/episode | Mandatory. The auto-captions on these very videos show ASR mangling "quasar"→"quazar" and "positron"→"posetron"; your TTS will mangle the same words |
| **Images (bulk)** | **FLUX.1 [schnell]** via Replicate/fal — or self-hosted **ComfyUI** on a rented GPU | $0.60/episode hosted, ~$0.15 self-hosted | ~175 body assets. Self-host once you pass ~10 episodes/month |
| **Images (hero)** | **FLUX.1 [dev]** or a premium model | $0.60–1.50/episode | ~25 images: the intro and the hero cutaways. This is where visible quality lives |
| **Motion (Ken Burns)** | **FFmpeg `zoompan`**, driven by Python | free | Reproduces exactly what competitors do: 3–5 % zoom, random direction. Render stills at 3840×2160, apply `zoompan`, downscale to 1080p — **skipping the 2× upscale causes visible jitter and is the #1 way automated Ken Burns looks cheap** |
| **Assembly (body, 3:00–end)** | **FFmpeg `xfade` chain**, driven by Python | free | 300+ clips with 1.2 s crossfades is a loop, not a timeline. Fully headless |
| **Assembly (intro, 0:00–3:00)** | **DaVinci Resolve (free)** | free | ~25 hand-cut shots are faster on a real timeline. The only part of the video a human edits |
| **Audio cleanup / mix** | **FFmpeg** (`loudnorm`, `acompressor`, `sidechaincompress`) | free | Bed ducking, light narration compression, −14 LUFS normalisation |
| **Music** | **Epidemic Sound** commercial — or a one-time CC0 ambient pack | $23.99/mo (≈$1.85/episode) or $0 | One unchanging drone loop per episode. Competitors use one bed for two hours |
| **Thumbnail** | **FLUX/premium generation + GIMP or Photopea** (free) | ~$0.30/episode | Generate 3–4 candidates, composite by hand |
| **Export** | **FFmpeg**, H.264 CRF 20–22, 1080p30, AAC 192k, **plus light grain** | free | The grain is not optional — dark gradients band badly under YouTube's transcode |
| **Captions** | **Whisper** (self-hosted) on your own narration WAV → SRT, uploaded as a **track** | free | Never burn into the picture |
| **Orchestration** | **Python + a plain job queue**, one directory per episode, JSON manifest | free | Do not adopt a workflow platform for a 15-step pipeline you run 13×/month |
| **Version control** | **Git** for scripts, prompts, templates and the manifest schema | free | The prompt library and style suffix are your actual product |
| **Asset library** | Flat directory + a JSON/SQLite index with tags, embeddings and a `last_used_episode` field | free | **The compounding asset.** Enables reuse without repetition and powers the duplicate check in QC |

---

## What is deliberately NOT in this stack

| Rejected | Why |
|---|---|
| **Premiere Pro / After Effects** | Monthly licence for a timeline you would open once per episode. FFmpeg does the body; Resolve free does the intro |
| **Remotion** | Excellent for programmatic *motion graphics*. Rendering 300 photographic stills for 2 hours through React/Canvas is far slower than FFmpeg's filter graph and buys nothing this format uses |
| **MoviePy** | Wraps FFmpeg and is markedly slower on long timelines. Call FFmpeg directly |
| **CapCut** | Not viable at 350 assets × 128 min; weak automation |
| **Video-generation models (Sora/Veo/Kling-class)** | Wrong tool and wrong price. This category is **~95 % still images with a 3 % zoom**. Generated video costs 100–1000× more per second and no competitor uses it |
| **A workflow platform (n8n / Airflow / Temporal)** | Operational overhead exceeding the pipeline itself at this scale. Revisit past ~30 episodes/month |
| **Any burned-in subtitle tool** | The only channel that burns captions has the worst views/video in the sample |
| **4K delivery** | Nothing here resolves past 1080p. Doubles render time and storage |
| **Auto-upload without review** | Publishing is the one step that must stay manual |

---

## Build order (do not build the whole stack at once)

| Phase | Build | Why first |
|---|---|---|
| **1 — Episodes 1–3** | Script pipeline + TTS + a **manual** Resolve assembly | Prove the script and voice work before automating anything. Assemble by hand so you learn what the template must do |
| **2 — Episodes 4–8** | FFmpeg `zoompan` + `xfade` assembler; JSON manifest schema | Now you know the parameters. Automate the 110-minute body; keep cutting the intro by hand |
| **3 — Episodes 9–15** | Image-prompt generation + batch generation + asset library index | You now have enough style history to build a real prompt library |
| **4 — Episodes 16+** | Self-hosted image generation; automated metadata; QC scripts | Cost optimisation, only once volume justifies it |

**Do not build phase 4 in week 1.** The measured evidence says the risk in this niche is script quality and visual repetition — not throughput.
