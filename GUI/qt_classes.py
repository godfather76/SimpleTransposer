from PySide6 import QtCore, QtWidgets, QtGui


@QtCore.Slot()
def default_func():
    print("Enter a function")


# class Dialog(QtWidgets.QDialog):
#     def __init__(self, root, parent=None, title='Enter Window Title', *args, **kwargs):
#         self.root = root
#         super().__init__(*args, **kwargs)
#         self.setWindowTitle(title)
#         self.show()

class CustomTitleBar(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initial_pos = None
        title_bar_layout = QtWidgets.QHBoxLayout(self)
        title_bar_layout.setContentsMargins(1, 1, 1, 1)
        title_bar_layout.setSpacing(2)
        self.title = QtWidgets.QLabel(f"{self.__class__.__name__}", self)
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet(
            """
        QLabel { text-transform: uppercase; font-size: 10pt; margin-left: 48px; }
        """
        )

        if title := parent.windowTitle():
            self.title.setText(title)
        title_bar_layout.addWidget(self.title)
        # Min button
        self.min_button = QtWidgets.QToolButton(self)
        min_icon = QtGui.QIcon()
        min_icon.addFile("min.svg")
        self.min_button.setIcon(min_icon)
        self.min_button.clicked.connect(self.window().showMinimized)

        # Max button
        self.max_button = QtWidgets.QToolButton(self)
        max_icon = QtGui.QIcon()
        max_icon.addFile("max.svg")
        self.max_button.setIcon(max_icon)
        self.max_button.clicked.connect(self.window().showMaximized)

        # Close button
        self.close_button = QtWidgets.QToolButton(self)
        close_icon = QtGui.QIcon()
        close_icon.addFile("close.svg")  # Close has only a single state.
        self.close_button.setIcon(close_icon)
        self.close_button.clicked.connect(self.window().close)

        # Normal button
        self.normal_button = QtWidgets.QToolButton(self)
        normal_icon = QtGui.QIcon()
        normal_icon.addFile("normal.svg")
        self.normal_button.setIcon(normal_icon)
        self.normal_button.clicked.connect(self.window().showNormal)
        self.normal_button.setVisible(False)
        # Add buttons
        buttons = [
            self.min_button,
            self.normal_button,
            self.max_button,
            self.close_button,
        ]
        for button in buttons:
            button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
            button.setFixedSize(QtCore.QSize(16, 16))
            button.setStyleSheet(
                """QToolButton {
                    border: none;
                    padding: 2px;
                }
                """
            )
            title_bar_layout.addWidget(button)

    def window_state_changed(self, state):
        if state == QtCore.Qt.WindowState.WindowMaximized:
            self.normal_button.setVisible(True)
            self.max_button.setVisible(False)
        else:
            self.normal_button.setVisible(False)
            self.max_button.setVisible(True)


class GroupBox(QtWidgets.QGroupBox):
    def __init__(self, root, parent=None, title='Enter Title', layout=None, alignment=None, *args, **kwargs):
        self.root = root
        if not alignment:
            alignment = QtCore.Qt.AlignCenter
        super().__init__(parent, alignment=alignment, *args, **kwargs)
        self.setTitle(title)
        if not layout:
            self.show()
        else:
            layout.addWidget(self)


class Widget(QtWidgets.QWidget):
    def __init__(self, root, parent=None, layout=None, *args, **kwargs):
        self.root = root
        super().__init__(parent, *args, **kwargs)
        if not layout:
            self.show()
        else:
            layout.addWidget(self)


class ComboBox(QtWidgets.QComboBox):
    def __init__(self, root, parent=None, layout=None, *args, **kwargs):
        self.root = root
        super().__init__(parent, *args, **kwargs)
        if not layout:
            self.show()
        else:
            layout.addWidget(self)



class DateEdit(QtWidgets.QDateEdit):
    def __init__(self, root, parent=None, layout=None, *args, **kwargs):
        self.root = root
        super().__init__(parent, *args, **kwargs)
        if not layout:
            self.show()
        else:
            layout.addWidget(self)


class Label(QtWidgets.QLabel):
    def __init__(self, root, parent=None, text='Enter Text', layout=None,  alignment=None, *args, **kwargs):
        self.root = root
        if not alignment:
            alignment = QtCore.Qt.AlignCenter
        super().__init__(parent, text=text, alignment=alignment, *args, **kwargs)
        if not layout:
            self.show()
        else:
            layout.addWidget(self)


class LineEdit(QtWidgets.QLineEdit):
    def __init__(self, root, parent=None, text=None, placeholderText='Enter Text Here', layout=None,  *args, **kwargs):
        self.root = root
        super().__init__(text=text, placeholderText=placeholderText, *args, **kwargs)
        if not layout:
            self.show()
        else:
            layout.addWidget(self)


class PushButton(QtWidgets.QPushButton):
    def __init__(self, root, parent=None, text='Enter Text', layout=None, func=default_func,  *args, **kwargs):
        self.root = root
        super().__init__(parent, text=text, *args, **kwargs)
        # func must be @QtCore.Slot()
        self.clicked.connect(func)
        if not layout:
            self.show()
        else:
            layout.addWidget(self)


class TextEdit(QtWidgets.QTextEdit):
    def __init__(self, root, parent=None, placeholderText='Enter Text', layout=None,  *args, **kwargs):
        self.root = root
        super().__init__(parent, placeholderText=placeholderText, *args, **kwargs)
        if not layout:
            self.show()
        else:
            layout.addWidget(self)


class TimeEdit(QtWidgets.QTimeEdit):
    def __init__(self, root, parent=None, layout=None, *args, **kwargs):
        self.root = root
        super().__init__(parent, *args, **kwargs)
        if not layout:
            self.show()
        else:
            layout.addWidget(self)
