import subprocess

# Function to test the script in the infrastructure
def test_script(script_name):
    try:
        # Run the script and capture output/errors
        result = subprocess.run(
            ["python", script_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            return f"Error: {result.stderr.strip()}"  # Return the error message
        return "Script executed successfully."
    except Exception as e:
        return f"Exception during testing: {str(e)}"

# Main logic
if __name__ == "__main__":
    script_name = "helloworld.py"

    print(f"Testing script: {script_name}")
    test_result = test_script(script_name)
    print(f"Test Result: {test_result}")

    if "Error" in test_result:
        print("\nFixing the script...")
        # Create a corrected version of the script
        fixed_code = """
print("Hello, World!")
"""
        with open(script_name, "w") as file:
            file.write(fixed_code)

        print("Re-testing the fixed script...")
        final_test_result = test_script(script_name)
        print(f"Final Test Result: {final_test_result}")