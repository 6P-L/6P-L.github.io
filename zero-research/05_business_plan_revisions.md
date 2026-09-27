# Zero Recommended Business Plan Revisions
_Strategic revisions to the End User Profile, Persona, Value Proposition and Business Plan, drawn from the synthetic study's most consistent findings. Organized step by step along Bill Aulet's 24 Steps of Disciplined Entrepreneurship._

> **Important:** These recommendations rest on 10 synthetic personas. "Confidence" is relative within this simulation, not a measure of market certainty. Treat each recommendation as a hypothesis with a named validation test, and act on it only after real interviews (see the Step 6 script) and live experiments confirm it.

## Summary of the four headline revisions

| Element | Current (deck, May 2026) | Recommended revision | Confidence |
|---|---|---|---|
| End User Profile | All 在校大学生 plus 考研/考公/法考 learners who "can't start, can't keep going" | Self-driven, AI-heavy exam candidates 1–6 months out, who already pay for a general AI, have digital materials and resent maintaining a manual tracking system | Med |
| Persona | User B (weak foundation, needs a supervisor) as the emotional anchor | P1-type pharmacy 考研 power user: already studying 8–10 h a day, loses about 1 h a day to re-orienting and Notion upkeep, and pays ¥68/mo for ChatGPT | Med |
| Value Proposition | 陪伴 companionship: "helps you start, persist and manage", with scaffolding and push | "Know exactly what to study tonight. Zero remembers every mistake and everything you're forgetting, from your own materials, with no upkeep." Answer-first, cited, and exports to Anki and Notion | Med |
| Business Plan | ¥39/¥99/¥199 monthly tiers; ARPU ¥78.9; LTV ¥473 over 6 months | Exam-cycle pricing; Pro positioned as a ChatGPT Plus replacement; planning ARPU ≈ ¥40–60; LTV modeled per exam cycle; plan for post-exam churn | Low–Med |

## Phase 1: Who is your customer?

### Step 1. Market segmentation
> **Recommendation:** Segment by learner behavior and trust source, not by exam type. There are four cells: (a) AI-heavy self-directed learners, (b) learners juggling several projects, (c) low-budget learners who need accountability, (d) trust-gated learners anchored on a human course or tutor. Exam type (考研, 法考, 国考, CET, MBA, MCAT) becomes a second dimension.
> **Evidence:** Needs, objections and WTP clustered by behavior rather than by exam. P1 (考研) and P10 (MCAT) are near-identical. P4 (法考) and P9 (MBA) share a trust gate despite different exams.
> **Validation test:** In real interviews, check whether segment-level WTP and feature preferences differ more by behavior cell than by exam type.

### Step 2. Select a beachhead market
> **Recommendation:** Beachhead: professional-course 考研 candidates (pharmacy, medicine-adjacent, 408 CS) 3–6 months before the exam who already pay for a general AI tool and study from PDFs. Deprioritize the low-budget supervision segment (User B type) and the trust-gated high-budget segments (法考 full-course, MBA) for now.
> **Evidence:** P1 is the strongest fit: she already pays ¥68/mo, her need is exactly memory plus grounding, and she runs a 40-person referral group. The supervision segment has real need but a ¥0–30 ceiling and a history of churn. P4 and P9 pay ¥0 because of trust, not price.
> **Validation test:** Recruit 10 real candidates matching the beachhead criteria. At least 4 should accept the Step 6 C3 paid-pilot offer.

### Step 3. Build an End User Profile
> **Recommendation:** Rewrite the profile as: age 21–26; 1–6 months before a high-stakes exam; studies 6–10 h a day; already pays ¥40–70/mo for a general AI or keeps a shared account; materials are PDFs; keeps a hand-built tracker (Notion, Sheets, Anki) that is stale or resented; decides alone; finds tools on 小红书 and in cohort WeChat groups; trusts nothing until it is accurate on their own subject.
> **Evidence:** 6 of 10 personas named a need matching this profile directly. Every persona who tracked by hand let it go stale.
> **Validation test:** Screen-share the artifacts (Step 6, W3) of 15 real users to confirm the "stale tracker" trait.

### Step 4. Calculate the TAM for the beachhead market
> **Recommendation:** Size the beachhead bottom-up and treat the result as an estimate to validate. 考研 registrants ≈ 3.4M/yr (deck). If 10–20% already pay for AI and study from PDFs, that is ≈ 340k–680k learners. At ¥45/mo × 4–5 paying months ≈ ¥200/learner per cycle, the TAM is ≈ ¥68M–136M per year.
> **Evidence:** Synthetic WTP median ¥30, mean ¥39; beachhead personas at ¥60–68; 6 of 10 pay only seasonally.
> **Validation test:** Survey 200+ 考研 candidates (e.g. via 小红书) on current AI spend and material format to replace the 10–20% placeholder.

### Step 5. Profile the Persona for the beachhead market
> **Recommendation:** Make a P1-type learner the persona and the team's shared reference point. For example: "林子涵, 22, pharmacy senior, 110 days to 考研. Pays ¥68/mo for shared ChatGPT and loses 40 min a day maintaining Notion. Quits any tool that gets drug facts wrong twice." Keep the deck's User B as a secondary persona for the accountability add-on.
> **Evidence:** P1's buying criteria (accuracy, replacing ChatGPT, exporting to Anki and Notion) are specific and product-actionable.
> **Validation test:** Find 3 real people who match the persona closely. Interview them, then correct the persona with their verbatims.

### Step 6. Full life-cycle use case
> **Recommendation:** Redesign the flow around what the persona actually does. (1) Discovery via a 小红书 post or a cohort chat. (2) First session: upload one PDF or import ChatGPT history, and get a useful "tonight" plan within 5 minutes with no setup. (3) Daily: ask for an answer, get a cited answer, and the mistake is logged automatically. (4) The next day: the "tonight" list is built from errors and decay. (5) Weekly: export to Anki or Notion. (6) Exam day: the product holds the learner's history. (7) After the exam: they switch to the next exam and the history carries over.
> **Evidence:** 6 of 10 need setup under 5–10 minutes. 6 of 10 need export or integration. 6 of 10 stop paying after the exam.
> **Validation test:** Measure time-to-first-value and first-week return in onboarding sessions with real users.

### Step 7. High-level product specification
> **Recommendation:** Re-rank the four pillars. (1) Automatic mistake and forgetting memory. (2) A daily "tonight" priority list. (3) Answers grounded in the learner's documents with page citations. (4) Answer-first mode with optional self-testing. Keep scaffolding as a toggle, not the default. Replace generic push with specific nudges that name the subject and error, and let users switch them off. Add import from ChatGPT threads, phone photos and 讲义 chapter structure, plus export to Anki and Notion.
> **Evidence:** A3 was Invalidated (0 V / 3 P / 7 I) and A5 was Invalidated (0 V / 5 P / 5 I). The most frequent objections were generic push being muted (10/10) and withheld answers sending people back to free AI (9/10).
> **Validation test:** A/B test the default mode (answer-first vs scaffold-first) against day-7 return and conversion. Run a holdout test of specific vs generic nudges.

### Step 8. Quantify the value proposition
> **Recommendation:** Quantify the value in hours and substitution, not in feelings. Examples: "Saves the ~1 h/day spent re-orienting and maintaining trackers (P1: 40 min of Notion plus re-explaining context)." "Replaces ChatGPT Plus for studying at a comparable price." "Turns 10 minutes of deciding what to study into a ready list."
> **Evidence:** In the synthetic round, time was the scarcest resource (7 of 10 used "waste" or "wasted" about time), and ¥99+ money moved only out of an existing line item.
> **Validation test:** Instrument time-to-start and re-orientation time for real users, before and after Zero. Publish the measured delta.

### Step 9. Identify your next 10 customers
> **Recommendation:** List 10 named real people who match the beachhead persona: current Zero payers, members of the deck's 小红书 cohort from 4/13, and 考研 group-chat organizers. Interview them with the v2 script and make the C3 paid-pilot offer.
> **Evidence:** Synthetic personas cannot be customers. This step is where the evidence has to come from real people.
> **Validation test:** At least 7 of 10 confirm the persona and at least 4 prepay for a pilot.

## Phase 2: What can you do for your customer?

### Step 10. Define your Core
> **Recommendation:** Redefine the Core from 陪伴 companionship to an accurate, compounding learner record: an error-and-decay memory that makes each day's recommendation better and moves with the learner from one exam to the next. That record is what competitors can't copy by adding a memory feature.
> **Evidence:** Memory was the one concept element that attracted interest from every segment. The deck's "time compounding" data-asset thesis fits this reframing.
> **Validation test:** Track whether recommendation acceptance rises with a user's history length (e.g. week 1 vs week 6).

### Step 11. Chart your competitive position
> **Recommendation:** Put these two axes on the chart: "remembers your mistakes and forgetting across sessions" and "grounded and cited from your own materials". The real competitor is free ChatGPT, Doubao or DeepSeek plus a hand-built Notion or Anki system, not Khanmigo. Position Zero as "the study layer that sits beside your AI and your Anki."
> **Evidence:** 9 of 10 fall back to free AI. 6 of 10 refuse to give up Anki, Notion, Obsidian, UWorld or 粉笔.
> **Validation test:** In real interviews, ask what they would do if Zero disappeared tomorrow. That answer identifies the true alternative.

## Phase 3: How does your customer acquire your product?

### Step 12. Determine the customer's Decision-Making Unit (DMU)
> **Recommendation:** For the beachhead, the learner is champion, end user and economic buyer all at once. Primary influencers are cohort peers and group-chat organizers, people who already passed (上岸 stories) and, in trust-gated segments, the teacher or tutor. Parents are an economic buyer only in the supervision segment.
> **Evidence:** 5 of 10 require an endorsement from a trusted peer or expert. P2 and P5 are parent-funded.
> **Validation test:** Ask every real interviewee: "Who did you ask before your last study purchase?"

### Step 13. Map the process to acquire a paying customer
> **Recommendation:** The funnel: 小红书 or cohort post → free trial with instant value (≤5 min) → accuracy proven on the learner's own material → specific nudge on day 2–3 → paywall at the moment the "tonight" list saves them time → an exam-cycle pass. Give group-chat organizers (P1 type) a referral mechanic.
> **Evidence:** The deck reports 74.2% checkout conversion once people reach the paywall. The synthetic round points to trial and first-session value as the bottleneck (6 of 10 require a free trial).
> **Validation test:** Instrument each funnel stage and find where real users drop off.

### Step 14. Estimate the TAM for follow-on markets
> **Recommendation:** Order the follow-on markets by how closely their need matches the beachhead. (1) Other professional 考研 tracks and CPA or multi-project grad students (P3 type). (2) Overseas high-stakes exams (MCAT, USMLE; P10 type), where the need converges. (3) 法考 and MBA through teacher or tutor partnerships (P4/P9 types). (4) Mass college finals and CET (P5 type) only through a free, viral tier.
> **Evidence:** 8 of 10 personas' needs matched P10's pattern (V or P on A8). The trust-gated segments need endorsement from a human authority.
> **Validation test:** Interview at least 5 overseas learners and at least 5 tutors, and re-score A8 with real data.

## Phase 4: How do you make money off your product?

### Step 15. Design a business model
> **Recommendation:** Move from open-ended monthly subscriptions to exam-cycle subscriptions, and keep monthly billing as a fallback. Add a B2B2C channel later: teachers and tutors could use Zero to track students, which would unlock the trust-gated segments.
> **Evidence:** 6 of 10 pay only in the months before their exam. The deck shows 55% already choose quarterly plans. P9 said: "If my tutor used it to track me and he checked it, maybe."
> **Validation test:** Offer both billing options to real users and compare cycle-level revenue and uptake.

### Step 16. Set your pricing framework
> **Recommendation:** Keep ¥39/mo as the entry price. Reposition ¥99 Pro explicitly as a "ChatGPT Plus replacement for studying" (top model plus unlimited grounding). Add an exam-cycle pass, e.g. 4 months for about ¥149–199. Keep the free tier generous enough to prove memory value within a week. Keep ¥199 for heavy users, but don't count on it.
> **Evidence:** Median WTP was ¥30. 0 of 10 would pay ¥39 unconditionally. ¥99+ appears only as substitution (P1, P7, P10). P5 compared prices to milk tea ("¥39 is like eight cups").
> **Validation test:** Run a Van Westendorp survey plus a real price test across the three offers with at least 200 users.

### Step 17. Calculate the Lifetime Value (LTV) of an acquired customer
> **Recommendation:** Rebuild LTV per exam cycle. For example: ¥40–60 ARPU × 4 paying months ≈ ¥160–240 per cycle, times the probability of returning for another exam (to be measured). Treat the deck's ¥473 (¥78.9 × 6 months) as an upper bound until real cohort data supports it.
> **Evidence:** The synthetic mean WTP of ¥39 is half the current ARPU. 6 of 10 said they would churn after the exam.
> **Validation test:** Build real payer cohorts aligned to exam dates and measure retention past each exam.

### Step 18. Map the sales process to acquire a customer
> **Recommendation:** Short term: founder-led content on 小红书 and B站 showing real "tonight lists" and accuracy on real textbooks. Medium term: a referral program for group-chat organizers and campus ambassadors in the beachhead majors. Long term: partnerships with tutors and 机构 (training institutions) for the trust-gated segments.
> **Evidence:** One 小红书 note brought in about 1,000 sign-ups (deck). Referral tendency is high for P1-type users and low for trust-gated ones.
> **Validation test:** Measure cost and conversion per channel for three content formats.

### Step 19. Calculate the Cost of Customer Acquisition (COCA)
> **Recommendation:** The current COCA of ¥0 is organic and won't last at scale. Budget COCA against per-cycle LTV: target COCA ≤ ¥60 so that LTV/COCA ≥ 3 at the conservative ¥180 LTV. Track paid, organic and referral COCA separately.
> **Evidence:** A lower per-cycle LTV squeezes the acceptable COCA well below what the deck's ¥473 LTV implies.
> **Validation test:** Run a small paid test (e.g. ¥5k on 小红书 薯条 post promotion) and measure real COCA for beachhead sign-ups.

## Phase 5: How do you design and build your business?

### Step 20. Identify key assumptions
> **Recommendation:** Replace the v1 assumption list with the revised set, ranked riskiest first. R1: an automatic error-and-decay memory plus a "tonight" list drives multi-day return better than push. R2: answer-first with optional testing beats scaffold-first on retention and conversion. R3: users pay ¥39+/mo or ¥149+ per cycle when Zero replaces ChatGPT Plus for studying. R4: a single factual error causes churn, and citations reduce it. R5: specific nudges don't get muted. R6: users will upload materials once format friction (photos, 讲义 structure) is removed. R7: overseas learners share the need.
> **Evidence:** A3, A5 and A7 were Invalidated. A1, A2, A4, A6 and A8 were Partially Validated (see the Step 4–5 dashboard).
> **Validation test:** Use the Step 6 v2 script for R1–R7, then run the experiments below.

### Step 21. Test key assumptions
> **Recommendation:** Run five experiments in priority order. (1) A/B test of answer-first vs scaffold-first default mode. (2) Holdout test of specific nudges vs generic push vs none. (3) Paid pilot with three price offers (Step 16). (4) An accuracy audit on 3 subjects (pharmacology, 刑法, 408), measuring error rate and churn after an error. (5) Churned-user interviews covering why they left and what brought them back to studying.
> **Evidence:** Each experiment targets an assumption the synthetic round contradicted or could not resolve.
> **Validation test:** Pre-register a success threshold for each experiment, e.g. answer-first improves day-7 return by at least 5 percentage points.

### Step 22. Define the Minimum Viable Business Product (MVBP)
> **Recommendation:** The MVBP is something a customer pays for, uses and gets value from, so it needs only three things. (1) Upload a PDF or import ChatGPT history, and get cited answers. (2) An automatic mistake log plus a daily "tonight" list. (3) Export to Anki. Sell it as an exam-cycle pass. Park AI-generated notes, multi-project management and 督学 personas until the MVBP converts.
> **Evidence:** This is the smallest bundle that addresses the biggest unmet need, which 6 of 10 named directly and 3 more named adjacently.
> **Validation test:** At least 30% of beachhead trial users pay for the pass within 14 days.

### Step 23. Show that "the dogs will eat the dog food"
> **Recommendation:** Prove it with behavior, not stated interest. Check whether real payers act on the "tonight" list on 4 or more days a week, whether exports to Anki are used, and whether users renew for their next exam. Report these metrics in the next deck instead of total registrations.
> **Evidence:** The deck's 96% "external memory" figure comes only from retained users. The synthetic round suggests exam deadlines, not memory, drive return.
> **Validation test:** Cohort metrics on "tonight" list acceptance, D7/D30 return aligned to exam dates, and renewal across exams.

### Step 24. Develop a product plan
> **Recommendation:** Next 90 days: ship the MVBP and experiments 1–4 in the 考研 beachhead. Days 90–180: add a CPA and grad-student multi-project mode and run an English-web MCAT pilot with UWorld and Anki integration. Days 180–365: build tutor and 机构 partnerships for 法考 and MBA, and a free, viral finals mode for mass college students. Revisit the 出海 track only after at least 5 real overseas interviews confirm A8.
> **Evidence:** The sequence follows the fit and WTP ranking in the synthetic segment table and protects the beachhead focus that Disciplined Entrepreneurship requires.
> **Validation test:** Hold a stage-gate review at each phase against the Step 21 thresholds before expanding.

## What not to change yet

- **Don't drop scaffolding entirely.** Make it optional. Real Zero users praise "它让我自己想明白", so run the A/B test before deciding.
- **Don't abandon the supervision segment.** Keep specific accountability as a paid add-on for parent-funded users and test whether parents would pay for it.
- **Don't cut prices before testing substitution framing.** The synthetic round suggests how Pro is framed matters more than its price.
