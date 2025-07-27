#!/usr/bin/env python3
"""
Setup script for Python Step by Step exercises
Checks environment and creates necessary directories
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Ensure Python 3.8 or higher is installed"""
    version = sys.version_info
    print(f"🐍 Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required!")
        print("Please update your Python installation.")
        return False
    
    print("✅ Python version is compatible")
    return True

def check_pip():
    """Check if pip is available"""
    try:
        import pip
        print("✅ pip is installed")
        return True
    except ImportError:
        print("❌ pip is not installed")
        print("Please install pip to continue")
        return False

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages")
        print("Try running: pip install -r requirements.txt")
        return False

def create_user_directories():
    """Create directories for user work"""
    print("\n📁 Creating work directories...")
    
    # Create a 'my-solutions' directory for student work
    my_solutions = Path("my-solutions")
    if not my_solutions.exists():
        my_solutions.mkdir()
        print(f"✅ Created {my_solutions} directory for your work")
        
        # Create a README in my-solutions
        readme_content = """# My Solutions

This directory is for your exercise solutions. Feel free to organize it however you like!

## Suggested Structure

```
my-solutions/
├── week-01-fortune-teller.py
├── week-02-mad-libs.py
├── week-03-number-game.py
└── ...
```

## Tips

- Save different versions as you improve your solutions
- Add comments to remember your thought process
- Compare with the official solutions after you're done
- Keep notes about what you learned from each exercise

Happy coding! 🐍
"""
        (my_solutions / "README.md").write_text(readme_content)
    else:
        print(f"ℹ️  {my_solutions} directory already exists")

def check_tkinter():
    """Check if tkinter is available (for later GUI projects)"""
    print("\n🖼️  Checking GUI support...")
    try:
        import tkinter
        print("✅ tkinter is available for GUI projects")
        return True
    except ImportError:
        print("⚠️  tkinter is not available")
        print("You'll need to install it for weeks 11-12:")
        if sys.platform == "linux":
            print("  Ubuntu/Debian: sudo apt-get install python3-tk")
            print("  Fedora: sudo dnf install python3-tkinter")
        elif sys.platform == "darwin":
            print("  macOS: tkinter should be included with Python")
            print("  If not, reinstall Python from python.org")
        elif sys.platform == "win32":
            print("  Windows: tkinter should be included with Python")
            print("  If not, reinstall Python from python.org")
        return False

def create_test_file():
    """Create a simple test file to verify setup"""
    print("\n🧪 Creating test file...")
    
    test_content = '''#!/usr/bin/env python3
"""
Test file to verify your setup is working correctly
"""

def test_python_basics():
    """Test basic Python operations"""
    print("Testing basic Python operations...")
    
    # Test 1: Variables and printing
    message = "Hello, Python Step by Step!"
    print(f"✓ Print test: {message}")
    
    # Test 2: Basic math
    result = 2 + 2
    assert result == 4
    print(f"✓ Math test: 2 + 2 = {result}")
    
    # Test 3: Lists
    fruits = ["apple", "banana", "orange"]
    assert len(fruits) == 3
    print(f"✓ List test: {fruits}")
    
    # Test 4: User input (commented out for automated testing)
    # name = input("Enter your name: ")
    # print(f"✓ Input test: Hello, {name}!")
    
    print("\\n✅ All basic tests passed!")

def test_imports():
    """Test that required imports work"""
    print("\\nTesting required imports...")
    
    try:
        import random
        print("✓ random module: OK")
    except ImportError:
        print("✗ random module: FAILED")
    
    try:
        import json
        print("✓ json module: OK")
    except ImportError:
        print("✗ json module: FAILED")
    
    try:
        import csv
        print("✓ csv module: OK")
    except ImportError:
        print("✗ csv module: FAILED")

if __name__ == "__main__":
    print("=== Python Step by Step Setup Test ===\\n")
    
    test_python_basics()
    test_imports()
    
    print("\\n🎉 Setup verification complete!")
    print("You're ready to start the exercises!")
'''
    
    test_file = Path("test_setup.py")
    test_file.write_text(test_content)
    os.chmod(test_file, 0o755)  # Make executable
    print(f"✅ Created {test_file}")
    print("   Run it with: python test_setup.py")

def main():
    """Run all setup checks"""
    print("=== Python Step by Step: Exercise Setup ===\n")
    print("This script will check your environment and set up")
    print("everything you need for the exercises.\n")
    
    all_good = True
    
    # Check Python version
    if not check_python_version():
        all_good = False
    
    # Check pip
    if not check_pip():
        all_good = False
    else:
        # Install requirements
        if not install_requirements():
            all_good = False
    
    # Create directories
    create_user_directories()
    
    # Check tkinter (just informational)
    check_tkinter()
    
    # Create test file
    create_test_file()
    
    # Final message
    print("\n" + "="*50)
    if all_good:
        print("✅ Setup complete! You're ready to start learning!")
        print("\nNext steps:")
        print("1. Run: python test_setup.py")
        print("2. Navigate to week-01-fortune-teller/")
        print("3. Start coding!")
    else:
        print("⚠️  Setup completed with some issues.")
        print("You can still start the exercises, but may need")
        print("to fix the issues above for some projects.")
    
    print("\nHappy coding! 🐍✨")

if __name__ == "__main__":
    main()