# Zero: synthetic primary market research study

Synthetic AI research is an exploratory simulation for refining hypotheses and interview scripts. Every finding here must be validated through primary interviews with real human end users.

| Step | File | What it is |
|---|---|---|
| 1 | `01_synthetic_end_users.md` | 10 synthetic end users × 30 characteristics (DE Steps 3 & 5) |
| 2 | `02_interview_script.md` | 8 ranked key assumptions (DE Step 20) + unbiased script v1 |
| 3 | `transcripts/P1.md` … `P10.md` | 10 in-character simulated interviews |
| 4–5 | `03_synthesis_dashboard.md` / `.html` | Synthesis dashboard (NotebookLM-ready Markdown + stand-alone HTML) |
| 6 | `04_real_user_interview_script.html` (+ `.md` source) | Annotated real-user interview script v2 |
| 7 | `05_business_plan_revisions.html` (+ `.md` source) | Recommended revisions along the 24 Steps |

Rebuild the HTML after editing any Markdown source: `python3 zero-research/tools/build_html.py` (no dependencies).
