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
    QListWidget,
    QPushButton,
)

from enums.enums import NewsAgency, YnaCategory, HankyungsCategory


class NewTyper(QWidget):
    def __init__(
        self, parent: QWidget | None = ..., flags: Qt.WindowFlags | Qt.WindowType = ...
    ) -> None:
        super().__init__()
        self.current_crawler = None
        self.current_article = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("NewsTyper")
        self.move(300, 300)
        self.resize(800, 500)
        self.show()

        hbox = QHBoxLayout()

        # "이전" 버튼
        self.back_button = QPushButton("이전")
        hbox.addWidget(self.back_button)
        self.back_button.hide()

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
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.article_list = QListWidget(self)
        self.article_list.itemClicked.connect(self.display_article_content)
        vbox.addWidget(self.article_list)
        vbox.addStretch(5)

        self.setLayout(vbox)

    def choice_agency(self, index):
        from news_crawler import YnaCrawler, HankyungCrawler

        selected_agency = self.agency_combo_box.itemData(index)
        self.category_combo_box.clear()

        if selected_agency == NewsAgency.YNA:
            self.current_crawler = YnaCrawler(selected_agency)
            self.category_combo_box.addItem("선택해주세요", None)
            for category in YnaCategory:
                self.category_combo_box.addItem(category.name, category)
        elif selected_agency == NewsAgency.HANKYUNG:
            self.current_crawler = HankyungCrawler(selected_agency)
            self.category_combo_box.addItem("선택해주세요", None)
            for category in HankyungsCategory:
                self.category_combo_box.addItem(category.name, category)

        # 카테고리 선택 시 실행
        self.category_combo_box.activated.connect(self.display_article_title)

    def display_article_title(self, index):
        self.back_button.hide()

        selected_category = self.category_combo_box.itemData(index)
        if selected_category is not None and self.current_crawler:
            # 선택된 카테고리에 따라 기사 링크 가져오기
            self.current_article = self.current_crawler.get_article_links(
                selected_category
            )

            self.article_list.clear()
            for title, url in self.current_article.items():
                self.article_list.addItem(title)

            self.article_list.itemClicked.connect(self.display_article_content)

    def display_article_content(self, item):
        # 선택된 기사의 본문을 가져옵니다.
        self.back_button.show()
        self.back_button.clicked.connect(self.display_article_title)
        title = item.text()

        # 기사 본문
        content = self.current_crawler.get_article_content(self.current_article[title])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = NewTyper()
    sys.exit(app.exec_())
