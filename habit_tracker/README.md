# Daily Habit Tracker

A simple command-line habit tracking program that prompts for daily activities across five life pillars and logs them to text files.

## Features

- **5 Life Pillars**: AIEngineer, Health, Home, Leisure, Community
- **13 Activities** tracked daily with specific time/session options
- **Simple Text Storage**: Each pillar has its own `.txt` file
- **Daily Logging**: Appends entries with date and all activities on one line per pillar

## Activities Tracked

### AIEngineer
- Grokking ML (30/60 min)
- Fast.ai DL (30/60 min)

### Health
- Walking (30/60/90 min)
- Meditation (1/2 sessions)
- Sleeping (4/6/8 hr)
- Napping (20/90 min)

### Home
- Cooking (30/60/90 min)
- Cleanup (30/60/90 min)

### Leisure
- TV Binging (60/90/120/360 min)
- Reading Non-Fiction (30/60/90 min)
- Painting (20/30/40 min)

### Community
- Blogging (20/30/40 min)
- Github Streak (commit counts)

## Setup

1. Navigate to the habit_tracker directory:
```bash
cd habit_tracker
```

2. Activate the virtual environment:
```bash
source venv/bin/activate
```

## Usage

Run the habit tracker:
```bash
python habit_tracker.py
```

The program will prompt you for each activity in order by pillar. Simply enter the time/session value from the available options.

## Output

Data is stored in the `data/` directory with one file per pillar:
- `AIEngineer.txt`
- `Health.txt`
- `Home.txt`
- `Leisure.txt`
- `Community.txt`

Each line format:
```
YYYY-MM-DD | Activity1: value unit | Activity2: value unit | ...
```

Example:
```
2025-12-11 | Walking: 30 min | Meditation: 1 session | Sleeping: 8 hr | Napping: 20 min
```

## Example Run

```
=== Daily Habit Tracker ===

--- AIEngineer ---
Grokking ML 30/60 Min? 30
Fast.ai DL 30/60 Min? 60

--- Health ---
Walking 30/60/90 Min? 30
Meditation 1/2 Min? 1
Sleeping 4/6/8 Min? 8
Napping 20/90 Min? 20

--- Home ---
Cooking 30/60/90 Min? 60
Cleanup 30/60/90 Min? 30

--- Leisure ---
TV Binging 60/90/120/360 Min? 90
Reading Non-Fiction 30/60/90 Min? 30
Painting 20/30/40 Min? 20

--- Community ---
Blogging 20/30/40 Min? 30
Github Streak - Commit counts? 5

✓ Habits tracked successfully!
```
