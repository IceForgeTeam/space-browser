# Space Browser
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import requests


class SpaceBrowser:
    def __init__(self):
        self.window = QWidget()
        self.window.setStyleSheet("background: #373737;border: 2px solid orange;")
        self.window.setWindowTitle("Space Browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.input_url = QTextEdit()
        self.input_url.setMaximumHeight(40)
        self.input_url.setStyleSheet(
            "border: 1px solid gold;border-top-left-radius: 15px;border-bottom-left-radius: 15px;background: #141414; color: white; font-size: 20px; padding: 3px;")

        self.search_button = QPushButton("Search")
        self.search_button.setMaximumHeight(40)
        self.search_button.setStyleSheet(
            "border: 2px solid gold;border-bottom-right-radius: 15px;border-top-right-radius: 15px;background: #141414; color: white; font-weight: 900; width: 65px;")

        self.prev_btn = QPushButton("<")
        self.prev_btn.setMaximumHeight(30)
        self.prev_btn.setStyleSheet(
            "border: 2px solid gold;border-radius: 15px;background: #141414; color: white; font-weight: 900; width: 35px;")

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMaximumHeight(30)
        self.forward_btn.setStyleSheet(
            "border: 2px solid gold;border-radius: 15px;background: #141414; color: white; font-weight: 900; width: 35px;")

        self.reload_btn = QPushButton("Reload")
        self.reload_btn.setMaximumHeight(30)
        self.reload_btn.setStyleSheet(
            "border: 2px solid gold;border-radius: 15px;background: #141414; color: white; font-weight: 900; width: 65px;")

        self.horizontal.addWidget(self.prev_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.reload_btn)
        self.horizontal.addWidget(self.input_url)
        self.horizontal.addWidget(self.search_button)

        self.browser = QWebEngineView()

        self.search_button.clicked.connect(lambda: self.navigation(self.input_url.toPlainText()))
        self.prev_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.reload_btn.clicked.connect(self.browser.reload)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        try:
            requests.get('http://127.0.0.1:8000/')
        except requests.exceptions.ConnectionError:
            self.browser.setUrl(QUrl("https://google.com/"))
        else:
            self.browser.setUrl(QUrl("http://127.0.0.1:8000/"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigation(self, url):
        if not url.startswith("http"):
            self.browser.setUrl(QUrl(f"https://google.com/search?q={url}"))
            self.browser.setUrl(QUrl(f"https://google.com/search?q={url}"))
        else:
            url = self.input_url.toPlainText()
            self.input_url.setText(url)
            self.browser.setUrl(QUrl(url))


app = QApplication([])
window = SpaceBrowser()
app.exec_()
