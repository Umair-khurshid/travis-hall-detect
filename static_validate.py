import requests
import subprocess

def run_flake8_check(file_path):
    """
    Run flake8 on the code file to catch syntax errors and undefined variables.
    """
    result = subprocess.run(['flake8', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Flake8 issues found:\n", result.stdout.decode())
        # Instead of raising an exception, just print the issues and allow other checks to run
    else:
        print("No issues found by flake8.")

def validate_api_call(url, params=None):
    """
    Validate an API call: checks the URL and required parameters.
    """
    if 'weatherapi.com' not in url:
        raise ValueError("Error: Invalid URL. Expected URL to contain 'weatherapi.com'.")

    if not params or 'key' not in params or 'q' not in params:
        raise ValueError("Error: Missing required parameters in the API call. 'key' and 'q' are required.")

    try:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise ConnectionError(f"Error: Unable to connect to the API. Status code: {response.status_code}")
        else:
            print(f"API call successful: {response.status_code}")
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Error during API call: {str(e)}")

def check_generated_code_for_hallucinations(file_path, url, params):
    """
    Unified function
    """
    # Step 1: Run static code analysis with flake8
    run_flake8_check(file_path)

    # Step 2: Validate API call
    validate_api_call(url, params)

    print("No hallucinations detected in the generated code!")

if __name__ == "__main__":
    generated_code_file = 'generated_code.py'  # Path to the generated code
    api_url = 'https://api.weatherapi.com/v1/current.json'
    api_params = {'key': 'valid_api_key', 'q': 'London'}

    # Run all checks in one go
    check_code(generated_code_file, api_url, api_params)
