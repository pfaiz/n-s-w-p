# NumberingSystems.py
# This script converts a given number in string format to integer and hexadecimal format.
# Usage: python3 NumberingSystems.py <number>
# The script expects exactly one argument (a number) and will display an error message if the requirements are not met.

import sys

def main():
    # Display header information
    print("\nNumbering Systems with Python")
    
    # Check for the correct number of arguments
    numberOfArgs = len(sys.argv)
    if numberOfArgs != 2:
        print("Error: This script requires exactly one argument (a number in string format).")
        print("Usage: python3 NumberingSystems.py <number>")
        sys.exit(1)
    
    # Process the argument
    numberAsString = sys.argv[1]
    
    try:
        # Convert the argument to an integer and hexadecimal format
        numberAsInt = int(numberAsString, base=10)
        numberAsHex = hex(numberAsInt)
        
        # Display the results
        print(f"Input: {numberAsString}")
        print(f"Number: {numberAsInt}")
        print(f"Hex: {numberAsHex}")
    
    except ValueError:
        print(f"Error: '{numberAsString}' is not a valid integer.")
        sys.exit(1)

if __name__ == "__main__":
    main()