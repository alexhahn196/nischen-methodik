# 09 — Cost Model

Covers brief step 25.

**Unit:** one 128-minute episode · ~16,000 words (~95,000 characters) · ~350 placed assets · ~200 newly generated
**Cadence:** 3/week = **13 episodes/month**

> ⚠️ **Pricing caveat.** API and subscription prices move constantly and my pricing knowledge has a cutoff. Treat every dollar figure as an **ESTIMATE to be re-verified on the vendor's pricing page before you commit**. The *ratios* and the *conclusion* are robust; the absolute numbers may drift ±30 %.

---

## 1. Cost per component

### Text-to-speech — 95,000 characters per episode

| Option | Unit price (est.) | Per episode | Notes |
|---|---|---|---|
| Self-hosted open-source (Kokoro / Piper / XTTS) | GPU time only | **$0.05–0.30** | Zero licence cost; quality is the open question |
| Azure Neural / Google Neural2 | ~$15–16 / 1M chars | **$1.45–1.55** | Broadcast-adequate, huge voice catalogue |
| OpenAI TTS | ~$15 / 1M chars | **$1.45** | Simple API, good prosody |
| Google Studio / Chirp3-HD | ~$30–160 / 1M chars | **$2.85–15.20** | Marked step up in naturalness |
| ElevenLabs Turbo/Flash (Scale tier, amortised) | ~$0.08–0.09 / 1k chars | **$8–9** | |
| ElevenLabs standard multilingual (Scale tier) | ~$0.165 / 1k chars | **$15.70** | The category's likely premium option |
| ElevenLabs (Pro tier, amortised) | ~$0.198 / 1k chars | **$18.80** | Poor value at 13 episodes/month |

**Note:** at 13 episodes/month you need ~1.24 M characters/month. That is above every entry-tier plan, so amortise a higher tier rather than paying per-overage.

### AI images — ~200 newly generated per episode

| Option | Unit price (est.) | Per episode |
|---|---|---|
| Self-hosted ComfyUI on a rented consumer GPU (~$0.35/hr, ~4 s/image) | GPU time | **$0.08–0.25** |
| FLUX.1 [schnell] via hosted API | ~$0.003 / image | **$0.60** |
| SDXL via hosted API | ~$0.0035 / image | **$0.70** |
| FLUX.1 [dev] via hosted API | ~$0.025 / image | **$5.00** |
| Premium models (Ideogram / Recraft / Imagen tier) | $0.03–0.08 / image | **$6–16** |

**Hybrid is the right answer:** ~25 "hero" images (the intro, the hero cutaways) on a premium model, ~175 on a fast model. That is **~$1.50–3.00** total and it is where the visible quality actually lives.

### Script LLM

| Workload | Tokens (est.) | Sonnet-class ($3/$15 per M) | Opus-class ($15/$75 per M) |
|---|---|---|---|
| Research + outline + sectioned draft + fact-check pass + prompt generation + metadata | ~400 k in / ~120 k out | **~$3.00** | **~$15.00** |
| Heavier research (more sources, more verification passes) | ~800 k in / ~180 k out | **~$5.10** | **~$25.50** |

### Everything else

| Item | Per episode |
|---|---|
| Music — Epidemic Sound commercial ($23.99/mo ÷ 13) | **$1.85** |
| Music — one-time CC0 / royalty-free pack, amortised | **~$0.00** |
| Thumbnail — 2–4 AI candidates | **$0.05–0.30** |
| Stock video (intro only, optional) | **$0–3.00** |
| Software — DaVinci Resolve, FFmpeg, Python | **$0.00** |
| Render — local machine | **$0.00** (electricity) |
| Render — cloud VM, 8 vCPU ≈ $0.30/hr × 5 h | **$1.50** |
| Storage / bandwidth | **~$0.20** |

---

## 2. The three versions

### 🟢 $20 VERSION — "Lean"

| Component | Choice | Cost |
|---|---|---|
| Script LLM | Sonnet-class, standard research depth | $3.00 |
| TTS | Azure / Google Neural2 or OpenAI TTS | $1.50 |
| Images | 200 × FLUX schnell | $0.60 |
| Hero images | 15 × FLUX dev | $0.38 |
| Music | CC0 pack, amortised | $0.00 |
| Thumbnail | 3 AI candidates | $0.10 |
| Render | Local | $0.00 |
| Storage | | $0.20 |
| **TOTAL** | | **$5.78** |
| **With 3× contingency for retries and rejects** | | **≈ $17** |

### 🟡 $35 VERSION — "Balanced" ← **RECOMMENDED**

| Component | Choice | Cost |
|---|---|---|
| Script LLM | Sonnet-class, heavier research + separate fact-check pass | $5.10 |
| TTS | ElevenLabs Turbo/Flash (Scale tier, amortised) | $8.50 |
| Images | 175 × FLUX schnell | $0.53 |
| Hero images | 25 × FLUX dev | $0.63 |
| Music | Epidemic Sound commercial | $1.85 |
| Thumbnail | 4 candidates + 1 premium | $0.30 |
| Stock video for intro | 2 clips, amortised subscription | $1.50 |
| Render | Cloud VM | $1.50 |
| Storage | | $0.20 |
| **TOTAL** | | **$20.11** |
| **With 1.7× contingency** | | **≈ $34** |

### 🔴 $50 VERSION — "Premium"

| Component | Choice | Cost |
|---|---|---|
| Script LLM | Opus-class for the script, Sonnet-class for the rest | $15.00 |
| TTS | ElevenLabs standard multilingual | $15.70 |
| Images | 200 × FLUX dev | $5.00 |
| Hero images | 25 × premium model | $1.50 |
| Music | Epidemic Sound commercial | $1.85 |
| Thumbnail | Premium generation + iterations | $0.80 |
| Stock video | 4 clips | $3.00 |
| Render | Cloud VM, 2× for a re-render | $3.00 |
| Storage | | $0.30 |
| **TOTAL** | | **$46.15** |

---

## 3. Which one to run

> ## **Start on the $35 "Balanced" build.**

**Why not $20:** the only two things this audience demonstrably notices are **script quality** and **image quality** — the comments on the leading physics channel complain about visuals and repetition, never about anything else. The $35 build spends its extra dollars almost entirely on the deeper research/fact-check pass and a better voice, which is exactly where the risk is.

**Why not $50:** the $50 build's extra $12 goes overwhelmingly to premium TTS ($15.70 vs $8.50) and an Opus-class script model. **Zero of the 40 top comments I read across the two priority channels mention the voice at all.** There is no evidence in this sample that voice premium buys anything. Spend that $12 on a second fact-check pass or on 50 more hero images instead.

**The honest headline: your $50 ceiling is roughly 2–3× more than this format actually needs.** A fully automated pipeline lands at **$6–20 of marginal cost**. The binding constraint on this business is **human hours, not dollars.**

---

## 4. Human time and machine time

| | First 5 episodes | Optimised |
|---|---|---|
| **Human labour** | **~8.3 h** | **~3.9 h** |
| Machine time (unattended, overlapping) | ~3.5–6.5 h | ~3.5–6.5 h |
| Wall-clock per episode | ~10–12 h | ~6–8 h |

Full stage-by-stage breakdown: `05_editing_analysis.md` §5.

**The irreducible core is ~2 hours:** reading the 16,000-word script (≈64 min minimum at a careful 250 wpm), scanning ~200 generated images (~20 min), and watching 6–8 QC timestamps (~20 min). Everything else compresses toward zero with automation. These three cannot, and they are the only things keeping you out of the bottom of this niche.

---

## 5. Monthly economics at 3 uploads/week

| | $20 build | **$35 build** | $50 build |
|---|---|---|---|
| Direct cost / episode | ~$17 | **~$34** | ~$46 |
| **Direct cost / month (13 episodes)** | **~$221** | **~$442** | **~$598** |
| Fixed subscriptions (music, stock, TTS tier floor) | ~$25 | ~$60 | ~$90 |
| **Total monthly cost** | **~$246** | **~$502** | **~$688** |
| **Human hours / month (optimised)** | **~51 h** | **~51 h** | **~51 h** |
| Human hours / week | ~12 h | ~12 h | ~12 h |

### Revenue context (measured, from NexLev RPM estimates on this sample)

| Video | Channel | RPM estimate | Range |
|---|---|---|---|
| `BLPBP5BaU-0` | Sleep On Physics | **$18.21** | $11.53–24.89 |
| `lqZntA10Q5g` | Calm Science | **$19.04** | $11.32–26.76 |
| `BA59TWIMNG4` | Sleepy Science | **$20.10** | $12.50–27.70 |
| `o2eIwICmo7w` | Calm Space | $14.26 | $7.50–21.02 |

**Physics carries a higher RPM than space in this sample ($18–20 vs $14).** These are third-party model estimates, not the creators' AdSense reports — treat as **MEDIUM confidence**.

Applying the measured views-per-video of your two closest analogues (Sleep On Physics 23,762 · Calm Science 22,296) at a conservative $12 RPM:

| Scenario | Views/video | Revenue/video | Monthly (13 videos) | Monthly cost ($35 build) | Margin |
|---|---|---|---|---|---|
| Well below analogues | 5,000 | $60 | $780 | $502 | +$278 |
| Half of analogues | 11,000 | $132 | $1,716 | $502 | **+$1,214** |
| **At analogue parity** | **23,000** | **$276** | **$3,588** | **$502** | **+$3,086** |

**Break-even is around 3,200 views per video** on the $35 build at a conservative $12 RPM.

⚠️ **Two things this table does not model:** (1) YouTube monetisation requires reaching the Partner Programme threshold first, so revenue is $0 for the first stretch regardless of views; (2) new channels in a saturated niche routinely sit far below established-channel averages for months. Calm Science took 29 videos to reach 5,720 subscribers. **Budget for 3–6 months of cost with no revenue.** That is **$1,500–3,000** on the $35 build.
