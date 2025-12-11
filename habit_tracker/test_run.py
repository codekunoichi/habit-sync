from io import StringIO
import sys
from habit_tracker import HabitTracker

# Simulate user inputs
test_inputs = [
    "30",   # Walking
    "1",    # Meditation
    "8",    # Sleeping
    "20",   # Napping
    "60",   # Cooking
    "30",   # Cleanup
    "90",   # TV Binging
    "30",   # Reading Non-Fiction
    "20",   # Painting
    "30",   # Blogging
    "5",    # Github Streak
    "30",   # Grokking ML
    "60"    # Fast.ai DL
]

# Reorder to match the actual order in the program
actual_inputs = [
    "30",   # Grokking ML
    "60",   # Fast.ai DL
    "30",   # Walking
    "1",    # Meditation
    "8",    # Sleeping
    "20",   # Napping
    "60",   # Cooking
    "30",   # Cleanup
    "90",   # TV Binging
    "30",   # Reading Non-Fiction
    "20",   # Painting
    "30",   # Blogging
    "5"     # Github Streak
]

sys.stdin = StringIO('\n'.join(actual_inputs))

tracker = HabitTracker()
tracker.run_tracker()

print("\nData files created successfully!")
