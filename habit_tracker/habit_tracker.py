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

    def run_tracker(self):
        today_date = datetime.now().strftime("%Y-%m-%d")
        pillar_data = {pillar: [] for pillar in self.pillar_files.keys()}

        print("=== Daily Habit Tracker ===\n")

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

        self.write_to_files(today_date, pillar_data)
        print("\n✓ Habits tracked successfully!")

    def write_to_files(self, date, pillar_data):
        for pillar, activities in pillar_data.items():
            file_path = self.pillar_files[pillar]
            entry = f"{date} | {' | '.join(activities)}\n"

            with open(file_path, 'a') as f:
                f.write(entry)


def main():
    tracker = HabitTracker()
    tracker.run_tracker()


if __name__ == "__main__":
    main()
