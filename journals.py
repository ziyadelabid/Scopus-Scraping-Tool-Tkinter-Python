from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Journal:

    def __init__(self, name, h_index, sjr, ranking, impact_factor):
        self.name = name
        self.h_index = h_index
        self.sjr = sjr
        self.ranking = ranking
        self.impact_factor = impact_factor

    def show(self):
        print('Journal : ' + self.name)
        print('h_index : ' + self.h_index)
        print('sjr : ' + self.sjr)
        print('overalranking : ' + self.ranking)
        print('Impact Factor : ' + self.impact_factor)


def get_journals(j_name):

    journal_name = j_name.replace(" ", "+")
    url = 'https://www.resurchify.com/find/?query=' + journal_name

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()

    soup = BeautifulSoup(page, 'html.parser')
    result = soup.find_all(class_='w3-white w3-container w3-card-4 w3-hover-light-gray')
    #del result[0]

    journals = []
    for journal in result:
        name = journal.find('h3').text
        if j_name.lower() in name.lower():
            names = journal.find_all('span')
            i_f = names[0].text.split(' ')[3]
            ranking = names[3].text.split(' ')[3]
            h_i = names[1].text.split(' ')[2]
            sjr = names[2].text.split(' ')[2]
            j = Journal(name, h_i, sjr, ranking, i_f)
            journals.append(j)

    return journals


# result = get_journals('Pattern recognition')
# for j in result:
#     j.show()
#     print('-----------------------------------------------------------')