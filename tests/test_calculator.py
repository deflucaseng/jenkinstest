#!/usr/bin/env python3
import subprocess
import sys
import re

def run_calculator():
    """Run the calculator binary and capture output"""
    try:
        result = subprocess.run(
            ['./build/calculator'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running calculator: {e}")
        return None

def test_calculator_output():
    """Test that the calculator produces expected output"""
    output = run_calculator()
    if not output:
        return False
    
    tests = [
        ("5 + 3 = 8", "Addition test"),
        ("5 - 3 = 2", "Subtraction test"),
        ("5 * 3 = 15", "Multiplication test"),
        ("5 / 3 = 1.66667", "Division test")
    ]
    
    all_passed = True
    for expected, test_name in tests:
        if expected in output:
            print(f"✓ {test_name} passed")
        else:
            print(f"✗ {test_name} failed")
            all_passed = False
    
    return all_passed

if __name__ == "__main__":
    print("Running Calculator Tests...")
    print("-" * 40)
    
    if test_calculator_output():
        print("-" * 40)
        print("All tests passed!")
        sys.exit(0)
    else:
        print("-" * 40)
        print("Some tests failed!")
        sys.exit(1)