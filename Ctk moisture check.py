import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("525x375")
app.title("Moisture Checker")

def e():
    exit()

def check1():
    label1.destroy()
    cb1.destroy()
    cb2.destroy()
    cb3.destroy()

    def subm():
        intqen = int(qen.get())

        if intqen >= 20 and intqen <= 60:
            l101 = customtkinter.CTkLabel(master= frame,text="You can grow the Crop/Fruit.",font=("Roboto",18))
            l101.pack()
        if intqen < 20:
            l102 = customtkinter.CTkLabel(master=frame,text="Your soil is still dry, please irrigate it more.",font=("Roboto",18))
            l102.pack()
        if intqen > 60:
            l103 = customtkinter.CTkLabel(master=frame,text="Your soil is over moistured let dry for some time",font=("Roboto",18))
            l103.pack()
    
    ql = customtkinter.CTkLabel(master=frame,text="""What is the moisture content of your soil?
    (write in percentage without the sign)""",font=("Roboto",20))
    ql.pack()

    qen = customtkinter.CTkEntry(master=frame,font=("Roboto",18))
    qen.pack(pady= 20,padx=25)

    sub = customtkinter.CTkButton(master = frame, font=("Roboto",20),text="Submit",command=subm)
    sub.pack(pady=15,padx=20)

def check2():
    label1.destroy()
    cb1.destroy()
    cb2.destroy()
    cb3.destroy()

    def subm():

        intqen = int(qen.get())

        if intqen >= 40 and intqen <= 80:
            l101 = customtkinter.CTkLabel(master= frame,text="You can grow the Vegetable.",font=("Roboto",18))
            l101.pack()
        if intqen < 40:
            l102 = customtkinter.CTkLabel(master=frame,text="Your soil is still dry, please irrigate it more.",font=("Roboto",18))
            l102.pack()
        if intqen > 80:
            l103 = customtkinter.CTkLabel(master=frame,text="Your soil is over moistured let dry for some time",font=("Roboto",18))
            l103.pack()
    
    ql = customtkinter.CTkLabel(master=frame,text="""What is the moisture content of your soil?
    (write in percentage without the sign)""",font=("Roboto",20))
    ql.pack()

    qen = customtkinter.CTkEntry(master=frame,font=("Roboto",18))
    qen.pack(pady= 20,padx=25)

    sub = customtkinter.CTkButton(master = frame, font=("Roboto",20),text="Submit",command=subm)
    sub.pack(pady=15,padx=20)

def check3():
    label1.destroy()
    cb1.destroy()
    cb2.destroy()
    cb3.destroy()

    def subm():

        intqen = int(qen.get())

        if intqen >= 25 and intqen <= 61:
            l101 = customtkinter.CTkLabel(master= frame,text="You can grow the Cereals, Pulses, Oilseeds, and Commercial crops.",font=("Roboto",18))
            l101.pack()
        if intqen < 25:
            l102 = customtkinter.CTkLabel(master=frame,text="Your soil is still dry, please irrigate it more.",font=("Roboto",18))
            l102.pack()
        if intqen > 61:
            l103 = customtkinter.CTkLabel(master=frame,text="Your soil is over moistured let dry for some time",font=("Roboto",18))
            l103.pack()
    
    ql = customtkinter.CTkLabel(master=frame,text="""What is the moisture content of your soil?
    (write in percentage without the sign)""",font=("Roboto",22))
    ql.pack()
    
    qen = customtkinter.CTkEntry(master=frame,font=("Roboto",20))
    qen.pack(pady= 20,padx=25)

    sub = customtkinter.CTkButton(master = frame, font=("Roboto",20),text="Submit",command=subm)
    sub.pack(pady=15,padx=20)

frame =customtkinter.CTkFrame(master=app)
frame.pack(pady=20,padx=60,fill="both",expand=True)

heading = customtkinter.CTkLabel(master= frame, text="Moisture Checker",text_color="Green",font=("Roboto",24))
heading.pack()

label1 = customtkinter.CTkLabel(master=frame,text="Enter the type of plant you want to grow:",font=("Roboto",18))
label1.pack()

cb1 = customtkinter.CTkCheckBox(master= frame, text="Crops\Fruits",font=("Roboto",15),command=check1)
cb1.pack(pady=15, padx=20)
cb2 = customtkinter.CTkCheckBox(master=frame,text="Vegetables",font=("Roboto",15),command=check2)
cb2.pack(pady=16.5, padx=20)
cb3 = customtkinter.CTkCheckBox(master = frame,text="Cereals, Pulses, Oilseeds,\n and Commercial crops",font=("Roboto",15),command=check3)
cb3.pack(pady=17, padx=20)

exbut = customtkinter.CTkButton(master=app,text="Exit App",font=("Roboto",14),command=e)
exbut.pack(padx = 10,pady=20)

app.mainloop()
