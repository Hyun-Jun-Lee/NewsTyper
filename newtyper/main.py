import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel


class NewTyper(QWidget):
    def __init__(
        self, parent: QWidget | None = ..., flags: Qt.WindowFlags | Qt.WindowType = ...
    ) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("NewsTyper")
        self.move(300, 300)
        self.resize(800, 500)
        self.show()

        self.layout = QVBoxLayout()
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("스포츠")
        self.comboBox.addItem("경제")
        self.comboBox.addItem("사회")
        self.comboBox.addItem("세계")

        self.label = QLabel("선택된 카테고리: ", self)

        # self.comboBox.activated[str].connect(self.onActivated)

        self.layout.addWidget(self.comboBox)
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

    # def onActivated(self, text):
    #     # 사용자가 선택한 카테고리를 처리하는 함수
    #     self.label.setText(f"선택된 카테고리: {text}")
    #     self.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = NewTyper()
    sys.exit(app.exec_())
