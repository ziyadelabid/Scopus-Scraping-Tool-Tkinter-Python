
from os import name
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from journals import *
from web_scraping import *
import csv
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def searchAuthor(inputId):

    root = Tk()
    root.geometry("1200x600+20+20")
    tv = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6, 7,
                      8, 9, 10), show="headings", height="12")
    tv.place(x=160, y=200)

    def createTable():
        idAuthor = inputId.get()
        result_object = get_publisher(idAuthor)
        author = result_object['author']
        documents = result_object['documents']
        nameAuthor = author.name
        numberDocuments = author.number_documents
        numberCitations = author.citations
        hIndex = author.h_index
        organization = author.organization

        # root.resizable(False,False)
        def sortPerType():
            rows = [(tv.set(item, '#1').lower(), item)
                    for item in tv.get_children('')]
            rows.sort()
            for index, (values, item) in enumerate(rows):
                tv.move(item, '', index)
        root.title(author.name)
        frame8 = Frame(master=root, width=1100, height=175, bg='blue')
        frame8.place(x=50, y=0)
        authorName_label = Label(master=frame8, text="Full name : " +
                                 nameAuthor, bg='blue', fg='white', font=(None, 14))
        authorName_label.place(x=60, y=20)
        numberDocuments_label = Label(
            master=frame8, text="Number of documents : " + numberDocuments, bg='blue', fg='white', font=(None, 14))
        numberDocuments_label.place(x=600, y=20)
        numberCitations_label = Label(
            master=frame8, text="Number of citations : " + numberCitations, bg='blue', fg='white', font=(None, 14))
        numberCitations_label.place(x=60, y=60)
        hindex_label = Label(master=frame8, text="H-index : " +
                             hIndex, bg='blue', fg='white', font=(None, 14))
        hindex_label.place(x=600, y=60)
        organization_label = Label(
            master=frame8, text="Organization : " + organization, bg='blue', fg='white', font=(None, 14))
        organization_label.place(x=60, y=120)
        tv.heading("#1", text="Type", command=sortPerType)
        tv.column("#1", minwidth=0, width=100, stretch=NO)
        tv.heading("#2", text="Title")
        tv.column("#2", minwidth=0, width=150, stretch=NO)
        tv.heading("#3", text="Authors")
        tv.column("#3", minwidth=0, width=150, stretch=NO)
        tv.heading("#4", text="Magazine")
        tv.column("#4", minwidth=0, width=150, stretch=NO)
        tv.heading("#5", text="Date")
        tv.column("#5", minwidth=0, width=35, stretch=NO)
        tv.heading("#6", text="h_index")
        tv.column("#6", minwidth=0, width=70, stretch=NO)
        tv.heading("#7", text="Sjr")
        tv.column("#7", minwidth=0, width=70, stretch=NO)
        tv.heading("#8", text="Ranking")
        tv.column("#8", minwidth=0, width=70, stretch=NO)
        tv.heading("#9", text="Impact Factor")
        tv.column("#9", minwidth=0, width=70, stretch=NO)
        tv.heading("#10", text="Q")
        tv.column("#10", minwidth=0, width=70, stretch=NO)
        for i in documents:
            tv.insert(parent='', index='end', values=(
                i.type, i.title, i.authors, i.magazine, i.date))

        # ====================Fonction pour selectionner l'élément courant et subir des opérations============

        def selectItem():
            curItem = tv.focus()
            valeursGeneral = tv.item(curItem)
            documentValues = valeursGeneral['values']
            magazine = documentValues[3]
            journals = get_journals(magazine)
            afficherJournal(magazine, journals, curItem)
        # ====================Fonction de suppression des dernières quatres colonnes dans la table============

        def clearRow():
            currentItem = tv.focus()
            tv.set(currentItem, '#6', "")
            tv.set(currentItem, '#7', "")
            tv.set(currentItem, '#8', "")
            tv.set(currentItem, '#9', "")
            tv.set(currentItem, '#10', "")

        # ====================Save info in Excel file============

        def exportToCSV():
            data = [tv.item(item)['values'] for item in tv.get_children()]
            df = pd.DataFrame(data, columns=[
                              'Type', 'Title', 'Authors', 'Magazine', 'Date', 'H-Index', 'Sjr', 'Ranking', 'Impact Factor', 'Q'])
            df.to_csv(nameAuthor + '.csv', sep="\t", encoding='utf-16', header=[
                      'Type', 'Title', 'Authors', 'Magazine', 'Date', 'H-Index', 'Sjr', 'Ranking', 'Impact Factor', 'Q'], index=False)
            messagebox.showinfo("Export completed !", "The data of " +
                                nameAuthor + " are exported successfully", master=root)

        # inputId.delete(0,END)
        btn_export = Button(master=root, text="Export", bg='#0cb071', activebackground="green", activeforeground='white',
                            fg='white', height=1, width=12, font=('Pangram', 15), command=lambda: exportToCSV())
        btn_export.place(x=320, y=475)
        btn_clear = Button(master=root, text="Clear", bg='red', activebackground="red", activeforeground='white',
                           fg='white', height=1, width=12, font=('Pangram', 15), command=lambda: clearRow())
        btn_clear.place(x=720, y=475)
        btn_journalSearch = Button(master=root, text="Search Journals", bg='blue', activebackground="blue",
                                   activeforeground='white', fg='white', height=1, width=13, font=('Pangram', 15), command=lambda: selectItem())
        btn_journalSearch.place(x=520, y=475)
    createTable()
# **************************************************************************
# Affichage des journaux pour chaque magazine
# ****************************************************************************

    def afficherJournal(magazine, journal,  currentItem):
        journalWindow = Tk()
        journalWindow.geometry("1200x600+20+20")

        def sort(magazine):
            col_names = ["Rank", "Sourceid", "Title", "Type",	"Issn",	"SJR",	"SJR Best Quartile",	"H index", "	Total Docs. (2020)"	, "Total Docs. (3years)"	, "Total Refs.", "	Total Cites (3years)"	, "Citable Docs. (3years)"	, "Cites / Doc. (2years)",	"Ref. / Doc."	, "Country", "Region",	"Publisher",	"Coverage",	"Categories"
                         ]
            df = pd.read_csv(
                'scimagojr2020.csv', sep=';', names=col_names, header=None)
            myRow = df.loc[df['Title'] ==
                           magazine]
            return(myRow['SJR Best Quartile'].values[0])
        frame9 = Frame(master=journalWindow, width=800, height=75, bg='blue')
        frame9.place(x=200, y=0)
        journal_label = Label(
            master=frame9, text="Journals List", bg='blue', fg='white', font=(None, 18))
        journal_label.place(x=300, y=25)
        tv_journal = ttk.Treeview(journalWindow, columns=(
            1, 2, 3, 4, 5, 6), show="headings", height="12")
        tv_journal.place(x=200, y=200)
        tv_journal.heading(1, text="Name")
        tv_journal.column(1, minwidth=0, width=300, stretch=NO)
        tv_journal.heading(2, text="h_index")
        tv_journal.column(2, minwidth=0, width=120, stretch=NO)
        tv_journal.heading(3, text="Sjr")
        tv_journal.column(3, minwidth=0, width=120, stretch=NO)
        tv_journal.heading(4, text="Ranking")
        tv_journal.column(4, minwidth=0, width=120, stretch=NO)
        tv_journal.heading(5, text="Impact factor")
        tv_journal.column(5, minwidth=0, width=120, stretch=NO)
        tv_journal.heading(6, text="Q")
        tv_journal.column(6, minwidth=0, width=120, stretch=NO)

        for i in journal:
            tv_journal.insert(parent='', index='end', values=(
                i.name, i.h_index, i.sjr, i.ranking, i.impact_factor, sort(magazine)))
        btn_ok = Button(master=journalWindow, text="OK", bg='#0cb071', activebackground="green",
                        fg='white', height=1, width=12, font=('Pangram', 16), command=lambda: selectItemJournal())
        btn_ok.place(x=500, y=500)
        # Selectionner un éléments dans la liste des journaux

        def selectItemJournal():
            curItem = tv_journal.focus()
            valeursGeneral = tv_journal.item(curItem)
            journalWindow.destroy()
            journalValues = valeursGeneral['values']
            # magazine=journalValues[0]
            h_index = journalValues[1]
            sjr = journalValues[2]
            ranking = journalValues[3]
            impact_factor = journalValues[4]
            q_sjr = journalValues[5]
            tv.set(currentItem, '#6', h_index)
            tv.set(currentItem, '#7', sjr)
            tv.set(currentItem, '#8', ranking)
            tv.set(currentItem, '#9', impact_factor)
            tv.set(currentItem, '#10', q_sjr)
