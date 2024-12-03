# PassBreachFinder

PassBreachFinder is a simple Python script that checks if a password has been compromised using the [Have I Been Pwned](https://haveibeenpwned.com/) service. The script automates the process of querying the website by using Selenium and retrieving the results for the given password.

## Features

- **Check if a password has been compromised**: Pass a password via the command line, and the script will tell you if it's been part of any known data breaches.
- **Headless Browser**: Uses a headless Firefox browser for automated web scraping without requiring a GUI.

## Prerequisites

To use this script, you’ll need the following:

- Python 3.x
- Selenium
- Geckodriver (for Firefox)
- Firefox Web Browser

### Install Required Packages

You can install the necessary Python libraries by running:

```bash
pip install -r requirements.txt
```

Additionally, make sure that [Geckodriver](https://github.com/mozilla/geckodriver/releases) is installed on your system and accessible via the `PATH`.

### Download Geckodriver (for Firefox):

1. Download the [Geckodriver](https://github.com/mozilla/geckodriver/releases) that matches your system’s architecture.
2. Extract it and add the path to the Geckodriver executable in your system's environment variables or specify the path directly in the script.

## Usage

1. Clone or download the script.
2. Open a terminal window in the directory where the script is located.
3. Run the script by providing a password using the `-p` option:

```bash
python app.py -p "your_password_here"
```

### Example:

```bash
python app.py -p "password123"
```

If the password has been compromised, you will see a message like:

```
password123 This password has been pwned 5 times.
```

If the password is safe, you will see:

```
safe
```

## How It Works

1. **Command-Line Argument**: The script accepts a password as an argument via the command line (`-p`).
2. **Headless Browser**: It uses Selenium with a headless Firefox browser to interact with the [Have I Been Pwned Passwords page](https://haveibeenpwned.com/Passwords).
3. **Password Checking**: It enters the provided password into the search form on the page and submits it. After waiting for the results, it checks if the password has been pwned.
4. **Results**: The script will display whether the password is safe or has been exposed in a data breach.

## Troubleshooting

- **Geckodriver Not Found**: If you're getting an error regarding `Geckodriver`, ensure it’s installed and properly referenced in the script or the environment variables.
- **Headless Mode**: If you'd like to see the browser in action (not headless), remove or comment out the line `options.add_argument("--headless")`.

## License

This script is licensed under the MIT License. See `LICENSE` for more details.
