# copying and selling of this code  or this project is ilegal 




from tkinter import *
from fpdf import FPDF
from time import strftime
import datetime as dt
from tkinter import ttk
import tkinter.messagebox as tmsg

screen = Tk()
screen.title("Restaurant")
screen.geometry("350x300")
screen.configure(background="green")
restaurant_name = "Aman's Restaurant"
Label(screen, text="Welcome to the Restaurant", fg="white", bg="green" , font="caliberi 18 bold").pack()
Label(screen, text = "", fg="white", bg="green").pack()
Label(screen, text= restaurant_name, font="caliberi 18 bold", fg="white", bg="green").pack()
Label(screen, text = "", fg="white", bg="green").pack()

cust_name = StringVar()
cust_mob = StringVar()
Label(screen, text= "Customer Details", fg="yellow", bg="green", font="timesnewroman 10 bold").place(x=100, y=100)
Label(screen, text = "", fg="white", bg="green").pack()
Label(screen, text= "Name : ", fg="yellow", bg="green", font="timesnewroman 10 ").place(x=60, y=130)
Label(screen, text = "", fg="white", bg="green").pack()
name = Entry(screen, textvariable = cust_name).place(x=150, y=130)
Label(screen, text= "Mobile :", fg="yellow", bg="green", font="timesnewroman 10 ").place(x=60, y=170)
Label(screen, text = "", fg="white", bg="green").pack()
mobile = Entry(screen, textvariable = cust_mob).place(x=150, y=170)

def time():
    string = strftime("%H:%M:%S %p")
    lbl.config(text = string)
    lbl.after(1000, time)

lbl = Label(screen, font="caliberi 20 bold", bg="purple", fg="white")
lbl.place(x=170, y=260)
time()

w = Label(screen, text =f"{dt.datetime.now(): %A,\n %b %d, %Y}", bg="white", fg="black", font="caliberi 10 bold").place(x=30, y=260)
# making restaurwnt menu

def rest_menu():
    global scree1
    screen1 = Toplevel(screen)
    screen1.title("Menu")
    screen1.geometry("500x500")
    screen1.configure(background = "yellow")

    item1 = IntVar()
    item2 = IntVar()
    item3 = IntVar()
    item4 = IntVar()
    item5 = IntVar()
    item6 = IntVar()
    item7 = IntVar()
    item8 = IntVar()
    item9 = IntVar()
    item10 = IntVar()

    Label(screen1, text = "SABJI", fg='red', bg= "yellow", font = "dutch801xbdbt 15 bold").place(x=20, y=30)

    Label(screen1, text = "Veg", fg='green', bg= "yellow", font = "caliberi 13").place(x=15, y=80)
    Label (screen1, text="Aloo Gobhi", fg='black', bg="yellow").place (x=10, y=130)
    entry1 = Entry(screen1,  width=10, textvariable = item1).place(x = 105, y=132)
    Label (screen1, text="Aloo jeera", fg='black', bg="yellow").place (x=10, y=160)
    entry2 = Entry (screen1, width=10,  textvariable= item2).place (x = 105, y=162)
    Label (screen1, text="Aloo Bhindi", fg='black', bg="yellow").place (x=10, y=190)
    entry3 = Entry (screen1,  width=10, textvariable= item3).place (x = 105, y=192)
    Label (screen1, text="Aloo fry", fg='black', bg="yellow").place (x=10, y=220)
    entry4 = Entry (screen1,  width=10, textvariable=item4).place (x = 105, y=222)
    Label (screen1, text="Aloo Shimla ", fg='black', bg="yellow").place (x=10, y=250)
    entry5 = Entry (screen1,  width=10, textvariable= item5).place (x = 105, y=252)
    Label (screen1, text="kadhai Paneer", fg='black', bg="yellow").place (x=10, y=280)
    entry6 = Entry (screen1, width=10,  textvariable= item6).place (x = 105, y=282)
    Label (screen1, text="Paneer Bhurji", fg='black', bg="yellow").place (x=10, y=310)
    entry7 = Entry (screen1,  width=10, textvariable= item7).place (x = 105, y=312)
    Label (screen1, text="Paneer Butter Masala", fg='black', bg="yellow").place (x=10, y=340)
    entry8 = Entry (screen1, width=10,  textvariable= item8).place ( x = 105, y=342)
    Label (screen1, text="Saahi Paneer", fg='black', bg="yellow").place (x=10, y=370)
    entry9 = Entry (screen1, width=10,  textvariable= item9).place ( x = 105, y=372)
    Label (screen1, text="Mix Veg", fg='black', bg="yellow").place (x=10, y=400)
    entry10 = Entry (screen1, width=10,  textvariable= item10).place ( x = 105, y=402)

    item11 = IntVar()
    item12 = IntVar()
    item13 = IntVar()
    item14 = IntVar()
    item15 = IntVar()
    item16 = IntVar()

    Label (screen1, text="Non - Veg", fg='green', bg="yellow", font="caliberi 13").place (x=15, y=480)

    Label (screen1, text="Chicken Rasawala ", fg='black', bg="yellow").place (x=10, y=530)
    entry11 = Entry(screen1,  width=10, textvariable = item11).place(x = 105, y=532)
    Label (screen1, text="Butter Chicken ", fg='black', bg="yellow").place (x=10, y=560)
    entry12 = Entry(screen1,  width=10, textvariable = item12).place(x = 105, y=562)
    Label (screen1, text="Chicken Patiala ", fg='black', bg="yellow").place (x=10, y=590)
    entry13 = Entry(screen1,  width=10, textvariable = item13).place(x = 105, y=592)
    Label (screen1, text="Chicken Kadhai ", fg='black', bg="yellow").place (x=10, y=620)
    entry14 = Entry(screen1, width=10,  textvariable = item14).place(x = 105, y=622)
    Label (screen1, text="Mutton Kofta ", fg='black', bg="yellow").place (x=10, y=650)
    entry15 = Entry(screen1, width=10,  textvariable = item15).place(x = 105, y=652)
    Label (screen1, text="Mutton Angara ", fg='black', bg="yellow").place (x=10, y=680)
    entry16 = Entry(screen1, width=10, textvariable = item16).place(x = 105, y=682)

    item17 = IntVar()
    item18 = IntVar()
    item19 = IntVar()
    item20 = IntVar()
    item21 = IntVar()
    item22 = IntVar()

    Label (screen1, text="Parathas", fg='red', bg="yellow", font="dutch801xbdbt 15 bold").place (x=250, y=30)

    Label (screen1, text="Aloo Paratha ", fg='black', bg="yellow").place (x=220, y=130)
    entry17 = Entry (screen1, width=10, textvariable=item17).place (x=320, y=132)
    Label (screen1, text="Methi Paratha", fg='black', bg="yellow").place (x=220, y=160)
    entry18 = Entry (screen1, width=10, textvariable=item18).place (x=320, y=162)
    Label (screen1, text="Gobhi Paratha", fg='black', bg="yellow").place (x=220, y=190)
    entry19 = Entry (screen1, width=10, textvariable=item19).place (x=320, y=192)
    Label (screen1, text="Oninon Paratha", fg='black', bg="yellow").place (x=220, y=220)
    entry20 = Entry (screen1, width=10, textvariable=item20).place (x=320, y=222)
    Label (screen1, text="Multi Paratha ", fg='black', bg="yellow").place (x=220, y=250)
    entry21 = Entry (screen1, width=10, textvariable=item21).place (x=320, y=252)
    Label (screen1, text="Paneer Paratha", fg='black', bg="yellow").place (x=220, y=280)
    entry22 = Entry (screen1, width=10, textvariable=item22).place (x=320, y=282)

    item23 = IntVar()
    item24 = IntVar()
    item25 = IntVar()
    item26 = IntVar()
    item27 = IntVar()

    Label(screen1, text = "Dal ", fg="red", bg="yellow", font = "dutch801xbdbt 15 bold").place(x=270, y=480)

    Label(screen1, text = "Dal Fry ", fg="black", bg="yellow").place(x=220, y=530)
    entry23 = Entry (screen1, width=10, textvariable=item23).place (x=320, y=532)
    Label(screen1, text="Dal tadka ", fg="black", bg="yellow").place(x=220, y=560)
    entry24 = Entry (screen1, width=10, textvariable=item24).place (x=320, y=562)
    Label(screen1, text="Dal Makhani ", fg="black", bg="yellow").place(x=220, y=590)
    entry25 = Entry (screen1, width=10, textvariable=item25).place (x=320, y=592)
    Label(screen1, text="Dal Palak ", fg="black", bg="yellow").place(x=220, y=620)
    entry26 = Entry (screen1, width=10, textvariable=item26).place (x=320, y=622)
    Label(screen1, text="Dal Kolhapuri ", fg="black", bg="yellow").place(x=220, y=650)
    entry27 = Entry (screen1, width=10, textvariable=item27).place (x=320, y=652)

    item28 = IntVar()
    item29 = IntVar()
    item30 = IntVar()
    item31 = IntVar()
    item32 = IntVar()
    item33 = IntVar()
    item34 = IntVar()

    Label (screen1, text="Chapati", fg='red', bg="yellow", font="dutch801xbdbt 15 bold").place (x=470, y=30)

    Label (screen1, text="Tandoori Roti ", fg='black', bg="yellow").place (x=450, y=130)
    entry28 = Entry (screen1, width=10, textvariable=item28).place (x=550, y=132)
    Label (screen1, text="Butter Roti ", fg='black', bg="yellow").place (x=450, y=160)
    entry29 = Entry (screen1, width=10, textvariable=item29).place (x=550, y=162)
    Label (screen1, text="Chapati ", fg='black', bg="yellow").place (x=450, y=190)
    entry30 = Entry (screen1, width=10, textvariable=item30).place (x=550, y=192)
    Label (screen1, text="Sp. Chapati ", fg='black', bg="yellow").place (x=450, y=220)
    entry31 = Entry (screen1, width=10, textvariable=item31).place (x=550, y=222)
    Label (screen1, text="Naan Roti ", fg='black', bg="yellow").place (x=450, y=250)
    entry32 = Entry (screen1, width=10, textvariable=item32).place (x=550, y=252)
    Label (screen1, text="Missi Roti ", fg='black', bg="yellow").place (x=450, y=280)
    entry33 = Entry (screen1, width=10, textvariable=item33).place (x=550, y=282)
    Label(screen1, text = "Makka Roti ", fg='black', bg="yellow").place (x=450, y=280)
    entry34 = Entry (screen1, width=10, textvariable=item34).place (x=550, y=282)

    item35 = IntVar ( )
    item36 = IntVar ( )
    item37 = IntVar ( )
    item38 = IntVar ( )
    item39 = IntVar()
    item40 = IntVar()
    item41 = IntVar()


    Label (screen1, text="Rice ", fg="red", bg="yellow", font="dutch801xbdbt 15 bold").place (x=470, y=480)

    Label (screen1, text="Fry Rice ", fg="black", bg="yellow").place (x=450, y=530)
    entry35 = Entry (screen1, width=10, textvariable=item35).place (x=550, y=532)
    Label (screen1, text="Plain Rice ", fg="black", bg="yellow").place (x=450, y=560)
    entry36 = Entry (screen1, width=10, textvariable=item36).place (x=550, y=562)
    Label (screen1, text="Steamed Rice ", fg="black", bg="yellow").place (x=450, y=590)
    entry37 = Entry (screen1, width=10, textvariable=item37).place (x=550, y=592)
    Label (screen1, text="Jeera Rice ", fg="black", bg="yellow").place (x=450, y=620)
    entry38 = Entry (screen1, width=10, textvariable=item38).place (x=550, y=622)
    Label (screen1, text="Veg Pulao ", fg="black", bg="yellow").place (x=450, y=650)
    entry39 = Entry (screen1, width=10, textvariable=item39).place (x=550, y=652)
    Label (screen1, text="Lemon Rice ", fg="black", bg="yellow").place (x=450, y=680)
    entry40 = Entry (screen1, width=10, textvariable=item40).place (x=550, y=682)
    Label (screen1, text="Maasala Rice ", fg="black", bg="yellow").place (x=450, y=710)
    entry41 = Entry (screen1, width=10, textvariable=item41).place (x=550, y=712)

    item42 = IntVar()
    item43 = IntVar()
    item44 = IntVar()
    item45 = IntVar()
    item46 = IntVar()

    Label (screen1, text="Tea ", fg='red', bg="yellow", font="dutch801xbdbt 15 bold").place (x=690, y=30)

    Label (screen1, text="Masala Tea ", fg='black', bg="yellow").place (x=660, y=130)
    entry42 = Entry (screen1, width=10, textvariable=item42).place (x=760, y=132)
    Label (screen1, text="Lemon Tea ", fg='black', bg="yellow").place (x=660, y=160)
    entry43 = Entry (screen1, width=10, textvariable=item43).place (x=760, y=162)
    Label (screen1, text="Ginjer Tea", fg='black', bg="yellow").place (x=660, y=190)
    entry44 = Entry (screen1, width=10, textvariable=item44).place (x=760, y=192)
    Label (screen1, text="Black Tea ", fg='black', bg="yellow").place (x=660, y=220)
    entry45 = Entry (screen1, width=10, textvariable=item45).place (x=760, y=222)
    Label (screen1, text="Hot Coffee ", fg='black', bg="yellow").place (x=660, y=250)
    entry46 = Entry (screen1, width=10, textvariable=item46).place (x=760, y=252)

    pay = StringVar()
    Label(screen1, text = "Payment Mode : ", bg="white", fg="blue", font="arial 12").place(x=900, y=100)
    pay_combo = ttk.Combobox(screen1, values = ('Cash', 'Card', 'Phone Pay', 'Google Pay', 'Paytm', 'Amazon Pay'), textvariable = pay)
    pay_combo.place(x=1080, y=100)
    pay_combo.config(state="readonly")
    pay_combo.set('Select Mode')

    def total():
        global scree1
        Label(screen1, text = "PDF Generated Sucessfully.", fg="black", bg="white", font="timesnewroman 20 bold").place(x=50, y=10)



        total = (item1.get() + item2.get() + item3.get() + item4.get() + item5.get() + item6.get() + item7.get() + item8.get() + item9.get() + item10.get()
                    + item11.get() + item12.get() + item13.get() + item14.get() + item15.get() + item16.get() + item17.get() + item18.get() + item19.get()
                 + item20.get() + item21.get() + item22.get() + item23.get() + item24.get() + item25.get() + item26.get() + item27.get() + item28.get()
                 + item29.get() + item30.get() + item31.get() + item32.get() + item33.get() + item34.get() + item35.get() + item36.get() + item37.get()
                 + item38.get() + item39.get() + item40.get() + item41.get() + item42.get() + item43.get() + item44.get() + item45.get() + item46.get())
       # save fpdf in a class called pdf
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)

        pdf.cell(150, 5, txt="Welcome To the Restaurant", border=2, align="C", ln=1)
        pdf.cell(20, 5, txt=f"Customer Name : {cust_name.get()}", align=LEFT, ln=2)
        pdf.cell(20,5, txt=f"Customer Mobile : {cust_mob.get()}", align=LEFT, ln=3)

        if item1.get() != 0:
            pdf.cell(20, 10, txt=f"Aloo Gobhi : {item1.get()}", align=LEFT, ln=4)
        if item2.get() != 0:
            pdf.cell(20, 10, txt=f"Aloo Jeera : {item2.get()}", align=LEFT, ln=5)
        if item3.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Aloo Bhindi : {item3.get()}", align=LEFT, ln=6)
        if item4.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Aloo Fry : {item4.get()}", align=LEFT, ln=7)
        if item5.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Aloo Shimla : {item5.get()}", align=LEFT, ln=8)
        if item10.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Mix Veg : {item10.get()}", align=LEFT, ln=9)
        if item6.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Kadhai Paneer : {item6.get()}", align=LEFT, ln=10)
        if item7.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Paneer Bhurji : {item7.get()}", align=LEFT, ln=11)
        if item8.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Paneer Butter Masala : {item8.get()}", align=LEFT, ln=12)
        if item9.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Saahi Paneer : {item9.get()}", align=LEFT, ln=13)
        if item11.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Chicken Rasawala : {item11.get()}", align=LEFT, ln=14)
        if item12.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Butter Chicken : {item12.get()}", align=LEFT, ln=15)
        if item13.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Chicken Patiala : {item13.get()}", align=LEFT, ln=16)
        if item14.get() != 0:
            pdf.cell(20, 10, txt=f"Chicken Kadhai : {item14.get()}", align=LEFT, ln=17)
        if item15.get() != 0:
            pdf.cell(20, 10, txt=f"Mutton Kofta : {item15.get()}", align=LEFT, ln=18)
        if item16.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Mutton Angara : {item16.get()}", align=LEFT, ln=19)
        if item17.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Aloo Paratha : {item17.get()}", align=LEFT, ln=20)
        if item18.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Methi Paratha : {item18.get()}", align=LEFT, ln=21)
        if item19.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Gobhi Paratha : {item19.get()}", align=LEFT, ln=22)
        if item20.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Onion Paratha : {item20.get()}", align=LEFT, ln=23)
        if item21.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Multi Paratha : {item21.get()}", align=LEFT, ln=24)
        if item22.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Paneer Paratha : {item22.get()}", align=LEFT, ln=25)
        if item23.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Dal Fry : {item23.get()}", align=LEFT, ln=26)
        if item24.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Dal Tadka : {item24.get()}", align=LEFT, ln=27)
        if item25.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Dal Makhani : {item25.get()}", align=LEFT, ln=28)
        if item26.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Dal Palak : {item26.get()}", align=LEFT, ln=29)
        if item27.get() != 0:
            pdf.cell(20, 10, txt=f"Dal Kolhapuri : {item27.get()}", align=LEFT, ln=30)
        if item28.get() != 0:
            pdf.cell(20, 10, txt=f"Tandoori Roti  : {item28.get()}", align=LEFT, ln=31)
        if item29.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Butter Roti : {item29.get()}", align=LEFT, ln=32)
        if item30.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Chapati : {item30.get()}", align=LEFT, ln=33)
        if item31.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Sp. Chapati : {item31.get()}", align=LEFT, ln=34)
        if item32.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Naan Roti : {item32.get()}", align=LEFT, ln=35)
        if item33.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Missi Roti : {item33.get()}", align=LEFT, ln=36)
        if item34.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Makka Roti : {item34.get()}", align=LEFT, ln=37)
        if item35.get ( ) != 0:
            pdf.cell(20, 10, txt=f" Fry Rice : {item35.get()}", align=LEFT, ln=38)
        if item36.get ( ) != 0:
            pdf.cell(20, 10, txt=f"plain Rice : {item36.get()}", align=LEFT, ln=39)
        if item37.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Steamed Rice : {item37.get()}", align=LEFT, ln=40)
        if item38.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Jeera Rice : {item38.get()}", align=LEFT, ln=41)
        if item39.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Veg Pulao : {item39.get()}", align=LEFT, ln=42)
        if item40.get() != 0:
            pdf.cell(20, 10, txt=f"Lemon Rice : {item40.get()}", align=LEFT, ln=43)
        if item41.get() != 0:
            pdf.cell(20, 10, txt=f"Masala Rice : {item41.get()}", align=LEFT, ln=45)
        if item42.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Masala Tea : {item42.get()}", align=LEFT, ln=46)
        if item43.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Lemon Tea : {item43.get()}", align=LEFT, ln=47)
        if item44.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Ginger Tea : {item44.get()}", align=LEFT, ln=48)
        if item45.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Black Tea : {item45.get()}", align=LEFT, ln=49)
        if item46.get ( ) != 0:
            pdf.cell(20, 10, txt=f"Hot Coffee : {item46.get()}", align=LEFT, ln=50)

        pdf.cell(200, 20, txt=f"Your Total Bill is : {total} Rs Only /-", align="C", ln=51)

        pdf.cell(100, 20, txt=f"Payement Mode : {pay.get()}", align=LEFT, ln=52)
        pdf.cell(80, 20, txt="Whatsapp Us : 1234567890                                                                  Call us : 0987654321", align=LEFT, ln=53)
        pdf.cell(50, 25, txt="***** Thank you for coming to our restaurant and also thanks to give us a chance to serve you better *****", align=CENTER, ln=54)

        pdf.output(f"{cust_mob.get()}.pdf")

        def ok():
            screen2.destroy()
            screen1.destroy()

        screen2 = Toplevel(screen1)
        screen2.title("Total Bill")
        screen2.geometry("250x250")
        Label(screen2, text = f"Your Total bill is : {total}").place(x=100, y=50)
        Button(screen2, text = "ok", command = ok).place(x=140, y=100)



    Button(screen1, text = "Total Bill", command = total).place(x=500, y=400)

Button(screen, text = "Restaurant Menu", font='arial 8', relief ="ridge", command = rest_menu).place(x=150, y=210)

screen.mainloop()
