from tkinter import *
from functools import partial
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *
from tkinter import font as tkFont
from tkinter.ttk import Combobox
import mysql.connector
import mysql.connector as mysqlob
from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button

def sign_in():
    def validateLogin(username, password):
        if username.get()=="" and password.get()=="":
            MsgBox = messagebox.showerror ('Empty Entry',message="Kindly fill the required details",icon = 'warning')
        elif username.get()=="":
            MsgBox = messagebox.showerror ('Empty Entry',message="Kindly fill the username",icon = 'warning')
        elif password.get()=="":
            MsgBox = messagebox.showerror ('Empty Entry',message="Kindly fill the password",icon = 'warning')
        else:
            hello1=username.get()
            hello2=password.get()
            db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
            myc=db.cursor()
            myc.execute("select username from user_table")
            resc=myc.fetchall( )
            for i in resc:
                copyx=(hello1,)
                if copyx==i:
                    myc.execute("select password from user_table where username= '%s' "%(hello1))
                    resc=myc.fetchall()
                    for i in resc:
                        copyy=(hello2,)
                        if copyy==i:
                            messagebox.showinfo ('Welcome',message="SIGN IN SUCCESSFULL")
                            tkWindow.destroy()
                            usernameEntry.delete(0, END)
                            passwordEntry.delete(0, END)
                        else:
                            messagebox.showerror ('Try Again',message="INCORRECT information")
            myc.execute("select username from user_table")
            res=myc.fetchall( )
            for i in res:
                copyx=(hello1,)
                if copyx!=i:  
                    messagebox.showerror ('Try Again',message="INCORRECT information")
            usernameEntry.delete(0, END)
            passwordEntry.delete(0, END)
        return        
    def exitLogin( ):
        MsgBox = messagebox.askquestion ('','Are you sure you want to exit the application?',icon = 'warning')
        if MsgBox == 'yes':
            tkWindow.destroy()
        else:
            exit
    tkWindow = Toplevel()  
    tkWindow.geometry('420x150')  
    tkWindow.title('SIGN IN')
    usernameLabel = tk.Label(tkWindow, text="User Name",font=24).place(x=20,y=7)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username).place(x=120,y=7)  
    passwordLabel = tk.Label(tkWindow,text="Password",font=24).place(x=20,y=40)  
    password = StringVar()
    passwordEntry = tk.Entry(tkWindow, textvariable=password, show='*').place(x=120,y=40)
    validateLogin = partial(validateLogin, username, password)
    loginButton = tk.Button(tkWindow, text="Login",font=24,fg="blue", command=validateLogin).place(x=100,y=82)
    exitButton=tk.Button(tkWindow,text="Exit",font=24,fg="red",command=exitLogin).place(x=210,y=82)
    tkWindow.mainloop()

def register():
    def validateregister(username,name,password,number):
        if (username.get()=="" or name.get()=="" or password.get()=="" or number.get==""):
            MsgBox = messagebox.showerror ('Empty Entry',message="Kindly fill the required details",icon = 'warning')
        else:
            db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
            myc=db.cursor()
            hello1=name.get()
            hello2=username.get()
            hello3=password.get()
            hello4=number.get()
            a=(hello1,hello2,hello3,hello4)
            q=("insert into user_table(name,username,password,number) values (%s,%s,%s,%s) ")
            myc.execute(q,a)
            db.commit()
            MsgBox = messagebox.showinfo ('Welcome',message="REGISTRATION SUCCESSFULL")
            tkWindow.destroy()
            return
    def exitregister( ):
        MsgBox = messagebox.askquestion ('','Are you sure you want to exit the application?',icon = 'warning')
        if MsgBox == 'yes':
            tkWindow.destroy()
        else:
            exit
    tkWindow = Toplevel()  
    tkWindow.geometry('330x230')  
    tkWindow.title('REGISTER')
    usernameLabel = tk.Label(tkWindow, text="User Name",font=24).place(x=20,y=40)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username).place(x=140,y=40)
    nameLabel = tk.Label(tkWindow, text=" Name",font=24).place(x=20,y=7)
    name = StringVar()
    nameEntry = Entry(tkWindow, textvariable=name).place(x=140,y=7)
    numberLabel = tk.Label(tkWindow, text="Phone Number",font=24).place(x=20,y=106)
    number = StringVar()
    numberEntry = Entry(tkWindow, textvariable=number).place(x=140,y=106) 
    passwordLabel = tk.Label(tkWindow,text="Password",font=24).place(x=20,y=73)  
    password = StringVar()
    passwordEntry = tk.Entry(tkWindow, textvariable=password, show='*').place(x=140,y=73)
    registerButton = tk.Button(tkWindow, text="Register",font=24,fg="blue", command=partial(validateregister,username,name,password,number)).place(x=86,y=150)
    exitButton=tk.Button(tkWindow,text="Exit",font=24,fg="red",command=exitregister).place(x=200,y=150)
    tkWindow.mainloop()
    
    
def show_frame(frame):
    frame.tkraise()
def resize_image2(event):
    new_width = event.width
    new_height = event.height
    image1 = copy_of_image2.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image1)
    # label1.config(image=photo)
    label1.image=photo
    print("done")

root = tk.Tk()
root.title("THEATREbook")
root.geometry('800x800')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)
frame5 = tk.Frame(root)
frame6 = tk.Frame(root)
frame7 = tk.Frame(root)
frame8 = tk.Frame(root)
frame9 = tk.Frame(root)
frame10 = tk.Frame(root)
for frame in (frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10):
    frame.grid(row=0, column=0, sticky='nsew')
print("done")
# ==========Frame2=======
copy_of_image2 = Image.open("neww (2).jpg")

photo2=copy_of_image2.resize((800,800),Image.LANCZOS)
image2=ImageTk.PhotoImage(photo2)
# label1= Label(frame2, image=image2).place(relx=0,rely=0)

# copy_of_image10=Image.open("neww (2).jpg")
# photo10=copy_of_image10.resize((800,800),Image.LANCZOS)
# image10=ImageTk.PhotoImage(photo10)
# label10= Label(frame10, image=image10).place(relx=0,rely=0)

label1 = Label(frame2, image=image2)
label1.place(x=0, y=0, relwidth=1, relheight=1)
label1.bind('<Configure>', resize_image2)
label1.image=photo2
delhi_button = Image.open("delhikd.png")
delhi = delhi_button.resize((295, 175), Image.LANCZOS)
delhinew = PhotoImage(delhi)
mumbai_button = Image.open("MUMBAIKD.png")
mumbai = mumbai_button.resize((295, 175), Image.LANCZOS)
mumbainew = ImageTk.PhotoImage(mumbai)
kolkata_button = Image.open("KOLKATAKD.png")
kolkata = kolkata_button.resize((295, 175), Image.LANCZOS)
kolkatanew = ImageTk.PhotoImage(kolkata)
chennai_button = Image.open("CHENNAIKD.png")
chennai = chennai_button.resize((295, 175), Image.LANCZOS)
chennainew = ImageTk.PhotoImage(chennai)
SIGNIN = tk.Button(frame2, text="SIGN IN", font=('Copperplate Gothic Light', 20, 'bold'), bg='goldenrod1', fg="brown4",
                   command=sign_in, relief="raised")
SIGNIN.place(height=50, width=150, relx=0.01, rely=0.01)
REGISTER = tk.Button(frame2, text="REGISTER", font=('Copperplate Gothic Light', 18, 'bold'), bg='goldenrod1',
                     fg="brown4", command=register, relief="raised")
REGISTER.place(height=50, width=150, relx=0.01, rely=0.09)
canvas = Canvas(frame2, height=550, width=770, bg="lightgoldenrod1")
canvas.place(relx=0.02, rely=0.168)
label2 = tk.Label(canvas, text="Select Your Location For Nearby Cinema Halls", font=('vijaya', 30, "bold"),
                  bg='light goldenrod1', fg="saddle brown")
label2.place(relx=0.1, rely=0.05)
back = tk.Button(frame2, text="BACK", font=('Copperplate Gothic Light', 18, 'bold'), bg='goldenrod1', fg="brown4",
                 command=lambda: show_frame(frame1), relief="raised")
back.place(height=75, width=150, relx=0.2, rely=0.877)

def shotc1():
    m1=tk.Label(frame7,text="A fisherman saves Jeetu from committing suicide, only to sell him to\n"
                                                 "a moneylender. Jeetu is then forced to pose as a man with\n"
                                                 "hearing and speech impairment, resulting in hilarious consequences.\n"
                                                "Release date: 9 June 2006 (India)\n"
                                                 "Director: Priyadarshan\n"
                                                 "Box office: 25.5 crores INR\n"
                                                 "Budget: 12 crores INR",height=13,width=50,font=("Arial",10))
    m1.place(relx=0.285,rely=0.4)
    b=tk.Button(m1,text="OK",font=("copperplate gothic light",10),command=lambda:m1.place_forget(),height=2,width=7)
    b.place(relx=0.4,rely=0.77)
def shotc2():
    m1=tk.Label(frame7,text="Dr. John Dolittle lives in solitude behind the high walls of his lush\n"
                                                "manor in 19th-century England. His only companionship comes\n"
                                               "from an array of exotic animals that he speaks to on a daily basis.\n"
                                               "But when young Queen Victoria becomes gravely ill, the eccentric\n"
                                               "doctor and his furry friends embark on an epic adventure to a\n"
                                               "mythical island to find the cure.\n"
                                                "Initial release: January 2020 (Austria)\n"
                                                 "Director: Stephen Gaghan\n"
                                                 "Box office: 24.52 crores USD\n"
                                                 "Budget: 17.5 crores USD",height=17,width=50,font=("Arial",10))
    m1.place(relx=0.4,rely=0.63)
    b=tk.Button(m1,text="OK",font=("copperplate gothic light",10),command=lambda:m1.place_forget(),height=2,width=7)
    b.place(relx=0.4,rely=0.82)
def shotc3():
    m1=tk.Label(frame7,text="Eight-year-old Kevin is accidentally left behind when his family leaves\n"
                                                "for France. At first, he is happy to be in charge, but when thieves try\n"
                                               "to break into his home, he tries to put up a fight.\n"
                                                "Release date: 18 October 1991 (India)\n"
                                                "Director: Chris Columbus\n"
                                               "Featured song: Somewhere in My Memory\n"
                                               "Film series: Home Alone",height=13,width=50,font=("Arial",10))
    m1.place(relx=0.45,rely=0.4)
    b=tk.Button(m1,text="OK",font=("copperplate gothic light",10),command=lambda:m1.place_forget(),height=2,width=7)
    b.place(relx=0.4,rely=0.77)
def shotc4():
    m1=tk.Label(frame7,text="The lives of Raju, Shyam and Baburao change completely when\n"
                                               "they get cheated by a fraudster. Now, they must find another way\n"
                                                "to repay the loan they took from a dreaded gangster.\n"
                                                "Release date: 9 June 2006 (India)\n"
                                                "Director: Neeraj Vora\n"
                                                "Box office: 69.12 crores INR",height=11,width=50,font=("Arial",10))
    m1.place(relx=0.4,rely=0.72)
    b=tk.Button(m1,text="OK",font=("copperplate gothic light",10),command=lambda:m1.place_forget(),height=2,width=7)
    b.place(relx=0.4,rely=0.77)    
def shots1():
    m1=tk.Label(frame6,text="After facing criticism from his son and employer, Shekhar, a gaming\n"
                                                 "programmer, creates an invincible virtual character called Ra.One.\n"
                                                 "Soon Ra.One enters the real world and kills Shekhar.\n"
                                                  "Release date: 26 October 2011 (India)\n"
                                                  "Director: Anubhav Sinha\n"
                                                  "Box office: 207 crores INR\n"
                                                  "Budget: 130 crores INR (2010)",height=13,width=50,font=("Arial",10))
    m1.place(relx=0.285,rely=0.4)
    b=tk.Button(m1,text="OK",font=("copperplate gothic light",10),command=lambda:m1.place_forget(),height=2,width=7)
    b.place(relx=0.4,rely=0.77)
def shots4():
    m1=tk.Label(frame6,text="Cobb steals information from his targets by entering their dreams.\n"
                                                "Saito offers to wipe clean Cobb's criminal history as payment for\n"
                                                 "performing an inception on his sick competitor's son.\n"
                                                 "Release date: 16 July 2010 (India)\n"
                                                 "Director: Christopher Nolan\n"
                                                 "Featured song: Non, je ne regrette rien\n"
                                                 "Box office: 83.68 crores USD",height=13,width=50,font=("Arial",10))
    m1.place(relx=0.285,rely=0.72)
    b=tk.Button(m1,text="OK",font=("copperplate gothic light",10),command=lambda:m1.place_forget(),height=2,width=7)
    b.place(relx=0.4,rely=0.78)
def shots3():
    m1=tk.Label(frame6,text="In the future, where Earth is becoming uninhabitable, farmer and\n"
                                               "ex-NASA pilot Cooper is asked to pilot a spacecraft along with a\n"
                                                "team of researchers to find a new planet for humans.\n"
                                                "Release date: 7 November 2014 (India)\n"
                                                "Director: Christopher Nolan\n"
                                                "Featured song: S.T.A.Y.\n"
                                                "Box office: 69.63 crores USD",height=13,width=50,font=("Arial",10))
    m1.place(relx=0.4,rely=0.63)
    b=tk.Button(m1,text="OK",font=("copperplate gothic light",10),command=lambda:m1.place_forget(),height=2,width=7)
    b.place(relx=0.4,rely=0.785)
def shots2():
    m1=tk.Label(frame6,text="A group of scientists at ISRO battle in their personal and professional\n"
                                                "lives and work tirelessly towards their only motive, the Mars Orbiter\n"
                                                 "Mission.\n"
                                                "Initial release: 15 August 2019 (Germany)\n"
                                                "Director: Jagan Shakti\n"
                                                "Producer: Akshay Kumar\n"
                                                "Budget: 32 crores INR (2019)",height=13,width=50,font=("Arial",10))
    m1.place(relx=0.285,rely=0.72)
    b=tk.Button(m1,text="OK",font=("copperplate gothic light",10),command=lambda:m1.place_forget(),height=2,width=7)
    b.place(relx=0.4,rely=0.79)
def shoth1():
    m1=tk.Label(frame5,text="An NRI and his wife decide to stay in his ancestral home, paying no\n"
                                                "heed to the warnings about ghosts. Soon, inexplicable occurrences\n"
                                                "cause him to call a psychiatrist to help solve the mystery.\n"
                                                " Release date: 12 October 2007 (India)\n"
                                                "Director: Priyadarshan\n"
                                                "Film series: Bhool Bhulaiyaa\n"
                                                "Music director: Pritam Chakraborty, Ranjit Barot\n",height=11,width=50,font=("Arial",10))
    m1.place(relx=0.285,rely=0.4)
    b=tk.Button(m1,text="OK",font=("copperplate gothic light",10),command=lambda:m1.place_forget(),height=2,width=7)
    b.place(relx=0.4,rely=0.77)
def shoth4():
    m1=tk.Label(frame5,text="The Perron family moves into a farmhouse where they experience\n"
                                                 "paranormal phenomena. They consult demonologists, Ed and Lorraine\n"
                                                 "Warren, to help them get rid of the evil entity haunting them.\n"
                                                 "Release date: 2 August 2013 (India)\n"
                                                 "Director: James Wan\n"
                                                 "Film series: The Conjuring\n"
                                                 "Box office: 31.95 crores USD",height=13,width=50,font=("Arial",10))
    m1.place(relx=0.4,rely=0.72)
    b=tk.Button(m1,text="OK",font=("copperplate gothic light",10),command=lambda:m1.place_forget(),height=2,width=7)
    b.place(relx=0.4,rely=0.785)
def shoth3():
    m1=tk.Label(frame5,text="Seven helpless and bullied children are forced to face their worst\n"
                                                "nightmares when Pennywise, a shape-shifting clown, reappears. The\n"
                                                "clown, an ancient evil torments children before feeding on them.\n"
                                                "Release date: 8 September 2017 (India)\n"
                                                "Director: Andrés Muschietti\n"
                                                "Film series: It\n"
                                                "Box office: 70.18 crores USD",height=13,width=50,font=("Arial",10))
    m1.place(relx=0.4,rely=0.4)
    b=tk.Button(m1,text="OK",font=("copperplate gothic light",10),command=lambda:m1.place_forget(),height=2,width=7)
    b.place(relx=0.4,rely=0.79)
def shoth2():
    m1=tk.Label(frame5,text="The people of Chanderi live under constant fear of Stree, the spirit\n"
                                                "of a woman who attacks men at night during festivals. Vicky,\n"
                                               "along with his friends, decides to unravel the mystery.\n"
                                                "Release date: 31 August 2018 (India)\n"
                                                "Director: Amar Kaushik\n"
                                                "Budget: 25 crores INR (2017)\n",height=11,width=50,font=("Arial",10))
    m1.place(relx=0.285,rely=0.72)
    b=tk.Button(m1,text="OK",font=("copperplate gothic light",10),command=lambda:m1.place_forget(),height=2,width=7)
    b.place(relx=0.4,rely=0.77)
def shot2():
    m1=tk.Label(frame4,text="RAW Agent Tiger joins forces with Zoya in order to rescue a group\n"
                                                "of nurses who are held hostage by a terrorist organisation.\n"
                                                "Release date: 22 December 2017 (India)\n"
                                                "Director: Ali Abbas Zafar\n"
                                                "Budget: 210 crores INR",height=11,width=50,font=("Arial",10))
    m1.place(relx=0.285,rely=0.72)
    b=tk.Button(m1,text="OK",font=("copperplate gothic light",10),command=lambda:m1.place_forget(),height=2,width=7)
    b.place(relx=0.4,rely=0.77)
def shot3():
    m1=tk.Label(frame4,text="Sunny, a psychopath working for a politician, brutally rapes and\n"
                                                 "murders innocent women, leaving a trail of battered bodies in his\n"
                                                 "wake. However, SP Shivani Roy vows to catch and bring him to\n"
                                                 "justice.\n"
                                                 "Release date: 13 December 2019 (India)\n"
                                                 "Director: Gopi Puthran\n"
                                                 "Box office: 67.12 crores INR\n"
                                                 "Budget: 20 crores INR",height=14,width=50,font=("Arial",10))
    m1.place(relx=0.45,rely=0.4)
    b=tk.Button(m1,text="OK",font=("copperplate gothic light",10),command=lambda:m1.place_forget(),height=2,width=7)
    b.place(relx=0.4,rely=0.8)
def shot4():
    m1=tk.Label(frame4,text="After Thanos, an intergalactic warlord, disintegrates half of the\n"
                                                "universe, the Avengers must reunite and assemble again to \n"
                                                "reinvigorate their trounced allies and restore balance.\n"
                                                "Release date: 26 April 2019 (India)\n"
                                                "Directors: Joe Russo, Anthony Russo\n"
                                                "Box office: 279.8 crores USD\n"
                                                "Budget: 35.6 crores USD (2019)\n"
                                                "Awards: MTV Movie Award for Best Villain, MORE",height=13,width=50,font=("Arial",10))
    m1.place(relx=0.4,rely=0.72)
    b=tk.Button(m1,text="OK",font=("copperplate gothic light",10),command=lambda:m1.place_forget(),height=2,width=7)
    b.place(relx=0.4,rely=0.79)
def shot1():
    m1=tk.Label(frame4,text="After Gordon, Dent and Batman begin an assault on Gotham's\n"
                                                 "organised crime,the mobs hire the Joker, a psychopathic criminal\n"
                                                 "mastermind who offers to kill Batman and bring the city to its knees.\n"
                                                 "Release date: 18 July 2008 (India)\n"
                                                 "Director: Christopher Nolan\n"
                                                 "Box office: 100.5 crores USD\n"
                                                 "Awards: Academy Award for Best Supporting Actor, MORE ",height=14,width=50,font=("Arial",10))
    m1.place(relx=0.3,rely=0.4)
    b=tk.Button(m1,text="OK",font=("copperplate gothic light",10),command=lambda:m1.place_forget(),height=2,width=7)
    b.place(relx=0.4,rely=0.78)

    

#==========Frame2=======
copy_of_image2 = Image.open("bluee (2).jpg")
photo2 = ImageTk.PhotoImage(copy_of_image2)
label1= Label(frame2, image=photo2)
label1.place(x=0, y=0, relwidth=1, relheight=1)
label1.bind('<Configure>', resize_image2)
delhi_button=Image.open("delhikd.png")
delhi= delhi_button.resize((295, 175), Image.LANCZOS)
delhinew=ImageTk.PhotoImage(delhi)
mumbai_button=Image.open("MUMBAIKD.png")
mumbai= mumbai_button.resize((295, 175), Image.LANCZOS)
mumbainew=ImageTk.PhotoImage(mumbai)
kolkata_button=Image.open("KOLKATAKD.png")
kolkata= kolkata_button.resize((295, 175), Image.LANCZOS)
kolkatanew=ImageTk.PhotoImage(kolkata)
chennai_button=Image.open("CHENNAIKD.png")
chennai= chennai_button.resize((295, 175), Image.LANCZOS)
chennainew=ImageTk.PhotoImage(chennai)
SIGNIN=tk.Button(frame2,text="SIGN IN" ,font=('Copperplate Gothic Light',20,'bold'),bg='goldenrod1',fg="brown4",command=sign_in,relief="raised")
SIGNIN.place(height=50,width=150,relx=0.01,rely=0.01)
REGISTER=tk.Button(frame2,text="REGISTER" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=register,relief="raised")
REGISTER.place(height=50,width=150,relx=0.01,rely=0.09)
canvas=Canvas(frame2, height=550, width=770,bg="lightgoldenrod1")
canvas.place(relx=0.02, rely=0.168)
label2=tk.Label(canvas,text="Select Your Location For Nearby Cinema Halls",font=('vijaya',30,"bold"),bg='light goldenrod1',fg="saddle brown")
label2.place(relx=0.1,rely=0.05)
back=tk.Button(frame2,text="BACK" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame1),relief="raised")
back.place(height=75,width=150,relx=0.2,rely=0.877)
def new(hellon):
    global c
    c=hellon
def selection():
    selection=str(var.get())
    global hellon
    if selection=="delhi":
        NEXT3=tk.Button(frame2,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame3),relief="raised")
        NEXT3.place(height=75,width=150,relx=0.6,rely=0.877)
        label=tk.Label(frame8,text="Choose your nearby movie hall",bg="white",fg="navyblue",font=("baskerville old face",24),width=22)
        label.place(relx=0.1,rely=0.2)
        def on_selection(event):
            hello=listbox.get(listbox.curselection())
            labelb=tk.Label(frame10,width=60,bg="white",height=2).place(relx=0.42,rely=0.43)
            label=tk.Label(frame10,text=hello,font=("Calibri (Body)",16),bg="white").place(relx=0.42,rely=0.43)
            def get():
                new=str(spinbox.get())
                if new=="1":
                    label=tk.Label(frame10,text="1 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    labelja=tk.Label(frame10,text="Rs. 150",font=("Calibri (Body)",18,"bold"),bg="white")
                    labelja.place(relx=0.5,rely=0.47)
                    hellon=labelja.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="2":
                    label=tk.Label(frame10,text="2 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    labelja=tk.Label(frame10,text="Rs. 300",font=("Calibri (Body)",18,"bold"),bg="white")
                    labelja.place(relx=0.5,rely=0.47)
                    hellon=labelja.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="3":
                    label=tk.Label(frame10,text="3 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    labelja=tk.Label(frame10,text="Rs. 450",font=("Calibri (Body)",18,"bold"),bg="white")
                    labelja.place(relx=0.5,rely=0.47)
                    hellon=labelja.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="4":
                    label=tk.Label(frame10,text="4 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    labelja=tk.Label(frame10,text="Rs. 600",font=("Calibri (Body)",18,"bold"),bg="white")
                    labelja.place(relx=0.5,rely=0.47)
                    hellon=labelja.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="5":
                    label=tk.Label(frame10,text="5 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    labelja=tk.Label(frame10,text="Rs. 750",font=("Calibri (Body)",18,"bold"),bg="white")
                    labelja.place(relx=0.5,rely=0.47)
                    hellon=labelja.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="6":
                    label=tk.Label(frame10,text="6 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    labelja=tk.Label(frame10,text="Rs. 900",font=("Calibri (Body)",18,"bold"),bg="white")
                    labelja.place(relx=0.5,rely=0.47)
                    hellon=labelja.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="7":
                    label=tk.Label(frame10,text="7 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    labelja=tk.Label(frame10,text="Rs. 1050",font=("Calibri (Body)",18,"bold"),bg="white")
                    labelja.place(relx=0.5,rely=0.47)
                    hellon=labelja.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="8":
                    label=tk.Label(frame10,text="8 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    labelja=tk.Label(frame10,text="Rs. 1200",font=("Calibri (Body)",18,"bold"),bg="white")
                    labelja.place(relx=0.5,rely=0.47)
                    hellon=labelja.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                else:
                    pass
            spinvar=IntVar()
            spinvar.set("1")
            spinbox=tk.Spinbox(frame8,from_=0,to=8,font=18,command=get)
            spinbox.place(relx=0.68,rely=0.51)
        listbox=tk.Listbox(frame8,height=19,width=44,font=("baskerville old face",14))
        listbox.insert(1,"INOX : EP3 Mall (Faridabad)")
        listbox.insert(2,"PVR : ECX (Chanakyapuri)")
        listbox.insert(3,"Miraj Chaudhary Cinemas (Ghaziabad)")
        listbox.insert(4,"MSX Silvercity , Haldiram Citymall (Faridabad)")
        listbox.insert(6,"PVR : Ambience(Gold) (Gurgaon)")
        listbox.insert(7,"Abhishek Cineplex (Chandni Chowk)")
        listbox.insert(8,"Amba Cinema (Delhi)")
        listbox.insert(9,"G3S Cinema (Rohini)")
        listbox.insert(10,"Fun Cinemas : TDI Mall (Moti Nagar)")
        listbox.insert(11,"M2K (Pitampura)")
        listbox.insert(12,"Movietime (Raja Garden)")
        listbox.insert(13,"Miraj Cinemas (Subhash Nagar)")
        listbox.insert(14,"PVR (Naraina)")
        listbox.insert(15,"PVR Plaza (Cannouht Place")
        listbox.insert(16,"WAVE Cinemas (Raja Garden)")
        listbox.insert(17,"PVR (Vikaspuri)")
        listbox.insert(18,"PVR Select City Walk(Gold) (Delhi)")
        listbox.insert(19,"M Cinemas (East of Kailash)")
        listbox.insert(20,"INOX (Nehru Place)")
        listbox.place(relx=0.1,rely=0.257)
        listbox.bind('<<ListboxSelect>>',on_selection)
        label2=tk.Label(frame8,text="Number of tickets",bg="white",fg="navyblue",font=("baskerville old face",24))
        label2.place(relx=0.66,rely=0.43)
    elif selection=="mumbai":
        NEXT3=tk.Button(frame2,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame3),relief="raised")
        NEXT3.place(height=75,width=150,relx=0.6,rely=0.877)
        label=tk.Label(frame8,text="Choose your nearby movie hall",bg="white",fg="navyblue",font=("baskerville old face",24),width=22)
        label.place(relx=0.1,rely=0.2)
        print(label.winfo_width())
        def on_selection(event):
            hello=listbox.get(listbox.curselection())
            labelb=tk.Label(frame10,width=60,bg="white",height=2).place(relx=0.42,rely=0.43)
            label=tk.Label(frame10,text=hello,font=("Calibri (Body)",16),bg="white").place(relx=0.42,rely=0.43)
            def get():
                new=str(spinbox.get())
                if new=="1":
                    label=tk.Label(frame10,text="1 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 150",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="2":
                    label=tk.Label(frame10,text="2 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 300",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="3":
                    label=tk.Label(frame10,text="3 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 450",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="4":
                    label=tk.Label(frame10,text="4 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 600",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="5":
                    label=tk.Label(frame10,text="5 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 750",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47) 
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="6":
                    label=tk.Label(frame10,text="6 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 900",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="7":
                    label=tk.Label(frame10,text="7 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 1050",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47) 
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="8":
                    label=tk.Label(frame10,text="8 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 1200",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
            spinvar=IntVar()
            spinvar.set("1")
            spinbox=tk.Spinbox(frame8,from_=0,to=8,font=18,command=get)
            spinbox.place(relx=0.68,rely=0.51)
        listbox=tk.Listbox(frame8,height=19,width=44,font=("baskerville old face",14))
        listbox.insert(1,"PVR Cinemax : Eternity Mall (Thane)")
        listbox.insert(2,"Carnival Cinemas : IMAX (Wadala)")
        listbox.insert(3,"Miraj Cinemas (Ulhasnagar)")
        listbox.insert(4,"Cinepolis : Fun Republic Mall ( Andheri(W) )")
        listbox.insert(6,"INOX : Nakshatra Mall ( Dadar(W) )")
        listbox.insert(7,"24 Karat (Jogeshwari)")
        listbox.insert(8,"Balaji Movieplex (Kopar Khairane)")
        listbox.insert(9,"Carnival : Huma (Kanjurmarg)")
        listbox.insert(10,"Cinemax : Infiniti Mall ( Malad(W) )")
        listbox.insert(11,"Gold Cinema ( Dadar(E) )")
        listbox.insert(12,"Citylight Cinema (Mahim)")
        listbox.insert(13,"Gold Cinema : ( Santacruz(W) )")
        listbox.insert(14,"G7 Multiplex ( Bandra(W) )")
        listbox.insert(15,"Maxus Cinemas ( Borivali(W) )")
        listbox.insert(16,"Metro INOX Cinemas (Marine Lines)")
        listbox.insert(17,"INOX Atria Mall (Worli)")
        listbox.insert(18,"Movietime Cubic Mall (Chembur)")
        listbox.insert(19,"Mukta A2 Cinemas (Lalbaugh)")
        listbox.insert(20,"Tilak Cineplex (Dombivali)")
        listbox.place(relx=0.1,rely=0.257)
        listbox.bind('<<ListboxSelect>>',on_selection)    
        label2=tk.Label(frame8,text="Number of tickets",bg="white",fg="navyblue",font=("baskerville old face",24))
        label2.place(relx=0.66,rely=0.43)
    elif selection=="kolkata":
        NEXT3=tk.Button(frame2,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame3),relief="raised")
        NEXT3.place(height=75,width=150,relx=0.6,rely=0.877)
        label=tk.Label(frame8,text="Choose your nearby movie hall",bg="white",fg="navyblue",font=("baskerville old face",24),width=22)
        label.place(relx=0.1,rely=0.2)
        print(label.winfo_width())
        def on_selection(event):
            hello=listbox.get(listbox.curselection())
            labelb=tk.Label(frame10,width=60,bg="white",height=2).place(relx=0.42,rely=0.43)
            label=tk.Label(frame10,text=hello,font=("Calibri (Body)",16),bg="white").place(relx=0.42,rely=0.43)
            def get():
                new=str(spinbox.get())
                if new=="1":
                    label=tk.Label(frame10,text="1 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 150",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="2":
                    label=tk.Label(frame10,text="2 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 300",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="3":
                    label=tk.Label(frame10,text="3 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 450",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="4":
                    label=tk.Label(frame10,text="4 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 600",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="5":
                    label=tk.Label(frame10,text="5 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 750",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="6":
                    label=tk.Label(frame10,text="6 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 900",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=lab.el2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="7":
                    label=tk.Label(frame10,text="7 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 1050",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="8":
                    label=tk.Label(frame10,text="8 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 1200",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
            spinbox=tk.Spinbox(frame8,from_=0,to=8,font=18,command=get)
            spinbox.place(relx=0.68,rely=0.51)
        listbox=tk.Listbox(frame8,height=19,width=44,font=("baskerville old face",14))
        listbox.insert(1,"Bioscope : Axis Mall (Rajarhat)")
        listbox.insert(2,"Carnival : Arti Suncity Mall (Barasat)")
        listbox.insert(3,"INOX : Star Mall (Madhyamgram)")
        listbox.insert(4,"Jayanti Cinemas : City Mall (Barackpore)")
        listbox.insert(6,"Jaya Cinemas , City Mall (Barasat)")
        listbox.insert(7,"Asoka Cinema (Behala)")
        listbox.insert(8,"Atindra Cinema (Kolkata)")
        listbox.insert(9,"Besusree Cinema (Kolkata)")
        listbox.insert(10,"Navina Cinema : (Tollygunge)")
        listbox.insert(11,"New Empire Cinema (Kolkata)")
        listbox.insert(12,"Rupmandir Cinema (Belgharia)")
        listbox.insert(13,"Sonali Cinema (Dunlop)")
        listbox.insert(14,"PVR Diamond Plaza (Jessore)")
        listbox.insert(15,"Lila Cinema (Baruipur)")
        listbox.insert(16,"Jaya Cinema (Lake Town)")
        listbox.insert(17,"SVF Cinemas (Narendrapur)")
        listbox.insert(18,"Star Theatre (Kolkata)")
        listbox.insert(19,"RDB Cinemas Salt Lake (Kolkata)")
        listbox.insert(20,"Rathindra Cine II (Kolkata)")
        listbox.place(relx=0.1,rely=0.257)
        listbox.bind('<<ListboxSelect>>',on_selection) 
        label2=tk.Label(frame8,text="Number of tickets",bg="white",fg="navyblue",font=("baskerville old face",24))
        label2.place(relx=0.66,rely=0.43)
    elif selection=="chennai":
        NEXT3=tk.Button(frame2,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame3),relief="raised")
        NEXT3.place(height=75,width=150,relx=0.6,rely=0.877)
        label=tk.Label(frame8,text="Choose your nearby movie hall",bg="white",fg="navyblue",font=("baskerville old face",24),width=22)
        label.place(relx=0.1,rely=0.2)
        print(label.winfo_width())
        def on_selection(event):
            hello=listbox.get(listbox.curselection())
            labelb=tk.Label(frame10,width=60,bg="white",height=2).place(relx=0.42,rely=0.43)
            label=tk.Label(frame10,text=hello,font=("Calibri (Body)",16),bg="white").place(relx=0.42,rely=0.43)
            def get():
                new=str(spinbox.get())
                if new=="1":
                    label=tk.Label(frame10,text="1 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 150",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="2":
                    label=tk.Label(frame10,text="2 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 300",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="3":
                    label=tk.Label(frame10,text="3 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 450",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="4":
                    label=tk.Label(frame10,text="4 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 600",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="5":
                    label=tk.Label(frame10,text="5 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 750",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="6":
                    label=tk.Label(frame10,text="6 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 900",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="7":
                    label=tk.Label(frame10,text="7 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 1050",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
                elif new=="8":
                    label=tk.Label(frame10,text="8 x seats",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.47)
                    label2=tk.Label(frame10,text="Rs. 1200",font=("Calibri (Body)",18,"bold"),bg="white")
                    label2.place(relx=0.5,rely=0.47)
                    hellon=label2.cget("text")
                    db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
                    myc=db.cursor()
                    hello1=hellon
                    a=(hello1,)
                    q=("insert into vabi(cost) values (%s) ")
                    myc.execute(q,a)
                    db.commit()
                    NEXT8=tk.Button(frame8,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame10),relief="raised")
                    NEXT8.place(height=75,width=150,relx=0.81,rely=0.9)
            spinbox=tk.Spinbox(frame8,from_=0,to=8,font=18,command=get)
            spinbox.place(relx=0.68,rely=0.51)
        listbox=tk.Listbox(frame8,height=19,width=44,font=("baskerville old face",14))
        listbox.insert(1,"Cinepolis , BSR Mall (Thoraipakkam)")
        listbox.insert(2,"BG Parimalam Cinemas (Kundrathur)")
        listbox.insert(3,"Kumaran Theatre  (Madipakkam)")
        listbox.insert(4,"PVR , Ampa Mall (Manickam Road)")
        listbox.insert(6,"AGS Cinemas OMR (Navlur)")
        listbox.insert(7,"GK Cinemas RGB (Porur)")
        listbox.insert(8,"Janatha Theatre 2K AC DTS (Pallavaram)")
        listbox.insert(9,"KK Cinemas 4K Dolby (Minjur)")
        listbox.insert(10,"Jothi Theatre 4K (Thomas Mount)")
        listbox.insert(11,"Kumaran Theatre (Madipakkam)")
        listbox.insert(12,"Carnival Cinemas EVP (Chennai)")
        listbox.insert(13,"Luxe Cinemas (Chennai)")
        listbox.insert(14,"Meenakshi Theatre 2K AC (Manali)")
        listbox.insert(15,"Odeon Mani Theatre (Tiruvottiyur)")
        listbox.insert(16,"Maliga Theatre (Mangadu)")
        listbox.insert(17,"MAYAJAAL Multiplex ECR (Chennai)")
        listbox.insert(18,"National Theatre 4K Dolby (Tambaram)")
        listbox.insert(19,"PVR Grand Galada (Pallavaram)")
        listbox.insert(20,"Rohini Silver Screens (Koyambedu)")
        listbox.place(relx=0.1,rely=0.257)
        listbox.bind('<<ListboxSelect>>',on_selection)       
        label2=tk.Label(frame8,text="Number of tickets",bg="white",fg="navyblue",font=("baskerville old face",24))
        label2.place(relx=0.66,rely=0.43)
var=StringVar()
radio_1=tk.Radiobutton(canvas,value="delhi",variable=var,image=delhinew,bg="goldenrod",command=selection)
radio_1.place(relx=0.03,rely=0.2)
radio_2=tk.Radiobutton(canvas,variable=var,value="mumbai",image=mumbainew,bg="goldenrod",command=selection)
radio_2.place(relx=0.513,rely=0.2)
radio_3=tk.Radiobutton(canvas,variable=var,value="chennai",image=chennainew,bg="goldenrod",command=selection)
radio_3.place(relx=0.03,rely=0.565)
radio_4=tk.Radiobutton(canvas,variable=var,value="kolkata",image=kolkatanew,bg="goldenrod",command=selection)
radio_4.place(relx=0.513,rely=0.565)
selection=str(var.get())
#============frame10=======
copy_of_image10=Image.open("neww (2).jpg")
photo10=copy_of_image10.resize((800,800),Image.LANCZOS)
image10=ImageTk.PhotoImage(photo10)
label10= Label(frame10, image=image10).place(relx=0,rely=0)
def destroy():
    root.destroy()
Back10=tk.Button(frame10,text="BACK",font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg='brown4',command=lambda:show_frame(frame8))
Back10.place(height=50,width=100,relx=0.01,rely=0.009)
exitt=tk.Button(frame10,text="EXIT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=destroy,relief="raised")
exitt.place(height=50,width=100,relx=0.01,rely=0.075)
label911=tk.Label(frame10,height=11,width=108,bg="white")
label911.place(relx=0.025,rely=0.167)
labeln=tk.Label(frame10,height=29,width=108,bg="white")
labeln.place(relx=0.025,rely=0.415)
ap=Image.open("logo.png")
ap9=ap.resize((135,150),Image.LANCZOS)
imageap=ImageTk.PhotoImage(ap9)
cc=Image.open("CREDIT.jpg")
cc9=cc.resize((200,150),Image.LANCZOS)
imagecc=ImageTk.PhotoImage(cc9)
dc=Image.open("DEBIT.jpg")
dc9=dc.resize((200,150),Image.LANCZOS)
imagedc=ImageTk.PhotoImage(dc9)
def show():
    labelnewla=tk.Label(frame10,height=15,width=75,bg="light grey")
    labelnewla.place(relx=0.2,rely=0.27)
    offer=tk.Label(labelnewla,bg="light grey",text="OFFERS",fg="navyblue",font=("Calibri Body",21,"bold")).place(relx=0.4,rely=0.02)
    ap=tk.Label(labelnewla,bg="light grey",text="Amazon Pay",fg="orange red",font=("Calibri Body",17)).place(relx=0.07,rely=0.17)
    cc=tk.Label(labelnewla,bg="light grey",text="Credit Card",fg="darkorchid4",font=("Calibri Body",17)).place(relx=0.07,rely=0.3)
    dc=tk.Label(labelnewla,bg="light grey",text="Debit Card",fg="navy",font=("Calibri Body",17)).place(relx=0.07,rely=0.43)
    ap1=tk.Label(labelnewla,bg="light grey",text="15% Discount on total price",fg="black",font=("Calibri Body",17)).place(relx=0.35,rely=0.17)
    ap2=tk.Label(labelnewla,bg="light grey",text="No offer this season",fg="black",font=("Calibri Body",17)).place(relx=0.35,rely=0.3)
    ap3=tk.Label(labelnewla,bg="light grey",text="20% Discount on ticket price",fg="black",font=("Calibri Body",17)).place(relx=0.35,rely=0.43)   
    b=tk.Button(labelnewla,text="OK",font=("copperplate gothic light",10),command=lambda:labelnewla.place_forget(),height=2,width=7)
    b.place(relx=0.45,rely=0.79)
def selectionNEW2():
    if str(var11.get())=="1":
        l=tk.Label(frame10,text="Via Amazon Pay : 15% discount on total price",font=("Calibri (Body)",18),bg="white").place(relx=0.03,rely=0.54)
        db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
        myc=db.cursor()
        myc.execute("select cost from vabi ORDER BY id DESC LIMIT 1")
        resc=myc.fetchall( )
        for i in resc:
            for j in i:
                s=j[3: ]
                si=int(s)
                newint=si*0.15
                C=(si-newint)
                def pay():
                        messagebox.showinfo ('Payment',message="PAYMENT SUCCESSFUL")
                strsi="Rs. "
                l1=tk.Label(frame10,text="Discount Offered",bg="white",font=("Calibri (Body)",18),relief="solid",width=24).place(relx=0.03,rely=0.66)
                l4=tk.Label(frame10,text=newint,bg="white",font=("Calibri (Body)",18),relief="solid",width=10).place(relx=0.55,rely=0.66)
                l2=tk.Label(frame10,text="Amount before discount",bg="white",font=("Calibri (Body)",18),relief="solid",width=24).place(relx=0.03,rely=0.6)
                l3=tk.Label(frame10,text=si,bg="white",font=("Calibri (Body)",18),relief="solid",width=10).place(relx=0.55,rely=0.6)
                l5=tk.Label(frame10,text="AMOUNT TO BE PAID ",bg="white",fg="RED",font=("Calibri (Body)",18),width=24,relief="solid").place(relx=0.03,rely=0.72)
                l6=tk.Label(frame10,text=C,bg="white",font=("Calibri (Body)",18),fg="blue",relief="solid",width=10).place(relx=0.55,rely=0.72)
                lr1=tk.Label(l4,text="Rs.",bg="white",font=("Calibri (Body)",15)).place(relx=0.572,rely=0.603)
                lr2=tk.Label(l4,text="Rs.",bg="white",font=("Calibri (Body)",15)).place(relx=0.563,rely=0.663)
                lr3=tk.Label(l4,text="Rs.",bg="white",fg="blue",font=("Calibri (Body)",15)).place(relx=0.56,rely=0.723)
                pay=tk.Button(frame10,text="PAY",font=('Copperplate Gothic Light',18,'bold'),bg='white',fg="blue",command=pay,relief="raised")
                pay.place(height=75,width=150,relx=0.425,rely=0.795)
    elif str(var11.get())=="2":
        l1=tk.Label(frame10,width=36,font=("Calibri (Body)",18),bg="white").place(relx=0.03,rely=0.54)
        l=tk.Label(frame10,text="Via Credit Card :  No Offer this season ",font=("Calibri (Body)",18),bg="white").place(relx=0.03,rely=0.54)
        db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
        myc=db.cursor()
        myc.execute("select cost from vabi ORDER BY id DESC LIMIT 1")
        resc=myc.fetchall( )
        for i in resc:
            for j in i:
                s=j[3: ]
                si=int(s)
                newint=0
                C=(si-newint)
                def pay():
                        messagebox.showinfo ('Payment',message="PAYMENT SUCCESSFUL")
                strsi="Rs. "
                l1=tk.Label(frame10,text="Discount Offered",bg="white",font=("Calibri (Body)",18),relief="solid",width=24).place(relx=0.03,rely=0.66)
                l4=tk.Label(frame10,text=newint,bg="white",font=("Calibri (Body)",18),relief="solid",width=10).place(relx=0.55,rely=0.66)
                l2=tk.Label(frame10,text="Amount before discount",bg="white",font=("Calibri (Body)",18),relief="solid",width=24).place(relx=0.03,rely=0.6)
                l3=tk.Label(frame10,text=si,bg="white",font=("Calibri (Body)",18),relief="solid",width=10).place(relx=0.55,rely=0.6)
                l5=tk.Label(frame10,text="AMOUNT TO BE PAID ",bg="white",fg="RED",font=("Calibri (Body)",18),width=24,relief="solid").place(relx=0.03,rely=0.72)
                l6=tk.Label(frame10,text=C,bg="white",font=("Calibri (Body)",18),fg="blue",relief="solid",width=10).place(relx=0.55,rely=0.72)
                lr1=tk.Label(l4,text="Rs.",bg="white",font=("Calibri (Body)",15)).place(relx=0.572,rely=0.603)
                lr2=tk.Label(l4,text="Rs.",bg="white",font=("Calibri (Body)",15)).place(relx=0.563,rely=0.663)
                lr3=tk.Label(l4,text="Rs.",bg="white",fg="blue",font=("Calibri (Body)",15)).place(relx=0.56,rely=0.723)
                pay=tk.Button(frame10,text="PAY",font=('Copperplate Gothic Light',18,'bold'),bg='white',fg="blue",command=pay,relief="raised")
                pay.place(height=75,width=150,relx=0.425,rely=0.795)
    elif str(var11.get())=="3":
        l=tk.Label(frame10,text="Via Debit Card :  20% discount on ticket price ",font=("Calibri (Body)",18),bg="white").place(relx=0.03,rely=0.54)
        db=mysqlob.connect(host="localhost",user="root",passwd="hello@123",database="movie_booking")
        myc=db.cursor()
        myc.execute("select cost from vabi ORDER BY id DESC LIMIT 1")
        resc=myc.fetchall( )
        for i in resc:
            for j in i:
                s=j[3: ]
                si=int(s)
                newint=si*0.2
                C=(si-newint)
                def pay():
                        messagebox.showinfo ('Payment',message="PAYMENT SUCCESSFUL")
                strsi="Rs. "
                l1=tk.Label(frame10,text="Discount Offered",bg="white",font=("Calibri (Body)",18),relief="solid",width=24).place(relx=0.03,rely=0.66)
                l4=tk.Label(frame10,text=newint,bg="white",font=("Calibri (Body)",18),relief="solid",width=10).place(relx=0.55,rely=0.66)
                l2=tk.Label(frame10,text="Amount before discount",bg="white",font=("Calibri (Body)",18),relief="solid",width=24).place(relx=0.03,rely=0.6)
                l3=tk.Label(frame10,text=si,bg="white",font=("Calibri (Body)",18),relief="solid",width=10).place(relx=0.55,rely=0.6)
                l5=tk.Label(frame10,text="AMOUNT TO BE PAID ",bg="white",fg="RED",font=("Calibri (Body)",18),width=24,relief="solid").place(relx=0.03,rely=0.72)
                l6=tk.Label(frame10,text=C,bg="white",font=("Calibri (Body)",18),fg="blue",relief="solid",width=10).place(relx=0.55,rely=0.72)
                lr1=tk.Label(l4,text="Rs.",bg="white",font=("Calibri (Body)",15)).place(relx=0.572,rely=0.603)
                lr2=tk.Label(l4,text="Rs.",bg="white",font=("Calibri (Body)",15)).place(relx=0.563,rely=0.663)
                lr3=tk.Label(l4,text="Rs.",bg="white",fg="blue",font=("Calibri (Body)",15)).place(relx=0.56,rely=0.723)
                pay=tk.Button(frame10,text="PAY",font=('Copperplate Gothic Light',18,'bold'),bg='white',fg="blue",command=pay,relief="raised")
                pay.place(height=75,width=150,relx=0.425,rely=0.795)
var11=IntVar()
radio_ap=tk.Radiobutton(label911,value=1,variable=var11,image=imageap,bg="white",command=selectionNEW2)
radio_ap.place(relx=0.0261,rely=0.02)
radio_credit=tk.Radiobutton(label911,variable=var11,value=2,image=imagecc,bg="white",command=selectionNEW2)
radio_credit.place(relx=0.245,rely=0.02)
radio_debit=tk.Radiobutton(label911,variable=var11,value=3,image=imagedc,bg="white",command=selectionNEW2)
radio_debit.place(relx=0.54,rely=0.02)
offer=tk.Button(label911,width=8,fg="navyblue",bg="white",font=("Algerian",16),text="OFFERS",command=show).place(relx=0.85,rely=0.367)
#============frame5========
copy_of_image5=Image.open("movie (6).jpg")
photo5=copy_of_image5.resize((800,800),Image.LANCZOS)
image5=ImageTk.PhotoImage(photo5)
label5= Label(frame5, image=image5).place(relx=0,rely=0)
horror_1=Image.open("bb.jpg")
horror1= horror_1.resize((260, 310), Image.LANCZOS) ## The (250, 250) is (height, width)
horrornew1=ImageTk.PhotoImage(horror1)
horror_2=Image.open("conjuring.jpg")
horror2= horror_2.resize((260, 310), Image.LANCZOS) ## The (250, 250) is (height, width)
horrornew2=ImageTk.PhotoImage(horror2)
horror_3=Image.open("it.jpg")
horror3= horror_3.resize((260, 310), Image.LANCZOS) ## The (250, 250) is (height, width)
horrornew3=ImageTk.PhotoImage(horror3)
horror_4=Image.open("stree.jpg")
horror4= horror_4.resize((260, 310), Image.LANCZOS) ## The (250, 250) is (height, width)
horrornew4=ImageTk.PhotoImage(horror4)
Back5=tk.Button(frame5,text="BACK",font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg='brown4',command=lambda:show_frame(frame3))
Back5.place(height=65,width=130,relx=0.01,rely=0.01)
def horror():
    horror=str(n2.get())
    if horror=="1":
        lab=tk.Label(frame10,text="",width=41,bg="white",height=2)
        lab.place(relx=0.03,rely=0.43)
        label=tk.Label(frame10,text="Movie Name : Bhool Bhulaiya",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.43)
        NEXT7=tk.Button(frame5,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame8),relief="raised")
        NEXT7.place(height=65,width=130,relx=0.01,rely=0.1)
    elif horror=="2":
        la=tk.Label(frame10,text="",bg="white",width=41,height=2)
        la.place(relx=0.03,rely=0.43)
        label=tk.Label(frame10,text="Movie Name : The Conjuring",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.43)
        NEXT7=tk.Button(frame5,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame8),relief="raised")
        NEXT7.place(height=65,width=130,relx=0.01,rely=0.1)
    elif horror=="3":
        la=tk.Label(frame10,text="",bg="white",width=41,height=2)
        la.place(relx=0.03,rely=0.43)
        label=tk.Label(frame10,text="Movie Name : It",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.43)
        NEXT7=tk.Button(frame5,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame8),relief="raised")
        NEXT7.place(height=65,width=130,relx=0.01,rely=0.1)
    elif horror=="4":
        la=tk.Label(frame10,text="",bg="white",width=41,height=2)
        la.place(relx=0.03,rely=0.43)
        label=tk.Label(frame10,text="Movie Name : Stree",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.43)
        NEXT7=tk.Button(frame5,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame8),relief="raised")
        NEXT7.place(height=65,width=130,relx=0.01,rely=0.1)
n2=IntVar()
c1_horror=tk.Checkbutton(frame5,image=horrornew1,variable=n2,onvalue=1,offvalue=0,bg="black",command=horror).place(relx=0.013,rely=0.2)
c2_horror=tk.Checkbutton(frame5,image=horrornew2,variable=n2,onvalue=2,offvalue=0,bg="black",command=horror).place(relx=0.5,rely=0.6)
c3_horror=tk.Checkbutton(frame5,image=horrornew3,variable=n2,onvalue=3,offvalue=0,bg="black",command=horror).place(relx=0.5,rely=0.2)
c4_horror=tk.Checkbutton(frame5,image=horrornew4,variable=n2,onvalue=4,offvalue=0,bg="black",command=horror).place(relx=0.013,rely=0.6)
b1h=tk.Button(frame5,text="Details",font=('Copperplate Gothic Light',14,'bold'),command=shoth1,width=6).place(relx=0.38,rely=0.37)
b2h=tk.Button(frame5,text="Details",font=('Copperplate Gothic Light',14,'bold'),command=shoth2,width=6).place(relx=0.38,rely=0.74)
b3h=tk.Button(frame5,text="Details",font=('Copperplate Gothic Light',14,'bold'),command=shoth3,width=6).place(relx=0.87,rely=0.37)
b4h=tk.Button(frame5,text="Details",font=('Copperplate Gothic Light',14,'bold'),command=shoth4,width=6).place(relx=0.87,rely=0.74)
#=============frame4=======
copy_of_image4=Image.open("movie (10).jpg")
photo4=copy_of_image4.resize((800,800),Image.LANCZOS)
image4=ImageTk.PhotoImage(photo4)
label4= Label(frame4, image=image4).place(relx=0,rely=0)
action_1=Image.open("darkknight.jpg")
action1= action_1.resize((260, 310), Image.LANCZOS) ## The (250, 250) is (height, width)
actionnew1=ImageTk.PhotoImage(action1)
action_2=Image.open("endgame.jpg")
action2= action_2.resize((260, 310), Image.LANCZOS) ## The (250, 250) is (height, width)
actionnew2=ImageTk.PhotoImage(action2)
action_3=Image.open("mardani.png")
action3= action_3.resize((260, 310), Image.LANCZOS) ## The (250, 250) is (height, width)
actionnew3=ImageTk.PhotoImage(action3)
action_4=Image.open("tiger.jpg")
action4= action_4.resize((260, 310), Image.LANCZOS) ## The (250, 250) is (height, width)
actionnew4=ImageTk.PhotoImage(action4)
Back4=tk.Button(frame4,text="BACK",font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg='brown4',command=lambda:show_frame(frame3))
Back4.place(height=65,width=130,relx=0.01,rely=0.01)
def action():
    action=str(n1.get())
    if action=="1":
        lab=tk.Label(frame10,text="",width=41,bg="white",height=2)
        lab.place(relx=0.03,rely=0.43)
        label=tk.Label(frame10,text="Movie Name : The Dark Knight",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.43)
        NEXT7=tk.Button(frame4,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame8),relief="raised")
        NEXT7.place(height=65,width=130,relx=0.01,rely=0.1)
    elif action=="2":
        lab=tk.Label(frame10,text="",width=41,bg="white",height=2)
        lab.place(relx=0.03,rely=0.43)
        label=tk.Label(frame10,text="Movie Name : Avengers Endgame",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.43)
        NEXT7=tk.Button(frame4,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame8),relief="raised")
        NEXT7.place(height=65,width=130,relx=0.01,rely=0.1)
    elif action=="3":
        lab=tk.Label(frame10,text="",width=41,bg="white",height=2)
        lab.place(relx=0.03,rely=0.43)
        label=tk.Label(frame10,text="Movie Name : Mardaani 2",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.43)
        NEXT7=tk.Button(frame4,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame8),relief="raised")
        NEXT7.place(height=65,width=130,relx=0.01,rely=0.1)
    elif action=="4":
        lab=tk.Label(frame10,text="",width=41,bg="white",height=2)
        lab.place(relx=0.03,rely=0.43)
        label=tk.Label(frame4,text="Movie Name : Tiger Zinda Hai",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.43)
        NEXT7=tk.Button(frame4,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame8),relief="raised")
        NEXT7.place(height=65,width=130,relx=0.01,rely=0.1)
n1=IntVar()
c1_action=tk.Checkbutton(frame4,image=actionnew1,variable=n1,onvalue=1,offvalue=0,bg="black",command=action).place(relx=0.013,rely=0.2)
c2_action=tk.Checkbutton(frame4,image=actionnew2,variable=n1,onvalue=2,offvalue=0,bg="slateblue4",command=action).place(relx=0.5,rely=0.6)
c3_action=tk.Checkbutton(frame4,image=actionnew3,variable=n1,onvalue=3,offvalue=0,bg="tan4",command=action).place(relx=0.5,rely=0.2)
c4_action=tk.Checkbutton(frame4,image=actionnew4,variable=n1,onvalue=4,offvalue=0,bg="saddle brown",command=action).place(relx=0.013,rely=0.6)
b1=tk.Button(frame4,text="Details",font=('Copperplate Gothic Light',14,'bold'),command=shot1,width=6).place(relx=0.38,rely=0.37)
b2=tk.Button(frame4,text="Details",font=('Copperplate Gothic Light',14,'bold'),command=shot2,width=6).place(relx=0.38,rely=0.74)
b3=tk.Button(frame4,text="Details",font=('Copperplate Gothic Light',14,'bold'),command=shot3,width=6).place(relx=0.87,rely=0.37)
b4=tk.Button(frame4,text="Details",font=('Copperplate Gothic Light',14,'bold'),command=shot4,width=6).place(relx=0.87,rely=0.74)
#===========frame6=======
copy_of_image6=Image.open("movie (5).jpg")
photo6=copy_of_image6.resize((800,800),Image.LANCZOS)
image6=ImageTk.PhotoImage(photo6)
label6= Label(frame6, image=image6).place(relx=0,rely=0)
scifi_1=Image.open("ra one.jpg")
scifi1= scifi_1.resize((260, 310), Image.LANCZOS)
scifinew1=ImageTk.PhotoImage(scifi1)
scifi_2=Image.open("INCEPTION.jpg")
scifi2= scifi_2.resize((260, 310), Image.LANCZOS)
scifinew2=ImageTk.PhotoImage(scifi2)
scifi_3=Image.open("interstellar.jpg")
scifi3= scifi_3.resize((260, 310), Image.LANCZOS)
scifinew3=ImageTk.PhotoImage(scifi3)
scifi_4=Image.open("mm2.jpg")
scifi4= scifi_4.resize((260, 310), Image.LANCZOS)
scifinew4=ImageTk.PhotoImage(scifi4)
Back6=tk.Button(frame6,text="BACK",font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg='brown4',command=lambda:show_frame(frame3))
Back6.place(height=65,width=130,relx=0.01,rely=0.01)
def scifi():
    scifi=str(n3.get())
    if scifi=="1":
        lab=tk.Label(frame10,text="",width=41,bg="white",height=2)
        lab.place(relx=0.03,rely=0.43)
        label=tk.Label(frame10,text="Movie Name : Ra. One",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.43)
        NEXT7=tk.Button(frame6,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame8),relief="raised")
        NEXT7.place(height=65,width=130,relx=0.01,rely=0.1)
    elif scifi=="2":
        lab=tk.Label(frame10,text="",width=41,bg="white",height=2)
        lab.place(relx=0.03,rely=0.43)
        label=tk.Label(frame10,text="Movie Name : Inception",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.43)
        NEXT7=tk.Button(frame6,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame8),relief="raised")
        NEXT7.place(height=65,width=130,relx=0.01,rely=0.1)
    elif scifi=="3":
        lab=tk.Label(frame10,text="",width=41,bg="white",height=2)
        lab.place(relx=0.03,rely=0.43)
        label=tk.Label(frame10,text="Movie Name : Interstellar",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.43)
        NEXT7=tk.Button(frame6,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame8),relief="raised")
        NEXT7.place(height=65,width=130,relx=0.01,rely=0.1)
    elif scifi=="4":
        lab=tk.Label(frame10,text="",width=41,bg="white",height=2)
        lab.place(relx=0.03,rely=0.43)
        label=tk.Label(frame10,text="Movie Name : Mission Mangal",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.43)
        NEXT7=tk.Button(frame6,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame8),relief="raised")
        NEXT7.place(height=65,width=130,relx=0.01,rely=0.1)
n3=IntVar()
c1_scifi=tk.Checkbutton(frame6,image=scifinew1,variable=n3,onvalue=1,offvalue=0,bg="black",command=scifi).place(relx=0.013,rely=0.2)
c2_scifi=tk.Checkbutton(frame6,image=scifinew2,variable=n3,onvalue=2,offvalue=0,bg="black",command=scifi).place(relx=0.5,rely=0.6)
c3_scifi=tk.Checkbutton(frame6,image=scifinew3,variable=n3,onvalue=3,offvalue=0,bg="black",command=scifi).place(relx=0.5,rely=0.2)
c4_scifi=tk.Checkbutton(frame6,image=scifinew4,variable=n3,onvalue=4,offvalue=0,bg="black",command=scifi).place(relx=0.013,rely=0.6)
b1s=tk.Button(frame6,text="Details",font=('Copperplate Gothic Light',14,'bold'),command=shots1,width=6).place(relx=0.38,rely=0.37)
b2s=tk.Button(frame6,text="Details",font=('Copperplate Gothic Light',14,'bold'),command=shots2,width=6).place(relx=0.38,rely=0.74)
b3s=tk.Button(frame6,text="Details",font=('Copperplate Gothic Light',14,'bold'),command=shots3,width=6).place(relx=0.87,rely=0.37)
b4s=tk.Button(frame6,text="Details",font=('Copperplate Gothic Light',14,'bold'),command=shots4,width=6).place(relx=0.87,rely=0.74)
#============frame7========
copy_of_image7=Image.open("movie (9).jpg")
photo7=copy_of_image7.resize((800,800),Image.LANCZOS)
image7=ImageTk.PhotoImage(photo7)
label7= Label(frame7, image=image7).place(relx=0,rely=0)
comedy_1=Image.open("chup.jpg")
comedy1= comedy_1.resize((260, 310), Image.LANCZOS)
comedynew1=ImageTk.PhotoImage(comedy1)
comedy_2=Image.open("dolittle.png")
comedy2= comedy_2.resize((260, 310), Image.LANCZOS)
comedynew2=ImageTk.PhotoImage(comedy2)
comedy_3=Image.open("home alone.jpg")
comedy3= comedy_3.resize((260, 310), Image.LANCZOS)
comedynew3=ImageTk.PhotoImage(comedy3)
comedy_4=Image.open("php.jpg")
comedy4= comedy_4.resize((260, 310), Image.LANCZOS)
comedynew4=ImageTk.PhotoImage(comedy4)
Back7=tk.Button(frame7,text="BACK",font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg='brown4',command=lambda:show_frame(frame3))
Back7.place(height=65,width=130,relx=0.01,rely=0.01)
def comedy():
    comedy=str(n4.get())
    if comedy=="1":
        lab=tk.Label(frame10,text="",width=41,bg="white",height=2)
        lab.place(relx=0.03,rely=0.43)
        label=tk.Label(frame10,text="Movie Name : Chup Chup Ke",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.43)
        NEXT7=tk.Button(frame7,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame8),relief="raised")
        NEXT7.place(height=65,width=130,relx=0.01,rely=0.1)
    elif comedy=="2":
        lab=tk.Label(frame10,text="",width=41,bg="white",height=2)
        lab.place(relx=0.03,rely=0.43)
        label=tk.Label(frame10,text="Movie Name : Dolittle",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.43)
        NEXT7=tk.Button(frame7,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame8),relief="raised")
        NEXT7.place(height=65,width=130,relx=0.01,rely=0.1)
    elif comedy=="3":
        lab=tk.Label(frame10,text="",width=41,bg="white",height=2)
        lab.place(relx=0.03,rely=0.43)
        label=tk.Label(frame10,text="Movie Name : Home Alone",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.43)
        NEXT7=tk.Button(frame7,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame8),relief="raised")
        NEXT7.place(height=65,width=130,relx=0.01,rely=0.1)
    elif comedy=="4":
        lab=tk.Label(frame10,text="",width=41,bg="white",height=2)
        lab.place(relx=0.03,rely=0.43)
        label=tk.Label(frame10,text="Movie Name : Phir Hera Pheri",font=("Calibri (Body)",16),bg="white").place(relx=0.03,rely=0.43)
        NEXT7=tk.Button(frame7,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame8),relief="raised")
        NEXT7.place(height=65,width=130,relx=0.01,rely=0.1)
n4=IntVar()
c1_comedy=tk.Checkbutton(frame7,image=comedynew1,variable=n4,onvalue=1,offvalue=0,bg="black",command=comedy).place(relx=0.013,rely=0.2)
c2_comedy=tk.Checkbutton(frame7,image=comedynew2,variable=n4,onvalue=2,offvalue=0,bg="black",command=comedy).place(relx=0.5,rely=0.6)
c3_comedy=tk.Checkbutton(frame7,image=comedynew3,variable=n4,onvalue=3,offvalue=0,bg="black",command=comedy).place(relx=0.5,rely=0.2)
c4_comedy=tk.Checkbutton(frame7,image=comedynew4,variable=n4,onvalue=4,offvalue=0,bg="black",command=comedy).place(relx=0.013,rely=0.6)
b1c=tk.Button(frame7,text="Details",font=('Copperplate Gothic Light',14,'bold'),command=shotc1,width=6).place(relx=0.38,rely=0.37)
b2c=tk.Button(frame7,text="Details",font=('Copperplate Gothic Light',14,'bold'),command=shotc2,width=6).place(relx=0.87,rely=0.74)
b3c=tk.Button(frame7,text="Details",font=('Copperplate Gothic Light',14,'bold'),command=shotc3,width=6).place(relx=0.87,rely=0.37)
b4c=tk.Button(frame7,text="Details",font=('Copperplate Gothic Light',14,'bold'),command=shotc4,width=6).place(relx=0.38,rely=0.74)
#============frame8========
copy_of_image8=Image.open("moviebackground2 (1).jpg")
photo8=copy_of_image8.resize((800,800),Image.LANCZOS)
image8=ImageTk.PhotoImage(photo8)
label8= Label(frame8, image=image8).place(relx=0,rely=0)
#==============frame3======
copy_of_image3=Image.open("res (7).jpg")
photo3=copy_of_image3.resize((800,800),Image.LANCZOS)
image3=ImageTk.PhotoImage(photo3)
label3= Label(frame3, image=image3).place(relx=0,rely=0)
Back3=tk.Button(frame3,text="BACK",font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg='brown4',command=lambda:show_frame(frame2))
Back3.place(height=75,width=150,relx=0.01,rely=0.01)
canvas2=Canvas(frame3, height=540, width=630,bg="lightgoldenrod2")
canvas2.place(relx=0.104, rely=0.166)
action_button=Image.open("actionnew.png")
action= action_button.resize((300, 280), Image.LANCZOS) ## The (250, 250) is (height, width)
actionnew=ImageTk.PhotoImage(action)
horror_button=Image.open("HORROR (1).png")
horror= horror_button.resize((300, 280), Image.LANCZOS) ## The (250, 250) is (height, width)
horrornew=ImageTk.PhotoImage(horror)
scifi_button=Image.open("scifi (2).png")
scifi= scifi_button.resize((300, 280), Image.LANCZOS) ## The (250, 250) is (height, width)
scifinew=ImageTk.PhotoImage(scifi)
comedy_button=Image.open("COMEDY.png")
comedy= comedy_button.resize((300, 280), Image.LANCZOS)
comedynew=ImageTk.PhotoImage(comedy)
def selectionNEW():
    selection=str(var1.get())
    if selection=="1":
        NEXT3=tk.Button(frame3,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame4),relief="raised")
        NEXT3.place(height=75,width=150,relx=0.81,rely=0.9)
        back=tk.Button(frame8,text="BACK" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame4),relief="raised")
        back.place(height=75,width=150,relx=0.01,rely=0.01)
    elif selection=="2":
        NEXT3=tk.Button(frame3,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame5),relief="raised")
        NEXT3.place(height=75,width=150,relx=0.81,rely=0.9)
        back=tk.Button(frame8,text="BACK" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame5),relief="raised")
        back.place(height=75,width=150,relx=0.01,rely=0.001)
    elif selection=="3":
        NEXT3=tk.Button(frame3,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame6),relief="raised")
        NEXT3.place(height=75,width=150,relx=0.81,rely=0.9)
        back=tk.Button(frame8,text="BACK" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame6),relief="raised")
        back.place(height=75,width=150,relx=0.01,rely=0.001)
    elif selection=="4":
        NEXT3=tk.Button(frame3,text="NEXT" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame7),relief="raised")
        NEXT3.place(height=75,width=150,relx=0.81,rely=0.9)
        back=tk.Button(frame8,text="BACK" ,font=('Copperplate Gothic Light',18,'bold'),bg='goldenrod1',fg="brown4",command=lambda:show_frame(frame7),relief="raised")
        back.place(height=75,width=150,relx=0.01,rely=0.001)
var1=IntVar()
radio_action=tk.Radiobutton(canvas2,value=1,variable=var1,image=actionnew,bg="darkorange2",command=selectionNEW)
radio_action.place(relx=0.0006,rely=0.0008)
radio_horror=tk.Radiobutton(canvas2,variable=var1,value=2,image=horrornew,bg="mediumorchid2",command=selectionNEW)
radio_horror.place(relx=0.0006,rely=0.5227)
radio_scifi=tk.Radiobutton(canvas2,variable=var1,value=3,image=scifinew,bg="steelblue",command=selectionNEW)
radio_scifi.place(relx=0.49,rely=0.0008)
radio_comedy=tk.Radiobutton(canvas2,variable=var1,value=4,image=comedynew,bg="olivedrab2",command=selectionNEW)
radio_comedy.place(relx=0.49,rely=0.5227)
# ==========Frame1=========
copy_of_image1 = Image.open("movie3.jpg")
background1=copy_of_image1.resize((798,795),Image.LANCZOS)
background_image1=ImageTk.PhotoImage(background1)
background_label1=Label(frame1, image=background_image1).place(relx=0,rely=0)
logo_image=Image.open("movielogo.png")
logoimage= ImageTk.PhotoImage(logo_image)
ENTER=tk.Button(frame1,text="ENTER" ,font=('Italiana',30,'bold'),bg='ivory3',fg="midnight blue",command=lambda:show_frame(frame2),relief="raised")
ENTER.place(height=80,width=200,relx=0.376,rely=0.7)
# #===============frame3====

show_frame(frame1)
root.mainloop()