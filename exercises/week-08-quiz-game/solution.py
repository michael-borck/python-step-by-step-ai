#!/usr/bin/env python3
"""
Quiz Game - Complete Solution
Week 8 Project

This solution implements a quiz game with file parsing, score tracking,
and a save system for high scores.
"""

import json
import os
import random

def load_questions(filename):
    """Load quiz questions from file"""
    questions = []
    
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        i = 0
        while i < len(lines):
            # Each question block is 6 lines
            if i + 5 < len(lines):
                question_text = lines[i].strip()
                option_a = lines[i + 1].strip()
                option_b = lines[i + 2].strip()
                option_c = lines[i + 3].strip()
                option_d = lines[i + 4].strip()
                correct_answer = lines[i + 5].strip()
                
                # Skip any empty lines between questions
                while i + 6 < len(lines) and lines[i + 6].strip() == "":
                    i += 1
                
                question = {
                    "question": question_text,
                    "options": {
                        "A": option_a[3:],  # Remove "A) " prefix
                        "B": option_b[3:],
                        "C": option_c[3:],
                        "D": option_d[3:]
                    },
                    "correct": correct_answer
                }
                questions.append(question)
            
            i += 6
            
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found!")
        return []
    except Exception as e:
        print(f"❌ Error loading questions: {e}")
        return []
    
    return questions

def display_question(question, question_num, total):
    """Display a single question"""
    print(f"\n📝 Question {question_num} of {total}")
    print("=" * 40)
    print(f"\n{question['question']}")
    print()
    
    for option, text in question['options'].items():
        print(f"{option}) {text}")
    
    print()

def get_user_answer():
    """Get and validate user answer"""
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        print("❌ Please enter A, B, C, or D")

def play_game(questions):
    """Main game loop"""
    if not questions:
        print("❌ No questions available!")
        return 0
    
    score = 0
    total_questions = len(questions)
    
    # Shuffle questions for variety
    random.shuffle(questions)
    
    print("\n🎮 Welcome to the Python Quiz Game! 🎮")
    print(f"Answer {total_questions} questions to test your knowledge!")
    
    for i, question in enumerate(questions, 1):
        display_question(question, i, total_questions)
        
        user_answer = get_user_answer()
        
        if user_answer == question['correct']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {question['correct']}")
    
    return score

def calculate_percentage(score, total):
    """Calculate score percentage"""
    if total == 0:
        return 0
    return (score / total) * 100

def get_grade(percentage):
    """Convert percentage to letter grade"""
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

def display_results(score, total):
    """Display game results"""
    percentage = calculate_percentage(score, total)
    grade = get_grade(percentage)
    
    print("\n🏁 Game Over! 🏁")
    print("=" * 40)
    print(f"Final Score: {score}/{total}")
    print(f"Percentage: {percentage:.1f}%")
    print(f"Grade: {grade}")
    
    # Fun feedback based on performance
    if percentage == 100:
        print("\n🌟 Perfect score! You're a Python master!")
    elif percentage >= 80:
        print("\n🎉 Great job! You know your Python!")
    elif percentage >= 60:
        print("\n👍 Good effort! Keep practicing!")
    else:
        print("\n📚 Keep studying! You'll do better next time!")

def load_high_scores(filename="high_scores.json"):
    """Load high scores from file"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error loading high scores: {e}")
        return []

def save_high_scores(scores, filename="high_scores.json"):
    """Save high scores to file"""
    try:
        with open(filename, 'w') as f:
            json.dump(scores, f, indent=2)
    except Exception as e:
        print(f"Error saving high scores: {e}")

def update_high_scores(name, score, total):
    """Update and display high scores"""
    high_scores = load_high_scores()
    
    # Add new score
    percentage = calculate_percentage(score, total)
    new_score = {
        "name": name,
        "score": score,
        "total": total,
        "percentage": percentage
    }
    high_scores.append(new_score)
    
    # Sort by percentage (descending) and keep top 10
    high_scores.sort(key=lambda x: x['percentage'], reverse=True)
    high_scores = high_scores[:10]
    
    # Save updated scores
    save_high_scores(high_scores)
    
    # Display high scores
    print("\n🏆 High Scores 🏆")
    print("=" * 40)
    for i, score_entry in enumerate(high_scores, 1):
        print(f"{i}. {score_entry['name']}: {score_entry['score']}/{score_entry['total']} ({score_entry['percentage']:.1f}%)")

def main():
    """Main program"""
    questions_file = "questions.txt"
    
    while True:
        print("\n📚 Python Quiz Game 📚")
        print("=" * 40)
        print("1. Play Game")
        print("2. View High Scores")
        print("3. Quit")
        
        choice = input("\nSelect option (1-3): ").strip()
        
        if choice == "1":
            # Load questions
            questions = load_questions(questions_file)
            if not questions:
                print("Cannot start game without questions!")
                continue
            
            # Play game
            score = play_game(questions)
            total = len(questions)
            
            # Display results
            display_results(score, total)
            
            # Get player name for high scores
            name = input("\nEnter your name for high scores: ").strip()
            if not name:
                name = "Anonymous"
            
            # Update high scores
            update_high_scores(name, score, total)
            
        elif choice == "2":
            # View high scores
            high_scores = load_high_scores()
            if high_scores:
                print("\n🏆 High Scores 🏆")
                print("=" * 40)
                for i, score_entry in enumerate(high_scores, 1):
                    print(f"{i}. {score_entry['name']}: {score_entry['score']}/{score_entry['total']} ({score_entry['percentage']:.1f}%)")
            else:
                print("\nNo high scores yet! Be the first to play!")
            
        elif choice == "3":
            print("\nThanks for playing! Goodbye! 👋")
            break
            
        else:
            print("❌ Invalid option! Please try again.")

if __name__ == "__main__":
    main()