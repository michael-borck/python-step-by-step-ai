#!/usr/bin/env python3
"""
Quiz Game - Starter Code
Week 8 Project

TODO: Create a quiz game that loads questions from a file
"""

import json

# Constants
QUESTIONS_FILE = "questions.txt"
SCORES_FILE = "high_scores.json"

def display_welcome():
    """Display welcome message and game title"""
    print("\n🎮 Python Quiz Game 🎮")
    print("====================")
    print("\nLoading questions...")

def load_questions(filename):
    """Load quiz questions from file"""
    questions = []
    
    # TODO: Open and read the questions file
    # TODO: Parse each question block (6 lines per question)
    # TODO: Create dictionary for each question
    # TODO: Handle file not found error
    
    return questions

def display_question(question, question_num, total_questions):
    """Display a single question with options"""
    # TODO: Show question number and points
    # TODO: Display question text
    # TODO: Show all answer options (A, B, C, D)
    pass

def get_user_answer():
    """Get and validate user's answer"""
    # TODO: Get input from user
    # TODO: Validate answer is A, B, C, or D
    # TODO: Handle both uppercase and lowercase
    # TODO: Return validated answer
    return ""

def check_answer(user_answer, correct_answer):
    """Check if the answer is correct"""
    # TODO: Compare answers (case insensitive)
    # TODO: Return True if correct, False otherwise
    return False

def display_feedback(is_correct, correct_answer, points_earned):
    """Display feedback after answering"""
    # TODO: Show if answer was correct or wrong
    # TODO: If wrong, show the correct answer
    # TODO: Display points earned
    pass

def load_high_scores():
    """Load high scores from file"""
    # TODO: Try to load scores from JSON file
    # TODO: If file doesn't exist, return empty list
    # TODO: Return list of score dictionaries
    return []

def save_high_scores(scores):
    """Save high scores to file"""
    # TODO: Sort scores by score value (highest first)
    # TODO: Keep only top 5 scores
    # TODO: Save to JSON file
    pass

def display_high_scores(scores):
    """Display the high scores table"""
    print("\nHigh Scores:")
    # TODO: Display each score with rank
    # TODO: Format nicely with name and score
    pass

def update_high_scores(scores, player_name, player_score):
    """Add new score to high scores if qualified"""
    # TODO: Create new score entry
    # TODO: Add to scores list
    # TODO: Sort and keep top 5
    # TODO: Return updated list
    return scores

def play_game(questions):
    """Main game loop"""
    score = 0
    correct_count = 0
    
    print(f"\nReady to test your Python knowledge?\n")
    
    # TODO: Loop through each question
    # TODO: Display question
    # TODO: Get user answer
    # TODO: Check if correct
    # TODO: Update score and count
    # TODO: Show feedback
    
    # Game over - show results
    total_possible = sum(q.get('points', 0) for q in questions)
    percentage = (correct_count / len(questions) * 100) if questions else 0
    
    print("\n🏁 Game Over! 🏁")
    print("================")
    print(f"Final Score: {score}/{total_possible} points")
    print(f"Correct: {correct_count}/{len(questions)} ({percentage:.0f}%)")
    
    return score

def main():
    """Main program"""
    display_welcome()
    
    # Load questions
    questions = load_questions(QUESTIONS_FILE)
    if not questions:
        print("❌ No questions found! Please create questions.txt")
        return
    
    print(f"Loaded {len(questions)} questions.")
    
    # Play the game
    final_score = play_game(questions)
    
    # Handle high scores
    high_scores = load_high_scores()
    
    # Check if it's a high score
    if not high_scores or final_score > min(s['score'] for s in high_scores):
        print("\n🏆 New High Score! 🏆")
        player_name = input("Enter your name: ")
        high_scores = update_high_scores(high_scores, player_name, final_score)
        save_high_scores(high_scores)
    
    # Display high scores
    display_high_scores(high_scores)
    
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()

