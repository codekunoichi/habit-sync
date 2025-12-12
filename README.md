# Daily Habit Tracker

A simple command-line habit tracking program that helps you build and maintain positive habits across five key life pillars.

## Intent

This application is designed to help you:
- **Track daily habits** across different areas of your life in a structured way
- **Build consistency** by logging activities every day
- **Identify patterns** in your behavior over time through simple text-based logs
- **Stay accountable** to your personal goals in AI/ML learning, health, home management, leisure, and community engagement
- **Start small** with predefined time intervals that make habit formation achievable

The pillar-based approach ensures balanced personal development across technical skills (AIEngineer), physical/mental wellness (Health), domestic responsibilities (Home), personal enrichment (Leisure), and external contribution (Community).

## Features

- **5 Life Pillars**: AIEngineer, Health, Home, Leisure, Community
- **14 Activities** tracked daily with specific time/session options
- **Flexible Tracking**: Use "0" to indicate activities not done
- **Simple Text Storage**: Each pillar has its own `.txt` file for easy review
- **Daily Logging**: Appends entries with date and all activities on one line per pillar
- **No External Dependencies**: Runs entirely on standard Python libraries

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
- Journaling (10/20/30 min)

### Community
- Blogging (20/30/40 min)
- Github Streak (commit counts)

**Note**: All activities accept "0" to indicate the activity was not done that day.

## Setup

### Prerequisites
- Python 3.6 or higher
- Virtual environment (included in the repository)

### Installation Steps

1. **Clone the repository** (if not already done):
```bash
git clone https://github.com/codekunoichi/habit-sync.git
cd habit-sync
```

2. **Navigate to the habit_tracker directory**:
```bash
cd habit_tracker
```

3. **Activate the virtual environment**:

   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

   On Windows:
   ```bash
   venv\Scripts\activate
   ```

4. **Verify the setup**:
```bash
python --version  # Should show Python 3.6+
```

## How to Run the Program

### Daily Tracking

1. **Make sure you're in the habit_tracker directory** with the virtual environment activated:
```bash
cd habit_tracker
source venv/bin/activate  # On macOS/Linux
```

2. **Run the tracker**:
```bash
python habit_tracker.py
```

3. **Follow the prompts** for each activity:
   - The program will ask about each activity in order by pillar
   - Enter the number corresponding to your activity duration
   - Use "0" if you didn't do the activity that day
   - Press Enter after each input

4. **Complete all prompts** to save your daily log

### What Happens When You Run

- The program displays prompts for 14 activities organized by 5 pillars
- Each prompt shows available options (e.g., "0/30/60/90 Min?")
- Your responses are validated against allowed values
- After all inputs, data is saved to `data/` directory
- You'll see "✓ Habits tracked successfully!" when complete

## How to Test the Program

### Automated Testing

The repository includes a test script that simulates user inputs to verify the tracker works correctly.

1. **Navigate to the habit_tracker directory and activate venv**:
```bash
cd habit_tracker
source venv/bin/activate  # On macOS/Linux
```

2. **Run the test script**:
```bash
python test_run.py
```

3. **What the test does**:
   - Simulates 14 inputs (one for each activity)
   - Includes some "0" values to test "not done" functionality
   - Creates entries in all 5 pillar files
   - Displays the same prompts as the interactive version
   - Shows "✓ Habits tracked successfully!" on completion

4. **Verify the test results**:
```bash
# View the latest entries in all pillar files
tail -1 data/*.txt
```

You should see entries with today's date showing the test values.

### Manual Testing

To manually test with your own inputs:

1. **Run the tracker interactively**:
```bash
python habit_tracker.py
```

2. **Test different scenarios**:
   - Enter valid options (e.g., 30, 60, 90 for Walking)
   - Try entering "0" for some activities
   - Test invalid inputs to see validation messages
   - Complete all prompts to verify data is saved

3. **Check the output**:
```bash
# View the latest entry for each pillar
tail -1 data/*.txt

# View complete history for a specific pillar
cat data/Health.txt
```

## Output

Data is stored in the `data/` directory with one file per pillar:
- `AIEngineer.txt`
- `Health.txt`
- `Home.txt`
- `Leisure.txt`
- `Community.txt`

### File Format

Each line represents one day's activities for that pillar:
```
YYYY-MM-DD | Activity1: value unit | Activity2: value unit | ...
```

### Example Entries

**Health.txt**:
```
2025-12-11 | Walking: 30 min | Meditation: 1 session | Sleeping: 8 hr | Napping: 20 min
2025-12-12 | Walking: 0 min | Meditation: 2 sessions | Sleeping: 6 hr | Napping: 0 min
```

**Leisure.txt**:
```
2025-12-11 | TV Binging: 90 min | Reading Non-Fiction: 30 min | Painting: 20 min | Journaling: 20 min
```

**Community.txt**:
```
2025-12-11 | Blogging: 30 min | Github Streak: 5 commits
2025-12-12 | Blogging: 0 min | Github Streak: 0 commits
```

## Example Run

### Interactive Session

```
=== Daily Habit Tracker ===

--- AIEngineer ---
Grokking ML 0/30/60 Min? 30
Fast.ai DL 0/30/60 Min? 0

--- Health ---
Walking 0/30/60/90 Min? 60
Meditation 0/1/2 Min? 1
Sleeping 0/4/6/8 Min? 8
Napping 0/20/90 Min? 0

--- Home ---
Cooking 0/30/60/90 Min? 60
Cleanup 0/30/60/90 Min? 30

--- Leisure ---
TV Binging 0/60/90/120/360 Min? 90
Reading Non-Fiction 0/30/60/90 Min? 30
Painting 0/20/30/40 Min? 20
Journaling 0/10/20/30 Min? 20

--- Community ---
Blogging 0/20/30/40 Min? 30
Github Streak - Commit counts (0 if not done)? 5

✓ Habits tracked successfully!
```

### Resulting Data Files

After the above session, the data files would contain:

**data/AIEngineer.txt**:
```
2025-12-12 | Grokking ML: 30 min | Fast.ai DL: 0 min
```

**data/Health.txt**:
```
2025-12-12 | Walking: 60 min | Meditation: 1 session | Sleeping: 8 hr | Napping: 0 min
```

**data/Home.txt**:
```
2025-12-12 | Cooking: 60 min | Cleanup: 30 min
```

**data/Leisure.txt**:
```
2025-12-12 | TV Binging: 90 min | Reading Non-Fiction: 30 min | Painting: 20 min | Journaling: 20 min
```

**data/Community.txt**:
```
2025-12-12 | Blogging: 30 min | Github Streak: 5 commits
```

## Tips for Daily Use

- **Set a reminder** to run the tracker at the same time each day (e.g., before bed)
- **Be honest** with "0" entries - they help identify patterns in what you're skipping
- **Review your logs** weekly by reading the pillar files to spot trends
- **Adjust time increments** if needed by modifying the activity options in the code
- **Keep backups** of your `data/` directory to preserve your tracking history
