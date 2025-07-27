#!/usr/bin/env python3
"""
Grade Analysis Tool - Starter Code
Week 9 Project

TODO: Create a grade analysis tool for processing student data from CSV files
"""

def load_student_data(filename):
    """Load student data from CSV file"""
    students = []
    
    # TODO: Open and read the CSV file
    # TODO: Parse header row for assignment names
    # TODO: Parse each student row
    # TODO: Create dictionary for each student
    # TODO: Handle file not found error
    
    return students, []  # Return students list and headers list

def calculate_student_average(scores):
    """Calculate average score for a student"""
    # TODO: Handle empty scores list
    # TODO: Filter out invalid scores (non-numeric)
    # TODO: Calculate and return average
    return 0.0

def get_letter_grade(average):
    """Convert numeric average to letter grade"""
    # TODO: Implement grading scale
    # A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60
    return "F"

def find_min_max_scores(scores):
    """Find minimum and maximum scores from a list"""
    # TODO: Filter valid scores
    # TODO: Return min and max values
    # TODO: Handle empty list
    return 0, 0

def generate_student_report(student, headers):
    """Generate individual student report"""
    # TODO: Calculate student's average
    # TODO: Get letter grade
    # TODO: Find highest and lowest scores
    # TODO: Format and display student information
    pass

def calculate_class_statistics(students):
    """Calculate overall class statistics"""
    # TODO: Calculate class average
    # TODO: Count grade distribution (A, B, C, D, F)
    # TODO: Find top performers
    # TODO: Return statistics dictionary
    return {}

def calculate_assignment_averages(students, headers):
    """Calculate average for each assignment"""
    assignment_averages = {}
    
    # TODO: For each assignment (header)
    # TODO: Collect all scores for that assignment
    # TODO: Calculate average
    # TODO: Store in dictionary
    
    return assignment_averages

def display_class_summary(stats, assignment_averages):
    """Display class overview and statistics"""
    print("\nClass Summary:")
    print("-" * 14)
    
    # TODO: Display total students
    # TODO: Display class average
    # TODO: Display grade distribution
    # TODO: Display top performers
    # TODO: Display assignment analysis
    pass

def display_grade_distribution(grade_counts, total_students):
    """Display grade distribution as percentages"""
    print("\nGrade Distribution:")
    
    # TODO: Calculate and display percentage for each grade
    # TODO: Format nicely with grade and count
    pass

def validate_score(score_str):
    """Validate and convert score string to number"""
    # TODO: Try to convert to float
    # TODO: Check if in valid range (0-100)
    # TODO: Return number or None if invalid
    try:
        score = float(score_str)
        if 0 <= score <= 100:
            return score
    except ValueError:
        pass
    return None

def main():
    """Main program"""
    print("📊 Grade Analysis Tool 📊")
    print("========================")
    
    # Get filename from user
    filename = input("Enter CSV filename (or press Enter for 'grades_sample.csv'): ").strip()
    if not filename:
        filename = "grades_sample.csv"
    
    # Load student data
    print(f"\nLoading data from {filename}...")
    students, headers = load_student_data(filename)
    
    if not students:
        print("❌ No student data found!")
        return
    
    print(f"Loaded {len(students)} students with {len(headers)} assignments.")
    
    # Generate individual reports
    print("\n📋 Individual Student Reports:")
    print("-" * 30)
    
    for student in students:
        generate_student_report(student, headers)
    
    # Calculate and display class statistics
    stats = calculate_class_statistics(students)
    assignment_averages = calculate_assignment_averages(students, headers)
    
    display_class_summary(stats, assignment_averages)
    
    print("\n" + "="*50)
    print("Analysis complete! 📈")

if __name__ == "__main__":
    main()

