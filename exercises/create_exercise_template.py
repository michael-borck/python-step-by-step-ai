#!/usr/bin/env python3
"""
Helper script to create exercise folder templates quickly
"""

import os
import sys

def create_exercise_structure(week_num, project_name, folder_name):
    """Create the folder structure for an exercise"""
    
    # Create directories
    base_dir = f"week-{week_num:02d}-{folder_name}"
    os.makedirs(base_dir, exist_ok=True)
    os.makedirs(f"{base_dir}/solutions", exist_ok=True)
    
    # Create empty files
    files = [
        f"{base_dir}/instructions.md",
        f"{base_dir}/starter_code.py",
        f"{base_dir}/hints.md",
        f"{base_dir}/tests.py",
        f"{base_dir}/solutions/solution_basic.py",
        f"{base_dir}/solutions/solution_intermediate.py",
        f"{base_dir}/solutions/solution_advanced.py"
    ]
    
    for file_path in files:
        if not os.path.exists(file_path):
            # Create file with basic header
            with open(file_path, 'w') as f:
                if file_path.endswith('.py'):
                    f.write(f'#!/usr/bin/env python3\n"""\n{project_name}\nFile: {os.path.basename(file_path)}\n"""\n\n')
                else:
                    f.write(f'# {project_name}\n\n')
    
    print(f"✅ Created structure for Week {week_num}: {project_name}")

# Remaining weeks to create
exercises = [
    (4, "Rock Paper Scissors", "rock-paper-scissors"),
    (5, "Temperature Converter", "temperature-converter"),
    (6, "Contact Book", "contact-book"),
    (7, "Journal App", "journal-app"),
    (8, "Quiz Game", "quiz-game"),
    (9, "Grade Analysis Tool", "grade-analysis"),
    (10, "Weather Dashboard", "weather-dashboard"),
    (11, "Text Adventure Game", "text-adventure"),
    (12, "Todo GUI Application", "todo-gui")
]

if __name__ == "__main__":
    print("Creating exercise templates for remaining weeks...\n")
    
    for week, name, folder in exercises:
        create_exercise_structure(week, name, folder)
    
    print("\n✅ All exercise folders created!")
    print("\nNext steps:")
    print("1. Fill in instructions.md for each week")
    print("2. Create appropriate starter code")
    print("3. Write hints and solutions")
    print("4. Add tests where applicable")