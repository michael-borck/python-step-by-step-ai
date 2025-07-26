#!/bin/bash

# Check exercise formatting in Quarto files
# This ensures exercises follow the 5-level system

set -e

STATUS=0

for file in "$@"; do
    if grep -q "exercise.*container" "$file"; then
        echo "Checking exercises in: $file"
        
        # Check for required exercise levels
        if ! grep -q "Level 1.*Trace" "$file"; then
            echo "  ⚠️  Missing Level 1: Trace exercise"
            STATUS=1
        fi
        
        # Check for details/summary in solutions
        if grep -q "solution.*content" "$file" && ! grep -q "<details>" "$file"; then
            echo "  ⚠️  Solutions should be in collapsible details sections"
            STATUS=1
        fi
        
        # Check for exercise numbering
        if grep -q "Exercise [0-9]" "$file" && ! grep -q "Exercise [0-9]\.[0-9]" "$file"; then
            echo "  ⚠️  Exercises should be numbered as X.Y (e.g., Exercise 1.1)"
            STATUS=1
        fi
        
        if [ $STATUS -eq 0 ]; then
            echo "  ✅ Exercise formatting looks good"
        fi
    fi
done

exit $STATUS