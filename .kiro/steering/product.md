# Product steering — SoberFuture

## What we're building

A mobile-first recovery journal and clinician support platform.

### App surfaces
- **Mobile app** (Expo React Native): primary client surface — phone + tablet
- **Web app** (Next.js): marketing site + PWA journal for web users
- **Clinician portal** (Next.js): admin/clinician workspace — web-first

### Core app tabs (mobile)
1. **Journal** — daily check-ins, mood tracking, text + media entries
2. **Insights** — AI-surfaced patterns, streaks, milestones
3. **Resources** — geo-attributed recovery resources (radius search, categories)
4. **Meetings** — AA/NA/SMART Recovery/Refuge Recovery meeting finder
5. **Goals** — milestones, shareable flashcards, progress timeline
6. **Community** — house/org/public forums with segmentation rules
7. **Profile** — settings, clinician connection, privacy controls

### Clinician portal features
- Patient list with segmentation (house/org/public/private)
- Document distribution to patients
- Patient upload review
- Forum moderation
- Analytics (de-identified, aggregated only)
- Approval workflows

## Privacy non-negotiables
- All journal content encrypted at rest and in transit
- No training on customer data by default
- Explicit opt-in required for any research/training use
- De-identification pipeline required before secondary use
- Clinician sees only what patient explicitly shares
- No diagnosis, no medical advice, no claims of being a therapist
