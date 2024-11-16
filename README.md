# Window Resizer App

## Project Overview
**Window Resizer App** is a program designed to adjust the size of windows running on the Windows operating system in real time.  
The app features a GUI built with PySide6 and leverages the Win32 API to implement window resizing functionality.

### Key Features
- Automatically fetches the list of active windows.
- Allows users to set custom width and height for selected windows.
- Intuitive and user-friendly interface.

---

## Installation Guide

### Prerequisites
1. Python 3.8 or later
2. `pip` package manager

### Installing Dependencies
Run the following command to install the required packages:

pip install pyside6 pywin32 psutil

# Build Instructions
To distribute the program as an executable file:

Install pyinstaller: Run the following command to install pyinstaller:

pip install pyinstaller

Build the executable: Navigate to the directory containing the script and run the following command:

pyinstaller --onefile --noconsole main.py

--onefile: Packages the program into a single executable file.
--noconsole: Hides the console window when running the application.
Locate the executable: The executable file will be created in the dist folder within the project directory.

Distribute: Share the executable file located in the dist folder. Ensure that the target system meets the program's requirements.

# Usage Instructions

1. Run the program (double-click the executable file or execute the Python script).
2. Select the window you want to resize from the Select Window dropdown menu.
3. Enter the desired width and height in the Width and Height fields.
4. Click the Resize Window button to instantly adjust the selected window's size.

# License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code, provided that proper credit is given to the original author.

# References and Resources

PySide6: https://pyside.org/

pywin32: https://github.com/mhammond/pywin32

psutil: https://github.com/giampaolo/psutil

# FAQ
1. The program is not working. What should I do?
Ensure Python and the required dependencies are correctly installed.
Try running the program with administrator privileges.
2. The dropdown does not display the desired window.
If the target window was opened after launching the program, restart the program to refresh the window list.
3. The program cannot resize a specific window.
Some system windows have restrictions on resizing due to Windows policies.
For additional questions, please contact gbin8498@gmail.com.
