from searchAuthor import searchAuthor
from tkinter import *
from journals import *
from web_scraping import *
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

window = Tk()
window.geometry("800x450+275+100")
window.resizable(False, False)
window.title("Web Scraping from Scopus")


# ====================Function to switch frames===============
def switch_frames(frame, page):
    frame.pack_forget()
    start_page(page)


def start_page(frame):
    frame.pack(fill=BOTH)


# ====================End of switching frames==================
# ======================Code Of Side Bar=======================
frame1 = Frame(master=window, width=175, bg="#515FFF")
frame1.pack_propagate(0)
frame1.pack(fill=BOTH, side=LEFT)

label = Label(frame1,
              text="Scopus",
              font=('Breadcrumbs', 20),
              foreground='blue',
              width=12,
              height=2,
              background='white').grid(row=0, column=0, pady=0)
b1 = Button(frame1,
            text="Search Author",
            font=('Pangram', 14),
            foreground='white',
            background='blue',
            width=16,
            command=lambda: switch_frames(frame3, frame2)).grid(row=1, column=0, pady=30, padx=0)
b1 = Button(frame1,
            text="Search by id",
            font=('Pangram', 14),
            foreground='white',
            background='blue',
            width=16,
            command=lambda: switch_frames(frame2, frame3)).grid(row=2, column=0, pady=10, padx=0)

# ======================End Code Of Side Bar======================


# ======================Code of searching by id=================
frame3 = Frame(master=window, width=175, height=800, bg="white")
frame3.pack_propagate(0)
frame3.pack(fill=BOTH)
frame5 = Frame(master=frame3, width=800, height=65,
               bg='orange').place(x=0, y=0)
l2 = Label(master=frame3, text="Search author By id", bg='orange',
           fg='white', font=(None, 18)).place(x=200, y=17)
id_l = Label(master=frame3, text="ID :", fg='#2F45FF',
             bg='white', font=(None, 14)).place(x=170, y=170)
inputId = Entry(master=frame3, highlightthickness=2)
inputId.place(x=300, y=175)
btn_Search_id = Button(master=frame3, text="Search", bg='#0cb071', activeforeground='white', activebackground="green",
                       fg='white', height=1, width=12, font=('Pangram', 16), command=lambda: searchAuthor(inputId)).place(x=240, y=270)
# ====================Code Of Searching author page===============
frame2 = Frame(master=window, width=175, height=800, bg="white")
frame2.pack_propagate(0)
frame2.pack(fill=BOTH)
frame4 = Frame(master=frame2, width=175, height=71,
               bg='orange').pack(fill=BOTH)
l2 = Label(master=frame4, text="Search author", bg='orange',
           fg='white', font=(None, 18)).place(x=400, y=17)
first_name_l = Label(master=frame2, text="First name :",
                     fg='#2F45FF', bg='white', font=(None, 14)).place(x=30, y=150)
last_name_l = Label(master=frame2, text="Last name :", fg='#2F45FF',
                    bg='white', font=(None, 14)).place(x=300, y=150)
affiliation_l = Label(master=frame2, text="Affiliation :",
                      fg='#2F45FF', bg='white', font=(None, 14)).place(x=30, y=200)
inputFirstN = Entry(master=frame2, highlightthickness=2)
inputFirstN.place(x=145, y=155)
inputLastN = Entry(master=frame2, highlightthickness=2)
inputLastN.place(x=415, y=155)
inputAffiliation = Entry(master=frame2, highlightthickness=2)
inputAffiliation.place(x=145, y=205)
btn_Search = Button(master=frame2, text="Search", bg='#0cb071', activebackground="green", fg='white',
                    height=1, width=12, font=('Pangram', 16), command=lambda: searchAuthor()).place(x=240, y=270)

window.mainloop()
