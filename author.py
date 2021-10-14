class Author:

    def __init__(self, name, organization, number_documents, citations, h_index):
        self.name = name
        self.organization = organization
        self.number_documents = number_documents
        self.citations = citations
        self.h_index = h_index

    def show(self):
        print('Author : ' + self.name)
        print('Organization : ' + self.organization)
        print('Number of documents : ' + self.number_documents)
        print('Citations : ' + self.citations)
        print('H-Index : ' + self.h_index)