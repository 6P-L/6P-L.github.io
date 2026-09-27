# Zero Synthetic User Research: Synthesis Dashboard

Study: synthetic primary market research on Zero, an AI-native active learning system (scaffolded tutoring, persistent cross-session memory, private document grounding, proactive push) for college finals and professional exams.

Baseline business context used in this dashboard: pricing tiers ¥0 trial / ¥39 base / ¥99 Pro / ¥199 heavy; current ARPU ¥78.9; current paid conversion 4.6%.

## Disclaimer: synthetic personas, not real customers

IMPORTANT. Every finding in this dashboard comes from 10 AI-generated synthetic personas answering an AI-simulated interview. This is an exploratory simulation. Its only legitimate uses are to refine hypotheses, sharpen the interview script and decide what to ask real people.

- All findings MUST be validated through primary interviews with real human end users before they inform product, pricing or go-to-market decisions.
- Synthetic personas cannot reliably predict real purchasing behavior, real risk tolerance or real-world study habits.
- Counts and percentages below are out of n = 10 synthetic personas. They are not statistically meaningful and must not be quoted as market data.
- The personas were written from the founder's deck, so they may reflect the founders' own assumptions back at them. Agreement with the deck is therefore weak evidence. Disagreement with the deck is more informative, but it still needs real-world confirmation.

## Source and method

Sources used by this dashboard:

- 01_synthetic_end_users.md: 10 persona profiles (P1 to P10), each with demographics, psychographics, behaviors and a backstory.
- 02_interview_script.md: 8 key assumptions (A1 to A8), ranked riskiest first, plus interview script v1 (W1 to W3, Q1 to Q10, C1 to C2, and the Z1 concept reaction).
- transcripts/P1.md to transcripts/P10.md: one simulated interview per persona, each with neutral interviewer notes and a stated WTP_MONTHLY line.

Method:

- Scoring rule. Each assumption was scored per persona from what the persona said about past behavior in W1 to C2: what they did, paid for, muted or abandoned. Reactions to the Z1 concept read were counted only when they agreed with past behavior. Polite interest in Z1 was never counted as validation on its own.
- Score codes. V = Validated: past behavior clearly supports the assumption for this persona. P = Partially validated: some support, or support only under conditions that change the assumption in a material way. I = Invalidated: past behavior contradicts the assumption, or it does not apply to this persona.
- Overall verdict rule. Validated if V is 6 or more out of 10. Invalidated if I is 6 or more out of 10, or if V = 0 and I is 5 or more. Partially Validated otherwise.
- Confidence. Confidence is Low or Med only. No synthetic finding is rated High. It is Med when the past-behavior evidence was consistent across personas and Low when it rests on stated intent, or on a single persona (as with A8).
- Currency. USD was converted at 7.2 RMB per USD. P10's $20 is about ¥144.
- Phrase counts. Counts cover respondent answers only. Interviewer questions, the concept text and the interviewer notes were excluded. A persona counts once per phrase, however often they used it.
- Analyst caveat. All scores are the judgment of one analyst. The per-persona rationale is given so each score can be challenged.

## 1. Executive summary

Executive summary of the Zero synthetic research (n = 10 synthetic personas, exploratory only):

- Biggest unmet need. Learners do not mainly lack motivation or explanations. What they lack is an accurate, zero-maintenance memory of their own mistakes and forgetting that turns into a concrete answer to "what should I work on tonight". 6 of 10 named this as their top problem at C2 (P1, P3, P4, P6, P9, P10), and 3 more named a close variant (P2, P5, P7). Every persona who tried to track this by hand abandoned it or let it go stale.
- Memory is the one concept element that drew real interest, but it is a pain reliever, not a return driver. A1 is Partially Validated (0 V / 7 P / 3 I). In every lapse the personas described, what brought them back was a deadline, guilt, peer comparison or a paid commitment. None came back because of a tool's memory.
- Two of Zero's four headline differentiators work against it as currently framed. Scaffolding (A3) is Invalidated (0 V / 3 P / 7 I): 9 of 10 said they would go back to free ChatGPT, Doubao (豆包) or DeepSeek if answers were withheld. Proactive push (A5) is Invalidated (0 V / 5 P / 5 I): all 10 had muted, ignored or abandoned a reminder, 督学 or 打卡 mechanism. Only highly specific, data-aware nudges drew any interest.
- The deck's core positioning, "starting and persisting" (没法开始 / 走不远), is Invalidated (A7: 2 V / 2 P / 6 I). Only P2 and P5 named motivation as their primary pain. For most personas the pain is diagnosis and prioritization: volume, forgetting, and not knowing where their errors are.
- Willingness to pay is low, seasonal and mostly a substitution for current spend. Median stated WTP is ¥30/month and the mean is ¥39.1/month. The mean is under half the current ¥78.9 ARPU. No persona would pay ¥39 without conditions. 3 of 10 would pay ¥99 or more, and only if Zero replaced something they already pay for (ChatGPT Plus, human 申论 批改 essay grading). 6 of 10 would pay only in the months before their exam.
- Accuracy is the gate before price. 7 of 10 have a one-strike rule: "wrong twice, I'm gone" (P1), or one wrong legal rule, drug fact or logic explanation and they delete the app (P4, P8, P9). The two highest-budget personas (P4, P9) call ¥99 "nothing" but pay ¥0 today because they do not trust AI.
- Tool fragmentation is real, but the pain is data silos and manual copying, not switching (A4 Partially Validated, 2 V / 4 P / 4 I). All 10 personas describe copying or pasting AI output by hand. Most say the switching itself is tolerable, and 6 of 10 insist Zero must export to or plug into Anki, Notion, Obsidian, UWorld or 粉笔 rather than replace them.

## 2. Quantitative findings

### 2a. Assumption scorecard: per-persona matrix (A1 to A8 by P1 to P10)

Per-persona assumption scorecard. V = Validated, P = Partially validated, I = Invalidated. Scores are based on past behavior (see Source and method).

| Assumption | P1 Lin | P2 Zhao | P3 Chen | P4 Wang | P5 Liu | P6 Zhang | P7 Huang | P8 Zhou | P9 Sun | P10 Sofia |
|---|---|---|---|---|---|---|---|---|---|---|
| A1 Memory drives multi-day return | P | P | P | P | I | P | P | I | I | P |
| A2 Pay ¥15-40 entry, share at ¥99+ | V | P | P | I | I | P | V | P | I | P |
| A3 Prefer scaffolding over raw answers | I | P | P | I | I | I | I | P | I | I |
| A4 Tool fragmentation is a wanted fix | V | I | V | P | I | I | P | P | I | P |
| A5 Proactive outreach is welcomed | P | P | P | P | I | I | I | I | I | P |
| A6 Willing to upload private materials | V | V | P | I | P | V | P | I | I | P |
| A7 Primary pain is starting/persisting | I | V | P | I | V | P | I | I | I | I |
| A8 Overseas need matches (see note) | V | P | P | V | I | V | V | I | V | P |

How A8 was scored. A8 asks whether overseas English-speaking learners share the same need and would adopt the same product. P10 Sofia is the only overseas persona, so she was scored on both need and adoption. She scored P: her need matches, but she would adopt only with UWorld and Anki integration, clear data ownership, r/MCAT proof and a substitution-only price. P1 to P9 were scored on whether their C2 core need matches P10's need pattern: "remember all my mistakes and tell me what to do tonight", meaning a memory of mistakes or forgetting plus next-action prioritization, answer-first, running alongside tools they already have. V = same pattern. P = adjacent pattern (accountability, or multi-project context). I = a different need (P5 wants cram shortcuts; P8 wants cited card generation). A8 counts therefore measure need convergence between markets, not overseas adoption.

### 2a. Assumption scorecard: per-persona rationale

Assumption scorecard rationale, one line per assumption, citing the behavior behind the scores:

- A1 rationale. No persona returned because of a tool's memory. Returns came from guilt or the 自习室 fee (P2), peer posts (P3, P7), the exam date (P5, P6, P8), the Saturday class (P9) and Reddit posts (P10). The P scores are personas for whom memory would cut the cost of re-orientation or decay: P1 took about 1 hour to re-orient, P3 loses about 10 minutes per switch, P4 has 民法 decay, P6 has a notes "graveyard", P7 notes 粉笔 gets her going "in two minutes", P10 spends about 15 minutes, and P2 wants skip-aware nudges. I scores: P5 restarts from chapter 1 every time, P8 already has Anki, and P9 is reset by his class and tutor.
- A2 rationale. V: P1 already pays ¥68/mo for ChatGPT and would switch at ¥68, up to ¥99. P7 already spends ¥150-250/mo on 申论 批改 (essay grading) and would pay ¥60, or ¥99 if Zero replaced 批改. P: payment is capped, seasonal or conditional on substitution (P2 ¥30, P3 ¥39, P6 ¥20, P8 ¥30 with citations only, P10 ¥144 only if she cancels ChatGPT). I: ¥0 today (P4, P5, P9).
- A3 rationale. 7 of 10 described past behavior that rejects withheld answers: closed a tab or app, went back to free AI, or want the answer and then drill. P2 and P3 accept scaffolding "in principle" but bypass it when tired or rushed. P8 accepts it only with a source citation on every step.
- A4 rationale. V: P1 (40 min/day of Notion upkeep, "I resent that time") and P3 ("tiring in a quiet way", three tracking places that "none of them talk to each other"). P: the pain is silos or copying rather than switching (P4, P7, P8, P10). I: P2 ("the phone is the problem"), P5, P6 ("I'd be suspicious of an all-in-one"), P9.
- A5 rationale. All 10 had muted, ignored, turned off or abandoned a reminder or 打卡 mechanism. P = openly asked for a specific, data-aware check-in: P1 "on pace", P2 "you haven't touched OS in four days", P3 "knowing why I disappeared", P4 "what I'm forgetting", P10 "you've missed three enzyme questions". I = rejected outreach outright.
- A6 rationale. V: already uploading freely (P1, P2, P6). P: willing for some materials only, or blocked by format (P3 won't upload her thesis; P5 has only phone photos; P7 is phone-only; P10 avoids paid Kaplan and UWorld PDFs). I: P4 (watermarked 讲义 carrying his name, risk of an account ban), P8 (内部资料 "internal material, do not share" slides, DRM-locked e-books), P9 ("I just don't see the point").
- A7 rationale. V: P2 ("I can study, I just can't make myself keep studying") and P5 ("Starting before it's too late"). P: P3 keeping parallel threads alive, P6 reviewing is a "discipline issue". I: volume and accuracy (P1, P8), forgetting and grading (P4), 申论 feedback (P7), weeknight hours (P9), plateau diagnosis (P10).
- A8 rationale. See "How A8 was scored" above.

### 2a. Assumption scorecard: summary table

Summary of assumption verdicts with exact counts out of 10 synthetic personas:

| Assumption | Validated n (%) | Partial n (%) | Invalidated n (%) | Overall verdict | Confidence |
|---|---|---|---|---|---|
| A1 Persistent memory drives multi-day return | 0 (0%) | 7 (70%) | 3 (30%) | Partially Validated | Med |
| A2 Pay ¥15-40 entry and meaningful share ¥99+ Pro | 2 (20%) | 5 (50%) | 3 (30%) | Partially Validated | Low |
| A3 Prefer scaffolding over instant raw answers | 0 (0%) | 3 (30%) | 7 (70%) | Invalidated | Med |
| A4 Tool fragmentation causes fatigue users want solved | 2 (20%) | 4 (40%) | 4 (40%) | Partially Validated | Med |
| A5 Proactive outreach is welcomed, not annoying | 0 (0%) | 5 (50%) | 5 (50%) | Invalidated | Med |
| A6 Willing to upload private/copyrighted materials | 3 (30%) | 4 (40%) | 3 (30%) | Partially Validated | Med |
| A7 Primary pain is starting and persisting | 2 (20%) | 2 (20%) | 6 (60%) | Invalidated | Med |
| A8 Overseas learners share need and would adopt | 5 (50%) | 3 (30%) | 2 (20%) | Partially Validated | Low |

Verdict notes, per assumption:

- A1 (Partially Validated). Memory is valued as relief from the cost of re-orientation and forgetting, but it is not what brings people back. The deck's 63.5% return rate may be driven by the exam calendar. Test this with real users.
- A2 (Partially Validated, Low). The entry range of ¥15-40 roughly holds for 6 of 10 personas (P1, P2, P3, P7, P8, P10, all with conditions). The "meaningful share at ¥99+" half is weak: 3 of 10, all conditional on replacing existing spend. Confidence is Low because stated WTP is the least reliable synthetic output.
- A3 (Invalidated). Invalidated as a default mode. "Answer first, then let me test myself" is the preferred pattern.
- A4 (Partially Validated). Reframe the pain from "too many tools" to "my records don't connect, and I copy by hand".
- A5 (Invalidated). Invalidated for generic or streak-style push. A narrower hypothesis, specific and content-aware nudges, is untested: 5 personas asked for it, but none has ever experienced it.
- A6 (Partially Validated). Barriers split between effort and format (phone photos, scanning, DRM) and rules or ownership (watermarks, 内部资料, thesis, paid question banks). Privacy is not the only barrier.
- A7 (Invalidated). The primary pain is prioritization and diagnosis, not motivation. The two personas it fits (P2, P5) have the lowest WTP.
- A8 (Partially Validated, Low). The need pattern converges across markets (8 of 10 V or P). Adoption of the same product is only partial for the single overseas persona. With n = 1 overseas persona, this cannot be confirmed.

### 2b. Willingness-to-pay distribution: per-persona table

Stated monthly WTP per persona, in RMB (USD converted at 7.2), with each persona's conditions. Source: the C2 answer and the WTP_MONTHLY line in each transcript.

| Persona | Stated monthly WTP (RMB) | Bucket | Conditions and ceiling | Paying months |
|---|---|---|---|---|
| P1 Lin Zihan | 68 | ¥50-99 | Replaces her shared ChatGPT Plus (¥68); up to ¥99 only if it also replaces most Notion upkeep and is accurate on pharmacology; 1-week free trial; "wrong twice" and she leaves | Until December exam, then stops |
| P2 Zhao Mingyuan | 30 | ¥30-49 | "That's really the top"; free trial; no annual prepay; will not pay ¥99; outreach must be specific | Not stated; no annual commitment |
| P3 Chen Siqi | 39 | ¥30-49 | Free trial that works in session one with no setup; must replace on-and-off ChatGPT Plus; ¥99 "is not" affordable as a student | Would drop after 1-2 months if it does not replace ChatGPT |
| P4 Wang Hao | 0 | ¥0 | ¥0 now (3 weeks before exam). Hypothetical ¥39 in June to October of a retake year, if proven by people who passed and error-free on 厚大 讲义 (course handouts); would fund it by dropping the 批改 package | Peak months only (June to October) |
| P5 Liu Jiayi | 0 | ¥0 | ¥0 during the semester; about ¥15 one-off in finals month only; "¥39 is like eight cups of milk tea" | Finals month only |
| P6 Zhang Wei | 20 | ¥1-29 | About the cost of API calls; must read and write Obsidian Markdown with export or API; ¥0 if he has to leave Obsidian; ¥99 and he would build it himself | 2-3 months around finals |
| P7 Huang Yutong | 60 | ¥50-99 | Strict, fast 申论 feedback; ¥99 only if it fully replaces human 批改 and is proven against her teacher's grading; phone-only; no annual plan | About 3 months, until the December exam |
| P8 Zhou Xinran | 30 | ¥30-49 | Only for Anki card generation where every card cites its textbook page; ¥0 for the concept as described; at ¥50 or more she would keep making cards herself; needs a senior's or teacher's endorsement | Not stated |
| P9 Sun Jianguo | 0 | ¥0 | ¥0 for software ("¥99 is nothing", but trust is the issue); would instead pay his tutor about ¥1,600/mo more; might try free if his tutor or admitted colleagues endorse it | Not applicable |
| P10 Sofia Martinez | 144 ($20) | ¥99+ | Only as a replacement for ChatGPT Plus; $0 incremental (maybe $10, about ¥72, for 3 months if it is an add-on); needs r/MCAT proof, UWorld and Anki integration, data deletion | About 3 months before April test (if add-on) |

### 2b. Willingness-to-pay distribution: buckets and statistics

WTP bucket distribution (n = 10 synthetic personas, headline stated value):

| WTP bucket (monthly) | Count | Percent | Personas |
|---|---|---|---|
| ¥0 | 3 | 30% | P4, P5, P9 |
| ¥1-29 | 1 | 10% | P6 |
| ¥30-49 | 3 | 30% | P2, P3, P8 |
| ¥50-99 | 2 | 20% | P1, P7 |
| ¥99+ | 1 | 10% | P10 (substitution only) |

WTP summary statistics:

| Metric | Value | Note |
|---|---|---|
| Mean stated WTP | ¥39.1/month | Sum ¥391 / 10; 50% of current ARPU of ¥78.9 |
| Median stated WTP | ¥30/month | Sorted: 0, 0, 0, 20, 30, 30, 39, 60, 68, 144 |
| Mean if P10 is scored at her incremental $0 | ¥24.7/month | P10 pays only by cancelling ChatGPT Plus |
| Median if P10 is scored at her incremental $0 | ¥25/month | |
| Mean, 9 domestic personas only | ¥27.4/month | Excludes P10 |
| Would pay ¥39 or more unconditionally | 0 of 10 (0%) | Every stated amount carries at least one condition |
| Stated ¥39 or more, with conditions | 4 of 10 (40%) | P1, P3, P7, P10 (5 of 10 if P4's hypothetical retake-year ¥39 is counted) |
| Would pay ¥99 or more, conditionally | 3 of 10 (30%) | P1, P7, P10 |
| Explicitly reject ¥99 on price or build-it-yourself grounds | 5 of 10 (50%) | P2, P3, P5, P6, P8 |
| Say ¥99 is affordable, but pay ¥0 on trust | 2 of 10 (20%) | P4, P9 |

Conditions attached to ¥99 (the Pro tier):

- P1. Zero must replace both ChatGPT Plus and most of her 40 min/day Notion upkeep, and be accurate on pharmacology facts. ¥99 is "the ceiling", and she would cut eating out to afford it.
- P7. Zero must fully replace human 申论 批改 (essay grading), after she has seen it grade several essays in line with her teacher's comments.
- P10. $20 (about ¥144) only if she cancels ChatGPT Plus for studying. If it is an add-on, $0 to $10.
- Common pattern. In all three cases ¥99+ is money moved from an existing line item (ChatGPT, or human grading). It is not new budget. The deck's Pro-upgrade path to a ¥78.9 ARPU implies the product must credibly displace ChatGPT Plus or a paid human service.

### 2b. Willingness-to-pay distribution: seasonality of payment

Seasonality and commitment patterns in stated WTP:

- 6 of 10 (60%) explicitly limit payment to exam-proximate months: P1 (until December), P4 (June to October only), P5 (finals month only), P6 (2-3 months around finals), P7 (about 3 months until December), P10 (3 months before the test if it is an add-on).
- 2 of 10 explicitly refuse annual or upfront plans: P2 ("I wouldn't pay for a year up front, no way") and P7 ("I wouldn't want an annual plan").
- 2 of 10 say they would not change their system close to an exam: P4 ("not going to change my system three weeks before the exam"), P7 (will not leave 粉笔 before December).
- Implication. This matches the deck's finding that 55% choose quarterly plans: the natural unit is one exam cycle, not an open-ended subscription. Expect heavy churn after exam dates. Annualized revenue per payer will be well below 12 times the monthly price, since most personas pay about 3 to 5 months per year.

### 2c. Top objections ranked by frequency

Objections to the Zero concept, ranked by the number of personas raising them (anywhere in the interview, backed by past behavior where available). n = 10.

| Rank | Objection | Count | Percent | Personas |
|---|---|---|---|---|
| 1 | Generic reminders or push will be muted (has muted, ignored or abandoned a reminder, 督学, 打卡 or streak mechanism before) | 10 | 100% | P1, P2, P3, P4, P5, P6, P7, P8, P9, P10 |
| 2 | Withholding the answer or Socratic guidance means going back to free ChatGPT, Doubao or DeepSeek | 9 | 90% | P1, P2, P3, P4, P5, P6, P7, P9, P10 |
| 3 | One factual error means deleting it (accuracy and trust gate) | 7 | 70% | P1, P3, P4, P7, P8, P9, P10 |
| 4 | Setup or upload effort too high (PDF upload, scanning, desktop-only, more than 5-10 minutes) | 6 | 60% | P2, P3, P4, P5, P7, P9 |
| 5 | Must export to or integrate with the existing system (Anki, Notion, Obsidian, UWorld, 粉笔, 厚大 chapter structure), not replace it | 6 | 60% | P1, P4, P6, P7, P8, P10 |
| 6 | Needs a free trial before paying | 6 | 60% | P1, P2, P3, P6, P9, P10 |
| 7 | Need ends at the exam; no annual or off-season payment | 6 | 60% | P1, P4, P5, P6, P7, P10 |
| 8 | Must replace existing spend, not be an additional subscription | 5 | 50% | P1, P3, P4, P7, P10 |
| 9 | Data privacy, copyright or ownership of uploads (thesis, watermarked 讲义, 内部资料, training use, deletion, export) | 5 | 50% | P3, P4, P6, P8, P10 |
| 10 | Requires endorsement from trusted peers or experts first (cohort, people who passed, senior or teacher, tutor, r/MCAT) | 5 | 50% | P3, P4, P8, P9, P10 |
| 11 | Price above the free-alternative ceiling (free AI or DIY is good enough) | 5 | 50% | P2, P3, P5, P6, P8 |
| 12 | Timing: will not switch systems close to the exam | 2 | 20% | P4, P7 |
| 13 | Feels like a gimmick or "built for teenagers" (edtech wrapper) | 2 | 20% | P6, P10 |
| 14 | Content-specific handling gaps (chemical structures and tables in PDFs; a single subject only, not thesis plus CPA) | 2 | 20% | P1, P3 |

Reading the objection ranking:

- The top two objections target two of Zero's four headline features (push and scaffolding), and they rest on past behavior, not speculation.
- Objections 3, 5, 9 and 10 together describe a trust stack. Zero has to be accurate, cite its sources, plug into tools users already trust, and be vouched for by someone the user trusts. Price comes after trust for the higher-budget personas.

## 3. Qualitative findings

### 3a. Representative verbatim quotes: A1 persistent memory and return

Verbatim quotes on Assumption A1 (persistent cross-session memory drives multi-day return). Verdict: Partially Validated.

- P1 Lin Zihan: "The AI tools don't know anything about it; every session they start from zero."
- P7 Huang Yutong: "For 行测 it didn't matter, because 粉笔 just drops me back where I stopped and shows my accuracy, so I got going in two minutes."
- P5 Liu Jiayi: "\"Remembers your progress\" sounds nice, but I don't have progress to remember, I restart every time."
- P9 Sun Jianguo: "So the class schedule is what resets me."

### 3a. Representative verbatim quotes: A2 willingness to pay

Verbatim quotes on Assumption A2 (pay ¥15-40 entry and a meaningful share ¥99+). Verdict: Partially Validated.

- P1 Lin Zihan: "Realistically, I'd pay ¥68 a month, the same as ChatGPT, and I'd drop the shared ChatGPT account to make room"
- P5 Liu Jiayi: "¥39 is like eight cups of milk tea, no way, and ¥99 is crazy for a student."
- P9 Sun Jianguo: "Not because ¥99 is expensive, ¥99 is nothing. It's because I don't trust it to pick the right topic, and if it picks wrong, I lose the evening, which is the thing I actually care about."
- P10 Sofia Martinez: "So the honest answer is about $20 a month, but only if it replaces ChatGPT Plus for studying, meaning I'd cancel ChatGPT."

### 3a. Representative verbatim quotes: A3 scaffolding versus raw answers

Verbatim quotes on Assumption A3 (learners prefer scaffolding over instant raw answers). Verdict: Invalidated.

- P5 Liu Jiayi: "Once I tried an app where the AI kept asking me \"what do you think the first step is?\" and I didn't know, that's why I was asking! It made me feel stupid so I closed it."
- P6 Zhang Wei: "If something had asked me \"what do you think the potential should be?\" I'd have closed the tab."
- P2 Zhao Mingyuan: "The \"step by step instead of giving answers\" part, I know it's good for me, but honestly if I'm tired at 4pm and it won't just tell me the answer, I'll open 豆包 in the other tab."
- P1 Lin Zihan: "with 110 days left I don't have time to be Socratic-methoded about aminoglycosides; sometimes I just need the table, correctly, now."

### 3a. Representative verbatim quotes: A4 tool fragmentation

Verbatim quotes on Assumption A4 (tool fragmentation causes cognitive fatigue that learners want solved). Verdict: Partially Validated.

- P1 Lin Zihan: "It's not unbearable — I'm used to it, I built it — but it's clunky and the copying is pure waste."
- P3 Chen Siqi: "It's tiring in a quiet way. No single tool is bad, but switching costs me focus every time."
- P2 Zhao Mingyuan: "So switching tools isn't the problem, the phone is the problem. I wouldn't pay anything just to have fewer apps, if that's what you're asking."
- P10 Sofia Martinez: "What bugs me more is that none of them talk to each other, so the \"what's my weak area\" thinking only happens in my head."

### 3a. Representative verbatim quotes: A5 proactive outreach

Verbatim quotes on Assumption A5 (proactive outreach is welcomed, not annoying). Verdict: Invalidated for generic push. Specific, data-aware nudges are untested.

- P2 Zhao Mingyuan: "It was the same template every day, \"同学们早上好，今天也要加油哦\", you could tell nobody was actually looking at me."
- P2 Zhao Mingyuan: "It would have to know specifically what I skipped, like \"你已经四天没碰操作系统了，上次你卡在PV操作\" — that would actually get me."
- P4 Wang Hao: "If something checked in on me, it would need to be about what I'm forgetting, not whether I'm studying. The second kind just annoys me." (The transcript italicizes "what" and "whether".)
- P1 Lin Zihan: "Honestly, I don't need someone to push me to show up. What I'd want is something that checks whether I'm on pace, not whether I'm awake."

### 3a. Representative verbatim quotes: A6 uploading private materials

Verbatim quotes on Assumption A6 (learners will upload private or copyrighted course materials). Verdict: Partially Validated.

- P1 Lin Zihan: "I upload them freely to Kimi, ChatGPT, whatever. I don't really worry about privacy for textbooks, they're everywhere anyway."
- P8 Zhou Xinran: "A lot of them literally say \"内部资料 请勿外传\" on the first slide, and I take that seriously."
- P5 Liu Jiayi: "But I don't have PDFs. It's all phone photos, like 200 of them. If an app wants me to upload a PDF or go to a computer to do it, I'm not going to do that."
- P4 Wang Hao: "The PDF versions are watermarked with my name and phone number, and the course terms say you can't distribute them."

### 3a. Representative verbatim quotes: A7 starting and persisting

Verbatim quotes on Assumption A7 (the primary pain is starting and persisting, not content or explanations). Verdict: Invalidated.

- P2 Zhao Mingyuan: "It's like, I can study, I just can't make myself keep studying."
- P4 Wang Hao: "I don't have a motivation problem, I have a savings problem, that's motivation enough."
- P9 Sun Jianguo: "I don't lack motivation. I lack hours. No app is going to give me hours."
- P10 Sofia Martinez: "Honestly it's the plateau and not knowing why."

### 3a. Representative verbatim quotes: A8 overseas learners

Verbatim quotes on Assumption A8 (overseas English-speaking learners share the need and would adopt the same product). Verdict: Partially Validated, Low confidence.

- P10 Sofia Martinez: "The \"remembers your progress\" part is literally the thing I've been complaining about, so that part gets my attention."
- P10 Sofia Martinez: "And I'd want to see people on r/MCAT actually say their score went up before I'd pay, a free trial isn't enough by itself."
- P7 Huang Yutong (domestic parallel to P10's need): "If it knew my recurring weaknesses and gave me tonight's one task, that's useful."

### 3b. Recurring organic language patterns

The words the synthetic personas actually used, counted as the number of personas (out of 10) using each phrase or close variant in their answers. Interviewer questions, the concept text and the interviewer notes are excluded.

| Phrase or pattern (as users say it) | Personas using it | Who | What it signals |
|---|---|---|---|
| "copy" / "paste" (moving AI output by hand) | 10 | All | Manual transfer is universal; the real fragmentation pain |
| "mute" / "turn off" / "swipe away" / "ignore" (notifications, reminders) | 9 | P1, P2, P3, P4, P5, P6, P7, P9, P10 | Default response to outreach |
| "trust" / "don't trust" | 9 | All except P5 | Trust is the gating variable |
| "the answer" (want it, give me it, get it fast) | 8 | P1, P2, P3, P5, P6, P7, P9, P10 | Answer-first expectation |
| "specific" (outreach or feedback must be specific) | 8 | P1, P2, P3, P4, P5, P6, P9, P10 | Generic equals noise |
| "annoying" / "annoy" | 8 | P1, P2, P3, P4, P5, P6, P7, P8 | Low tolerance for friction |
| "waste" / "wasted" (time more than money) | 7 | P1, P2, P4, P5, P7, P9, P10 | Time is the scarce currency |
| "打卡" (check-in) | 7 | P1, P2, P3, P4, P5, P7, P8 | Familiar but short-lived accountability ritual |
| "what should I do" / "what's next" / "tonight" | 7 | P3, P4, P5, P7, P8, P9, P10 | Prioritization is the job to be done |
| "generic" (describing reminders, plans or feedback) | 6 | P1, P3, P4, P7, P9, P10 | The word users use to dismiss 督学-style services |
| "replace" (Zero must replace X) | 6 | P1, P3, P7, P8, P9, P10 | Substitution, not addition |
| "free trial" / "free tier" / "try it free" | 6 | P1, P2, P3, P6, P9, P10 | Trial is table stakes |
| "delete it" / "I'm gone" / "I'm done" (one-strike exit) | 6 | P1, P3, P4, P8, P9, P10 | Unforgiving on errors |
| "go back to ChatGPT / 豆包" | 5 | P1, P2, P3, P5, P10 | Free AI is the default fallback |
| "tired" | 5 | P2, P3, P7, P9, P10 | Evening fatigue drives the answer-first preference |
| "in my head" (tracking lives only in my head) | 4 | P2, P6, P7, P10 | No external record of weaknesses |
| "guilt" | 4 | P2, P5, P9, P10 | Guilt, not tools, is the return trigger |
| "performative" / "performing studying" (about 打卡 groups) | 3 | P6, P7, P8 | Social check-ins feel fake |
| "Socratic" | 3 | P1, P7, P10 | Used only negatively |
| "graveyard" (notes never reviewed) | 1 | P6 | Vivid framing of review failure |
| "a system prompt with a subscription" | 1 | P6 | Power-user prior against AI wrappers |

Caveat on 3b. Phrase repetition partly reflects a shared generator (all 10 personas were written by the same AI). Real users will use different, messier language. This list is a starting vocabulary to listen for, not evidence of market language.

### 3c. The single biggest unmet need

Biggest unmet need, stated precisely: "Tell me what to work on tonight, based on an accurate record of what I got wrong and what I'm forgetting, without me having to maintain that record."

This need has three parts, and each is backed by evidence:

- Part 1. An automatic, persistent record of my own mistakes and decay. Manual tracking failed for almost everyone who tried it:
  - P1 spends about 40 min/day on Notion upkeep, which she resents.
  - P2 stopped updating his plan in June and has reviewed his 错题本 (error notebook) about 3 times.
  - P3's Excel plan is "usually three days out of date"; she has done 4-5 "delete and re-plan" resets this year.
  - P6's vault is a "graveyard".
  - P7: "If it's not automatic, I won't keep it up."
  - P10 logs about half of her missed questions and has 200+ unsearchable ChatGPT threads.
- Part 2. Turned into a next action, not a dashboard:
  - P9: "knowing immediately which weak topic to spend tonight's 40 minutes on, with the right problems ready."
  - P7: "gave me tonight's one task."
  - P10: "remember all my mistakes and tell me what to do tonight."
  - P4: "Knowing exactly what from 民法 is leaking out and making me review that and only that, at the right time."
- Part 3. Accurate enough to trust. 7 of 10 have a one-strike rule on errors, so a wrong recommendation or fact destroys the value.

C2 pick map (the one problem each persona would pay to remove):

| Persona | C2 problem picked | Matches biggest unmet need? |
|---|---|---|
| P1 | Context and record-keeping (re-explaining to AI, 40 min of Notion) | Direct |
| P2 | Noticing when he disappears from a subject and pulling him back | Adjacent (memory-driven, specific nudge) |
| P3 | "where was I, and what should I do next across all my projects" | Direct |
| P4 | Forgetting: what from 民法 is leaking, reviewed at the right time | Direct |
| P5 | Passing 高数: "these are the problem types, do these ten" | Adjacent (prioritization from her own materials) |
| P6 | Resurfacing his own notes and past mistakes at the right time | Direct |
| P7 | Fast, strict 申论 feedback (plus recurring weaknesses and tonight's task) | Adjacent (feedback job) |
| P8 | Anki card-making with a page citation per card | Different (content conversion) |
| P9 | Knowing which weak topic to spend tonight's 40 minutes on | Direct |
| P10 | "remember all my mistakes and tell me what to do tonight" | Direct |

Result: 6 of 10 direct, 3 of 10 adjacent, 1 of 10 different.

Why this matters for Zero: of Zero's four pillars, persistent memory plus document grounding already come closest to this need. Scaffolding and generic push do not serve it and, per sections 2a and 2c, actively repel users.

### 3d. Surprises and contradictions versus the founder's deck narrative

Contradictions between the synthetic findings and the founder's deck (all require real-user validation):

1. "陪伴" (companionship) and "没法开始 / 走不远" (can't start, can't keep going) positioning versus a prioritization pain. The deck frames the core problem as starting and persisting. Only 2 of 10 personas agree (P2, P5), and they are the two with the lowest ability to pay (¥30 and ¥0). Most personas "show up" but do not know what to work on.
2. Scaffolding as a differentiator versus scaffolding as a churn trigger. The deck's quote "它让我自己想明白" ("it lets me figure it out myself") suggests learners value guided discovery. In the simulation, 9 of 10 said withholding answers sends them back to free AI. P5 reports leaving a guided app after one session because it "made me feel stupid". The preferred form of active learning is answer first, then self-testing (Anki, drills, generated questions), under the learner's control.
3. Push as retention versus push as mute. The deck cites User B and U17 on proactive outreach. All 10 synthetic personas had a past record of muting or abandoning check-ins, including a paid ¥299 督学 service (P2) and paid-course 班主任 (class coordinator) messages (P1, P3, P9). The only outreach anyone asked for was hyper-specific: naming the skipped subject, the recurring error or the forgetting risk.
4. The memory moat versus memory as a feature. The deck's 96% "external memory" figure comes from retained users (survivorship). In the simulation, memory is the most valued element but never the reason someone came back. Deadlines, guilt, peers and sunk-cost commitments (paid classes, the 自习室 fee) drive return.
5. ARPU ¥78.9 versus a ¥30 median. Stated WTP clusters at ¥30-39 and is mostly a substitution for ChatGPT Plus. The Pro tier is supported only where Zero would replace a paid line item. Competing for the ChatGPT or 批改 budget, not new budget, is the real pricing game.
6. Trust, not price, blocks the high-budget segments. P4 (¥12,800 course) and P9 (¥19,800 class plus a ¥400/h tutor) both call ¥99 trivial and both pay ¥0. The path in is endorsement by their human authority (teacher, tutor) and zero factual errors, not a discount.
7. The upload barrier is often effort and format, not privacy. P5 has only camera-roll photos, P7 and P9 will not scan, P8's e-books are DRM-locked, and P4 will not photograph 800 pages. The deck's 58.7% upload rate among returning users may exclude exactly these people.
8. Fragmentation is about silos, not switching. Most personas are "used to" switching. The pain is that errors and progress are spread across 3-4 places that "don't talk to each other", plus universal copy-paste. That favors integrations and export (Anki, Notion, Obsidian, UWorld, 粉笔) over an all-in-one replacement.
9. The overseas persona looks like the best domestic early adopter. P10's need and objections closely mirror P1's. This suggests the 出海 (overseas expansion) track may not need a different core product, but it adds stricter data-ownership, integration and community-proof requirements. With n = 1, this is a hypothesis only.
10. The supervision paradox. The persona who most needs accountability (P2) has the lowest budget, the worst setup tolerance and a documented history of churning from a paid supervision product.

## 4. Segment implications

Segment fit assessment across the 10 synthetic personas. It is based on need fit, feature fit, WTP and adoption barriers.

| Persona | Segment | Fit | Why |
|---|---|---|---|
| P1 Lin Zihan | Pharmacy 考研 power user | Beachhead (strongest) | Already pays ¥68/mo for AI; PDFs ready; high referral (runs a 40-person group); need is exactly memory plus grounding; rejects scaffolding and push; needs Anki and Notion export and accuracy on structures and tables |
| P10 Sofia Martinez | US MCAT post-bacc | Beachhead candidate (overseas) | Same need pattern as P1; pays $20/mo for ChatGPT; needs UWorld and Anki integration, data deletion and r/MCAT proof; substitution-only pricing |
| P3 Chen Siqi | MPAcc multi-project (thesis + CPA) | Secondary / conditional | Clear "where was I" pain across projects; ¥39 if it replaces ChatGPT Plus with zero setup; thesis upload caution; adoption only via cohort peers |
| P7 Huang Yutong | Working professional, 国考 | Adjacent segment with high WTP | Highest willingness to spend (¥60-99), but for strict 申论 grading, which is a different core job; phone-only; will not leave 粉笔 |
| P4 Wang Hao | Full-time 法考 | Later / off-season opportunity | Strong forgetting-and-resurfacing need with high budget, but trust-gated, locked to his course structure, and ¥0 during peak season; possible entry through retake years and 讲义-aligned review |
| P6 Zhang Wei | 985 CS top student | Poor paying fit (possible free-tier tester) | Mistake-resurfacing need matches, but he rejects scaffolding and push, prices at API cost, builds his own tools, and has low consumer referral |
| P2 Zhao Mingyuan | 二战考研, low budget | Need fit, poor economic fit | Only persona for whom specific outreach is the core value; ¥30 ceiling; churned from paid 督学; low setup tolerance |
| P8 Zhou Xinran | Clinical medicine | Poor fit as specified | Memory already solved by Anki; will not upload 内部资料 slides; wants cited card generation (a separate wedge); ¥30 only for that |
| P9 Sun Jianguo | MBA 联考, high budget | Poor fit | Trusts humans only; pays ¥0 for software; possible only as a tutor-facing tool |
| P5 Liu Jiayi | 二本 sophomore crammer | Poor fit | Seasonal crammer; ¥0-15; no PDFs; wants answers fast; rejects scaffolding; free-tier dorm virality at best |

Beachhead hypothesis (to test with real users): self-driven, AI-heavy candidates for a high-stakes exam, 3 to 6 months out, who:

1. already pay for a general AI tool (ChatGPT Plus or equivalent);
2. have their materials in digital form (PDF);
3. have already built a manual tracking system (Notion, Sheets, Anki) that they resent maintaining.

In this simulation that is P1 and P10, with P3 as a near neighbor. What Zero must sell to them:

- Replace ChatGPT for studying, plus automatic error memory and a "tonight" plan.
- Answer first by default, with optional self-testing.
- Export to Anki and Notion.
- Cited, accurate grounding.
- Push only when it is specific.

Poor-fit pattern: learners who are trust-gated by a human authority (P4, P9), learners with no digital materials or budget (P5), and power users who build their own tools (P6). The segment the deck emphasizes for 陪伴 (companionship) and supervision (P2, like the deck's User B) has real need but weak economics and a history of churn.

## 5. Open questions that only real human interviews can answer

Open questions for real-user validation (synthetic personas cannot answer these reliably):

1. Actual payment behavior. Do real users who say ¥30-68 actually convert at those prices, and what share cancels ChatGPT Plus rather than stacking subscriptions? Test with real checkout or pre-sale, not stated WTP.
2. The return driver. Among Zero's actual 63.5% returners, how much of return timing follows exam dates and deadlines, and how much follows Zero's memory or push? Needs cohort data aligned to exam calendars, plus retrospective interviews with churned users, not only retained ones.
3. Specific push. Does a hyper-specific, data-aware nudge ("4 days since OS; last stuck on PV operations") actually change behavior, or is it muted like everything else? No persona has experienced one. It needs a live experiment.
4. Scaffolding in practice. Do real Zero users who praise "它让我自己想明白" ("it lets me figure it out myself") use step-by-step mode voluntarily, and does answer-first-then-quiz perform as well or better on retention and conversion? An A/B test of the default mode is needed.
5. Tolerance for accuracy failures. What error rate do real users tolerate before abandoning, and does source-page citation change that threshold?
6. Upload norms. How do real students and schools treat "内部资料" (internal) slides, watermarked course 讲义 (handouts) and paid question banks? Would school or teacher endorsement unlock uploads? How much of the non-upload group is blocked by format (phone photos, DRM) rather than policy?
7. Seasonality economics. What is real lifetime value per exam cycle, and do users return for the next exam (for example CPA subject 2, or a 考研 retake)?
8. Trust transfer. Can a human authority (tutor, 助教 teaching assistant, 班主任 class coordinator, senior student) endorse or oversee Zero well enough to unlock the high-budget, trust-gated segments (P4, P9-type)?
9. Overseas. Do real overseas learners (beyond one MCAT persona) share the need? What do data-ownership and integration expectations (UWorld, Anki, AnKing) cost to meet?
10. Real language. What words do real users use for the "what should I do tonight" problem? The phrase list in 3b comes from a single generator and must be replaced with real verbatims.
11. Who actually pays. For students funded by their parents (P2, P5), who is the real buyer? Would parents pay for the specific-accountability version?
12. Adjacent jobs. Is strict AI essay grading (申论, 主观题 written answers) or cited flashcard generation a better wedge than general tutoring for specific exam segments?

## Appendix: machine-readable data

Machine-readable dataset for charts (n = 10 synthetic personas; scores V/P/I; amounts in RMB/month; USD converted at 7.2).

```json
{
  "meta": {
    "study": "Zero synthetic user research",
    "n": 10,
    "synthetic": true,
    "disclaimer": "Synthetic AI personas; exploratory only; must be validated with real human interviews; cannot predict real purchasing behavior.",
    "score_codes": {"V": "Validated", "P": "Partially validated", "I": "Invalidated"},
    "verdict_rule": "Validated if V>=6; Invalidated if I>=6 or (V=0 and I>=5); otherwise Partially Validated",
    "usd_to_rmb": 7.2,
    "baseline": {"arpu_rmb": 78.9, "paid_conversion_pct": 4.6, "tiers_rmb": [0, 39, 99, 199]}
  },
  "personas": [
    {"id": "P1", "name": "Lin Zihan"},
    {"id": "P2", "name": "Zhao Mingyuan"},
    {"id": "P3", "name": "Chen Siqi"},
    {"id": "P4", "name": "Wang Hao"},
    {"id": "P5", "name": "Liu Jiayi"},
    {"id": "P6", "name": "Zhang Wei"},
    {"id": "P7", "name": "Huang Yutong"},
    {"id": "P8", "name": "Zhou Xinran"},
    {"id": "P9", "name": "Sun Jianguo"},
    {"id": "P10", "name": "Sofia Martinez"}
  ],
  "assumptions": [
    {
      "id": "A1",
      "name": "Persistent cross-session memory drives multi-day return",
      "scores": {"P1": "P", "P2": "P", "P3": "P", "P4": "P", "P5": "I", "P6": "P", "P7": "P", "P8": "I", "P9": "I", "P10": "P"},
      "counts": {"V": 0, "P": 7, "I": 3},
      "verdict": "Partially Validated",
      "confidence": "Med"
    },
    {
      "id": "A2",
      "name": "Will pay ¥15-40 entry and a meaningful share ¥99+ Pro for private-document tutoring",
      "scores": {"P1": "V", "P2": "P", "P3": "P", "P4": "I", "P5": "I", "P6": "P", "P7": "V", "P8": "P", "P9": "I", "P10": "P"},
      "counts": {"V": 2, "P": 5, "I": 3},
      "verdict": "Partially Validated",
      "confidence": "Low"
    },
    {
      "id": "A3",
      "name": "Prefer proactive guidance/scaffolding over instant raw answers",
      "scores": {"P1": "I", "P2": "P", "P3": "P", "P4": "I", "P5": "I", "P6": "I", "P7": "I", "P8": "P", "P9": "I", "P10": "I"},
      "counts": {"V": 0, "P": 3, "I": 7},
      "verdict": "Invalidated",
      "confidence": "Med"
    },
    {
      "id": "A4",
      "name": "Tool fragmentation causes cognitive fatigue learners want solved",
      "scores": {"P1": "V", "P2": "I", "P3": "V", "P4": "P", "P5": "I", "P6": "I", "P7": "P", "P8": "P", "P9": "I", "P10": "P"},
      "counts": {"V": 2, "P": 4, "I": 4},
      "verdict": "Partially Validated",
      "confidence": "Med"
    },
    {
      "id": "A5",
      "name": "Proactive outreach is welcomed, not annoying",
      "scores": {"P1": "P", "P2": "P", "P3": "P", "P4": "P", "P5": "I", "P6": "I", "P7": "I", "P8": "I", "P9": "I", "P10": "P"},
      "counts": {"V": 0, "P": 5, "I": 5},
      "verdict": "Invalidated",
      "confidence": "Med"
    },
    {
      "id": "A6",
      "name": "Willing to upload private/copyrighted course materials",
      "scores": {"P1": "V", "P2": "V", "P3": "P", "P4": "I", "P5": "P", "P6": "V", "P7": "P", "P8": "I", "P9": "I", "P10": "P"},
      "counts": {"V": 3, "P": 4, "I": 3},
      "verdict": "Partially Validated",
      "confidence": "Med"
    },
    {
      "id": "A7",
      "name": "Primary pain is starting and persisting, not content or explanations",
      "scores": {"P1": "I", "P2": "V", "P3": "P", "P4": "I", "P5": "V", "P6": "P", "P7": "I", "P8": "I", "P9": "I", "P10": "I"},
      "counts": {"V": 2, "P": 2, "I": 6},
      "verdict": "Invalidated",
      "confidence": "Med"
    },
    {
      "id": "A8",
      "name": "Overseas English-speaking learners share the same need and would adopt the same product",
      "scoring_note": "P10 scored on own need and adoption; P1-P9 scored on whether their core need matches P10's pattern (mistake memory + tonight's priority, answer-first, alongside existing tools).",
      "scores": {"P1": "V", "P2": "P", "P3": "P", "P4": "V", "P5": "I", "P6": "V", "P7": "V", "P8": "I", "P9": "V", "P10": "P"},
      "counts": {"V": 5, "P": 3, "I": 2},
      "verdict": "Partially Validated",
      "confidence": "Low"
    }
  ],
  "wtp": [
    {"persona": "P1", "amount_rmb": 68, "ceiling_rmb": 99, "conditions": "Replaces shared ChatGPT Plus; ¥99 ceiling only if it also replaces most Notion upkeep and is accurate on pharmacology; 1-week free trial; stops after December exam", "bucket": "¥50-99", "seasonal": true},
    {"persona": "P2", "amount_rmb": 30, "ceiling_rmb": 30, "conditions": "Hard ceiling; free trial; no annual prepay; outreach must be specific; would not pay ¥99", "bucket": "¥30-49", "seasonal": false},
    {"persona": "P3", "amount_rmb": 39, "ceiling_rmb": 39, "conditions": "Free trial that works in first session with no setup; must replace on-and-off ChatGPT Plus; ¥99 not affordable as student", "bucket": "¥30-49", "seasonal": false},
    {"persona": "P4", "amount_rmb": 0, "ceiling_rmb": 39, "conditions": "¥0 now (3 weeks to exam); hypothetical ¥39 only June-October of a retake year if proven by passers and error-free on 厚大 讲义", "bucket": "¥0", "seasonal": true},
    {"persona": "P5", "amount_rmb": 0, "ceiling_rmb": 15, "conditions": "¥0 during semester; ~¥15 one-off in finals month only; prefers free version roommates use", "bucket": "¥0", "seasonal": true},
    {"persona": "P6", "amount_rmb": 20, "ceiling_rmb": 20, "conditions": "About the cost of API calls; requires Obsidian Markdown read/write and export/API; ¥0 if it requires leaving Obsidian; only 2-3 months around finals", "bucket": "¥1-29", "seasonal": true},
    {"persona": "P7", "amount_rmb": 60, "ceiling_rmb": 99, "conditions": "Strict, fast 申论 feedback; ¥99 only if it fully replaces human 批改 after proof vs teacher; phone-only; ~3 months until exam; no annual plan", "bucket": "¥50-99", "seasonal": true},
    {"persona": "P8", "amount_rmb": 30, "ceiling_rmb": 30, "conditions": "Only for Anki card generation with source-page citation per card; ¥0 for concept as described; needs senior/teacher endorsement; ≥¥50 she keeps making cards herself", "bucket": "¥30-49", "seasonal": false},
    {"persona": "P9", "amount_rmb": 0, "ceiling_rmb": 0, "conditions": "¥0 for software due to trust; would add ~¥1,600/month to human tutor instead; might try free if tutor or admitted colleagues endorse", "bucket": "¥0", "seasonal": false},
    {"persona": "P10", "amount_rmb": 144, "ceiling_rmb": 144, "incremental_amount_rmb": 0, "conditions": "$20 only as replacement for ChatGPT Plus; $0 incremental (maybe $10 for 3 months pre-test); needs r/MCAT proof, UWorld/Anki integration, data ownership/deletion", "bucket": "¥99+", "seasonal": true}
  ],
  "wtp_summary": {
    "mean_rmb": 39.1,
    "median_rmb": 30,
    "mean_rmb_p10_incremental": 24.7,
    "median_rmb_p10_incremental": 25,
    "buckets": [
      {"bucket": "¥0", "count": 3, "pct": 30},
      {"bucket": "¥1-29", "count": 1, "pct": 10},
      {"bucket": "¥30-49", "count": 3, "pct": 30},
      {"bucket": "¥50-99", "count": 2, "pct": 20},
      {"bucket": "¥99+", "count": 1, "pct": 10}
    ],
    "pay_39_unconditionally": 0,
    "stated_39_plus_with_conditions": 4,
    "pay_99_conditionally": 3,
    "pay_99_conditionally_personas": ["P1", "P7", "P10"],
    "explicitly_seasonal": 6
  },
  "objections": [
    {"text": "Generic reminders/push will be muted", "count": 10, "personas": ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10"]},
    {"text": "Withholding answers / Socratic guidance means going back to free AI", "count": 9, "personas": ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P9", "P10"]},
    {"text": "One factual error means deleting it (accuracy/trust gate)", "count": 7, "personas": ["P1", "P3", "P4", "P7", "P8", "P9", "P10"]},
    {"text": "Setup/upload effort too high (PDF, scanning, desktop, >5-10 min)", "count": 6, "personas": ["P2", "P3", "P4", "P5", "P7", "P9"]},
    {"text": "Must export to or integrate with existing system, not replace it", "count": 6, "personas": ["P1", "P4", "P6", "P7", "P8", "P10"]},
    {"text": "Needs a free trial before paying", "count": 6, "personas": ["P1", "P2", "P3", "P6", "P9", "P10"]},
    {"text": "Need ends at exam; no annual/off-season payment", "count": 6, "personas": ["P1", "P4", "P5", "P6", "P7", "P10"]},
    {"text": "Must replace existing spend, not be an additional subscription", "count": 5, "personas": ["P1", "P3", "P4", "P7", "P10"]},
    {"text": "Data privacy/copyright/ownership of uploads", "count": 5, "personas": ["P3", "P4", "P6", "P8", "P10"]},
    {"text": "Requires trusted peer or expert endorsement first", "count": 5, "personas": ["P3", "P4", "P8", "P9", "P10"]},
    {"text": "Price above free-alternative ceiling", "count": 5, "personas": ["P2", "P3", "P5", "P6", "P8"]},
    {"text": "Will not switch systems close to exam", "count": 2, "personas": ["P4", "P7"]},
    {"text": "Feels like a gimmick / built for teenagers", "count": 2, "personas": ["P6", "P10"]},
    {"text": "Content-specific handling gaps (structures/tables; multi-project)", "count": 2, "personas": ["P1", "P3"]}
  ],
  "phrases": [
    {"phrase": "copy / paste", "count": 10},
    {"phrase": "mute / turn off / swipe away / ignore", "count": 9},
    {"phrase": "trust / don't trust", "count": 9},
    {"phrase": "the answer", "count": 8},
    {"phrase": "specific", "count": 8},
    {"phrase": "annoying / annoy", "count": 8},
    {"phrase": "waste / wasted", "count": 7},
    {"phrase": "打卡", "count": 7},
    {"phrase": "what should I do / what's next / tonight", "count": 7},
    {"phrase": "generic", "count": 6},
    {"phrase": "replace", "count": 6},
    {"phrase": "free trial / free tier", "count": 6},
    {"phrase": "delete it / I'm gone / I'm done", "count": 6},
    {"phrase": "go back to ChatGPT / 豆包", "count": 5},
    {"phrase": "tired", "count": 5},
    {"phrase": "in my head", "count": 4},
    {"phrase": "guilt", "count": 4},
    {"phrase": "performative / performing studying", "count": 3},
    {"phrase": "Socratic", "count": 3},
    {"phrase": "graveyard", "count": 1},
    {"phrase": "a system prompt with a subscription", "count": 1}
  ],
  "biggest_unmet_need": {
    "statement": "Tell me what to work on tonight, based on an accurate record of what I got wrong and what I'm forgetting, without me having to maintain that record.",
    "direct_match": ["P1", "P3", "P4", "P6", "P9", "P10"],
    "adjacent_match": ["P2", "P5", "P7"],
    "different": ["P8"]
  }
}
```
