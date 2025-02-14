# This is a basic Python start file. Feel free to modify it to suit your needs.

# Import necessary modules
import sys  # For interacting with the system (e.g., command-line arguments)
import os   # For interacting with the operating system (e.g., file paths)

# Define constants (optional, but recommended for clarity)
# Example:
PI = 3.14159
DEFAULT_VALUE = 0


# Define functions (organize your code into reusable blocks)
def main():
    """
    This is the main function where the program execution starts.
    """
    print("Hello, world!")

    # Example of using command-line arguments
    if len(sys.argv) > 1:
        print("Arguments passed from the command line:", sys.argv[1:])

    # Example of checking the current working directory
    print("Current working directory:", os.getcwd())

    # Call other functions if needed
    # another_function()


def another_function():
    """
    This is an example of another function.  You can create as many as you need.
    """
    print("This is another function.")


# Main execution block
if __name__ == "__main__":
    """
    This ensures the main() function is called only when the script is
    executed directly (not imported as a module).
    """
    main()
