import requests
from lxml import etree
import lxml.html
import csv


def parse(url, song_name):
    try:
        api = requests.get(url)
    except:
        return
    tree = lxml.html.document_fromstring(api.text)
    text_original = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/text()')
    text_translate = tree.xpath('//*[@id="click_area"]/div//*[@class="translate"]/text()')
    path = song_name + ".csv"
    csv_writer(text_original, text_translate, path)


def pre_parse(song_name):
    url = "https://www.amalgama-lab.com/songs/t/tones_and_i/" + song_name + ".html"
    # parse("https://www.amalgama-lab.com/songs/t/tones_and_i/dance_monkey.html")
    parse(url, song_name)


def csv_writer(original, translate, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for i in range(len(original)):
            writer.writerow(original[i])
            writer.writerow(translate[i])


if __name__ == "__main__":
    # you should use not capital letters and _ between words
    name_of_song = input()
    pre_parse(name_of_song)
