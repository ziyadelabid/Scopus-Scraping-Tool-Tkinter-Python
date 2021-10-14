import time

from selenium import webdriver
from document import Document
from author import Author
import pathlib

import sys


def get_publisher(author_id):

    path = str(pathlib.Path(__file__).parent.absolute()) + '\\chromedriver'

    # path = r'C:\\Users\\PREDATOR\Desktop\\chrome\\chromedriver'

    driver = webdriver.Chrome(executable_path=path)

    url = 'https://www.scopus.com/authid/detail.uri?authorId=' + author_id

    driver.get(url)

    author_name = driver.find_element_by_css_selector(
        '#author-general-details > div > h2').text
    organization = driver.find_element_by_css_selector(
        '#author-general-details > div > div:nth-child(5) > micro-ui > scopus-institution-name-link > span').text
    documents_number = driver.find_element_by_css_selector(
        '#scopus-author-profile-page-control-microui__ScopusAuthorProfilePageControlMicroui > div:nth-child(2) > div > micro-ui > scopus-author-details > section > div > div.col-lg-6.col-24 > section > div:nth-child(1) > h3').text
    citations = driver.find_element_by_css_selector(
        '#scopus-author-profile-page-control-microui__ScopusAuthorProfilePageControlMicroui > div:nth-child(2) > div > micro-ui > scopus-author-details > section > div > div.col-lg-6.col-24 > section > div:nth-child(2) > h3').text
    h_index = driver.find_element_by_css_selector(
        '#scopus-author-profile-page-control-microui__ScopusAuthorProfilePageControlMicroui > div:nth-child(2) > div > micro-ui > scopus-author-details > section > div > div.col-lg-6.col-24 > section > div:nth-child(3) > h3').text
    documents = driver.find_elements_by_css_selector(
        ".results-list-item[data-component='results-list-item']")

    org_info = organization.split('\n')
    if len(org_info) == 3:
        del org_info[1]
    organization = ''.join(org_info)

    author = Author(author_name, organization,
                    documents_number, citations, h_index)
    # author.show()
    print('***************************************************************')
    result = []
    for document in documents:
        title = document.find_element_by_css_selector(
            'div > div.col-19 > h5 > span').text
        doc_type = document.find_element_by_css_selector(
            "div > div.col-19 > .text-meta[data-component='document-type']").text
        authors = document.find_element_by_css_selector(
            'div > div.col-19 > div.author-list').text

        div_meta = document.find_element_by_css_selector(
            'div > div.col-19 > div.text-width-34')
        all_meta = div_meta.find_elements_by_class_name('text-meta')
        meta = []
        for text_meta in all_meta:
            meta.append(text_meta.text)

        d = Document(doc_type, title, authors, meta[0], ', '.join(meta[1:]))
        # d.show()
        result.append(d)
        print('****************************************************')

    driver.close()
    print('chrome finished')
    time.sleep(1)
    print('program finished')

    result = {"author": author, "documents": result}

    return result


# result_object = get_publisher('56426407100')
# result_object['author'].show()
# for i in result_object['documents']:
#     i.show()
#     print("----------------------------------------------")
