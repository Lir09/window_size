import sys
import win32gui
import win32con  # win32con을 추가해야 합니다.
import win32process
import psutil
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton

class WindowResizerApp(QWidget):
    def __init__(self):
        super().__init__()

        # 윈도우 GUI 구성
        self.setWindowTitle("Window Resizer")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # 실행 중인 프로세스 목록에서 창 제목 가져오기
        self.process_label = QLabel("Select Window:")
        self.process_dropdown = QComboBox(self)
        self.load_processes()
        layout.addWidget(self.process_label)
        layout.addWidget(self.process_dropdown)

        # 크기 입력
        self.width_label = QLabel("Width:")
        self.width_input = QLineEdit(self)
        layout.addWidget(self.width_label)
        layout.addWidget(self.width_input)

        self.height_label = QLabel("Height:")
        self.height_input = QLineEdit(self)
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)

        # 크기 조절 버튼
        self.resize_button = QPushButton("Resize Window", self)
        self.resize_button.clicked.connect(self.resize_window)
        layout.addWidget(self.resize_button)

        self.setLayout(layout)

    def load_processes(self):
        """실행 중인 모든 창을 열거하여 해당 창을 드롭다운에 추가"""
        def callback(hwnd, extra):
            """EnumWindows 콜백 함수. 창 핸들과 제목을 처리."""
            if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
                _, pid = win32process.GetWindowThreadProcessId(hwnd)
                process = psutil.Process(pid)
                window_text = win32gui.GetWindowText(hwnd)
                self.process_dropdown.addItem(f"{window_text} ({process.name()})", hwnd)

        win32gui.EnumWindows(callback, None)

    def resize_window(self):
        # 선택된 창 핸들과 너비, 높이 값
        hwnd = self.process_dropdown.currentData()
        width = int(self.width_input.text())
        height = int(self.height_input.text())

        if hwnd:
            # 창 크기 조절
            win32gui.SetWindowPos(hwnd, 0, 0, 0, width, height, win32con.SWP_NOMOVE | win32con.SWP_NOZORDER)
        else:
            print("Window not found!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowResizerApp()
    window.show()
    sys.exit(app.exec())
