# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Habit-Sync is a daily habit tracking application that organizes activities into 5 life pillars: AIEngineer, Health, Home, Leisure, and Community. The system tracks 13 different activities with specific time/session options and logs them to pillar-specific text files.

## Development Environment

**Working Directory**: `habit_tracker/`

All Python development happens in the `habit_tracker/` subdirectory, not the repository root.

### Setup Commands

```bash
cd habit_tracker
source venv/bin/activate
```

### Running the Application

```bash
# Run the habit tracker interactively
python habit_tracker.py

# Run automated test
python test_run.py
```

## Architecture

### Core Design: Pillar-Based Organization

The application organizes habits into 5 pillars, each stored in a separate text file in `data/`:

- **AIEngineer.txt**: Grokking ML, Fast.ai DL
- **Health.txt**: Walking, Meditation, Sleeping, Napping
- **Home.txt**: Cooking, Cleanup
- **Leisure.txt**: TV Binging, Reading Non-Fiction, Painting
- **Community.txt**: Blogging, Github Streak

### Data Storage Format

Each pillar file stores one line per day:
```
YYYY-MM-DD | Activity1: value unit | Activity2: value unit | ...
```

Example:
```
2025-12-11 | Walking: 30 min | Meditation: 1 session | Sleeping: 8 hr | Napping: 20 min
```

### HabitTracker Class Structure

The `HabitTracker` class (habit_tracker.py) uses a data-driven design:

- `self.activities`: Dictionary mapping pillars to activity configurations
- `self.pillar_files`: Maps pillar names to output file paths
- Activities are defined with `name` and `options` (valid time/count values)

**Key Methods**:
- `prompt_activity()`: Interactive CLI prompting with validation
- `run_tracker()`: Main loop through all pillars and activities
- `write_to_files()`: Appends formatted entries to pillar files

### Activity Configuration

Activities have two types of options:
1. **Time-based**: List of valid minute values (e.g., [30, 60, 90])
2. **Count-based**: String "commits" for free-form numeric input

Units are determined by activity name:
- "Meditation" ’ session/sessions
- "Sleeping" ’ hr
- "commits" option ’ commits
- Default ’ min

## Adding New Activities

To add a new activity, modify the `self.activities` dictionary in `HabitTracker.__init__()`:

```python
"PillarName": [
    {"name": "Activity Name", "options": [30, 60, 90]},
    # or for count-based:
    {"name": "Activity Name", "options": "commits"}
]
```

Also add the corresponding pillar file to `self.pillar_files` if it's a new pillar.

## Git Workflow

**Ignored directories**: `venv/`, `data/`, `__pycache__/`

The project uses focused, single-file commits. When committing changes, create separate commits per file with descriptive messages explaining the purpose of each change.

## Future Expansion

The current implementation (Phase 1) provides command-line tracking with text file storage. Future phases may include:
- FastAPI backend for web access
- Google Sheets integration
- External API connections (Fitbit, GitHub)
- Jinja2 templates for web UI
- Mobile-responsive dashboard
