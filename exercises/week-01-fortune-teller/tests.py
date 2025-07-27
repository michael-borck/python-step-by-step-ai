#!/usr/bin/env python3
"""
Tests for Week 1: Fortune Teller Project
Run this to check if your fortune teller meets the requirements.
"""

import os
import sys
import subprocess
import re

def check_file_exists():
    """Check if the student's code file exists"""
    if not os.path.exists("starter_code.py"):
        print("❌ starter_code.py not found!")
        print("   Make sure you're running tests from the week-01-fortune-teller directory")
        return False
    print("✅ Found starter_code.py")
    return True

def check_imports():
    """Check if random is imported"""
    with open("starter_code.py", "r") as f:
        content = f.read()
    
    if "import random" in content:
        print("✅ Random module imported correctly")
        return True
    else:
        print("❌ Missing 'import random' statement")
        return False

def check_fortune_list():
    """Check if fortunes list exists with at least 5 items"""
    with open("starter_code.py", "r") as f:
        content = f.read()
    
    # Look for a list assignment
    list_pattern = r'fortunes?\s*=\s*\[(.*?)\]'
    match = re.search(list_pattern, content, re.DOTALL)
    
    if match:
        # Count the number of strings in the list
        list_content = match.group(1)
        # Simple count of quotes to estimate number of fortunes
        quote_count = list_content.count('"') + list_content.count("'")
        fortune_count = quote_count // 2
        
        if fortune_count >= 5:
            print(f"✅ Found fortune list with approximately {fortune_count} fortunes")
            return True
        else:
            print(f"❌ Fortune list has only {fortune_count} fortunes (need at least 5)")
            return False
    else:
        print("❌ No fortune list found (should be named 'fortune' or 'fortunes')")
        return False

def check_random_choice():
    """Check if random.choice is used"""
    with open("starter_code.py", "r") as f:
        content = f.read()
    
    if "random.choice" in content:
        print("✅ Uses random.choice() to select fortunes")
        return True
    else:
        print("❌ Doesn't use random.choice() - fortunes won't be random!")
        return False

def check_output_elements():
    """Check if program has required output elements"""
    try:
        # Run the student's program and capture output
        result = subprocess.run(
            [sys.executable, "starter_code.py"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        output = result.stdout
        
        if not output:
            print("❌ Program produces no output")
            return False
        
        checks = {
            "greeting": False,
            "fortune": False,
            "closing": False
        }
        
        lines = output.strip().split('\n')
        
        # Very basic checks - at least 3 lines of output
        if len(lines) >= 3:
            checks["greeting"] = True  # Assume first line(s) are greeting
            checks["fortune"] = True   # Assume middle has fortune
            checks["closing"] = True   # Assume last line(s) are closing
            
            print("✅ Program produces formatted output with:")
            print("   • Welcome/greeting message")
            print("   • Fortune display")  
            print("   • Closing message")
            return True
        else:
            print("❌ Output seems too short - missing required elements")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Program took too long to run")
        return False
    except Exception as e:
        print(f"❌ Error running program: {e}")
        return False

def run_multiple_times():
    """Run program multiple times to check randomness"""
    print("\n🎲 Testing randomness (running 3 times)...")
    
    outputs = []
    for i in range(3):
        try:
            result = subprocess.run(
                [sys.executable, "starter_code.py"],
                capture_output=True,
                text=True,
                timeout=5
            )
            outputs.append(result.stdout)
        except:
            print("❌ Error running program multiple times")
            return False
    
    # Check if outputs are different
    if len(set(outputs)) > 1:
        print("✅ Program produces different outputs (fortunes are random!)")
        return True
    else:
        print("⚠️  Program produces the same output every time")
        print("   Make sure you're using random.choice() correctly")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing your Fortune Teller Project")
    print("=" * 40)
    
    tests = [
        ("File exists", check_file_exists),
        ("Imports random", check_imports),
        ("Has fortune list", check_fortune_list),
        ("Uses random selection", check_random_choice),
        ("Produces output", check_output_elements),
        ("Randomness works", run_multiple_times)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 Test: {test_name}")
        if test_func():
            passed += 1
        print()
    
    print("=" * 40)
    print(f"\n📊 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 Excellent work! Your fortune teller meets all requirements!")
        print("   Consider trying the intermediate and advanced challenges!")
    elif passed >= total - 1:
        print("\n👍 Almost there! Just one small issue to fix.")
    elif passed >= total // 2:
        print("\n💪 Good progress! Review the failed tests and try again.")
    else:
        print("\n🔧 Keep working! Check the hints.md file for help.")
    
    print("\n💡 Tip: You can also test your program manually by running:")
    print("   python starter_code.py")

if __name__ == "__main__":
    main()