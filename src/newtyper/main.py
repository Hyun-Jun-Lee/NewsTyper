import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, pyqtProperty
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QComboBox,
    QLabel,
    QHBoxLayout,
    QListWidget,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QMessageBox,
)

from newtyper.data_manager import DataManager
from enums.enums import LanguageEnum


class NewTyper(QWidget):
    def __init__(
        self, parent: QWidget | None = ..., flags: Qt.WindowFlags | Qt.WindowType = ...
    ) -> None:
        super().__init__()
        self.data_manager = DataManager()
        self.current_quote = None
        self.article_list = None
        self.check_and_load_quotes()
        self.init_ui()

    def check_and_load_quotes(self):
        """데이터베이스 확인 및 초기화."""
        if self.data_manager.is_empty():
            result = self.data_manager.load_quotes()
            if not result:
                QMessageBox.critical(self, "오류", "데이터 로드에 실패했습니다.")
                return

    def init_ui(self):
        self.setWindowTitle("NewsTyper")
        self.move(300, 300)
        self.resize(800, 500)
        self.show()

        hbox = QHBoxLayout()

        # 언어 선택
        language_layout = QHBoxLayout()
        language_layout.addStretch(1)

        agency_label = QLabel("Select Language:", self)
        language_layout.addWidget(agency_label)

        self.language_combobox = QComboBox(self)
        self.language_combobox.addItem("Select", None)
        language_layout.addWidget(self.language_combobox)
        hbox.addLayout(language_layout)

        for language in LanguageEnum:
            self.language_combobox.addItem(language.value, language)

        self.language_combobox.activated.connect(self.choice_language)

        # 언어 선택
        language_layout = QHBoxLayout()

        self.language_combobox = QComboBox(self)
        language_layout.addStretch(1)

        hbox.addLayout(language_layout)

        # 수직 정렬
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        # 타이핑 완료 문장
        self.completed_sentences_display = QTextEdit()
        self.completed_sentences_display.setReadOnly(True)
        vbox.addWidget(self.completed_sentences_display)

        # 기사 타이핑
        # TODO : sentence_label 과 user_input 배치 정렬 / 메서드 정리
        self.sentence_label = QLabel("여기에 기사 내용이 표시됩니다.")
        self.user_input = QLineEdit(self)
        self.animation = QPropertyAnimation(self.user_input, b"geometry")

        vbox.addWidget(self.sentence_label)
        vbox.addWidget(self.user_input)

        self.setLayout(vbox)

        # 사용자 입력 감지
        self.user_input.textChanged.connect(self.check_and_continue)

    def choice_language(self, index):
        selected_language = self.language_combobox.itemData(index)
        self.display_quotes(selected_language)
        self.language_combobox.clear()

    def display_quotes(self, language: str):
        current_quote = self.data_manager.get_random_quote()
        if language == LanguageEnum.KR:
            self.current_quote = current_quote.kr_content
        else:
            self.current_quote = current_quote.en_content
        self.current_author = current_quote.author

        display_text = f"{self.current_quote} - {self.current_author}"

        self.sentence_label.setText(display_text)
        self.sentence_label.setWordWrap(True)
        self.user_input.clear()

    def check_and_continue(self):
        user_input = self.user_input.text()

        if not self.current_quote:
            return

        if user_input == self.current_quote:
            self.display_next_sentence()
            self.display_quotes(self.language_combobox.currentData())
            self.user_input.setStyleSheet("")  # 기본 스타일로 재설정
        else:
            correct_input = self.current_quote[: len(user_input)]
            if user_input == correct_input:
                # 입력이 문장의 일부와 일치하는 경우, 테두리를 초록색으로 변경
                self.user_input.setStyleSheet("border: 2px solid green;")
            else:
                # 입력이 잘못된 경우, 테두리를 빨간색으로 변경
                self.shakeAnimation()
                self.user_input.setStyleSheet("border: 2px solid red;")

    def shakeAnimation(self):
        start_geometry = self.user_input.geometry()
        self.animation.setDuration(100)  # 애니메이션 지속 시간 설정
        self.animation.setLoopCount(1)  # 애니메이션 반복 횟수
        self.animation.setKeyValueAt(0, start_geometry)
        self.animation.setKeyValueAt(
            0.1,
            QRect(
                start_geometry.x() - 10,
                start_geometry.y(),
                start_geometry.width(),
                start_geometry.height(),
            ),
        )
        self.animation.setKeyValueAt(0.2, start_geometry)
        self.animation.setKeyValueAt(
            0.3,
            QRect(
                start_geometry.x() + 10,
                start_geometry.y(),
                start_geometry.width(),
                start_geometry.height(),
            ),
        )
        self.animation.setKeyValueAt(0.4, start_geometry)
        self.animation.setKeyValueAt(
            0.5,
            QRect(
                start_geometry.x() - 10,
                start_geometry.y(),
                start_geometry.width(),
                start_geometry.height(),
            ),
        )
        self.animation.setKeyValueAt(0.6, start_geometry)
        self.animation.setKeyValueAt(
            0.7,
            QRect(
                start_geometry.x() + 10,
                start_geometry.y(),
                start_geometry.width(),
                start_geometry.height(),
            ),
        )
        self.animation.setKeyValueAt(0.8, start_geometry)
        self.animation.setKeyValueAt(
            0.9,
            QRect(
                start_geometry.x() - 10,
                start_geometry.y(),
                start_geometry.width(),
                start_geometry.height(),
            ),
        )
        self.animation.setKeyValueAt(1, start_geometry)
        self.animation.finished.connect(
            lambda: self.user_input.setGeometry(start_geometry)
        )
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = NewTyper()
    sys.exit(app.exec_())
