# Post-Program Sustainment Guide — Team Members

*For participants who completed the Deep Learning Program (DLP)*
*Improving AI Transformation | August 2026*

---

You finished the program. The Embedded Engineer is gone. The training sessions are over.

What happens now is entirely up to you.

This guide is for keeping the discipline alive, recognizing what you actually built, and understanding what comes next. It won't hold your hand — you've already demonstrated you don't need that. But it will help you stay sharp when no one is watching.

---

## 1. Take Stock of What You Built

Before moving forward, get clear on what you actually have. Not what you intended to build — what you *built*, tested, iterated, and committed.

Go through the codebase and inventory your artifacts. For each one, ask yourself:

| Question | What it tells you |
|----------|-------------------|
| Is it committed? | Is it real or just something you tried once? |
| Does it have a Python evaluation script with an LLM judge? | Can you tell if it's getting better or worse against your EC? |
| Have you run at least two iterations on it? | Is this a working skill or a lucky one? |
| Are you actually using it? | Did your behavior change, or just your to-do list? |

A useful prompt for a quick audit:

> *"List all AI skills, adversarial agents, and Python evaluation scripts I committed in the last 12 weeks. For each: name, what problem it solves, current quality, and whether it's part of my daily workflow."*

Be honest with yourself. DLP Completion has four Evaluation Criteria — craft, evaluate, iterate, adopt. You may have nailed three and let one slip. Knowing where you are is more valuable than assuming you're solid across the board.

---

## 2. Keeping the Discipline Alive Without the Embedded Engineer

The Embedded Engineer created external accountability. Weekly check-ins, coaching sessions, someone who'd notice if you stopped iterating. That scaffolding is gone now.

The evaluate-iterate habit is what separates DLP Completion from Basic Prompting. Without it, you'll slowly drift back to "update the skill and hope for the better." That's how good skills die quietly.

**Make it a regular practice, not a project:**

- Block 30–60 minutes every two weeks for artifact review. Not a big event — just: *Is this still working? Should I test a hypothesis?*
- When a skill produces worse output than it used to, treat it like a failing test. Investigate before changing anything.
- Commit your evaluation script runs. Future-you will thank current-you for the documented baseline.

**Find a peer to stay accountable to:**

Pick one teammate from the program. Not a manager — a peer. Agree to a simple standing check-in: *"What did you iterate this sprint?"* It doesn't have to be formal. It just has to exist.

**Protect the habit during crunch:**

The first time a deadline hits and someone says "just ship it," you'll be tempted to skip the evaluation step. That's the moment the habit either holds or breaks. The evaluate-iterate loop doesn't take long when you're doing it regularly. It only feels expensive when you've let it lapse.

---

## 3. The Next Horizon: Continued Adoption of the Core DLP Skills

DLP Completion is about powerful, disciplined single-task automation inside your own workflow. The next step is extending those skills — coordinating *across workflows*, across handoffs, across people.

**What continued adoption looks like:**

- Applying the evaluate-iterate discipline to additional workflow steps beyond the ones you built during the program
- Building each step in a multi-step process with its own evaluated, iterated skill — not just one smart prompt
- Designing outputs of Step N to be explicit inputs of Step N+1 (format, structure, completeness)
- Building a custom harness — a Python program that orchestrates multiple model calls, passes artifacts between steps, runs evaluation scripts at each step, and manages the overall workflow (this is the Stage 4 Deep Learning Program — a future course, not this one)
- Coordinating across multiple people so that AI-assisted work becomes a shared process — not just your personal tooling

**How to know you're ready to extend:**

- You have at least 2–3 artifacts that have gone through multiple documented evaluation cycles against their Evaluation Criteria (EC)
- You understand failure modes in your current skills well enough to explain them
- You can see a specific multi-step process in your work where the handoffs are the bottleneck
- Your manager is willing to allocate time for the coordination it requires

The goal of the DLP was trajectory, not arrival. Extending beyond single-process work is a design project, not a solo skill-writing sprint. When you're ready to pursue it seriously, it's worth bringing Improving back in.

---

## 4. When Your Skills Stop Working

They will. Models update. Context windows change. Team processes shift. A skill that worked for three months will eventually produce results that feel subtly worse, then obviously worse.

**Diagnosing degradation:**

First, check whether your evaluation script is catching it. If you've been running regular evaluations, you'll have a baseline. If not, now is the time to run your evaluation script with the LLM judge and see where you actually are.

Then ask:
- Did the model change? (Check version history, release notes)
- Did the inputs change? (Are the stories, tickets, or context documents structured differently than they used to be?)
- Did the task change? (Is the work the skill was designed for actually different now?)
- Did the standard change? (Are you expecting more from it than you were before? Did your EC shift?)

**Iterate vs. rebuild:**

| Iterate when... | Rebuild when... |
|-----------------|-----------------|
| Performance drifted gradually | The task it was built for no longer exists |
| The core approach still makes sense | The model capabilities have fundamentally changed |
| You can articulate a specific hypothesis to test | The evaluation script itself is no longer meaningful |
| Runs still pass most EC | Evaluations are failing broadly and you don't know why |

Rebuilding isn't failure — it's what mature engineers do when accumulated drift exceeds what iteration can recover. The discipline is the same either way: new version goes through the same evaluate-iterate loop as the original.

---

## 5. Bringing Others Along

You will have teammates who weren't in the program. Some will be curious. Some will be skeptical. Some will do whatever you put in front of them.

You don't need to teach the whole program — just invite people into specific practices.

**Start with evaluation, not generation:**

Most people have already written some AI prompts. Instead of teaching them to write better skills, ask: *"How do you know if that skill is working?"* That question opens the door to evaluation, which is the real skill.

**Share artifacts, don't lecture:**

Check in a skill file with a README that explains what it does and how to iterate on it. That's a better teacher than a conversation. People learn by using working examples.

**Coach one specific moment:**

If a colleague is about to change a skill because they got one bad result, that's your coaching moment. Ask: *"What does your evaluation script say? Have you run it against the new version?"* You don't need to give a presentation — just ask the right question at the right time.

**Set realistic expectations:**

You can bring someone from naive to informed in a few hours of pairing. You can't bring them to DLP Completion without weeks of practice and feedback. What you can do is plant the seed for the right discipline and model what it looks like in your own work.

---

## 6. Warning Signs You're Drifting Back to Basic Prompting

Basic Prompting behavior can creep back in without you noticing. Here's what to watch for:

**In your skills:**
- You changed a skill because it gave a bad result — without first running your evaluation script
- You can't remember the last time you committed a new iteration
- You've been meaning to update the evaluation script for weeks but haven't gotten to it
- You're using skills that you didn't write and don't understand

**In your process:**
- You stopped the 30-minute iteration sessions and told yourself you'd restart "when things calm down"
- AI tools are things you use *when convenient*, not default behavior
- You're solving the same problems manually that you automated three months ago

**In your thinking:**
- You've started saying "it's faster to just do it myself" as a default, not an exception
- You haven't thought about extending your skills since the program ended
- You're not sure what artifacts are currently checked in and working

**What to do if you see these signs:**

Don't spiral. Just run the audit from Section 1. Get clear on where you are, pick one artifact, and run a documented iteration cycle. The habit doesn't take long to rebuild once you start — it's the starting that's hard.

DLP Completion isn't a destination you reach and keep forever without maintenance. It's a set of behaviors. The behaviors are yours now. Keep them.

---

*Deep Learning Program | Improving*
*Questions about what comes next? Talk to your Account Manager or reach out to Improving directly.*