# Browser Bot — Automated Form Fill & Download

A Python desktop app that automates logging in, filling a web form, and downloading a file from [demoqa.com](https://demoqa.com). Built with Selenium for browser automation and Tkinter for the GUI.

---

## Features

- Log in to demoqa.com automatically
- Fill out the text-box form with name, email, and address details
- Download a file from the Upload & Download page
- Simple desktop GUI — no command line needed

---

## Project Structure

```
Browser_Bot_4_Automated_download/
│
├── main.py                        # WebAutomation class — all Selenium logic
├── gui.py                         # Tkinter GUI — desktop interface
├── chromedriver-mac-arm64/
│   └── chromedriver               # ChromeDriver binary (macOS ARM)
└── README.md
```

---

## Requirements

- Python 3.13+
- Google Chrome (version 148+)
- ChromeDriver (matching your Chrome version, ARM64 binary included)

Install Python dependencies:

```bash
pip install selenium
```

---

## Setup

1. Clone or download the project folder.
2. Make sure Google Chrome is installed on your machine.
3. Confirm the ChromeDriver binary is in place at `chromedriver-mac-arm64/chromedriver`.
4. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate       # macOS/Linux
.venv\Scripts\activate          # Windows
```

5. Install dependencies:

```bash
pip install selenium
```

---

## Usage

### Option 1 — GUI (recommended)

Run the desktop interface:

```bash
python gui.py
```

1. Enter your demoqa.com username and password.
2. Fill in your full name, email, current address, and permanent address.
3. Click **Submit** — the bot will log in, fill the form, and download the file automatically.
4. Click **Close Browser** when done.

### Option 2 — Command line

Run the automation directly without the GUI:

```bash
python main.py
```

Credentials and form data are hardcoded at the bottom of `main.py` — edit them before running.

---

## How It Works

### `main.py` — `WebAutomation` class

| Method | Description |
|---|---|
| `__init__()` | Sets up Chrome with custom download directory (project folder) |
| `login(username, password)` | Navigates to the login page and authenticates |
| `fill_form(fullname, email, current_address, permanent_address)` | Navigates to `/text-box`, removes ad iframes, fills and submits the form |
| `download()` | Navigates to `/upload-download`, removes ads, and clicks the download button |
| `close()` | Quits the browser |

### `gui.py` — `App` class

Tkinter desktop window with two sections:

- **Login fields** — username and password
- **Form fields** — full name, email, current address, permanent address
- **Submit button** — triggers the full automation sequence
- **Close Browser button** — safely quits Chrome

---

## Notes

- Downloads are saved to the project's working directory (`os.getcwd()`).
- The ChromeDriver path is hardcoded for macOS ARM64 (`chromedriver-mac-arm64/chromedriver`). Update `main.py` line 14 if you are on a different platform.
- A 3-second sleep after the download click gives Chrome time to start the download before the browser closes.
- Ad iframes on demoqa.com are removed via JavaScript before each interaction to prevent them intercepting clicks.

---

## Troubleshooting

| Problem | Likely cause | Fix |
|---|---|---|
| `SessionNotCreatedException` | ChromeDriver version doesn't match Chrome | Download matching ChromeDriver from [chromedriver.chromium.org](https://chromedriver.chromium.org) |
| `TimeoutException` | Page loaded slowly or element ID changed | Increase the `WebDriverWait` timeout in `main.py` |
| File not downloaded | Browser closed too fast | Increase the `time.sleep(3)` value in `download()` |
| `No browser is open yet` warning | Submit not clicked before Close Browser | Always click Submit first |

---

## Built With

- [Selenium](https://www.selenium.dev/) — browser automation
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — desktop GUI (Python standard library)
- [demoqa.com](https://demoqa.com) — practice automation website

---

*Author: Peter Thomson*
*Last updated: 20/05/2026*