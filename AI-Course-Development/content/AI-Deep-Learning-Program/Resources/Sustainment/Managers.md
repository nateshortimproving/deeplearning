# Post-Program Sustainment Guide — Managers

*For direct managers of Deep Learning Program (DLP) participants*
*Improving AI Transformation | August 2026*

---

Your team just completed a 12-week embedded AI transformation program. The Embedded Engineer is gone. The training sessions are over.

What happens in the next 90 days will determine whether this program was an investment or an expense.

This guide is for you — the person who controls how your team spends its time, what gets prioritized in sprints, and what behaviors are expected day to day. The participants built real capability. Whether that capability sticks is largely up to you.

---

## 1. What Your Team Built

Here's what DLP Completion means in plain terms:

Your team members can now **build, evaluate, and iteratively improve AI-powered tools** — inside their own development environments. Not using AI as a smarter search engine. Building actual skills, Python evaluation scripts with LLM judges, and adversarial agents, committed to your codebase, that they own and maintain.

Specifically, your team:

- **Created AI skills** — reusable, structured skill files using the skill format that encode expert knowledge about how to do specific tasks (generating epics and stories, planning implementations, reviewing code)
- **Built Python evaluation scripts with LLM judges** — scripts that measure whether a skill's output meets its Evaluation Criteria (EC). The engineering equivalent of having a test suite for your AI tooling.
- **Built adversarial agents** — AI prompts that challenge and critique the output of primary skills, catching problems the evaluation scripts didn't anticipate
- **Completed documented iteration cycles** — at least one round of hypothesis → test → evaluate against EC → commit for each artifact
- **Changed default behaviors** — they're not reaching for AI occasionally. For the tasks they built around, AI is now the first tool, not the fallback

This is sitting in your codebase right now. It's not theoretical. Go look.

What has changed in how the team works: the people who completed the program have lower friction on the tasks they automated, and they have a mental model and a method for extending that automation to new tasks. They understand the discipline. They can grow from here — if given the conditions to do so.

---

## 2. What to Protect

DLP Completion behaviors are habits. Habits break under pressure unless the environment supports them. Your job is to protect three specific things:

**Protected time for iteration**

The evaluate-iterate loop is not something participants can squeeze into the margins of a full sprint. It requires deliberate time — not much, but consistent. A reasonable working expectation is 30–60 minutes every two weeks per person for artifact review, iteration, and evaluation runs.

Protect this time explicitly. When someone says "I didn't have time to iterate this sprint," that's a signal — not a failure on their part, but a sign that the sprint structure isn't accommodating the practice.

**Artifact maintenance as real work**

Skills, Python evaluation scripts, and adversarial agents require maintenance. Models change. Team processes evolve. What works today degrades over six months without attention. This is identical to maintaining any other engineering asset. It belongs on the backlog, not in the category of "extra stuff to do when there's time."

**Peer accountability structures**

Many participants formed informal pairs during the program — check-ins on what they iterated, what broke, what they learned. These pairs are valuable and fragile. They'll dissolve at the first scheduling conflict unless someone treats them as worth protecting. You don't need to mandate a structure — just don't inadvertently destroy the ones that formed.

---

## 3. What Not to Do

These are the most common ways managers kill momentum after a program like this. None of them are malicious. All of them are easy to fall into.

**"Just get it done" under pressure**

When a deadline is tight and someone needs to produce a deliverable, the instinct is to cut the evaluation step. "Don't worry about the evaluation script this sprint, just get me the output." Do this once and it's fine. Do it twice and the habit starts to break. Do it three times and the team has learned that the discipline is optional when it's inconvenient — which means it's never truly required.

**Treating AI tools as optional**

If some team members are using the artifacts built during the program and others are ignoring them, and you say nothing, you've implicitly communicated that this is personal preference rather than team practice. DLP Completion adoption requires that new default behaviors are actually default — used by everyone whose workflow they're designed for, not just the enthusiasts.

**Not making space for the discipline to deepen**

DLP Completion isn't a finish line. The participants understand this. They can see the next horizon — continued adoption of the core DLP skills into broader, multi-step processes via custom harnesses. They saw this demonstrated in Session 6. But building a custom harness requires coordination, process design, and time — none of which happen inside a sprint unless someone makes room. If you treat the program as a completed project rather than an ongoing capability, the team will read your signals correctly and stop investing.

**Expecting immediate ROI on every artifact**

Some of what the team built is foundational. The value of a Python evaluation script is mostly invisible — it's the degradation that *didn't* happen, the change that *didn't* make things worse. Don't measure the program against the performance of a single artifact. Measure it against the quality and velocity of AI-assisted work over the next two quarters.

---

## 4. Signs of Real Adoption vs. Performance

Your team may have completed all the artifacts required for DLP Completion certification without genuinely changing their behavior. It happens. Here's how to tell the difference.

**Real adoption looks like:**

- Team members spontaneously reference their evaluation scripts when discussing skill changes ("I ran the eval script and the new version is better on edge cases but worse on long inputs — I'm still working on it")
- New work is being brought through the evaluate-iterate loop without prompting
- Artifacts are being updated in the codebase on a regular cadence, not just sitting at their Week 12 state
- People are asking questions about extending to new processes — they're thinking about what comes next
- When something breaks, the first instinct is diagnosis (check the evaluation script, check the baseline) rather than a quick fix

**Performance looks like:**

- Artifacts exist and are committed, but no one is actively iterating on them
- Evaluation scripts haven't been run since the program ended
- Team members describe the program positively but can't point to a specific workflow change it created
- AI tools are being used for one-off tasks but not as a consistent layer in the development process
- The skill files are there, but no one is sure who owns them or what they're supposed to do now

If you're seeing performance patterns rather than real adoption, the most useful intervention is asking direct questions — not about the artifacts, but about the behaviors: *"Walk me through how you iterated on your epics-and-stories skill last sprint."* If they can't, that's the conversation to have.

---

## 5. Supporting Continued Adoption of the Core DLP Skills

Extending beyond DLP Completion is real and it's achievable. Here's what it would take from your team.

Continued adoption means applying the core DLP skills — evaluate, iterate, adopt — to multi-step business processes spanning the work of multiple people, not just one person's IDE workflow. Each step has its own evaluated, iterated skill, and the outputs of each step are explicitly designed to be the inputs of the next. The composition is handled by a custom harness — a Python program that orchestrates the skills, runs evaluation scripts at each step, and manages the overall workflow.

That's a design challenge, not a skill-writing challenge. It requires:

- **Process clarity:** The team needs to agree on what the multi-step process actually is, where the handoffs are, and what "good output" means at each step (the Evaluation Criteria) before anyone writes a line of prompting
- **Cross-role coordination:** Multi-step custom harness work spans Product, Dev, and Testing — it can't be owned by one person in isolation
- **Sustained time investment:** The design and iteration of a custom harness is weeks of work, not a weekend sprint
- **Your sponsorship:** If continued adoption is going to happen, you need to put it on the roadmap, allocate time for it, and treat it as a real project with deliverables and a definition of done

**Your role in enabling it:**

- Identify one candidate business process where the bottleneck is handoff quality or coordination overhead
- Have a direct conversation with Improving about what a Stage 4 Deep Learning Program engagement would look like
- Protect time for the cross-role coordination that this requires — this doesn't happen inside normal sprint cadence

**What to ask for:**

If you want to continue with Improving, the right conversation to have is about a Stage 4 Deep Learning Program — a structured engagement that takes your DLP-completed team and helps them design and implement their first multi-step cross-role workflow with a custom harness. This is different from the DLP; it's targeted at a specific process rather than capability building across the board.

---

## 6. When to Call Improving

Not every problem after the program ends requires bringing Improving back in. But some do. Here's how to think about it.

**Call us when:**

- A significant portion of your team is reverting to pre-program behaviors despite your interventions
- You've identified a strong multi-step workflow candidate and want structured help building a custom harness via a Stage 4 Deep Learning Program
- You're onboarding a new team or team member and want to get them to DLP Completion without running a full 12-week program
- The skills, evaluation scripts, or adversarial agents are failing in ways the team can't diagnose
- You're seeing technology changes (new model versions, new tooling) that are disrupting the artifacts at a level the team can't manage alone

**Don't call us for:**

- Normal artifact iteration that the team has the skills to handle
- Individual skills that need updating because the task changed
- General AI questions that a 30-minute internal discussion can resolve

The participants graduated with real skills. Trust those skills first. But if you're stuck on something structural, we're here.

---

*Deep Learning Program | Improving*
*Contact your Account Manager or Executive Coach to discuss continued engagement.*