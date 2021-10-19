import requests
import json

COUNTRIES = requests.get('https://raw.githubusercontent.com/mledoze/countries/master/countries.json')

wiki_link = 'https://en.wikipedia.org/wiki/'

with open('countries.json', 'w', encoding='utf-8') as file:
    file.write(COUNTRIES.text)

country_list = open('countries.json')


class CountryWikiFinder:

    wiki_link = 'https://en.wikipedia.org/wiki/'

    def __init__(self, data):
        self.data = data
        self.cursor = -1
        self.stop = len(self.data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor == self.stop:
            raise StopIteration
        self.cursor += 1
        country_name = self.data[self.cursor]['name']['common']
        return f"{country_name} - {wiki_link+country_name.replace(' ', '_')}"


with open('result_file.txt', 'w') as file:
    for item in CountryWikiFinder(json.load(country_list)):
        file.write(f"{item}\n")
