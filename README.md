# PRODIGY_CS_04
Basic keylogger program in Python that records keystrokes and saves them to a file.

# Simple Keylogger - Task 04

This project implements a basic keylogger in Python that records keyboard inputs and stores them in a file.

## Features
- Logs keystrokes in real-time
- Saves input to a text file
- Handles special keys (e.g., Enter, Space)
- Stops logging when ESC key is pressed

## How It Works
The program uses the `pynput` library to listen for keyboard events. Each key pressed is captured and written to a log file.

## How to Run

1. Install required library:
   ```bash
   pip install pynput
