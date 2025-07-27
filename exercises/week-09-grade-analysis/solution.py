#!/usr/bin/env python3
"""
Grade Analysis Tool - Complete Solution
Week 9 Project

This solution implements a grade analysis tool that reads CSV data,
calculates statistics, and generates comprehensive reports.
"""

def load_student_data(filename):
    """Load student data from CSV file"""
    students = []
    headers = []
    
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        if not lines:
            print("❌ Error: CSV file is empty!")
            return [], []
        
        # Parse headers (skip "Student" column)
        headers = lines[0].strip().split(',')[1:]
        
        # Parse student data
        for line in lines[1:]:
            if line.strip():  # Skip empty lines
                values = line.strip().split(',')
                name = values[0]
                
                # Convert scores to numbers, handle invalid data
                scores = []
                for score_str in values[1:]:
                    score = validate_score(score_str)
                    if score is not None:
                        scores.append(score)
                    else:
                        scores.append(0)  # Default for invalid scores
                
                students.append({
                    "name": name,
                    "scores": scores
                })
        
        return students, headers
        
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found!")
        return [], []
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return [], []

def validate_score(score_str):
    """Validate and convert score string to number"""
    try:
        score = float(score_str.strip())
        if 0 <= score <= 100:
            return score
        else:
            return None  # Invalid range
    except ValueError:
        return None  # Not a number

def calculate_student_average(scores):
    """Calculate average of student scores"""
    if not scores:
        return 0.0
    
    valid_scores = [s for s in scores if s is not None]
    if not valid_scores:
        return 0.0
    
    return sum(valid_scores) / len(valid_scores)

def get_letter_grade(average):
    """Convert numerical average to letter grade"""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def find_min_max_scores(scores):
    """Find minimum and maximum scores"""
    if not scores:
        return 0, 0
    
    valid_scores = [s for s in scores if s is not None and s > 0]
    if not valid_scores:
        return 0, 0
    
    return min(valid_scores), max(valid_scores)

def generate_student_report(student, headers):
    """Generate detailed report for a single student"""
    scores = student['scores']
    average = calculate_student_average(scores)
    letter = get_letter_grade(average)
    min_score, max_score = find_min_max_scores(scores)
    
    print(f"\n👤 {student['name']}")
    print("-" * 40)
    
    # Show individual scores with assignment names
    score_details = []
    for i, score in enumerate(scores):
        if i < len(headers):
            score_details.append(f"{headers[i]}: {score:.1f}")
    
    # Print scores in columns for better readability
    for i in range(0, len(score_details), 3):
        print("  " + " | ".join(score_details[i:i+3]))
    
    print(f"\n  📊 Average: {average:.1f}%")
    print(f"  🎯 Grade: {letter}")
    print(f"  📈 Highest: {max_score:.1f}%")
    print(f"  📉 Lowest: {min_score:.1f}%")

def calculate_class_average(students):
    """Calculate overall class average"""
    if not students:
        return 0.0
    
    total_score = 0
    total_assignments = 0
    
    for student in students:
        total_score += sum(student['scores'])
        total_assignments += len(student['scores'])
    
    return total_score / total_assignments if total_assignments > 0 else 0

def calculate_assignment_averages(students, headers):
    """Calculate average for each assignment"""
    if not students or not headers:
        return {}
    
    assignment_averages = {}
    
    for i, assignment in enumerate(headers):
        total = 0
        count = 0
        
        for student in students:
            if i < len(student['scores']):
                total += student['scores'][i]
                count += 1
        
        assignment_averages[assignment] = total / count if count > 0 else 0
    
    return assignment_averages

def find_top_performers(students, n=3):
    """Find top N performing students"""
    # Calculate averages for all students
    student_averages = []
    for student in students:
        avg = calculate_student_average(student['scores'])
        student_averages.append((student['name'], avg))
    
    # Sort by average (highest first)
    student_averages.sort(key=lambda x: x[1], reverse=True)
    
    # Return top N
    return student_averages[:n]

def find_struggling_students(students, threshold=70):
    """Find students below threshold"""
    struggling = []
    
    for student in students:
        avg = calculate_student_average(student['scores'])
        if avg < threshold:
            struggling.append((student['name'], avg))
    
    # Sort by average (lowest first)
    struggling.sort(key=lambda x: x[1])
    
    return struggling

def calculate_grade_distribution(students):
    """Calculate distribution of letter grades"""
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    
    for student in students:
        average = calculate_student_average(student['scores'])
        letter = get_letter_grade(average)
        grade_counts[letter] += 1
    
    return grade_counts

def display_class_summary(students, headers):
    """Display comprehensive class summary"""
    if not students:
        print("No student data to analyze!")
        return
    
    print("\n" + "=" * 50)
    print("📊 CLASS SUMMARY REPORT 📊")
    print("=" * 50)
    
    # Overall statistics
    class_avg = calculate_class_average(students)
    print(f"\n📈 Class Average: {class_avg:.1f}%")
    print(f"📚 Total Students: {len(students)}")
    print(f"📝 Total Assignments: {len(headers)}")
    
    # Grade distribution
    grade_dist = calculate_grade_distribution(students)
    total_students = len(students)
    
    print("\n🎯 Grade Distribution:")
    for grade in ["A", "B", "C", "D", "F"]:
        count = grade_dist[grade]
        percentage = (count / total_students * 100) if total_students > 0 else 0
        bar = "█" * int(percentage / 2)  # Visual bar chart
        print(f"  {grade}: {count:2d} students ({percentage:5.1f}%) {bar}")
    
    # Top performers
    print("\n🏆 Top Performers:")
    top_students = find_top_performers(students, 3)
    for i, (name, avg) in enumerate(top_students, 1):
        print(f"  {i}. {name}: {avg:.1f}%")
    
    # Struggling students
    struggling = find_struggling_students(students, 70)
    if struggling:
        print("\n⚠️  Students Needing Support (< 70%):")
        for name, avg in struggling:
            print(f"  - {name}: {avg:.1f}%")
    
    # Assignment analysis
    assignment_avgs = calculate_assignment_averages(students, headers)
    print("\n📝 Assignment Averages:")
    
    # Sort assignments by average (lowest first)
    sorted_assignments = sorted(assignment_avgs.items(), key=lambda x: x[1])
    
    print("  Hardest assignments:")
    for assignment, avg in sorted_assignments[:3]:
        print(f"    - {assignment}: {avg:.1f}%")
    
    print("  Easiest assignments:")
    for assignment, avg in sorted_assignments[-3:]:
        print(f"    - {assignment}: {avg:.1f}%")

def export_report(students, headers, filename="grade_report.txt"):
    """Export analysis report to file"""
    try:
        with open(filename, 'w') as f:
            # Redirect print to file
            import sys
            original_stdout = sys.stdout
            sys.stdout = f
            
            # Generate all reports
            display_class_summary(students, headers)
            
            print("\n\n" + "=" * 50)
            print("INDIVIDUAL STUDENT REPORTS")
            print("=" * 50)
            
            for student in students:
                generate_student_report(student, headers)
            
            # Restore stdout
            sys.stdout = original_stdout
            
        print(f"\n✅ Report exported to '{filename}'")
        
    except Exception as e:
        print(f"❌ Error exporting report: {e}")

def main():
    """Main program"""
    print("🎓 Grade Analysis Tool 🎓")
    print("=" * 50)
    
    # Get filename
    filename = input("Enter CSV filename (or press Enter for 'grades_sample.csv'): ").strip()
    if not filename:
        filename = "grades_sample.csv"
    
    # Load data
    print(f"\nLoading data from '{filename}'...")
    students, headers = load_student_data(filename)
    
    if not students:
        print("No data to analyze!")
        return
    
    print(f"✅ Loaded {len(students)} students with {len(headers)} assignments")
    
    while True:
        print("\n" + "-" * 50)
        print("OPTIONS:")
        print("1. View Class Summary")
        print("2. View Individual Student Report")
        print("3. View All Student Reports")
        print("4. Export Full Report to File")
        print("5. Quit")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == "1":
            display_class_summary(students, headers)
            
        elif choice == "2":
            print("\nStudents:")
            for i, student in enumerate(students, 1):
                print(f"{i}. {student['name']}")
            
            try:
                student_num = int(input("\nSelect student number: ")) - 1
                if 0 <= student_num < len(students):
                    generate_student_report(students[student_num], headers)
                else:
                    print("❌ Invalid student number!")
            except ValueError:
                print("❌ Please enter a valid number!")
                
        elif choice == "3":
            for student in students:
                generate_student_report(student, headers)
                
        elif choice == "4":
            export_filename = input("Enter export filename (or press Enter for 'grade_report.txt'): ").strip()
            if not export_filename:
                export_filename = "grade_report.txt"
            export_report(students, headers, export_filename)
            
        elif choice == "5":
            print("\nThank you for using Grade Analysis Tool! 👋")
            break
            
        else:
            print("❌ Invalid option! Please try again.")

if __name__ == "__main__":
    main()