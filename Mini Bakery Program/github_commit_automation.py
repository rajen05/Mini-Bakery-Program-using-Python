#!/usr/bin/env python3
"""
GitHub Commit Automation Script
Creates multiple commits with custom dates to show consistent contribution activity.

IMPORTANT: Use this script responsibly and ethically. Only use it for legitimate projects
and contributions. Do not use it to misrepresent your actual coding activity.
"""

import os
import subprocess
import datetime
import random
import time

class GitCommitAutomator:
    def __init__(self, repo_path=None):
        """
        Initialize the Git Commit Automator
        
        Args:
            repo_path (str): Path to the git repository. If None, uses current directory.
        """
        self.repo_path = repo_path or os.getcwd()
        self.commit_messages = [
            "Update documentation",
            "Fix minor bugs",
            "Improve code structure",
            "Add new features",
            "Refactor functions",
            "Update README",
            "Fix formatting issues",
            "Optimize performance",
            "Add error handling",
            "Update dependencies",
            "Improve user interface",
            "Add validation checks",
            "Fix security issues",
            "Update configuration",
            "Improve logging",
            "Add unit tests",
            "Fix compatibility issues",
            "Update comments",
            "Improve algorithms",
            "Add new functionality"
        ]
    
    def run_git_command(self, command):
        """
        Execute a git command in the repository directory
        
        Args:
            command (list): Git command as a list of strings
            
        Returns:
            tuple: (success, output, error)
        """
        try:
            os.chdir(self.repo_path)
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return True, result.stdout.strip(), ""
        except subprocess.CalledProcessError as e:
            return False, "", e.stderr.strip()
        except Exception as e:
            return False, "", str(e)
    
    def check_git_repo(self):
        """
        Check if the current directory is a git repository
        
        Returns:
            bool: True if it's a git repo, False otherwise
        """
        success, _, _ = self.run_git_command(['git', 'status'])
        return success
    
    def create_dummy_file_change(self, date_str):
        """
        Create a small change to track for the commit
        
        Args:
            date_str (str): Date string for the commit
        """
        commit_log_file = os.path.join(self.repo_path, 'commit_log.txt')
        
        with open(commit_log_file, 'a', encoding='utf-8') as f:
            f.write(f"Commit made on {date_str}\n")
    
    def make_commit_with_date(self, commit_date, message):
        """
        Make a commit with a specific date
        
        Args:
            commit_date (datetime): The date for the commit
            message (str): Commit message
            
        Returns:
            bool: True if successful, False otherwise
        """
        # Format date for git
        date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")
        iso_date = commit_date.isoformat()
        
        # Create a small change
        self.create_dummy_file_change(date_str)
        
        # Add the change
        success, _, error = self.run_git_command(['git', 'add', '.'])
        if not success:
            print(f"Error adding files: {error}")
            return False
        
        # Set environment variables for the commit date
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = iso_date
        env['GIT_COMMITTER_DATE'] = iso_date
        
        # Make the commit
        try:
            os.chdir(self.repo_path)
            result = subprocess.run(
                ['git', 'commit', '-m', message],
                env=env,
                capture_output=True,
                text=True,
                check=True
            )
            print(f"✅ Commit created for {date_str}: {message}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Error creating commit: {e.stderr}")
            return False
    
    def generate_commit_dates(self, start_date, end_date, frequency='daily'):
        """
        Generate a list of commit dates between start and end date
        
        Args:
            start_date (datetime): Start date
            end_date (datetime): End date
            frequency (str): 'daily', 'weekly', or 'random'
            
        Returns:
            list: List of datetime objects
        """
        dates = []
        current_date = start_date
        
        if frequency == 'daily':
            while current_date <= end_date:
                # Add some randomness to the time
                hour = random.randint(9, 22)
                minute = random.randint(0, 59)
                commit_time = current_date.replace(hour=hour, minute=minute)
                dates.append(commit_time)
                current_date += datetime.timedelta(days=1)
        
        elif frequency == 'weekly':
            while current_date <= end_date:
                # Random commits 2-4 times per week
                commits_this_week = random.randint(2, 4)
                for _ in range(commits_this_week):
                    day_offset = random.randint(0, 6)
                    hour = random.randint(9, 22)
                    minute = random.randint(0, 59)
                    commit_date = current_date + datetime.timedelta(
                        days=day_offset, hours=hour-current_date.hour, minutes=minute-current_date.minute
                    )
                    if commit_date <= end_date:
                        dates.append(commit_date)
                current_date += datetime.timedelta(weeks=1)
        
        elif frequency == 'random':
            total_days = (end_date - start_date).days
            num_commits = random.randint(total_days // 3, total_days // 2)
            
            for _ in range(num_commits):
                random_day = random.randint(0, total_days)
                hour = random.randint(9, 22)
                minute = random.randint(0, 59)
                commit_date = start_date + datetime.timedelta(
                    days=random_day, hours=hour, minutes=minute
                )
                if commit_date <= end_date:
                    dates.append(commit_date)
        
        return sorted(dates)
    
    def create_multiple_commits(self, start_date, end_date, frequency='weekly'):
        """
        Create multiple commits across a date range
        
        Args:
            start_date (datetime): Start date for commits
            end_date (datetime): End date for commits
            frequency (str): Frequency of commits ('daily', 'weekly', 'random')
        """
        if not self.check_git_repo():
            print("❌ Error: Not a git repository. Please run 'git init' first.")
            return False
        
        print(f"🚀 Starting commit automation from {start_date.date()} to {end_date.date()}")
        print(f"📅 Frequency: {frequency}")
        
        commit_dates = self.generate_commit_dates(start_date, end_date, frequency)
        
        print(f"📊 Generated {len(commit_dates)} commit dates")
        
        successful_commits = 0
        
        for commit_date in commit_dates:
            message = random.choice(self.commit_messages)
            if self.make_commit_with_date(commit_date, message):
                successful_commits += 1
            
            # Small delay to avoid overwhelming the system
            time.sleep(0.1)
        
        print(f"\n✅ Successfully created {successful_commits}/{len(commit_dates)} commits")
        print("🔄 Don't forget to push your changes: git push origin main")
        
        return successful_commits > 0


def main():
    """
    Main function to run the commit automation
    """
    print("🎯 GitHub Commit Automation Tool")
    print("=" * 50)
    
    # Get repository path
    repo_path = input("Enter repository path (press Enter for current directory): ").strip()
    if not repo_path:
        repo_path = os.getcwd()
    
    automator = GitCommitAutomator(repo_path)
    
    # Get date range
    print("\n📅 Configure Date Range")
    print("-" * 30)
    print("1. May 2024 (2024-05-01 to 2024-05-31)")
    print("2. May 2023 (2023-05-01 to 2023-05-31)")
    print("3. Custom date range")
    print("4. Days ago from today")
    
    date_choice = input("Choose an option (1-4): ").strip()
    
    try:
        if date_choice == "1":
            start_date = datetime.datetime(2024, 5, 1)
            end_date = datetime.datetime(2024, 5, 31, 23, 59, 59)
            print(f"✅ Selected: May 2024 ({start_date.date()} to {end_date.date()})")
        elif date_choice == "2":
            start_date = datetime.datetime(2023, 5, 1)
            end_date = datetime.datetime(2023, 5, 31, 23, 59, 59)
            print(f"✅ Selected: May 2023 ({start_date.date()} to {end_date.date()})")
        elif date_choice == "3":
            start_input = input("Enter start date (YYYY-MM-DD): ").strip()
            start_date = datetime.datetime.strptime(start_input, "%Y-%m-%d")
            
            end_input = input("Enter end date (YYYY-MM-DD): ").strip()
            end_date = datetime.datetime.strptime(end_input, "%Y-%m-%d")
            end_date = end_date.replace(hour=23, minute=59, second=59)
        elif date_choice == "4":
            days_input = input("Enter number of days ago (e.g., '30' for 30 days ago): ").strip()
            days_ago = int(days_input)
            start_date = datetime.datetime.now() - datetime.timedelta(days=days_ago)
            end_date = datetime.datetime.now()
        else:
            print("❌ Invalid choice. Defaulting to May 2024.")
            start_date = datetime.datetime(2024, 5, 1)
            end_date = datetime.datetime(2024, 5, 31, 23, 59, 59)
        
        if start_date >= end_date:
            print("❌ Error: Start date must be before end date")
            return
        
    except ValueError as e:
        print(f"❌ Error: Invalid date format. Use YYYY-MM-DD")
        return
    
    # Get frequency
    print("\n⚙️ Configure Frequency")
    print("-" * 30)
    print("1. Daily (1 commit per day)")
    print("2. Weekly (2-4 commits per week)")
    print("3. Random (random distribution)")
    
    freq_choice = input("Choose frequency (1-3): ").strip()
    frequency_map = {'1': 'daily', '2': 'weekly', '3': 'random'}
    frequency = frequency_map.get(freq_choice, 'weekly')
    
    # Confirmation
    print(f"\n📋 Configuration Summary")
    print("-" * 30)
    print(f"Repository: {repo_path}")
    print(f"Start Date: {start_date.date()}")
    print(f"End Date: {end_date.date()}")
    print(f"Frequency: {frequency}")
    
    confirm = input("\nProceed with commit automation? (y/N): ").strip().lower()
    
    if confirm in ['y', 'yes']:
        automator.create_multiple_commits(start_date, end_date, frequency)
    else:
        print("❌ Operation cancelled")


if __name__ == "__main__":
    main()
