"""A minimal PySide6 calculator window skeleton."""

import sys

from PySide6.QtWidgets import (
    QApplication,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


class CalculatorWindow(QMainWindow):
    """Main window for the calculator practice project."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Calculator")
        self.resize(320, 420)


def main() -> int:
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
