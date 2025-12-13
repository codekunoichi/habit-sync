from io import StringIO
import sys
from habit_tracker import HabitTracker

# Testing with some 0 values to indicate activities not done
test_inputs = [
    "30",   # Grokking ML
    "0",    # Fast.ai DL - not done
    "30",   # Walking
    "1",    # Meditation
    "8",    # Sleeping
    "0",    # Napping - not done
    "60",   # Cooking
    "0",    # Cleanup - not done
    "90",   # TV Binging
    "30",   # Reading Non-Fiction
    "20",   # Painting
    "20",   # Journaling
    "30",   # Blogging
    "0"     # Github Streak - not done
]


def test_without_date():
    """Test the tracker without specifying a date (uses today's date)."""
    print("=" * 60)
    print("TEST 1: Running tracker without date argument (today's date)")
    print("=" * 60)

    sys.stdin = StringIO('\n'.join(test_inputs))
    tracker = HabitTracker()
    tracker.run_tracker()
    print("\n✓ Test 1 completed: Data saved for today's date\n")


def test_with_date():
    """Test the tracker with a specific date (yesterday)."""
    print("=" * 60)
    print("TEST 2: Running tracker with date argument (12102024)")
    print("=" * 60)

    sys.stdin = StringIO('\n'.join(test_inputs))
    tracker = HabitTracker()
    tracker.run_tracker("2024-12-10")  # Pass date in YYYY-MM-DD format
    print("\n✓ Test 2 completed: Data saved for 12/10/2024\n")


if __name__ == "__main__":
    # Run both tests
    test_without_date()
    test_with_date()

    print("=" * 60)
    print("ALL TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print("\nYou can verify the results by running:")
    print("  tail -2 data/*.txt")
    print("\nYou should see entries for both today and 2024-12-10")
