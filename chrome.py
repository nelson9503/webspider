import json
import html2text
import chromedriver_autoinstaller
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class GoogleChrome:

    def __init__(self, headless: bool = True, windowSize: list = [1600, 800]):
        check_installed = self.__check_chrome_installed()
        if check_installed == False:
            self.chrome = None
        else:
            self.path = chromedriver_autoinstaller.install()
            self.options = Options()
            if headless == True:
                self.options.add_argument("--headless")
            self.options.add_argument(
                "window-size={},{}".format(windowSize[0], windowSize[1]))
            self.chrome = Chrome(self.path, options=self.options)

    def __check_chrome_installed(self):
        try:
            chromedriver_autoinstaller.get_chrome_version()
        except IndexError:
            return False
        return True

    def close(self):
        """
        close the connection to google chrome.
        """
        self.chrome.close()

    def connect(self):
        """
        connect to google chrome.
        """
        self.chrome = Chrome(self.path, options=self.options)

    def browse(self, url: str):
        """
        browser the url.
        """
        self.chrome.get(url)
    
    def getHTML(self) -> str:
        """
        get the html contents from current page.
        """
        html = self.chrome.page_source
        return html

    def getText(self, splitToLines: bool = True) -> str/list:
        """
        get text contents from current page.
        """
        text = self.chrome.page_source
        text = html2text.html2text(text)
        if splitToLines == True:
            text = text.split("\n")
        return text

    def getJSON(self) -> dict:
        """
        get json contents from current page.
        """
        text = self.getText()
        try:
            j = json.loads(text)
        except:
            j = {}
        return j
