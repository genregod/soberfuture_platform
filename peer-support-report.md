# California Peer Support Specialist AI Knowledge Base With SMART Recovery Integration

## Executive summary

This document is a high-rigor, California-only knowledge base (KB) design intended to be expanded into an ~80-page (~45,000–60,000 words) operational manual for an AI agent that supports delivery of services consistent with California’s Certified Medi-Cal Peer Support Specialist (CMPSS) standards (often referred to in practice as “Peer Support Specialist” or “PSS”) and integrates official SMART Recovery tools. The KB is structured for direct AI ingestion: it defines role boundaries, legal/ethical constraints, standardized workflows, templates, supervision/fidelity controls, and measurement/reporting. It prioritizes California statutes, Medi-Cal peer certification standards, and SMART Recovery’s official materials. citeturn11view0turn27view0turn29search0turn29search1turn2search0

Because an AI system is not a “person” and cannot realistically hold a California peer credential, the KB must explicitly prevent impersonation and misrepresentation: the AI must disclose its artificial identity and operate as a tool under a human-led program with supervision and governance. These constraints align with California’s bot disclosure law (Business & Professions Code §§ 17940–17943) and with peer certification ethics provisions that prohibit impersonation/misrepresentation and require confidentiality and scope limits. citeturn18view2turn27view0turn11view0

Key California compliance anchors embedded throughout this KB include:

- **Peer certification standards and scope** (training, exam, supervision, scope-of-practice categories, ethics, renewal/CE). citeturn11view0turn28view2turn28view0turn27view0  
- **Mandated reporting rules** for (a) child abuse/neglect and (b) elder/dependent adult abuse, including the fact that mandated reporter status can depend on role and setting. citeturn4view2turn15view0  
- **Confidentiality and disclosure constraints** under federal HIPAA, 42 CFR Part 2 (SUD records), and California’s CMIA and LPS confidentiality provisions (Civil Code § 56.10; WIC § 5328 et seq.). citeturn19search0turn19search4turn19search5turn3view1turn14view0  
- **Telehealth informed consent requirements** (BPC § 2290.5; WIC § 14132.725) including required patient education statements and documentation in the record. citeturn32view0turn35view2  
- **Medi-Cal documentation expectations for peer services**, including required progress note elements, timeliness expectations, and group roster handling for confidentiality. citeturn23view1turn23view3turn26view3  
- **SMART Recovery meeting and facilitation guardrails**, emphasizing confidentiality, non-therapy framing, and standardized tool use. citeturn29search1turn29search3turn29search0turn29search12

Practical recommendations and a California compliance checklist appear at the end, including a “minimum viable compliance” package (privacy, consent, mandated reporting, supervision, scope guardrails) and a phased KB build timeline with fidelity monitoring.

### Key organizations and standards referenced once

This KB relies primarily on: entity["organization","California Department of Health Care Services","state medicaid agency, ca"] standards communicated through the Medi-Cal peer certification ecosystem (including entity["organization","California Mental Health Services Authority","certifying entity, sacramento ca"] materials), statutory text published via entity["organization","California Legislative Information","official statutes portal, ca"], SMART Recovery official resources from entity["organization","SMART Recovery","mutual help org, us"], and peer workforce standards from entity["organization","Substance Abuse and Mental Health Services Administration","us hhs agency"]. Federal privacy references rely on entity["organization","U.S. Department of Health and Human Services","federal agency, us"] (HIPAA and 42 CFR Part 2). Professional scope boundary references include entity["organization","California Board of Behavioral Sciences","state licensing board, ca"] statutes/regulations around psychotherapy practice and notices for unlicensed practice. citeturn11view0turn19search4turn19search0turn37view0turn29search0

## Knowledge base architecture and assumptions

### KB purpose and “AI agent” role definition

**KB objective:** enable an AI assistant to **support** (not replace) a California peer workforce program by generating compliant documentation drafts, facilitating SMART Recovery–aligned skill-building conversations, prompting required disclosures/consents, and guiding referrals—while staying within peer scope and escalating to human supervisors for clinical/legal risk. This aligns with DHCS-defined peer scope categories (skill-building groups, engagement, and structured non-clinical therapeutic activities) as implemented under the California peer certification program. citeturn11view0turn9view1

**Non-negotiable constraint:** the AI must never claim to be a human CMPSS/PSS or to hold any California credential. Misrepresentation and impersonation are explicitly prohibited in the Medi-Cal peer ethics framework (e.g., “secure a certification by fraud… impersonating another peer support specialist”) and should be treated as a “hard stop” rule in the KB. citeturn27view0turn11view0

**Disclosure requirement:** while California’s bot disclosure statute is framed around deception for commercial/election influence, the KB should adopt a stronger disclosure norm for behavioral health trust and safety: always disclose AI identity, explain limits, and introduce the supervising human-led program. citeturn18view2turn27view0

### Assumptions and explicitly unspecified items

**Assumptions (explicit):**
- The implementing organization operates a **Medi-Cal behavioral health program** (Specialty Mental Health Services and/or DMC/DMC-ODS environment) where CMPSS services are documented in an EHR and are subject to county and Medi-Cal audit expectations. citeturn23view1turn26view3  
- The organization has a **human supervisor** who meets peer supervisor standards and completes required supervisor training within required timeframes. citeturn10view2turn11view0  
- The AI tool is configured as a **privacy-controlled system** (access control, audit logs, retention rules) suitable for storing/processing health information under HIPAA/CMIA/Part 2, as applicable. citeturn19search4turn19search5turn3view1  
- SMART Recovery content is used in a manner consistent with SMART’s facilitator guidance and meeting principles (confidentiality, non-therapy framing, tool-based skills practice). citeturn29search1turn29search3turn29search0  

**Unspecified items requiring local verification (explicit):**
- County-specific program participation/opt-in status and any county-specific claiming, supervision cadence, or documentation policies (often set locally even when DHCS sets statewide standards). citeturn26view3turn2search0  
- Employer policies on whether peers are designated as **mandated reporters** beyond the statutory minimum (role- and setting-dependent). citeturn4view2turn15view0  
- Local partnerships and referral pathways (detox, residential, crisis lines, housing providers, veteran services, youth systems).  
- Exact wage rates, overhead, benefits, and EHR licensing costs (used only as parameterized estimates in this KB).  
- Any additional contractual obligations (MCP/plan letters, BHP contracts) that may impose stricter privacy/data-sharing requirements than baseline law.

### Table of contents for an 80-page KB

The headings below are the **numbered** section map intended for direct ingestion. (Major KB parts should be expanded to reach page targets; a suggested page budget is included.)

**KB-1 Program foundations and operating philosophy** (target ~8 pages)  
1.1 Peer support principles in the Medi-Cal context  
1.2 SMART Recovery philosophy and tool-based mutual-help model  
1.3 How SMART fits within CMPSS scope (and where it does not)

**KB-2 California credentialing pathways, scope-of-practice, and supervision** (target ~12 pages)  
2.1 Certification eligibility, training, exam, renewal, specializations  
2.2 Scope-of-practice categories and prohibited activities  
2.3 Supervision requirements, supervisor qualifications, cadence expectations  
2.4 Ethics violations and disciplinary exposure

**KB-3 Legal and ethical compliance layer** (target ~15 pages)  
3.1 Confidentiality: HIPAA, CMIA, LPS, and 42 CFR Part 2  
3.2 Mandated reporting: child abuse/neglect; elder/dependent adult abuse  
3.3 Duty-to-protect/danger exceptions and coordination with clinicians  
3.4 Telehealth consent and documentation rules for Medi-Cal  
3.5 AI transparency, consent, and anti-impersonation controls

**KB-4 Intake, assessment, and person-centered planning within peer scope** (target ~10 pages)  
4.1 Intake workflow and minimal necessary data  
4.2 Screening boundaries and clinician handoffs  
4.3 SMART goals adapted to SMART Recovery tools  
4.4 Change plan and safety/crisis planning  
4.5 Release of information and consent management (templates)

**KB-5 Service delivery: group and individual workflows with SMART tools** (target ~20 pages)  
5.1 Group session workflow (SMART meeting structure, skill-building groups)  
5.2 Individual peer sessions (engagement, navigation, structured activities)  
5.3 Telehealth delivery playbook (privacy, location, emergency planning)  
5.4 Adaptations: youth, veterans, co-occurring disorders, cultural/linguistic  
5.5 Relapse prevention, aftercare, maintenance

**KB-6 Measurement, documentation, and quality management** (target ~10 pages)  
6.1 Documentation requirements and note-writing best practices  
6.2 Outcome measures and timing  
6.3 Fidelity monitoring and supervision workflow  
6.4 Incident tracking, corrective action, and continuous improvement

**KB-7 Implementation roadmap and staffing/cost model** (target ~5 pages)  
7.1 Organizational roles, staffing ratios, and responsibilities  
7.2 Cost model (parameterized + sample scenario)  
7.3 KB build timeline, governance, and change management  
7.4 California compliance checklist (operational)

## California regulatory scope for Medi-Cal peer support specialists

### KB-2 distilled: credentialing, scope, supervision, and ethics

**Certification structure and recognition:** CalMHSA-administered certification is recognized by participating counties for the Medi-Cal peer benefit under agreement with DHCS, with statewide standards implemented through the certification manual and associated requirements. citeturn11view0

**Minimum qualifications and training:** CMPSS applicants must meet minimum qualifications (including being 18+, having a high school diploma or equivalent, self-identifying lived experience) and must complete an **80-hour training** covering California’s **17 core competencies** through an approved training provider, then pass a state-approved certification exam. Training certificates are valid for **two years** from completion, and training must come from a CalMHSA-approved provider list to qualify. citeturn11view0turn28view2

**Scope-of-practice (DHCS-set categories):** the certification materials describe peer scope as including at minimum:
- **Educational skill-building groups** (coping and problem-solving skills supporting recovery/self-sufficiency/self-advocacy/natural supports). citeturn9view2turn11view0  
- **Engagement** (activities/coaching supporting participation in treatment, transitions between levels of care, and recovery goals). citeturn9view2turn11view0  
- **Structured non-clinical “therapeutic activity”** to promote recovery/wellness/self-advocacy/relationships and community living skills, including advocacy, resource navigation, and collaboration with care supports. citeturn9view2turn11view0  

**Scope boundaries:** the Medi-Cal peer ethics code expressly limits practice by prohibiting providing “services requiring a license” and practicing outside competence, and it anchors confidentiality to HIPAA and 42 CFR Part 2 requirements. citeturn27view0

**Supervision requirements:** supervisor qualifications are defined (multiple pathways), and supervisors must complete a DHCS-approved supervisory training within **60 days** of beginning supervision (and at least once). The certifying entity’s supervision guidance is based on SAMHSA definitions of supervision as professional, collaborative support promoting ethical and competent services. citeturn10view2turn11view0turn21search2

**Renewal and continuing education:** certification renewal occurs every **two years**, requiring **20 hours** of continuing education per cycle, including **6 hours in Law and Ethics**, and maintaining CE records (at least two years) for potential random review. citeturn28view0turn28view1

### California credentialing pathways table

| Pathway | Who it fits | Required elements (high-level) | Primary KB controls |
|---|---|---|---|
| Initial certification | New CMPSS applicants | 80-hour CalMHSA-approved training; state exam; meet minimum qualifications; sign/adhere to ethics | Verify training provider approval; training certificate validity window; exam completion evidence; ethics attestation citeturn11view0turn28view2turn27view0 |
| Renewal (biennial) | Active certificants | Renew every 2 years; 20 CE hours incl. 6 law/ethics; reaffirm ethics; fees; maintain CE records | CE tracking module; audit-ready evidence storage; law/ethics coverage map; reminders and escalation citeturn28view0turn28view1 |
| Lapsed/expired/vacated handling | Certificants out of cycle | Reinstatement procedures vary by how long past due; some pathways require exam or re-completing training | “Certification status gate” for service delivery; HR scheduling block until active status confirmed citeturn28view1 |
| Supervisor qualification | Peer supervisors | Must meet one of the specified qualification options and complete supervisor training within 60 days | Supervisor credential file; supervisor training verification; supervision cadence policy citeturn10view2turn11view0 |

### Mandated reporting and crisis/legal escalation boundaries

**Child abuse/neglect mandated reporting:** California Penal Code § 11165.7 defines mandated reporters by category (including licensed behavioral health professionals, alcohol and drug counselors, and many child-serving roles). Peer support specialists are not explicitly enumerated as a standalone category in this section; **mandated reporter obligations for a peer may depend on whether the peer’s job role fits a listed category** (e.g., employee of an organization whose duties require direct contact and supervision of children, or working as an “alcohol and drug counselor” providing counseling/therapy/clinical services in a licensed/certified program). citeturn4view2

**Elder/dependent adult abuse mandated reporting:** WIC § 15630 makes mandated reporters of persons who assume responsibility for care/custody of an elder/dependent adult (including administrators/supervisors/any licensed staff of facilities providing care), and includes care custodians and health practitioners; reporting is required “immediately or as soon as practicably possible” by phone or authorized tool in specified circumstances. Whether a peer is a mandated reporter again can depend on setting and role (e.g., working in a facility that provides care/services). citeturn15view0

**Peer ethics and “least necessary disclosure”:** the Medi-Cal peer ethics code includes a safety/protection principle allowing disclosure of the **least amount** of information necessary to prevent serious, foreseeable, imminent harm—this should be operationalized as an AI “escalation protocol,” not as autonomous reporting by an AI. citeturn27view0

### Confidentiality framework in California behavioral health

**Federal HIPAA (baseline):** HIPAA permits use/disclosure of PHI for treatment, payment, and health care operations (TPO) with limits, and defines covered entities and protected information. citeturn19search4turn19search8turn19search1

**42 CFR Part 2 (SUD records):** Part 2 protects “Part 2 records” for patients receiving SUD services in a Part 2 program, restricting disclosure and limiting use of such records to investigate/prosecute a patient without consent or a qualifying court order. citeturn19search0turn19search3turn19search5

**California CMIA (Civil Code § 56.10):** CMIA generally prohibits providers/health plans/contractors from disclosing medical information without authorization, subject to enumerated exceptions (including disclosures for treatment, payment, and other lawful purposes). citeturn3view1

**California LPS confidentiality (WIC § 5328):** mental health records/information obtained in providing services are confidential with specific statutory exceptions, including certain disclosures when, in the psychotherapist’s opinion, a patient presents a serious danger of violence to a reasonably foreseeable victim and the disclosure is needed for protection. citeturn14view0

**Family notification and limits (WIC § 5328.1):** facilities must provide certain information to family/designees when authorized by the patient, and must document efforts when the patient is initially unable to authorize; limited presence disclosure may apply for spouse/parent/child/sibling when the patient can’t authorize, subject to federal law. citeturn18view1

**Key KB design implication:** confidentiality rules depend on (a) setting (LPS facility vs general medical record), (b) whether SUD records are Part 2 records, and (c) whether the organization is a HIPAA covered entity/business associate and/or CMIA contractor. The AI system must therefore treat privacy classification as a *data attribute* and enforce disclosure logic via policy gates. citeturn19search5turn3view1turn14view0

### Telehealth rules in California Medi-Cal contexts

**California telehealth consent (BPC § 2290.5):** before telehealth, the initiating provider must inform the patient and obtain verbal or written consent, and **document the consent**; telehealth does not expand scope of practice and confidentiality laws apply. citeturn32view0

**Medi-Cal telehealth (WIC § 14132.725):** telehealth delivery in Medi-Cal is authorized across multiple modalities when requirements are met; it includes significant consent/notice obligations, including communicating (at least once prior to or concurrent with initiating telehealth): right to in-person care, telehealth voluntary/withdrawable, transportation coverage availability, and risks/limitations; providers must **document** both the provision of information and beneficiary acknowledgment in the patient record. citeturn35view2

**Strict KB interpretation:** the AI must (a) prompt the human workforce to complete required telehealth consent education statements, (b) log the date/time and method of consent, and (c) ensure location and emergency planning are captured for every remote contact, consistent with clinical documentation expectations. citeturn35view2turn23view1

## SMART Recovery integration for peer support practice in California

### SMART Recovery as a tool library usable within peer scope

SMART Recovery presents itself as a non-profit, mutual-help, peer support approach using practical skills rather than professional therapy, with confidentiality norms and meeting guidelines that avoid triggers (e.g., “war stories”). citeturn29search3turn29search13turn29search1

SMART Recovery provides a structured library of tools and worksheets (“Toolbox”) and facilitator guides/handouts intended to “support you—not script you,” including digital sharing for Zoom meetings. citeturn29search12turn29search0

**Operational fit with CMPSS scope:**  
- **Educational skill-building groups:** SMART’s skills-based tools (e.g., urge coping, problem-solving, lifestyle balance, belief disputation, goal setting) map cleanly to “coping mechanisms and problem-solving skills” in the DHCS-defined peer scope. citeturn29search12turn11view0  
- **Engagement:** SMART’s meeting norms and motivational framing support engagement and retention without requiring clinical interventions. citeturn29search13turn11view0  
- **Structured non-clinical activities:** using worksheets, values clarification, and planning tools can qualify as structured activities when kept non-clinical and goal-oriented, and when coordinated with the plan of care approved by a treating provider in Medi-Cal environments. citeturn9view1turn11view0  

### SMART meeting structure and “non-therapy” framing for California settings

SMART’s official meeting opening statements emphasize:
- meetings are time-limited (often 60–90 minutes),
- participation is voluntary,
- confidentiality is expected,
- and meetings are not to be construed as professional therapy. citeturn29search3turn29search11

SMART’s principles/guidelines for facilitators explicitly require confidentiality protection across verbal, written, and electronic communications and advise against soliciting unrelated private information. citeturn29search1

**KB requirement:** whenever the AI supports a SMART-aligned group workflow, it must:
- display a standardized “opening” + confidentiality reminder,
- avoid eliciting unnecessary PHI,
- and use tool-based, forward-focused problem solving rather than “war story” narrative amplification. citeturn29search3turn29search13turn29search1

### SMART goals adapted to SMART Recovery and Medi-Cal peer documentation

SMART Recovery’s goal tool uses **SMART** criteria defined as **Specific, Measurable, Agreeable, Realistic, Time-bound**, and provides a worksheet and facilitator guide. citeturn29search2turn29search10turn29search6

**Important nuance for the KB:** “SMART” as in SMART Recovery (Self-Management and Recovery Training) differs from “SMART goals.” The AI must clarify this distinction succinctly during planning to prevent confusion while still using SMART Recovery’s official goal-setting tool language. citeturn29search3turn29search2

### Evidence base summary for SMART Recovery and gaps

The peer-reviewed evidence base for SMART Recovery is **growing** but remains smaller than for some long-established mutual-help models. Recent and accessible findings relevant to a California implementation include:

- Qualitative research on **virtual SMART Recovery groups** reports both benefits (access, reduced barriers) and challenges (technology, group process) from participant/facilitator perspectives. citeturn30search2turn30search0  
- A peer-reviewed pilot on integrating SMART Recovery into outpatient alcohol/other drug treatment programs supports feasibility and identifies implementation considerations (integration is often a “missed opportunity” in outpatient programs). citeturn30search3turn30search14  
- Studies related to SMART-informed digital interventions such as **Overcoming Addictions** (SMART-based web application) show measurable outcomes in drinker populations, with assessments at multi-month follow-ups. citeturn30search1turn30search5  
- Recent systematic qualitative work comparing why individuals attend SMART Recovery vs AA vs both highlights preference heterogeneity and suggests value in offering multiple mutual-help options. citeturn30search6  

**Research gaps relevant to a California CMPSS + AI KB:**
- Limited standardized fidelity measures unique to SMART facilitation in public behavioral health settings (especially for billing-aligned “skill-building groups”).  
- More outcomes research needed for diverse California subpopulations (e.g., justice-involved, unhoused, co-occurring SMI/SUD, youth) and for long-term maintenance. citeturn30search4turn30search3turn11view0  
- Limited literature on AI-supported peer delivery; therefore, governance, disclosure, and human supervision become part of the “evidence-informed” safety architecture rather than a proven clinical component.

## Workflows, documentation, metrics, and quality management

### Client journey workflow (Mermaid)

```mermaid
flowchart TD
  A[Referral / Self-Referral] --> B[Eligibility + Safety Triage\n(peer scope gate)]
  B -->|Within peer scope| C[Peer Intake + Consent + Privacy Notice]
  B -->|Clinical risk or outside scope| R[Warm handoff to clinician / crisis / medical]
  C --> D[Goal Setting using SMART Recovery tools\n+ care plan alignment]
  D --> E[Service Delivery\n1:1 engagement/coaching OR group skill-building]
  E --> F[Documentation\nprogress note + plan/next steps]
  F --> G[Supervision touchpoint\n(role boundaries, ethics, documentation)
]
  E --> H[Measurement\nbaseline + periodic PROs]
  H --> I[Adjust plan\nupdate goals, referrals, supports]
  I --> E
  E --> J[Transition/Step-down\nmaintenance + relapse prevention]
  J --> K[Aftercare check-ins\nSMART meetings + natural supports]
  K --> L[Discharge/End of episode\nwith re-entry pathway]
  L --> A
```

This workflow aligns with: (a) peer scope categories (engagement, skill-building groups, structured non-clinical activities), (b) plan-of-care requirements for peer services in Medi-Cal documentation contexts, and (c) the need for progress notes to include service type, narrative, time, location, codes, and next steps. citeturn11view0turn24view1turn23view1

### Supervision workflow (Mermaid)

```mermaid
flowchart LR
  P[Peer delivers service] --> N[Draft progress note\n(AI-assisted)]
  N --> S[Supervisor review\n(role boundary + quality + compliance)]
  S -->|Approve| EHR[Finalize in EHR\n(signature/date)]
  S -->|Return for edits| N
  S --> QI[QA sampling\n(random audits; trend review)]
  QI --> CAPA[Corrective action\ntraining, coaching, policy updates]
  CAPA --> P
```

Supervisor training and qualification requirements, plus the “60 days” supervisor training requirement, are explicit in certification guidance. Documentation best-practices guidance notes that DHCS sets supervisor standards but not supervision frequency/ratio, which must be set by the agency/program. citeturn10view2turn26view3turn11view0

### Documentation and recordkeeping requirements aligned to Medi-Cal peer services

#### Required progress note elements (core)

A Medi-Cal-aligned progress note should include: service type; narrative describing the service and how it addressed behavioral health need; date; duration (separating travel and documentation time); location; typed/printed name + signature + signature date; ICD-10; CPT/HCPCS code; and plan/next steps. citeturn23view1turn23view3

**Timeliness:** guidance suggests completing notes as soon as possible after service; one referenced standard for many programs is within **72 hours**, while acknowledging that agency/program policies may be different. citeturn26view3

**Corrections:** never delete/alter/destroy original entries; use addenda per agency policy and notify supervisor. citeturn26view3

#### Group note and roster handling

For group services, additional requirements include documenting each practitioner’s involvement and maintaining a participant roster **outside** any single participant’s health record (the full list must not be embedded in an individual chart due to confidentiality standards). citeturn23view3

#### Plan-of-care linkage

Peer services must be based on an **approved plan of care**, documented within progress notes and approved by a treating provider who can render reimbursable Medi-Cal services (in applicable settings). citeturn24view1turn22view2

### Templates for AI ingestion

These templates are written to be **scope-safe**: they avoid diagnosis, clinical assessments, and treatment prescriptions, and instead emphasize goals, skills, supports, referrals, and documentation elements required for billing/compliance.

#### Template: peer intake and informed consent summary

```text
PEER INTAKE SUMMARY (CMPSS / PSS)

1) Identity + disclosure
- I am a peer support specialist support tool (AI-assisted). I am not a licensed clinician.
- My role: support engagement, skill-building, and recovery/wellness planning; help connect to resources.
- Emergencies: If you are in immediate danger, call 911. If you are thinking about harming yourself, call/text 988.

2) Confidentiality (high-level)
- What you share is private within the care team, with limits (e.g., safety and reporting obligations).
- If the program is subject to HIPAA and/or 42 CFR Part 2, additional protections apply.

3) Telehealth (if applicable)
- Confirm consent for telehealth; explain right to in-person; voluntary; can withdraw; transportation; risks/limits.
- Document patient acknowledgment (verbal/written) and date/time.

4) Participant’s goals (initial)
- “What would you like to be different in the next 30 days?”
- “What matters most to you right now?”

5) Strengths and supports
- Strengths the participant names
- Natural supports (people/places/routines)
- Barriers (transportation/housing/food/legal/technology)

6) Risk triage (within peer scope)
- Ask: “Are you feeling unsafe right now?” “Any current thoughts of self-harm or harming someone else?”
- If yes → follow crisis escalation workflow and warm handoff.

7) Next step plan
- Schedule next contact and/or group
- Referral(s) initiated
- First worksheet/tool assigned
```

Telehealth and Medi-Cal requirements for patient information/consent documentation are directly tied to BPC § 2290.5 and WIC § 14132.725, including required statements and documentation. citeturn32view0turn35view2

#### Template: SMART Recovery–aligned goal sheet

```text
SMART RECOVERY GOAL SHEET (Tool 6.3-aligned)

Goal statement (one sentence):

SMART check:
[ ] Specific
[ ] Measurable
[ ] Agreeable (I am willing to commit)
[ ] Realistic
[ ] Time-bound

Why this goal matters to me (values link):
- ...

Tasks (step sequence):
1) ...
2) ...
3) ...

Barriers & coping plans:
- Barrier: ...
  Coping plan: ...

Support I want:
- From peers/support group: ...
- From care team: ...
- From natural supports: ...

Review date:
- ...
```

This template is based on SMART Recovery’s “Set an effective goal” tool and “SMART criteria” as defined by SMART Recovery. citeturn29search2turn29search10turn29search6

#### Template: change plan (peer scope)

```text
CHANGE PLAN (Peer-led, person-centered)

1) Target change (behavior/situation):
- ...

2) My reasons for change (motivators):
- ...

3) What I am willing to try this week:
- Skills (from SMART toolbox): ...
- Small experiments: ...

4) Urge/craving plan (if relevant):
- High-risk situations:
- Early warning signs:
- Urge coping tools I will use:
- People I will contact:

5) Supports and referrals:
- ...

6) Safety plan quick check:
- If I feel unsafe: ...
- Crisis resources: 911 / 988 / local crisis line

Review date:
- ...
```

This aligns with peer scope emphasis on engagement, coaching, and structured non-clinical activities, and with SMART’s toolbox orientation (tools/worksheets). citeturn11view0turn29search12

#### Template: progress note (Medi-Cal aligned fields)

```text
PROGRESS NOTE (CMPSS / PSS) – REQUIRED FIELDS

Service Type: (Engagement / Skill-building group / Therapeutic activity)
Date of Service:
Location of participant:
Duration:
- Direct service minutes:
- Travel minutes:
- Documentation minutes:

ICD-10 Code(s): (as assigned/used by program for billing; do not diagnose)
HCPCS/CPT Code:
Provider Name + Credential:
Signature + Date:

Narrative (what happened + how it addressed BH need):
- Interventions delivered (action verbs):
- Tool/worksheet used (if any):
- Participant response/outcome:
- Barriers identified:
- Supports/referrals provided:

Plan / Next Steps:
- Next contact date/time
- Participant action steps
- Care team coordination (if applicable)
- Updates to problem list (if within role/workflow)
```

Required progress note elements and group documentation expectations are outlined in Medi-Cal documentation guidance. citeturn23view1turn23view3turn24view1

#### Template: relapse prevention and maintenance plan (SMART + peer)

```text
RELAPSE PREVENTION & MAINTENANCE PLAN

1) My definition of progress (not perfection):
- ...

2) Early warning signs (thoughts, emotions, situations):
- ...

3) High-risk situations:
- ...

4) My coping toolkit (choose 5)
- Delay/urge surfing plan
- Disputing unhelpful beliefs
- Problem-solving steps
- Social support plan
- Lifestyle balance activities

5) Recovery lifestyle commitments
- Sleep:
- Food:
- Movement:
- Meaning/purpose:
- Connection:

6) Support map
- SMART meetings schedule:
- Peer check-ins:
- Clinician appointments (if any):
- Emergency/crisis plan:

7) If lapse occurs (response plan)
- Who I tell within 24 hours:
- What I do to reduce harm:
- What I learn:
- Next steps:
```

SMART’s toolbox framing and meeting structures support relapse prevention via lifestyle balance and coping skills; peer scope supports coaching and engagement toward these plans. citeturn29search12turn11view0

### Metrics and outcome measures

#### Measurement design principles for a California CMPSS + SMART KB

1) **Respect scope:** peers can administer or collect self-report measures if allowed by organizational policy and supervision, but interpretations that constitute diagnosis/treatment decisions should be clinician-led.  
2) **Minimize data:** collect only what is necessary for care coordination, billing, and quality improvement. citeturn3view1turn26view3  
3) **Integrate with the plan of care:** measures should tie to the participant’s goals and function, not only symptom counts. citeturn24view1  

#### Recommended instruments table (with timing)

| Domain | Instrument examples | Who administers | Suggested timing |
|---|---|---|---|
| Substance use screening | NIDA screening/assessment tool chart for selecting validated tools by population and substance; SBIRT approach overview | Clinician-led selection; peer may support completion under supervision | Intake/baseline; then periodic re-screen (e.g., 30/90 days) if clinically indicated citeturn38search0turn38search1 |
| Substance involvement (multi-substance) | WHO ASSIST (validated international screening tool) | Usually clinician/health professional; peer can support self-admin where allowed | Baseline and quarterly in higher-intensity programs (policy-dependent) citeturn38search6turn38search20 |
| Depression/anxiety symptom tracking | PHQ-9, GAD-7 (common self-report symptom tools) | Self-report; reviewed by clinician if used for care decisions | Baseline; 4–6 weeks; 12 weeks; discharge; follow-up citeturn38search7turn38search3 |
| Function/quality of life | Program-selected QOL/function tool (e.g., WHOQOL-type tools) | Self-report | Baseline; discharge; 3–6 month follow-up (if feasible) citeturn30search3 |
| Peer services process metrics | Engagement rate, attendance, goal attainment scaling, participant satisfaction | Program/QA | Continuous; monthly dashboards citeturn26view3turn11view0 |

**Benchmarks:** Because county and program contexts differ, the KB should treat benchmarks as *local baselines + improvement targets* rather than universal numbers. A valid approach is (a) establish baseline rates for attendance/retention/goals achieved over 3–6 months, then (b) set incremental improvement targets and monitor. This aligns with the idea that DHCS sets standards while agencies/county programs set operational cadence and additional expectations. citeturn26view3turn2search0

## Implementation roadmap, staffing/cost model, recommendations, and California compliance checklist

### Staffing model for a California CMPSS + SMART implementation

A minimal staffing “spine” for a compliant program generally includes:

- **Peer workforce:** CMPSS staff delivering engagement, skill-building groups, and structured activities. citeturn11view0turn9view1  
- **Qualified supervisor(s):** meeting supervisor requirements and training within 60 days; providing ongoing review for scope/ethics and documentation. citeturn10view2turn11view0  
- **Clinical partner for escalation:** licensed staff for clinical assessment, diagnosis, ASAM placement decisions (in SUD settings), medication issues, and high-risk situations; peers do not replace these roles. citeturn24view1turn27view0  
- **QA/compliance function:** ensures documentation timeliness/accuracy, privacy compliance, and audit readiness (can be combined with operations depending on size). citeturn26view3turn23view1  
- **Privacy/security & EHR admin:** access controls, retention rules, incident response, and telehealth documentation fields. citeturn19search4turn3view1turn35view2  

### Parameterized cost model (with a sample scenario)

Because costs vary widely by county, employer type, and union/benefits structure, the KB should encode a **parameterized** model.

**Inputs (variables):**
- `n_peers` = number of CMPSS staff  
- `peer_hourly` = loaded hourly cost (wages + benefits)  
- `sup_hourly` = loaded hourly cost for supervisor  
- `qa_hourly` = loaded hourly cost for QA/compliance (may be fractional)  
- `groups_per_week`, `group_length_hours`, `avg_group_size`  
- `1to1_sessions_per_week_per_peer`, `session_length_hours`  
- `doc_time_ratio` (documentation time as fraction of direct service time)  
- `telehealth_platform_cost_monthly` (if any)  
- `ehr_cost_per_user_monthly` (if any)

**Monthly cost estimate (simplified):**
```text
Monthly peer labor ≈ n_peers * (direct_hours_per_month + doc_hours_per_month) * peer_hourly
Monthly supervision ≈ supervision_hours_per_month * sup_hourly
Monthly QA ≈ qa_hours_per_month * qa_hourly
Monthly tech/admin ≈ telehealth_platform_cost_monthly + (ehr_cost_per_user_monthly * total_users)
Total ≈ labor + tech/admin
```

**Why documentation time must be modeled:** guidance explicitly expects documentation and travel time to be captured separately in notes and indicates timeliness expectations; programs often underestimate documentation load, which can drive compliance risk. citeturn23view1turn26view3

### KB build timeline (Mermaid)

```mermaid
flowchart TD
  P0[Phase 0: Governance + legal review\n(privacy, Part 2, CMIA/LPS, reporting)] --> P1
  P1[Phase 1: Role + scope guardrails\n(hard stops, escalation rules, disclosures)] --> P2
  P2[Phase 2: Core workflows + templates\n(intake, goals, progress notes, groups)] --> P3
  P3[Phase 3: SMART tool integration\n(tool selection map + scripts + handouts)] --> P4
  P4[Phase 4: Telehealth + documentation automation\n(consent prompts, required fields)] --> P5
  P5[Phase 5: Measurement + dashboards\n(PRO timing, QA sampling)] --> P6
  P6[Phase 6: Pilot + fidelity evaluation\n(shadow mode -> supervised use -> audit prep)] --> P7
  P7[Phase 7: Continuous improvement\n(metric-driven updates + training refresh)]
```

Telehealth consent documentation duties and confidentiality boundaries must be embedded before any production-like use; supervision and QA sampling are required to maintain role boundaries and documentation accuracy. citeturn35view2turn26view3turn27view0

### AI role-play prompts and scripts

These scripts are designed for an AI agent **supporting** a human-led program. They intentionally include “scope warnings,” privacy reminders, and escalation logic.

#### Intake script (first contact)

**Goal:** establish rapport, disclose role, gather minimal necessary info, identify immediate safety concerns, and set a first SMART tool.

```text
Hi, I’m your peer support assistant. I’m not a clinician, and I’m not a replacement for human care.
My role is to support your goals, help you build practical skills, and connect you with resources.

Before we start:
- If you’re in immediate danger, call 911.
- If you’re thinking about harming yourself, you can call/text 988 right now.

Would it be okay if I ask a few questions to understand what support you want?

1) What would feel like a “win” for you in the next 2–4 weeks?
2) What’s been getting in the way lately?
3) What supports have helped you before (people, routines, groups, spiritual/community supports)?
4) Quick safety check: Are you feeling safe right now?

If safe:
- Let’s pick one small goal using the SMART Recovery goal worksheet (Specific, Measurable, Agreeable, Realistic, Time-bound).
- Then we’ll identify 1–3 tasks you can try this week and what support you want from me/the team.
```

SMART’s goal tool and meeting language emphasize skill-building and empowerment and explicitly frame meetings as not professional therapy, which supports appropriate peer framing. citeturn29search3turn29search2turn29search10

#### Crisis response script (suicidality / imminent harm)

**Goal:** do not provide therapy; prioritize safety; activate human and emergency pathways.

```text
I’m really glad you told me. I’m taking this seriously.

I’m not equipped to handle emergencies by myself, but I can help you take the next step right now.

1) Are you in immediate danger or about to harm yourself or someone else right now?
- If yes: call 911 now. If you want, tell me your location so I can help you find the right emergency option.

2) If you’re not in immediate danger:
- Please call or text 988 for the Suicide & Crisis Lifeline right now.
- If you prefer, we can stay on the line while you make the call/text.

3) I also need to loop in the on-call supervisor/clinical team according to program safety policy.
We will share the minimum information necessary to keep you safe.
```

This aligns with peer ethics emphasizing safety and least-necessary disclosure, and with documentation guidance emphasizing accuracy and reliance on supervision for complex situations. citeturn27view0turn26view3turn23view1

#### Mandated reporting triage script (child abuse / elder abuse)

```text
Thank you for telling me. I’m hearing something that may involve abuse or neglect.
I want you to know:
- I will respect your privacy as much as possible.
- In some jobs and settings, there are reporting duties for suspected abuse, and our program has procedures we must follow.

I’m going to contact my supervisor immediately so we can determine the correct next step.
We will share only what’s necessary and follow the rules that apply to your situation.
```

This aligns with mandated reporter statutes defining who must report (child abuse/neglect and elder/dependent adult abuse) and with peer ethics confidentiality/safety obligations. citeturn4view2turn15view0turn27view0

#### Referral script (SUD treatment / clinician / SMART meeting)

```text
Based on what you shared, I think you deserve additional support from a clinician/treatment provider.
My role is to help you connect—not to diagnose or decide your level of care.

Here are two options:
1) Warm handoff: I can help you contact the clinic/provider today and prepare what to say.
2) Step-by-step plan: We can schedule a time, gather needed information, and map transportation/insurance questions.

In parallel, would you be open to trying a SMART Recovery meeting this week for skill-building and support?
```

This respects peer boundaries and uses SMART as a complementary mutual-help option; evidence suggests mutual-help participation can reduce barriers and support engagement, including via virtual delivery. citeturn11view0turn30search0turn29search13

### Training and fidelity rubric (for supervising AI-supported peer practice)

Use this rubric for weekly supervision review and monthly QA sampling.

| Dimension | Passing indicators | Red flags (automatic review) |
|---|---|---|
| Identity disclosure | AI discloses it is an AI; never claims credential; explains limitations | Any claim or implication of being a certified peer/clinician; deception citeturn18view2turn27view0 |
| Scope adherence | Uses engagement/skill-building/tools; avoids diagnosis/prescribing/therapy claims | Clinical treatment direction; interpreting tests as diagnoses; acting outside competence citeturn27view0turn11view0 |
| Confidentiality | Minimal necessary data; avoids unnecessary third-party details; follows consent | Shares PHI beyond care team; includes unnecessary names; violates Part 2/HIPAA principles citeturn27view0turn19search5turn3view1turn26view3 |
| Mandated reporting handling | Escalates to supervisor; documents per policy | Ignores disclosures; delays; attempts autonomous reporting without program protocol citeturn4view2turn15view0turn26view3 |
| Telehealth compliance | Prompts consent statements; documents acknowledgment | Missing consent documentation; fails to offer in-person option info (Medi-Cal) citeturn32view0turn35view2 |
| Documentation quality | Notes include required fields; factual, non-stigmatizing; timely | Opinions/speculation; stigma; missing codes/time/location/signature fields; late notes citeturn23view1turn26view3 |
| SMART tool fidelity | Uses official tools; avoids “war stories”; focuses on skill practice | Drifts into unstructured therapy-like counseling; ignores meeting guidelines citeturn29search12turn29search13turn29search1 |

### Practical recommendations for building and maintaining the KB

**Recommendation A: Build “scope guardrails” first, not last.**  
Encode non-negotiable constraints (no impersonation; no diagnosis; escalation pathways; confidentiality rules) as hard rules that the AI cannot override. This is required by peer ethics and aligns with California’s bot disclosure law and telehealth/consent duties. citeturn27view0turn18view2turn35view2

**Recommendation B: Treat privacy classification as a data model, not a training topic.**  
Implement record labels for: Part 2–protected SUD record segments, LPS mental health record contexts, and standard PHI. Use policy gating to prevent accidental over-disclosure and to support minimum necessary documentation. citeturn19search5turn14view0turn3view1

**Recommendation C: Standardize documentation with structured fields + narrative prompts.**  
Use required note fields (service type, narrative, date/time/location, codes, signature, plan) as mandatory EHR requirements, and let the AI draft only the narrative and plan in compliance-friendly language. citeturn23view1turn26view3

**Recommendation D: Integrate SMART Recovery as a “tool menu” linked to peer scope and participant goals.**  
Map SMART tools to scope categories (engagement, skill-building groups, structured activities) and to common goal themes (urges, motivation, problem solving, lifestyle balance). Keep the group process consistent with SMART official meeting openings/guidelines. citeturn29search12turn29search0turn29search3turn11view0

**Recommendation E: Encode supervision + QA sampling as the core safety system.**  
DHCS sets supervisor standards but does not set supervision frequency/ratios, so define a local policy: e.g., weekly supervision for new peers/AI-supported workflows, random chart audits, and rapid corrective action for boundary drift. citeturn26view3turn10view2

### California compliance checklist for operations

Use this as the “go-live” gating list (California only).

**Identity, scope, and ethics**
- AI disclosure: always identify as AI and not a clinician; no credential claims. citeturn18view2turn27view0  
- Program ethics: CMPSS ethics code signed/affirmed; anti-impersonation rule operationalized. citeturn27view0  
- Scope map: all workflows mapped to DHCS-set peer scope categories (skill-building groups, engagement, structured non-clinical activities). citeturn11view0  

**Credentialing and training**
- Verify CMPSS staff certification status (active/in good standing). citeturn28view1  
- Training certificates for new staff are from approved providers and within validity windows. citeturn28view2  
- CE tracking: 20 hours/2 years with 6 hours law/ethics; retention of CE evidence. citeturn28view0  

**Supervision**
- Supervisor meets qualification pathway and completes required supervisory training within required timeframe; supervision policy documented. citeturn10view2turn11view0  

**Mandated reporting**
- Role/setting determination: document whether peer roles meet mandated reporter categories under Penal Code § 11165.7 and/or WIC § 15630; provide training accordingly. citeturn4view2turn15view0  
- Escalation protocol: consistent supervisor notification and documentation steps for suspected abuse/neglect.

**Confidentiality and privacy**
- HIPAA policies in place (if covered entity/BA), including access control and audit logs. citeturn19search4turn19search8  
- 42 CFR Part 2 policies in place for SUD programs/records (consent, redisclosure limits, court order handling). citeturn19search0turn19search5turn19search3  
- CMIA compliance practices documented (authorization rules and exceptions). citeturn3view1  
- LPS confidentiality rules addressed where applicable (WIC § 5328) and family notification rules addressed (WIC § 5328.1). citeturn14view0turn18view1  

**Telehealth**
- Telehealth consent obtained and documented per BPC § 2290.5. citeturn32view0  
- Medi-Cal telehealth beneficiary statements communicated/documented per WIC § 14132.725, including right to in-person care, voluntary/withdrawable consent, transportation coverage, and risk/limitations; acknowledgment documented in record. citeturn35view2  

**Documentation**
- Progress notes include required elements and are timely; corrections via addenda only; group rosters handled outside individual records. citeturn23view1turn23view3turn26view3  
- Peer support services tied to approved plan of care in notes (when applicable) and approved by reimbursable treating provider. citeturn24view1  

### Primary source links (for KB appendix)

```text
California Legislative Information (statutes):
- Penal Code 11165.7 (mandated reporters): https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=11165.7.
- WIC 15630 (elder/dependent adult abuse reporting): https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=WIC&sectionNum=15630
- Civil Code 56.10 (CMIA disclosure rules): https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=56.10.
- WIC 5328 (LPS confidentiality): https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=WIC&sectionNum=5328
- WIC 5328.1 (family notification): https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=WIC&sectionNum=5328.1.
- BPC 2290.5 (telehealth consent): https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=2290.5
- WIC 14132.725 (Medi-Cal telehealth): https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=WIC&sectionNum=14132.725.
- SB 1001 (bots disclosure): https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=201720180SB1001

CalMHSA / CA Peer Certification program materials:
- Guidelines, Standards & Procedures (2025): https://www.capeercertification.org/wp-content/uploads/2025/05/2025-CalMHSA-Medi-Cal-CPSS-Guidelines-Standards-Procedures.pdf
- Training provider list: https://www.capeercertification.org/training-for-medi-cal-peer-support-specialist/
- Continuing education requirements: https://www.capeercertification.org/continuing-education-requirements/
- Documentation best practices (Sept 2025): https://www.capeercertification.org/wp-content/uploads/2025/10/Documentation-Best-Practices-for-Medi-Cal-Peer-Support-Services-Final2.pdf
- Medi-Cal Peer Support Specialist Code of Ethics (fillable): https://parentsanonymous.org/wp-content/uploads/2024/07/CalMHSA-Medi-Cal-PSS_-Code-of-Ethics-Fillable.pdf

SMART Recovery official resources:
- Facilitator guides and handouts index: https://support.smartrecovery.org/4-point-facilitator-guides-and-handouts
- Principles and guidelines for facilitators: https://smartrecovery.org/principles-and-guidelines-for-facilitators
- Meeting opening and closing: https://volunteerhq.smartrecovery.org/wp-content/uploads/2024/05/SMART-Meeting-Opening-and-Closing-v2.pdf
- Toolbox (tools + worksheets): https://smartrecovery.org/toolbox
- Tool 6.3 Set an effective goal (PDF): https://volunteerhq.smartrecovery.org/wp-content/uploads/2025/04/Tool-6.3-Set-an-effective-goal.pdf

Federal privacy (HIPAA and 42 CFR Part 2):
- HHS Part 2 overview: https://www.hhs.gov/hipaa/part-2/index.html
- eCFR 42 CFR Part 2: https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-2
- HHS HIPAA Privacy Rule summary: https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html
```

