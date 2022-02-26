import jieba
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from PIL import Image
import numpy as np


def extract_text(url):
    """Extract html content."""
    page_source = requests.get(url).content
    bs_source = BeautifulSoup(page_source)
    report_text = bs_source.find_all('p')

    text = ''

    for p in report_text:
        text += p.get_text()
        text += '\n'

    return text


def word_frequency(text):
    from collections import Counter
    mask01 = Image.open("word_05.png")
    graph = np.array(mask01)
    words = [word for word in jieba.cut(text, cut_all=True) if len(word) >= 2]
    c = Counter(words)
    frequency = dict()
    for word_freq in c.most_common(10):
        # frequency[word_freq[0]] = float(word_freq[1])
        for i in range(100):
            frequency[word_freq[0] + str(i)] = float(word_freq[1])
    word_cloud = WordCloud(font_path='C:\Windows\Fonts\STXINGKA.TTF', background_color='white', mask=graph)
    word_cloud.generate_from_frequencies(frequency)
    word_cloud.to_file('word_cloudsophie.png')
url_2016 = 'http://www.gov.cn/guowuyuan/2016-03/05/content_5049372.htm'
text_2016 = extract_text(url_2016)
word_frequency(text_2016)
