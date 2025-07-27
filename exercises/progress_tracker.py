#!/usr/bin/env python3
"""
Progress Tracker for Python Step by Step Exercises
Helps students track their completion of exercises and projects
"""

import json
import os
from datetime import datetime

class ProgressTracker:
    """Track student progress through all exercises"""
    
    def __init__(self, student_name="Student"):
        self.student_name = student_name
        self.progress_file = "my_progress.json"
        self.exercises = self._get_exercise_list()
        self.progress = self._load_progress()
    
    def _get_exercise_list(self):
        """Get list of all exercises"""
        return [
            {"week": 1, "name": "Fortune Teller", "folder": "week-01-fortune-teller"},
            {"week": 2, "name": "Mad Libs Generator", "folder": "week-02-mad-libs"},
            {"week": 3, "name": "Number Guessing Game", "folder": "week-03-number-game"},
            {"week": 4, "name": "Rock Paper Scissors", "folder": "week-04-rock-paper-scissors"},
            {"week": 5, "name": "Temperature Converter", "folder": "week-05-temperature-converter"},
            {"week": 6, "name": "Contact Book", "folder": "week-06-contact-book"},
            {"week": 7, "name": "Journal App", "folder": "week-07-journal-app"},
            {"week": 8, "name": "Quiz Game", "folder": "week-08-quiz-game"},
            {"week": 9, "name": "Grade Analysis Tool", "folder": "week-09-grade-analysis"},
            {"week": 10, "name": "Weather Dashboard", "folder": "week-10-weather-dashboard"},
            {"week": 11, "name": "Text Adventure Game", "folder": "week-11-text-adventure"},
            {"week": 12, "name": "Todo GUI Application", "folder": "week-12-todo-gui"}
        ]
    
    def _load_progress(self):
        """Load existing progress or create new"""
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r') as f:
                return json.load(f)
        else:
            # Initialize progress
            progress = {
                "student_name": self.student_name,
                "started_date": datetime.now().isoformat(),
                "exercises": {}
            }
            for exercise in self.exercises:
                progress["exercises"][exercise["folder"]] = {
                    "status": "not_started",
                    "started_date": None,
                    "completed_date": None,
                    "challenges_completed": [],
                    "notes": ""
                }
            return progress
    
    def save_progress(self):
        """Save progress to file"""
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f, indent=2)
    
    def mark_started(self, week_num):
        """Mark an exercise as started"""
        exercise = self.exercises[week_num - 1]
        folder = exercise["folder"]
        if self.progress["exercises"][folder]["status"] == "not_started":
            self.progress["exercises"][folder]["status"] = "in_progress"
            self.progress["exercises"][folder]["started_date"] = datetime.now().isoformat()
            self.save_progress()
            print(f"✅ Marked Week {week_num}: {exercise['name']} as started!")
    
    def mark_completed(self, week_num):
        """Mark an exercise as completed"""
        exercise = self.exercises[week_num - 1]
        folder = exercise["folder"]
        self.progress["exercises"][folder]["status"] = "completed"
        self.progress["exercises"][folder]["completed_date"] = datetime.now().isoformat()
        self.save_progress()
        print(f"🎉 Congratulations! Week {week_num}: {exercise['name']} completed!")
    
    def add_challenge(self, week_num, challenge_name):
        """Add a completed challenge"""
        exercise = self.exercises[week_num - 1]
        folder = exercise["folder"]
        challenges = self.progress["exercises"][folder]["challenges_completed"]
        if challenge_name not in challenges:
            challenges.append(challenge_name)
            self.save_progress()
            print(f"⭐ Challenge '{challenge_name}' completed for Week {week_num}!")
    
    def add_note(self, week_num, note):
        """Add a note about an exercise"""
        exercise = self.exercises[week_num - 1]
        folder = exercise["folder"]
        self.progress["exercises"][folder]["notes"] = note
        self.save_progress()
        print(f"📝 Note added for Week {week_num}")
    
    def show_progress(self):
        """Display current progress"""
        print("\n" + "="*60)
        print(f"📊 Progress Report for {self.progress['student_name']}")
        print("="*60)
        
        # Count statistics
        total = len(self.exercises)
        completed = sum(1 for ex in self.progress["exercises"].values() 
                       if ex["status"] == "completed")
        in_progress = sum(1 for ex in self.progress["exercises"].values() 
                         if ex["status"] == "in_progress")
        
        # Overall progress
        print(f"\nOverall Progress: {completed}/{total} completed ({completed/total*100:.1f}%)")
        progress_bar = "█" * (completed * 20 // total) + "░" * ((total - completed) * 20 // total)
        print(f"[{progress_bar}]")
        
        # Part-by-part breakdown
        print("\n📚 Part I: Computational Thinking (Weeks 1-4)")
        self._show_part_progress(0, 4)
        
        print("\n📚 Part II: Building Systems (Weeks 5-8)")
        self._show_part_progress(4, 8)
        
        print("\n📚 Part III: Real-World Programming (Weeks 9-12)")
        self._show_part_progress(8, 12)
        
        # Challenges completed
        total_challenges = sum(len(ex["challenges_completed"]) 
                             for ex in self.progress["exercises"].values())
        if total_challenges > 0:
            print(f"\n🏆 Total Challenges Completed: {total_challenges}")
    
    def _show_part_progress(self, start_idx, end_idx):
        """Show progress for a specific part"""
        for i in range(start_idx, end_idx):
            exercise = self.exercises[i]
            status = self.progress["exercises"][exercise["folder"]]["status"]
            
            # Status icon
            if status == "completed":
                icon = "✅"
            elif status == "in_progress":
                icon = "🔄"
            else:
                icon = "⬜"
            
            # Display line
            print(f"  {icon} Week {exercise['week']:2d}: {exercise['name']}")
            
            # Show challenges if any
            challenges = self.progress["exercises"][exercise["folder"]]["challenges_completed"]
            if challenges:
                print(f"     Challenges: {', '.join(challenges)}")

def main():
    """Interactive progress tracker"""
    print("🎯 Python Step by Step - Progress Tracker")
    print("="*40)
    
    # Get or create student name
    if os.path.exists("my_progress.json"):
        with open("my_progress.json", 'r') as f:
            data = json.load(f)
            student_name = data.get("student_name", "Student")
    else:
        student_name = input("Enter your name: ") or "Student"
    
    tracker = ProgressTracker(student_name)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Show my progress")
        print("2. Mark exercise as started")
        print("3. Mark exercise as completed")
        print("4. Add completed challenge")
        print("5. Add note to exercise")
        print("6. Exit")
        
        choice = input("\nEnter choice (1-6): ")
        
        if choice == "1":
            tracker.show_progress()
        elif choice == "2":
            week = int(input("Enter week number (1-12): "))
            tracker.mark_started(week)
        elif choice == "3":
            week = int(input("Enter week number (1-12): "))
            tracker.mark_completed(week)
        elif choice == "4":
            week = int(input("Enter week number (1-12): "))
            challenge = input("Enter challenge name: ")
            tracker.add_challenge(week, challenge)
        elif choice == "5":
            week = int(input("Enter week number (1-12): "))
            note = input("Enter note: ")
            tracker.add_note(week, note)
        elif choice == "6":
            print("\nKeep up the great work! 🚀")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()