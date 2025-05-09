from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from PIL import Image,ImageTk
import pymysql
from termcolor import colored

class volleyball:

    def __init__(self,root,bg):

        self.root=root
        self.bg=bg

#---------------frm1-------------------------------------------------------------------------------------------------------------------------
    print(colored("Coding by iliya","yellow"))

    def create_frm(self,r,c):

        self.frm = Frame(self.root,bg=self.bg,width=500, height=400)
        self.frm.grid(row=r,column=c)
        image5=Image.open("img/dow.png")
        resize_img=image5.resize((100,100))
        img5=ImageTk.PhotoImage(resize_img)
        l4=Label(self.frm,image=img5,bg="sky blue")
        l4.place(x=355,y=240) 

        image6=Image.open("img/vnl.png")
        resize_img=image6.resize((100,100))
        img6=ImageTk.PhotoImage(resize_img)
        l5=Label(self.frm,image=img6,bg="sky blue")
        l5.place(x=10,y=240) 

        self.create_lable()
        self.create_button()
    

#---------------frm2----------------------------------------------------------------------------------------------------------------------------

    def create_frm2(self):

        volly=Toplevel()
        self.frm2=Frame(volly,bg="#BDB76B",width=500,height=400)
        self.frm2.grid(row=0,column=0)

        image4=Image.open("img/b1.png")
        resize_img=image4.resize((200,200))
        img4=ImageTk.PhotoImage(resize_img)
        l4=Label(self.frm2,image=img4,bg="#BDB76B")
        l4.place(x=300,y=5)

        image7=Image.open("img/world.png")
        resize_img=image7.resize((150,150))
        img7=ImageTk.PhotoImage(resize_img)
        l7=Label(self.frm2,image=img7,bg="#BDB76B")
        l7.place(x=10,y=30) 


        self.create_combo()
        self.create_lbl2()
        self.create_btn2()


#-----------------frm3-----------------------------------------------------------------------------------------------------------------------
   
    def create_frm3(self):

        settings=Toplevel()  
        settings.title("Tips")   
        self.frm3=Frame(settings,bg="black",width=600,height=450)
        self.frm3.grid(row=0,column=0)
        self.create_lbl3()

#----------------------combo------------------------------------------------------------------------------------------------------------------
    def create_combo(self):

        self.combob=Combobox(self.frm2,values=("IRAN","JAPAN","FRANCE","POLAND","ITALY","BRAZIL"))
        self.combob.place(x=220,y=180)

#---------------------lbl1-----------------------------------------------------------------------------------------------------------------------------        
    def create_lable(self):

        self.lbl=Label(self.frm,text="Welcome to my app",bg="sky blue",fg="dark blue",font=("@Kozuka Mincho Pr6N M",20))
        self.lbl.place(x=150,y=80)


        self.lbl2=Label(self.frm,text="this is a volleyball game",bg="sky blue",fg="red",font=20)
        self.lbl2.place(x=10,y=360)

        self.lbl15=Label(self.frm,text="Coding by: Iliyadayi",bg="sky blue",fg="red",font=20)
        self.lbl15.place(x=10,y=10)

#---------------lbl2---------------------------------------------------------------------------------------------------------------------------------
    def create_lbl2(self):

        self.lbl3=Label(self.frm2,text="select team:",bg="#BDB76B",fg="black",font=3)
        self.lbl3.place(x=100,y=175)

        self.lbl4=Label(self.frm2,text=" Volleyball is a very famous game",bg="#BDB76B",fg="red",font=30)
        self.lbl4.place(x=10,y=10)

        self.lbl5=Label(self.frm2,text="volleyball soccer",bg="#BDB76B",fg="blue",font=3)
        self.lbl5.place(x=10,y=350)

        self.lbl14=Label(self.frm2,text="Coding by: Iliyadayi",bg="#BDB76B",fg="red",font=3)
        self.lbl14.place(x=300,y=350)
#---------------lbl3--------------------------------------------------------------------------------------------------------------------------
    def create_lbl3(self):

        self.lbl6=Label(self.frm3,text="wellcome to volleyball game. now i help you to play this game." ,bg="black",fg="white",font=2)
        self.lbl6.place(x=10,y=10)
        
        self.lbl7=Label(self.frm3,text="frist you should press the let's go button to go to the page1. ",bg="black",fg="white",font=2)
        self.lbl7.place(x=10,y=60)

        self.lbl8=Label(self.frm3,text="then in page one you should select a volleyball team.",bg="black",fg="white",font=2)
        self.lbl8.place(x=10,y=110)
        
        self.lbl9=Label(self.frm3,text="then if you press select button you go to page2. ",bg="black",fg="white",font=2)
        self.lbl9.place(x=10,y=160)

        self.lbl10=Label(self.frm3,text="in page2 you have the combination of the volleyball team",bg="black",fg="white",font=2)
        self.lbl10.place(x=10,y=210)

        self.lbl11=Label(self.frm3,text="and if you like to save it in database you should press the red ",bg="black",fg="white",font=2)
        self.lbl11.place(x=10,y=260)

        self.lbl12=Label(self.frm3,text=" button its name is save in database.",bg="black",fg="white",font=2)
        self.lbl12.place(x=10,y=310)

        self.lbl13=Label(self.frm3,text="Coding by : iliya dayi",bg="black",fg="red",font=2)
        self.lbl13.place(x=370,y=400)
#-------------------btn1----------------------------------------------------------------------------------------------------------------------------
    def create_button(self):

        self.btn=Button(self.frm,text="let's go",bg="dark blue",fg="sky blue",width=16,height=5,command=self.create_frm2)
        self.btn.place(x=200,y=150)

        self.btn=Button(self.frm,text="Tips",bg="red",fg="white",width=16,height=5,command=self.create_frm3)
        self.btn.place(x=200,y=260)

#-----------------=btn2---------------------------------------------------------------------------------------------------------------------------
    def create_btn2(self):

        self.btn2=Button(self.frm2,text="select",bg="pink",fg="black",command=self.show_v)
        self.btn2.place(x=290,y=250)
#---------------------show-----------------------------------------------------------------------------------------------------------------------------
    def show_v(self):
        self.volley=self.combob.get()

        if self.volley == "IRAN":

            self.IRAN_page()

        elif self.volley == "JAPAN":

            self.japan_page()
             
        elif self.volley == "ITALY":

            self.ITALY_page() 

        elif self.volley == "BRAZIL":

            self.brazil_page()

        elif self.volley == "POLAND":

            self.poland_page()

        elif self.volley == "FRANCE":

            self.france_page()

#-------------japan------------------------------------------------------------------------------------------------------------------------------
    def japan_page(self):

        page1=Toplevel()
        page1.config(bg="#BDB76B")
        page1.geometry("980x700+0+0")
        page1.title("Japan Page")


        self.frm1=Frame(page1,width=200,height=200,bg="#BDB76B")
        self.frm1.grid(row=0,column=0,padx=10,pady=10) 
        image=Image.open("img/yuki.jpeg")
        resize_img=image.resize((200,200))	
        img=ImageTk.PhotoImage(resize_img)
        l2=Label(self.frm1,image=img)
        l2.place(x=35,y=20)   


        self.frm2=Frame(page1,width=200,height=200,bg="#BDB76B")
        self.frm2.grid(row=1,column=0,padx=10,pady=10) 
        image2=Image.open("img/ran.jpg")
        resize_img=image2.resize((200,200))
        img2=ImageTk.PhotoImage(resize_img)
        l3=Label(self.frm2,image=img2)
        l3.place(x=35,y=20)   


        self.frm3=Frame(page1,width=200,height=200,bg="#BDB76B")
        self.frm3.grid(row=0,column=1,padx=10,pady=10)
        image3=Image.open("img/onodera.webp")
        resize_img=image3.resize((200,200))
        img3=ImageTk.PhotoImage(resize_img)
        l4=Label(self.frm3,image=img3)
        l4.place(x=35,y=30)   


        self.frm4=Frame(page1,width=200,height=200,bg="#BDB76B")
        self.frm4.grid(row=1,column=1,padx=10,pady=10) 
        image4=Image.open("img/yamamoto.jpeg")
        resize_img=image4.resize((200,200))
        img4=ImageTk.PhotoImage(resize_img)
        l4=Label(self.frm4,image=img4)
        l4.place(x=35,y=20)   


        self.frm5=Frame(page1,width=200,height=200,bg="#BDB76B")
        self.frm5.grid(row=0,column=2,padx=10,pady=10) 
        image5=Image.open("img/yuji.jpeg")
        resize_img=image5.resize((200,200))
        img5=ImageTk.PhotoImage(resize_img)
        l5=Label(self.frm5,image=img5)
        l5.place(x=35,y=20) 


        self.frm6=Frame(page1,width=200,height=200,bg="#BDB76B")
        self.frm6.grid(row=1,column=2,padx=10,pady=10) 
        image6=Image.open("img/skita.jpeg")
        resize_img=image6.resize((200,200))
        img6=ImageTk.PhotoImage(resize_img)
        l6=Label(self.frm6,image=img6)
        l6.place(x=35,y=20)

        btn4=Button(page1,text="save in database",width=13,height=2,bg="red",fg="white",command=self.getinfo_japan)
        btn4.place(x=330,y=647)


        l7=Label(page1,text="press button to save in database",bg="#BDB76B",fg="white",font=1)
        l7.place(x=10,y=650)
        

        page1.mainloop() 
#---------------------italy--------------------------------------------------------------------------------------------------------------------
    def ITALY_page(self):

        page2=Toplevel()
        page2.config(bg="sky blue")
        page2.geometry("980x700+0+0")
        page2.title("Italy Page")


        self.frm1=Frame(page2,width=200,height=200,bg="sky blue")
        self.frm1.grid(row=0,column=0,padx=10,pady=10) 
        image=Image.open("img/lavai.jpeg")
        resize_img=image.resize((200,200))	
        img=ImageTk.PhotoImage(resize_img)
        l2=Label(self.frm1,image=img)
        l2.place(x=35,y=20)   


        self.frm2=Frame(page2,width=200,height=200,bg="sky blue")
        self.frm2.grid(row=1,column=0,padx=10,pady=10) 
        image2=Image.open("img/mekelato.jpg")
        resize_img=image2.resize((200,200))
        img2=ImageTk.PhotoImage(resize_img)
        l3=Label(self.frm2,image=img2)
        l3.place(x=35,y=20)   


        self.frm3=Frame(page2,width=200,height=200,bg="sky blue")
        self.frm3.grid(row=0,column=1,padx=10,pady=10)
        image3=Image.open("img/ruso.jpg")
        resize_img=image3.resize((200,200))
        img3=ImageTk.PhotoImage(resize_img)
        l4=Label(self.frm3,image=img3)
        l4.place(x=35,y=30)   


        self.frm4=Frame(page2,width=200,height=200,bg="sky blue")
        self.frm4.grid(row=1,column=1,padx=10,pady=10) 
        image4=Image.open("img/balaso.jpeg")
        resize_img=image4.resize((200,200))
        img4=ImageTk.PhotoImage(resize_img)
        l4=Label(self.frm4,image=img4)
        l4.place(x=35,y=20)   


        self.frm5=Frame(page2,width=200,height=200,bg="sky blue")
        self.frm5.grid(row=0,column=2,padx=10,pady=10) 
        image5=Image.open("img/romano.jpeg")
        resize_img=image5.resize((200,200))
        img5=ImageTk.PhotoImage(resize_img)
        l5=Label(self.frm5,image=img5)
        l5.place(x=35,y=20) 


        self.frm6=Frame(page2,width=200,height=200,bg="sky blue")
        self.frm6.grid(row=1,column=2,padx=10,pady=10) 
        image6=Image.open("img/ge.jpg")
        resize_img=image6.resize((200,200))
        img6=ImageTk.PhotoImage(resize_img)
        l6=Label(self.frm6,image=img6)
        l6.place(x=35,y=20) 
        btn4=Button(page2,text="save in database",width=13,height=2,bg="red",fg="white",command=self.getinfo_italy)
        btn4.place(x=330,y=647)

        l7=Label(page2,text="press button to save in database",bg="sky blue",fg="white",font=1)
        l7.place(x=10,y=650)

        page2.mainloop() 
    
#-------------------france------------------------------------------------------------------------------------------------------------------
    def france_page(self):

        page3=Toplevel()
        page3.config(bg="sky blue")
        page3.geometry("980x700+0+0")
        page3.title("France Page")


        self.frm1=Frame(page3,width=200,height=200,bg="sky blue")
        self.frm1.grid(row=0,column=0,padx=10,pady=10) 
        image=Image.open("img/cle.jpg")
        resize_img=image.resize((200,200))	
        img=ImageTk.PhotoImage(resize_img)
        l2=Label(self.frm1,image=img)
        l2.place(x=35,y=20)   


        self.frm2=Frame(page3,width=200,height=200,bg="sky blue")
        self.frm2.grid(row=1,column=0,padx=10,pady=10) 
        image2=Image.open("img/patry.jpeg")
        resize_img=image2.resize((200,200))
        img2=ImageTk.PhotoImage(resize_img)
        l3=Label(self.frm2,image=img2)
        l3.place(x=35,y=20)   


        self.frm3=Frame(page3,width=200,height=200,bg="sky blue")
        self.frm3.grid(row=0,column=1,padx=10,pady=10)
        image3=Image.open("img/chna.jpg")
        resize_img=image3.resize((200,200))
        img3=ImageTk.PhotoImage(resize_img)
        l4=Label(self.frm3,image=img3)
        l4.place(x=35,y=30)   


        self.frm4=Frame(page3,width=200,height=200,bg="sky blue")
        self.frm4.grid(row=1,column=1,padx=10,pady=10) 
        image4=Image.open("img/grbencof.jpeg")
        resize_img=image4.resize((200,200))
        img4=ImageTk.PhotoImage(resize_img)
        l4=Label(self.frm4,image=img4)
        l4.place(x=35,y=20)   


        self.frm5=Frame(page3,width=200,height=200,bg="sky blue")
        self.frm5.grid(row=0,column=2,padx=10,pady=10) 
        image5=Image.open("img/boyer.jpeg")
        resize_img=image5.resize((200,200))
        img5=ImageTk.PhotoImage(resize_img)
        l5=Label(self.frm5,image=img5)
        l5.place(x=35,y=20) 


        self.frm6=Frame(page3,width=200,height=200,bg="sky blue")
        self.frm6.grid(row=1,column=2,padx=10,pady=10) 
        image6=Image.open("img/brizard.jpeg")
        resize_img=image6.resize((200,200))
        img6=ImageTk.PhotoImage(resize_img)
        l6=Label(self.frm6,image=img6)
        l6.place(x=35,y=20) 

        btn4=Button(page3,text="save in database",width=13,height=2,bg="red",fg="white",command=self.getinfo_france)
        btn4.place(x=330,y=647)

        l7=Label(page3,text="press button to save in database",bg="sky blue",fg="white",font=1)
        l7.place(x=10,y=650)

        page3.mainloop() 
    
#----------------brazil---------------------------------------------------------------------------------------------------------------------------
    def brazil_page(self):

        page4=Toplevel()
        page4.config(bg="sky blue")
        page4.geometry("980x700+0+0")
        page4.title("Brazil Page")


        self.frm1=Frame(page4,width=200,height=200,bg="sky blue")
        self.frm1.grid(row=0,column=0,padx=10,pady=10) 
        image=Image.open("img/luca.jpg")
        resize_img=image.resize((200,200))	
        img=ImageTk.PhotoImage(resize_img)
        l2=Label(self.frm1,image=img)
        l2.place(x=35,y=20)   


        self.frm2=Frame(page4,width=200,height=200,bg="sky blue")
        self.frm2.grid(row=1,column=0,padx=10,pady=10) 
        image2=Image.open("img/ho.webp")
        resize_img=image2.resize((200,200))
        img2=ImageTk.PhotoImage(resize_img)
        l3=Label(self.frm2,image=img2)
        l3.place(x=35,y=20)   


        self.frm3=Frame(page4,width=200,height=200,bg="sky blue")
        self.frm3.grid(row=0,column=1,padx=10,pady=10)
        image3=Image.open("img/otavoia.jpeg")
        resize_img=image3.resize((200,200))
        img3=ImageTk.PhotoImage(resize_img)
        l4=Label(self.frm3,image=img3)
        l4.place(x=35,y=30)   


        self.frm4=Frame(page4,width=200,height=200,bg="sky blue")
        self.frm4.grid(row=1,column=1,padx=10,pady=10) 
        image4=Image.open("img/lebero.jpg")
        resize_img=image4.resize((200,200))
        img4=ImageTk.PhotoImage(resize_img)
        l4=Label(self.frm4,image=img4)
        l4.place(x=35,y=20)   


        self.frm5=Frame(page4,width=200,height=200,bg="sky blue")
        self.frm5.grid(row=0,column=2,padx=10,pady=10) 
        image5=Image.open("img/ala.jpeg")
        resize_img=image5.resize((200,200))
        img5=ImageTk.PhotoImage(resize_img)
        l5=Label(self.frm5,image=img5)
        l5.place(x=35,y=20) 


        self.frm6=Frame(page4,width=200,height=200,bg="sky blue")
        self.frm6.grid(row=1,column=2,padx=10,pady=10) 
        image6=Image.open("img/brono.jpeg")
        resize_img=image6.resize((200,200))
        img6=ImageTk.PhotoImage(resize_img)
        l6=Label(self.frm6,image=img6)
        l6.place(x=35,y=20) 

        btn4=Button(page4,text="save in database",width=13,height=2,bg="red",fg="white",command=self.getinfo_brazil)
        btn4.place(x=330,y=647)

        l7=Label(page4,text="press button to save in database",bg="sky blue",fg="white",font=1)
        l7.place(x=10,y=650)

        page4.mainloop() 

#----------------poland-------------------------------------------------------------------------------------------------------------------------------
    def poland_page(self):

        page5=Toplevel()
        page5.config(bg="sky blue")
        page5.geometry("980x700+0+0")
        page5.title("Poland Page")


        self.frm1=Frame(page5,width=200,height=200,bg="#BDB76B")
        self.frm1.grid(row=0,column=0,padx=10,pady=10) 
        image=Image.open("img/ku.jpeg")
        resize_img=image.resize((200,200))	
        img=ImageTk.PhotoImage(resize_img)
        l2=Label(self.frm1,image=img)
        l2.place(x=35,y=20)   


        self.frm2=Frame(page5,width=200,height=200,bg="#BDB76B")
        self.frm2.grid(row=1,column=0,padx=10,pady=10) 
        image2=Image.open("img/sw.jpeg")
        resize_img=image2.resize((200,200))
        img2=ImageTk.PhotoImage(resize_img)
        l3=Label(self.frm2,image=img2)
        l3.place(x=35,y=20)   


        self.frm3=Frame(page5,width=200,height=200,bg="#BDB76B")
        self.frm3.grid(row=0,column=1,padx=10,pady=10)
        image3=Image.open("img/by.jpeg")
        resize_img=image3.resize((200,200))
        img3=ImageTk.PhotoImage(resize_img)
        l4=Label(self.frm3,image=img3)
        l4.place(x=35,y=30)   


        self.frm4=Frame(page5,width=200,height=200,bg="#BDB76B")
        self.frm4.grid(row=1,column=1,padx=10,pady=10) 
        image4=Image.open("img/zator.jpeg")
        resize_img=image4.resize((200,200))
        img4=ImageTk.PhotoImage(resize_img)
        l4=Label(self.frm4,image=img4)
        l4.place(x=35,y=20)   


        self.frm5=Frame(page5,width=200,height=200,bg="#BDB76B")
        self.frm5.grid(row=0,column=2,padx=10,pady=10) 
        image5=Image.open("img/loen.jpeg")
        resize_img=image5.resize((200,200))
        img5=ImageTk.PhotoImage(resize_img)
        l5=Label(self.frm5,image=img5)
        l5.place(x=35,y=20) 


        self.frm6=Frame(page5,width=200,height=200,bg="#BDB76B")
        self.frm6.grid(row=1,column=2,padx=10,pady=10) 
        image6=Image.open("img/ffff.jpeg")
        resize_img=image6.resize((200,200))
        img6=ImageTk.PhotoImage(resize_img)
        l6=Label(self.frm6,image=img6)
        l6.place(x=35,y=20) 

        btn4=Button(page5,text="save in database",width=13,height=2,bg="red",fg="white",command=self.getinfo_poland)
        btn4.place(x=330,y=647)

        l7=Label(page5,text="press button to save in database",bg="#BDB76B",fg="white",font=1)
        l7.place(x=10,y=650)

        page5.mainloop()


#------------------------iran----------------------------------------------------------------------------------------------------------------------

    def IRAN_page(self):

        page6=Toplevel()
        page6.config(bg="#BDB76B")
        page6.geometry("980x700+0+0")
        page6.title("IRAN page")


        self.frm1=Frame(page6,width=200,height=200,bg="#BDB76B")
        self.frm1.grid(row=0,column=0,padx=10,pady=10) 
        image=Image.open("img/sf.jpeg")
        resize_img=image.resize((200,200))	
        img=ImageTk.PhotoImage(resize_img)
        l2=Label(self.frm1,image=img)
        l2.place(x=35,y=20)   


        self.frm2=Frame(page6,width=200,height=200,bg="#BDB76B")
        self.frm2.grid(row=1,column=0,padx=10,pady=10) 
        image2=Image.open("img/sar.jpeg")
        resize_img=image2.resize((200,200))
        img2=ImageTk.PhotoImage(resize_img)
        l3=Label(self.frm2,image=img2)
        l3.place(x=35,y=20)   


        self.frm3=Frame(page6,width=200,height=200,bg="#BDB76B")
        self.frm3.grid(row=0,column=1,padx=10,pady=10)
        image3=Image.open("img/sat.jpeg")
        resize_img=image3.resize((200,200))
        img3=ImageTk.PhotoImage(resize_img)
        l4=Label(self.frm3,image=img3)
        l4.place(x=35,y=30)   


        self.frm4=Frame(page6,width=200,height=200,bg="#BDB76B")
        self.frm4.grid(row=1,column=1,padx=10,pady=10) 
        image4=Image.open("img/yaz.jpeg")
        resize_img=image4.resize((200,200))
        img4=ImageTk.PhotoImage(resize_img)
        l4=Label(self.frm4,image=img4)
        l4.place(x=35,y=20)   


        self.frm5=Frame(page6,width=200,height=200,bg="#BDB76B")
        self.frm5.grid(row=0,column=2,padx=10,pady=10) 
        image5=Image.open("img/am.webp")
        resize_img=image5.resize((200,200))
        img5=ImageTk.PhotoImage(resize_img)
        l5=Label(self.frm5,image=img5)
        l5.place(x=35,y=20) 


        self.frm6=Frame(page6,width=200,height=200,bg="#BDB76B")
        self.frm6.grid(row=1,column=2,padx=10,pady=10) 
        image6=Image.open("img/vadi.jpeg")
        resize_img=image6.resize((200,200))
        img6=ImageTk.PhotoImage(resize_img)
        l6=Label(self.frm6,image=img6)
        l6.place(x=35,y=20) 




        btn4=Button(page6,text="save in database",width=13,height=2,bg="red",fg="white",command=self.getinfo_IRAN)
        btn4.place(x=330,y=647)

        l8=Label(page6,text="press button to save in database",bg="#BDB76B",fg="white",font=1)
        l8.place(x=10,y=650)

        page6.mainloop()
        
#----------------mysql----------------------------------------------------------------------------------------------------------------------------

    def getinfo_IRAN(self):

        teamname = self.combob.get()

        try:

            dbconnact=pymysql.connect(host="localhost",user="root",password="root",database="volleyball")
            cursor=dbconnact.cursor()
            query = f"insert into team (teamname,libero,Behindline,playcards,center,onnet,straight) value('{teamname}','hazratpor','amin','vadi','esfandeair','siatad','shrifi');"
            cursor.execute(query)
            dbconnact.commit()
            print(colored("thank you to play volleyball game","green"))

        except:
            print(colored("error","red"))

#-----------------japan----------------------------------------------------------------------------------------------------------------------


    def getinfo_japan(self):

        teamname = self.combob.get()

        try:

            dbconnact=pymysql.connect(host="localhost",user="root",password="root",database="volleyball")
            cursor=dbconnact.cursor()
            query = f"insert into team (teamname,libero,Behindline,playcards,center,onnet,straight) value('{teamname}','yammamoto','yuji','skita','ran','onodera','yuki');"
            cursor.execute(query)
            dbconnact.commit()
            print(colored("thank you to play volleyball game","green"))

        except:
            print(colored("error","red"))

#-------------------italy------------------------------------------------------------------------------------------------------------------

    def getinfo_italy(self):

        teamname = self.combob.get()
        
        try:
            dbconnact=pymysql.connect(host="localhost",user="root",password="root",database="volleyball")
            cursor=dbconnact.cursor()
            query = f"insert into team (teamname,libero,Behindline,playcards,center,onnet,straight) value('{teamname}','balaso','romano','gianelli','lavia','ruso','mikelto');"
            cursor.execute(query)
            dbconnact.commit()
            print(colored("thank you to play volleyball game","green"))

        except:
            print(colored("error","red"))


#--------------------poland------------------------------------------------------------------------------------------------------------

    def getinfo_poland(self):

        teamname = self.combob.get()
        
        try:

            dbconnact=pymysql.connect(host="localhost",user="root",password="root",database="volleyball")
            cursor=dbconnact.cursor()
            query = f"insert into team (teamname,libero,Behindline,playcards,center,onnet,straight) value('{teamname}','zatorsky','shifka','yanush','bartosh','benic','loen');"
            cursor.execute(query)
            dbconnact.commit()
            print(colored("thank you to play volleyball game","green"))

        except:

            print(colored("error","red"))


#-----------------------brazil------------------------------------------------------------------------------------------------------------         
    def getinfo_brazil(self):

        teamname = self.combob.get()
        
        try:

            dbconnact=pymysql.connect(host="localhost",user="root",password="root",database="volleyball")
            cursor=dbconnact.cursor()
            query = f"insert into team (teamname,libero,Behindline,playcards,center,onnet,straight) value('{teamname}','thales','honorato','bruno','alan','otavio','lucarli');"
            cursor.execute(query)
            dbconnact.commit()
            print(colored("thank you to play volleyball game","green"))

        except:

            print(colored("error","red"))



#---------------------france------------------------------------------------------------------------------------------------------------------------------------------

    def getinfo_france(self):

        teamname = self.combob.get()
        
        try:

            dbconnact=pymysql.connect(host="localhost",user="root",password="root",database="volleyball")
            cursor=dbconnact.cursor()
            query = f"insert into team (teamname,libero,Behindline,playcards,center,onnet,straight) value('{teamname}','grebnikov','clonate','brizard','patry','chinese','boyer');"
            cursor.execute(query)
            dbconnact.commit()
            print(colored("thank you to play volleyball game","green"))

        except:

            print(colored("error","red"))


#----------------------root-----------------------------------------------------------------------------------------------------------------
root=Tk()



root.title("volleyball game")


root.geometry("500x400")
vb=volleyball(root,"sky blue")
vb.create_frm(0,0)



root.mainloop()