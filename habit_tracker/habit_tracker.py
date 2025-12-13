import argparse
from datetime import datetime
from pathlib import Path


class HabitTracker:
    def __init__(self):
        self.data_dir = Path(__file__).parent / "data"
        self.data_dir.mkdir(exist_ok=True)

        self.pillar_files = {
            "AIEngineer": self.data_dir / "AIEngineer.txt",
            "Health": self.data_dir / "Health.txt",
            "Home": self.data_dir / "Home.txt",
            "Leisure": self.data_dir / "Leisure.txt",
            "Community": self.data_dir / "Community.txt"
        }

        self.activities = {
            "AIEngineer": [
                {"name": "Grokking ML", "options": [30, 60]},
                {"name": "Fast.ai DL", "options": [30, 60]}
            ],
            "Health": [
                {"name": "Walking", "options": [30, 60, 90]},
                {"name": "Meditation", "options": [1, 2]},
                {"name": "Sleeping", "options": [4, 6, 8]},
                {"name": "Napping", "options": [20, 90]}
            ],
            "Home": [
                {"name": "Cooking", "options": [30, 60, 90]},
                {"name": "Cleanup", "options": [30, 60, 90]}
            ],
            "Leisure": [
                {"name": "TV Binging", "options": [60, 90, 120, 360]},
                {"name": "Reading Non-Fiction", "options": [30, 60, 90]},
                {"name": "Painting", "options": [20, 30, 40]},
                {"name": "Journaling", "options": [10, 20, 30]}
            ],
            "Community": [
                {"name": "Blogging", "options": [20, 30, 40]},
                {"name": "Github Streak", "options": "commits"}
            ]
        }

    def prompt_activity(self, activity_name, options):
        if options == "commits":
            while True:
                response = input(f"{activity_name} - Commit counts (0 if not done)? ").strip()
                if response.isdigit() or response == "0":
                    return response
                print("Please enter a valid number of commits.")
        else:
            options_str = "0/" + "/".join(str(opt) for opt in options)
            while True:
                response = input(f"{activity_name} {options_str} Min? ").strip()
                if response == "0" or response in [str(opt) for opt in options]:
                    return response
                print(f"Please enter one of: {options_str}")

    def run_tracker(self, target_date=None):
        if target_date:
            date_str = target_date
        else:
            date_str = datetime.now().strftime("%Y-%m-%d")

        pillar_data = {pillar: [] for pillar in self.pillar_files.keys()}

        print(f"=== Daily Habit Tracker ({date_str}) ===\n")

        for pillar, activities in self.activities.items():
            print(f"\n--- {pillar} ---")
            for activity in activities:
                activity_name = activity["name"]
                options = activity["options"]

                value = self.prompt_activity(activity_name, options)

                if options == "commits":
                    unit = "commits"
                elif activity_name in ["Meditation"]:
                    unit = "session" if value == "1" else "sessions"
                elif activity_name in ["Sleeping"]:
                    unit = "hr"
                elif activity_name in ["Napping"]:
                    unit = "min"
                else:
                    unit = "min"

                pillar_data[pillar].append(f"{activity_name}: {value} {unit}")

        self.write_to_files(date_str, pillar_data)
        print("\n✓ Habits tracked successfully!")

    def write_to_files(self, date, pillar_data):
        for pillar, activities in pillar_data.items():
            file_path = self.pillar_files[pillar]
            entry = f"{date} | {' | '.join(activities)}\n"

            with open(file_path, 'a') as f:
                f.write(entry)


def parse_date(date_input):
    """Parse date from MMDDYYYY format to YYYY-MM-DD format."""
    try:
        date_obj = datetime.strptime(date_input, "%m%d%Y")
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        print(f"Error: Invalid date format '{date_input}'. Expected format: MMDDYYYY (e.g., 12112024)")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Daily Habit Tracker - Track your habits across 5 life pillars"
    )
    parser.add_argument(
        "date",
        nargs="?",
        default=None,
        help="Optional date in MMDDYYYY format (e.g., 12112024). If not provided, uses today's date."
    )

    args = parser.parse_args()

    target_date = None
    if args.date:
        target_date = parse_date(args.date)
        if target_date is None:
            return

    tracker = HabitTracker()
    tracker.run_tracker(target_date)


if __name__ == "__main__":
    main()
