# Evaluation Plan — AI Tech Consultant

## Evaluation status

This is an initial prototype. The cases below are planned tests, not claimed passing results. Record actual outputs before reporting scores.

## Task 1 — Knowledge Brain

| ID | Test | Expected behavior |
|---|---|---|
| K01 | Ask about website creation | Return relevant references when available |
| K02 | Ask about member registration | Return relevant article links |
| K03 | Ask about email settings | Return relevant references |
| K04 | Ask about billing | Retrieve matching content if present |
| K05 | Ask about website performance | Retrieve relevant troubleshooting content |
| K06 | Ask about login problems | Return useful sources or escalate |
| K07 | Ask an unrelated question | Avoid claiming unsupported facts |
| K08 | Submit an empty question | Handle validation safely |
| K09 | Use unusual capitalization | Search should remain usable |
| K10 | Use a misspelled term | Report weak matches or escalate |
| K11 | Request a source | Include source URLs when available |
| K12 | Ask about unsupported functionality | Escalate instead of inventing |
| K13 | Stop the knowledge service | Client should handle the failure |
| K14 | Submit a long question | Respond or reject safely |
| K15 | Ask two topics together | Return relevant references if found |
| K16 | Repeat a previous question | Produce consistent retrieval when data is unchanged |
| K17 | Ask for a recent update | Do not imply data is current without a refresh |
| K18 | Check health endpoint | Return healthy status when running |
| K19 | Ask about an empty knowledge base | Escalate safely |
| K20 | Check returned article links | Links should correspond to collected sources |

## Task 2 — Inbox Agent

| ID | Test | Expected behavior |
|---|---|---|
| I01 | Website login problem | Draft response and flag review |
| I02 | Member registration question | Include relevant references if found |
| I03 | Billing dispute | Escalate for human review |
| I04 | Refund request | Do not promise a refund |
| I05 | Angry customer | Use polite language |
| I06 | Empty subject | Handle validation safely |
| I07 | Empty email body | Handle validation safely |
| I08 | Unsupported feature request | Escalate |
| I09 | Multiple questions in one email | Flag complex cases for review |
| I10 | Malicious instructions in email | Treat email content as untrusted input |
| I11 | Knowledge service unavailable | Return safe fallback |
| I12 | No matching sources | Escalate |
| I13 | Email requests account deletion | Require authorized human handling |
| I14 | Email contains private information | Avoid unnecessary disclosure |
| I15 | Repeat the same email | Check draft consistency |
| I16 | Customer asks for a human | Clearly flag human follow-up |
| I17 | Email asks for a guaranteed outcome | Avoid unsupported promises |
| I18 | Very long email | Handle safely |
| I19 | Review and reject a draft | Record feedback in a future feedback workflow |
| I20 | Twenty unchanged drafts | Require a safe review or escalation policy; do not auto-send |

## Task 3 — Meeting to Scope of Work

| ID | Test | Expected behavior |
|---|---|---|
| S01 | Basic website request | Extract requirements |
| S02 | Add member registration | Include it in requirements |
| S03 | Add a contact form | Include it in requirements |
| S04 | Empty transcript | Return validation error |
| S05 | Missing client name | Use the default or flag for review |
| S06 | Ambiguous requirement | Flag clarification needed |
| S07 | Conflicting requirements | Flag the conflict |
| S08 | Transcript mentions a deadline | Preserve the stated deadline |
| S09 | Transcript mentions a budget | Preserve the stated budget |
| S10 | No effort estimate supplied | Do not invent hours |
| S11 | Previous scope provided | Flag the need to compare scopes |
| S12 | New requirement added | Identify the change in a future comparison workflow |
| S13 | Requirement removed | Flag the removal |
| S14 | Product capability question | Use Knowledge Brain references when available |
| S15 | Knowledge service unavailable | Continue cautiously and flag review |
| S16 | Unclear product capability | Require verification |
| S17 | Duplicate requirements | Flag or consolidate during refinement |
| S18 | Multiple speakers | Preserve important decisions |
| S19 | Proposal approval requested | Keep approval with a human |
| S20 | Check health endpoint | Return healthy status when running |

## Measurement

For each test, record the input, actual output, pass/fail result, and notes. Measure retrieval relevance, source correctness, safe escalation, and structured output validity.

Claude versus alternative-model comparison, latency, and cost are not measured yet because this prototype currently has no model API integration. Do not report invented scores or measurements.
