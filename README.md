# CG-COM

This script checks a list of names from `CGCOM` automatically

## Installation

Before running the code, make sure you have installed the required dependencies by running the command:
```bash
pip install -r requirements.txt
```


## Usage

Also, before running the code, ensure that you have set a valid JSESSIONID in the `vars.py` file.

When running the code, you will be prompted to enter the captcha code that is displayed at that time.

## Functionalities

- [x] **Checking a List of Names:** The script takes a list of names and queries a service to check each name.

- [x] **Detecting Valid Responses:** It detects valid responses from the service and processes them accordingly.

- [x] **Checking the Captcha:** The script prompts the user to enter the captcha code displayed at that time and verifies it.

- [x] **Checking JSESSIONID Expiry:** It checks if the JSESSIONID stored in the `vars.py` file has expired.

- [ ] **Saving Names to JSON File:** If there are any results for a name, the script saves the name in a JSON file.

- [ ] **Saving Valid Data as HTML:** The script saves the valid data as an HTML file.

