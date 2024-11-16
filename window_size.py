import sys
import win32gui
import win32con
import win32process
import psutil
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton

class WindowResizerApp(QWidget):
    def __init__(self):
        super().__init__()

        # Configuring Windows GUI
        self.setWindowTitle("Window Resizer")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Import window title from running process list
        self.process_label = QLabel("Select Window:")
        self.process_dropdown = QComboBox(self)
        self.load_processes()
        layout.addWidget(self.process_label)
        layout.addWidget(self.process_dropdown)

        # Enter Size
        self.width_label = QLabel("Width:")
        self.width_input = QLineEdit(self)
        layout.addWidget(self.width_label)
        layout.addWidget(self.width_input)

        self.height_label = QLabel("Height:")
        self.height_input = QLineEdit(self)
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)

        # Sizing button
        self.resize_button = QPushButton("Resize Window", self)
        self.resize_button.clicked.connect(self.resize_window)
        layout.addWidget(self.resize_button)

        self.setLayout(layout)

    def load_processes(self):
        """List all running windows and add them to the dropdown"""
        def callback(hwnd, extra):
            """EnumWindows callback function that handles window handles and titles."""
            if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
                _, pid = win32process.GetWindowThreadProcessId(hwnd)
                process = psutil.Process(pid)
                window_text = win32gui.GetWindowText(hwnd)
                self.process_dropdown.addItem(f"{window_text} ({process.name()})", hwnd)

        win32gui.EnumWindows(callback, None)

    def resize_window(self):
        # Selected Window Handle, Width, Height Values
        hwnd = self.process_dropdown.currentData()
        width = int(self.width_input.text())
        height = int(self.height_input.text())

        if hwnd:
            # Window size adjustment
            win32gui.SetWindowPos(hwnd, 0, 0, 0, width, height, win32con.SWP_NOMOVE | win32con.SWP_NOZORDER)
        else:
            print("Window not found!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowResizerApp()
    window.show()
    sys.exit(app.exec())
