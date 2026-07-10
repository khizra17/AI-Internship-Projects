# Week 1 — Rule-Based Chatbot

Part of a 30-day, project-based AI internship: one AI project shipped every week for four weeks. This is the foundation project — small by design, meant to lock down the fundamentals before the projects get more complex.

## What it does

A simple command-line chatbot that responds to predefined greetings and exits cleanly on command. No ML, no APIs — pure control flow and decision-making logic.

**Example:**
```
Welcome back!

You: hello
Hi there!

You: how are you?
I am doing great. Thank You!

You: exit
```

## Requirements (from project rubric)

- [x] Handle greetings and exit commands
- [x] Use decision-making logic for responses
- [x] Run in a continuous loop

## Design notes

- Responses are handled via a **dictionary lookup** (`Greetings.get()`) rather than a long if-elif chain. This was confirmed as an acceptable pattern for the decision-logic requirement — dictionary dispatch is a common, cleaner alternative to nested conditionals once the number of cases grows.
- User input is normalized (lowercased, stripped) before matching, so the bot isn't case- or whitespace-sensitive.
- The loop runs indefinitely until the user types `exit`, at which point it breaks cleanly.

## How to run

```bash
python chatbot.py
```

## What's next

This project is the base for three more weekly builds, each adding complexity on top of this control-flow foundation. Progress will be tracked week by week in this repo.
