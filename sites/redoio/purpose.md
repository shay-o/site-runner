---
version: v1
date: 2026-05-25
source: Drafted by consultant from the Site's own homepage, left nav, and Role selector text as of 2026-05-25. Not yet reviewed with the team.
changelog:
  - v1 (2026-05-25): Initial draft from Site materials.
---

# Site Purpose — Redo.io

## What the Site is for

Redo.io is a free, AI-assisted platform for exploring, analysing, and generating insights about the California prison population, with the goal of helping users correct injustices in the legal system. It aims to be a one-stop shop for prison-sentence analytics — from high-level population snapshots to individual case histories, from cohort-building for legal claims to demographic disparity detection.

## Who the Site is for

The About section names three personas: **district attorneys, public defenders, and academic researchers**. The Role selector in the left nav groups users into three Roles, with example personas under each:

- **Legal** — Public Defender, District Attorney, Paralegal, Legal Assistant
- **Technical** — Data Scientist, Engineer, Analyst
- **General** — Journalist, Academic Researcher, Community Advocate

The Role choice affects what data and controls are exposed within Tools that surface the selector.

## Use Cases the Site claims to serve

Drawn from the Site's own copy. Each will become a Use Case document once confirmed with the team; some will be unserved or partially served by current Journeys.

1. Get a high-level snapshot of the CDCR population (or the non-non-non subset).
2. Build a custom cohort of similarly situated cases for a Racial Justice Act prima-facie claim.
3. Build a custom cohort for a discovery motion.
4. Build a custom cohort for policy research.
5. Analyse patterns and trends within a cohort — counties, sentence lengths, racial disparities, themes over time.
6. Inspect individual cases within a cohort to identify strong candidates for relief.
7. Find cases similar to a specific case using weighted profile matching.
8. Find a specific person or run a narrow natural-language query against the dataset.
9. Detect demographic disparities in sentencing within a cohort for an RJA claim or policy work.
10. Upload a user-supplied dataset and query it (left nav claim — homepage does not mention upload).
11. Explore justice-reform programs via the Justice Reform Q&A tool.
12. Request additional data or variables not currently in the dataset.
13. Report a bug or suggest improvements to the platform.
14. Look up what a variable in the dataset means or how it was calculated.
15. Understand what telemetry the platform collects about a user.
16. Find a step-by-step guide or technical reference for using the platform.

## Non-goals

To be defined with the team. The Site materials do not explicitly state what the platform is *not* for, which is itself worth probing — without non-goals, scope-creep findings are hard to make stick.

## Open questions

The following must be resolved with the team before Site Criteria v1 can be derived. Each is a finding from the Purpose draft itself, not from a Review Run.

1. **"Start here" contradiction.** The homepage tags Scenario Builder as "Start here." The left nav's "How to Use" lists Dashboard + Data Analysis as Step 1 and Scenario Builder as Step 2. These imply two different entry-point mental models. Which is canonical?
2. **Persona reconciliation.** The About section names 3 personas (DA, public defender, academic researcher). The Role selector lists 9+ personas across 3 Roles, including journalists and community advocates not in the About list. Are journalists and community advocates in scope, out of scope, or aspirational?
3. **Role selector inconsistency.** The Role selector is present on some Tools and absent from others. Is this intentional (some Tools genuinely don't need Role-specific behaviour), legacy (selector added later, not retrofitted), or a bug?
4. **When the Role selector is absent, what is the default Role?** Affects how we define Journeys through those Tools.
5. **Custom Query capability conflict.** The homepage describes Custom Query as natural-language search over "our dataset." The left nav says users can upload their own datasets and query them. Which is current behaviour? If both, is upload a Legal/Technical/General feature, or all three?
6. **Justice Reform Q&A.** Surfaced in the left nav but not on the homepage. Recent addition, discovery gap, or de-emphasised? Is it intended to be a primary Tool or a secondary one?
7. **Non-goals.** What is the Site explicitly *not* for? E.g., legal advice, case management, real-time data, charging decisions, individual prediction.
8. **Success measure for the Site as a whole.** "Correct injustices in the legal system" is the mission. What's the operational definition that tells you the Site is succeeding — RJA claims filed, motions won, research published, total active users by Role?

## Notes on sources

- Homepage copy and tool list: `https://tool.redoio.info/` as of 2026-05-25, captured in `/Users/jamesoreilly/Documents/Notes/Scratch & Misc/Temp - redoio.info home page.md`.
- Left nav copy and "How to Use" steps: same source, captured 2026-05-25.
- Role selector text: same source.
- About section: same source.
