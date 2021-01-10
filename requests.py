import json
import requests
import html2text


def get_web_html(url: str) -> str:
    """
    Get full html page contents from url.
    """
    r = requests.get(url)
    return r.text


def get_web_text(url: str, splitToLines: bool) -> str/list:
    """
    Get the text contents from url.
    """
    r = requests.get(url)
    text = html2text.html2text(r.text)
    if splitToLines == True:
        text = text.split("\n")
    return text


def get_web_json(url: str) -> dict:
    """
    Get the json response from url.
    """
    r = requests.get(url)
    return json.loads(r.text)


def get_web_photo(url: str, savepath: str):
    """
    Download photo from url and save it to savepath.
    """
    r = requests.get(url)
    with open(savepath, 'wb') as f:
        f.write(r.content)
