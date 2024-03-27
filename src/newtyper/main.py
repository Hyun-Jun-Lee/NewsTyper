import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QComboBox,
    QLabel,
    QHBoxLayout,
)

from enums.enums import NewsAgency, YnaCategory, HankyungsCategory


class NewTyper(QWidget):
    def __init__(
        self, parent: QWidget | None = ..., flags: Qt.WindowFlags | Qt.WindowType = ...
    ) -> None:
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("NewsTyper")
        self.move(300, 300)
        self.resize(800, 500)
        self.show()

        hbox = QHBoxLayout()

        # 언론사 선택
        agency_layout = QHBoxLayout()
        agency_layout.addStretch(1)

        agency_label = QLabel("뉴스 에이전시 선택:", self)
        agency_layout.addWidget(agency_label)

        self.agency_combo_box = QComboBox(self)
        self.agency_combo_box.addItem("선택해주세요", None)
        agency_layout.addWidget(self.agency_combo_box)
        hbox.addLayout(agency_layout)

        for category in NewsAgency:
            self.agency_combo_box.addItem(category.value, category)

        self.agency_combo_box.activated.connect(self.choice_agency)

        # 카테고리 선택
        category_layout = QHBoxLayout()

        category_label = QLabel("선택된 카테고리: ", self)
        category_layout.addWidget(category_label)

        self.category_combo_box = QComboBox(self)
        self.category_combo_box.addItem("선택해주세요", None)
        category_layout.addWidget(self.category_combo_box)
        category_layout.addStretch(1)

        hbox.addLayout(category_layout)

        # 수직 정렬
        vbox = QVBoxLayout()
        vbox.addStretch(0)
        vbox.addLayout(hbox)
        vbox.addStretch(3)

        self.setLayout(vbox)

    def choice_agency(self, index):
        selected_agency = self.agency_combo_box.itemData(index)
        self.category_combo_box.clear()

        if selected_agency == NewsAgency.YNA:
            for category in YnaCategory:
                self.category_combo_box.addItem(category.name, category)
        elif selected_agency == NewsAgency.HANKYUNG:
            for category in HankyungsCategory:
                self.category_combo_box.addItem(category.name, category)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = NewTyper()
    sys.exit(app.exec_())
