import requests
import lxml.html
import csv
import os


def parse(url, song_name):

    base_url = "https://www.amalgama-lab.com"
    api = requests.get(base_url)
    try:
        api = requests.get(url)
    except requests.exceptions.Timeout:
        api = requests.get(url)
    except requests.exceptions.TooManyRedirects:
        print("Bad url")
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        raise SystemExit(e)

    tree = lxml.html.document_fromstring(api.text)
    text_original = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/text()')
    text_translate = tree.xpath('//*[@id="click_area"]/div//*[@class="translate"]/text()')
    path = song_name + ".csv"
    csv_writer(text_original, text_translate, path)


def pre_parse(song_name):
    url = "https://www.amalgama-lab.com/songs/t/tones_and_i/" + song_name + ".html"
    parse(url, song_name)


def csv_writer(original, translate, path):
    if os.path.exists(path):
        with open(path, "w", newline='') as csv_file:
            try:
                writer = csv.writer(csv_file, delimiter=';')
                for i in range(len(original)):
                    writer.writerow(original[i])
                    writer.writerow(translate[i])
            except OSError:
                print("Could not open/read file:", path)


if __name__ == "__main__":
    # you should use not capital letters and _ between words
    name_of_song = input()
    pre_parse(name_of_song)
