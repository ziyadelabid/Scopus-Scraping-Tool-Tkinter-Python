class Document:

    def __init__(self, type, title, authors, magazine, date):
        self.type = type
        self.title = title
        self.authors = authors
        self.magazine = magazine
        self.date = date

    def show(self):
        print('type : ' + self.type)
        print('title : ' + self.title )
        print('authors : ' + self.authors)
        print('magazine : ' + self.magazine)
        print('date : ' + self.date)