---
slug: skill-animazioni
title: "Animations that feel right"
area: skill
where_it_runs: PC
level: medium
cost: "€0; GSAP is free"
package: "none: third-party skill from the source"
status: "I use it"
---

# Animations that feel right

**The problem.** Animations made by the AI were too many or wrong: random durations, stiff curves, menus that open from the center instead of from the button, stutters on slow computers.

**How I solved it.** For pages with motion I use a group of third-party skills. Emil Kowalski's (animate, choreograph, emil-design-eng, apple-design, review-animations, animation-performance) decide whether to animate, with what curve and duration, in what order. GreenSock's for GSAP (scrolltrigger, timeline) are for scrolling. LottieFiles' motion-design for the general principles. I name them in the brief only when there's motion.

**Why this way.** The first question of these skills is "should it animate?", and often the answer is no: they spare me motion added just to fill space. The rules on performance and reduced motion keep the page light even on Windows with reduced animations.

**When you need it.** Landing pages and sites where motion is part of the story, interfaces with menus, panels and transitions.

**When you DON'T need it.** Static pages, documents, internal dashboards where speed matters: there less motion is better.

**How to get it.** Third-party skills, from the source: https://github.com/emilkowalski/skills (MIT), https://github.com/greensock/gsap-skills, https://github.com/LottieFiles/motion-design-skill (MIT).
