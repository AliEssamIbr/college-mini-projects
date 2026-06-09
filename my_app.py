import customtkinter as ctk
from PIL import Image
from new_bank_system import BANK
from datetime import datetime as dt
session_data ={
    "client_id" : ""
}
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
background_URL = "C:/users/lenovo-a/OneDrive/pictures/Screenshots/Screenshot 2026-05-25 211730.png"
text_color = "white"
bg_text_color = "#0B032C"
hover_color = "#0c0c3e"
fg_color="#0f0f53"
DB_connection = BANK()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.name = "" 
        self.title("Multi-Screen App")
        self.geometry("1545x850") 
        self.Screens = [MainScreen,ApplicationMainScreen,ApplyingScreen,AppliReview,AppliReviewAdmin,AdminMainScreen,AdminClientCenterScreen,AdminClientDisplayAll,AdminClientDisplaySingle,ClientCenterScreen,ClientCenterLoginScreen,AdminMessageDisplayAll,ClientSettingsScreen,ClientMainScreen,ClientCardsScreen,AdminCreditReview,AdminDebitReview]
        self.transfer_id = ""
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Loop through and initialize the screens
        for F in self.Screens:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainScreen")

    def show_frame(self, page_name):
        """Bring any frame to the front"""
        frame = self.frames[page_name]
        frame.tkraise()


class MainScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.bg_image = ctk.CTkImage(
            light_image=Image.open(background_URL),
            dark_image=Image.open(background_URL),
            size=(1545, 850)
        )
        bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.big_boi_panel = ctk.CTkFrame(self,height=750,width=1400,border_width=5,border_color="gold",fg_color="#050521")
        self.big_boi_panel.place(anchor="center",relx=0.5,rely=0.5)
        label = ctk.CTkLabel(self.big_boi_panel, text="BANK", font=("Arial", 58,"bold"), text_color=text_color,bg_color=bg_text_color)
        label.place(anchor="center", relx=0.5, rely=0.1)
        name_label = ctk.CTkLabel(self.big_boi_panel, text="MADE BY: B E A N Z  >B))", font=("Arial", 11,"bold"), text_color=text_color,bg_color=bg_text_color)
        name_label.place(anchor="center", relx=0.1, rely=0.95)

        button = ctk.CTkButton(
            self.big_boi_panel, 
            text="USER PLATFORM",
            font=("arial",30),
            command=lambda: controller.show_frame("ClientCenterLoginScreen"),
            bg_color=bg_text_color,
            text_color=text_color,
            hover_color=hover_color,
            fg_color=bg_text_color,
            corner_radius=1,
            border_color="gold",
            border_width=5
        )
        button.place(anchor="center", relx=0.5, rely=0.45)
        button1 = ctk.CTkButton(
            self.big_boi_panel, 
            text="ADMIN PLATFORM",
            font=("arial",30),
            command=lambda: controller.show_frame("AdminMainScreen"),
            bg_color=bg_text_color,
            text_color=text_color,
            hover_color=hover_color,
            fg_color=bg_text_color,
            corner_radius=1,
            border_color="gold",
            border_width=5
        )
        button1.place(anchor="center", relx=0.5, rely=0.55)
        button2 = ctk.CTkButton(
            self.big_boi_panel, 
            text="APPLICATION PLATFORM",
            font=("arial",30),
            command=lambda: controller.show_frame("ApplicationMainScreen"),
            bg_color=bg_text_color,
            text_color=text_color,
            hover_color=hover_color,
            fg_color=bg_text_color,
            corner_radius=1,
            border_color="gold",
            border_width=5
        )
        button2.place(anchor="center", relx=0.5, rely=0.65)
class ApplicationMainScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.bg_image = ctk.CTkImage(
            light_image=Image.open(background_URL),
            dark_image=Image.open(background_URL),
            size=(1545, 850)
        )
        bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.big_boi_panel = ctk.CTkFrame(self,height=750,width=1400,border_width=5,border_color="gold",fg_color="#050521")
        self.big_boi_panel.place(anchor="center",relx=0.5,rely=0.5)
        label = ctk.CTkLabel(self.big_boi_panel, text="BANK", font=("Arial", 58), text_color=text_color,bg_color=bg_text_color)
        label.place(anchor="center", relx=0.5, rely=0.08)

        label1 = ctk.CTkLabel(self.big_boi_panel, text="APPLICATION PLATFORM", font=("Arial", 40), text_color=text_color,bg_color=bg_text_color)
        label1.place(anchor="center", relx=0.5, rely=0.15)

        EntryButton = ctk.CTkButton(self.big_boi_panel,border_color="gold",command=lambda: controller.show_frame("ApplyingScreen"),text="APPLY FOR AN ACCOUNT",font=("Arial",30),text_color=text_color,fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1,border_width=5)
        EntryButton.place(anchor="center", relx=0.5, rely=0.45)
        checkButton = ctk.CTkButton(self.big_boi_panel,border_color="gold",text="CHECK AN EXISTING APPLICATION",font=("Arial",30),text_color=text_color,fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1,border_width=5,command=lambda: controller.show_frame("AppliReview"))
        checkButton.place(anchor="center", relx=0.5, rely=0.55)
        Exitbutton = ctk.CTkButton(
            self.big_boi_panel, 
            text="EXIT",
            font=("Arial",20,"bold"),
            command=lambda: controller.show_frame("MainScreen"),
            bg_color=bg_text_color,
            text_color=text_color,
            hover_color=hover_color,
            fg_color=fg_color,
            width=1390,
            corner_radius=1
        )
        Exitbutton.place(anchor="center", relx=0.5, rely=0.97)
class AdminMainScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller


        self.bg_image = ctk.CTkImage(
            light_image=Image.open(background_URL),
            dark_image=Image.open(background_URL),
            size=(1545, 850)
        )
        bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.big_boi_panel = ctk.CTkFrame(self,height=720,width=1000,border_width=5,border_color="gold",fg_color="#050521")
        self.big_boi_panel.place(anchor="center",relx=0.5,rely=0.5)
        label = ctk.CTkLabel(self.big_boi_panel, text="BANK", font=("Arial", 58), text_color=text_color,bg_color=bg_text_color)
        label.place(anchor="center", relx=0.5, rely=0.08)
        label1 = ctk.CTkLabel(self.big_boi_panel, text="ADMIN PLATFORM", font=("Arial", 40), text_color=text_color,bg_color=bg_text_color)
        label1.place(anchor="center", relx=0.5, rely=0.15)
        client_review_Button = ctk.CTkButton(self.big_boi_panel,border_color="gold",command=lambda: controller.show_frame("AppliReviewAdmin"),text="REVIEW CLIENT APPLICATIONS",font=("Arial",30),bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=300,border_width=2)
        client_review_Button.place(anchor="center", relx=0.5, rely=0.45)
        credit_review_Button = ctk.CTkButton(self.big_boi_panel,border_color="gold",command=lambda: controller.show_frame("AdminCreditReview"),text="REVIEW CREDIT CARD APPLICATIONS",font=("Arial",30),bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=300,border_width=2)
        credit_review_Button.place(anchor="center", relx=0.5, rely=0.55)
        debit_review_Button = ctk.CTkButton(self.big_boi_panel,border_color="gold",command=lambda: controller.show_frame("AdminDebitReview"),text="REVIEW DEBIT CARD APPLICATIONS",font=("Arial",30),bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=300,border_width=2)
        debit_review_Button.place(anchor="center", relx=0.5, rely=0.65)
        user_center_Button = ctk.CTkButton(self.big_boi_panel,border_color="gold",command=lambda: controller.show_frame("AdminClientCenterScreen"),text="USER CENTER CONTROL",font=("Arial",30),bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=300,border_width=2)
        user_center_Button.place(anchor="center", relx=0.5, rely=0.75)
        Exitbutton = ctk.CTkButton(self.big_boi_panel,text="EXIT",font=("Arial",20,"bold"),command=lambda: controller.show_frame("MainScreen"),bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=990)
        Exitbutton.place(anchor="center",relx=0.5,rely=0.972)
class ApplyingScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        
        self.bg_image = ctk.CTkImage(
            light_image=Image.open(background_URL),
            dark_image=Image.open(background_URL),
            size=(1545, 850)
        )
        self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.big_boi_panel = ctk.CTkFrame(self,height=750,width=1400,border_width=5,border_color="gold",fg_color="#050521")
        self.big_boi_panel.place(anchor="center",relx=0.5,rely=0.5)
        label1 = ctk.CTkLabel(self.big_boi_panel, text="PLEASE ENTER YOUR PERSONAL INFORMATION", font=("Arial", 40), text_color=text_color,bg_color=bg_text_color)
        label1.place(anchor="center", relx=0.5, rely=0.18)

        
        label = ctk.CTkLabel(self.big_boi_panel, text="BANK", font=("Arial", 58), text_color=text_color,bg_color=bg_text_color)
        label.place(anchor="center", relx=0.5, rely=0.08)

        self.NameLabel = ctk.CTkLabel(self.big_boi_panel, text="FULL NAME : ", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color)
        self.NameEntry = ctk.CTkEntry(self.big_boi_panel,border_color="gold",corner_radius=1,bg_color=bg_text_color,width=400,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30))
        self.NameEntry.place(anchor="center", relx=0.5, rely=0.3)
        self.NameLabel.place(anchor="center", relx=0.3, rely=0.3)

        self.DOBLabel = ctk.CTkLabel(self.big_boi_panel, text="D.O.B : ", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color)
        self.DOBEntry = ctk.CTkEntry(self.big_boi_panel,border_color="gold",corner_radius=1,bg_color=bg_text_color,width=400,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30))
        self.DOBEntry.place(anchor="center", relx=0.5, rely=0.4)
        self.DOBLabel.place(anchor="center", relx=0.33, rely=0.4)

        self.GenderLabel = ctk.CTkLabel(self.big_boi_panel, text="GENDER : ", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color)
        self.GenderEntry = ctk.CTkOptionMenu(self.big_boi_panel,corner_radius=1,bg_color=bg_text_color,width=400,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30),dropdown_fg_color=bg_text_color,dropdown_hover_color="grey",dropdown_font=("Arial", 30),values=["MALE","FEMALE"],button_color="#D4AF37",button_hover_color="#AA820A")
        self.GenderEntry.place(anchor="center", relx=0.5, rely=0.5)
        self.GenderLabel.place(anchor="center", relx=0.313, rely=0.5)

        self.NatLabel = ctk.CTkLabel(self.big_boi_panel, text="NATIONALITY : ", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color)
        self.NatEntry = ctk.CTkEntry(self.big_boi_panel,border_color="gold",corner_radius=1,bg_color=bg_text_color,width=400,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30))
        self.NatEntry.place(anchor="center", relx=0.5, rely=0.6)
        self.NatLabel.place(anchor="center", relx=0.29, rely=0.6)

        self.JobLabel = ctk.CTkLabel(self.big_boi_panel, text="JOB : ", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color)
        self.JobEntry = ctk.CTkEntry(self.big_boi_panel,border_color="gold",corner_radius=1,bg_color=bg_text_color,width=400,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30))
        self.JobEntry.place(anchor="center", relx=0.5, rely=0.7)
        self.JobLabel.place(anchor="center", relx=0.34, rely=0.7)

        self.YearlyLabel = ctk.CTkLabel(self.big_boi_panel, text="YEARLY INCOME : ", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color)
        self.YearlyEntry = ctk.CTkEntry(self.big_boi_panel,border_color="gold",corner_radius=1,bg_color=bg_text_color,width=400,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30))
        self.YearlyEntry.place(anchor="center", relx=0.5, rely=0.8)
        self.YearlyLabel.place(anchor="center", relx=0.27, rely=0.8)

        def adding():
            name = self.NameEntry.get()
            dob = self.DOBEntry.get()
            gender = self.GenderEntry.get()
            natio = self.NatEntry.get()
            job = self.JobEntry.get()
            yrinc = self.YearlyEntry.get()
            s = DB_connection.add_application(name,dob,gender,natio,job,yrinc)
            if s == False:
                self.ErrorLabel.configure(text="PLEASE FILL OUT ALL THE FIELDS")
            if s == True:
                self.ErrorLabel.configure(text="FORUM SUBMITTED SUCCESSFULLY!")
                self.NameEntry.delete(0,"end")
                self.DOBEntry.delete(0,"end")
                self.JobEntry.delete(0,"end")
                self.YearlyEntry.delete(0,"end")
                self.GenderEntry.set("Choose an option...")
                self.NatEntry.delete(0,"end")
            if s == "INCORRECT YRINCOME":
                self.ErrorLabel.configure(text="PLEASE ONLY ENTER DIGITS IN THE YEARLY INCOME FIELD")
        def exitingappli():
            self.NameEntry.delete(0,"end")
            self.DOBEntry.delete(0,"end")
            self.JobEntry.delete(0,"end")
            self.YearlyEntry.delete(0,"end")
            self.GenderEntry.set("Choose an option...")
            self.NatEntry.delete(0,"end")
            self.ErrorLabel.configure(text="")
            self.controller.show_frame("ApplicationMainScreen")
        def clearing():
            self.NameEntry.delete(0,"end")
            self.DOBEntry.delete(0,"end")
            self.JobEntry.delete(0,"end")
            self.YearlyEntry.delete(0,"end")
            self.GenderEntry.set("Choose an option...")
            self.NatEntry.delete(0,"end")
            self.ErrorLabel.configure(text="")
            
        self.SubmitButton = ctk.CTkButton(self.big_boi_panel,text="SUBMIT", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color,hover_color=hover_color,fg_color=fg_color,command=adding)
        self.SubmitButton.place(anchor="center", relx=0.9, rely=0.5)
        self.ClearButton = ctk.CTkButton(self.big_boi_panel,text="CLEAR", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color,hover_color=hover_color,fg_color=fg_color,command=clearing)
        self.ClearButton.place(anchor="center", relx=0.9, rely=0.6)
        self.ErrorLabel = ctk.CTkLabel(self.big_boi_panel, text="", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color)
        self.ErrorLabel.place(anchor="center", relx=0.5, rely=0.9)




        Exitbutton = ctk.CTkButton(
            self, 
            text="EXIT",
            font=("Arial",20,"bold"),
            command=exitingappli,
            bg_color=bg_text_color,
            text_color=text_color,
            hover_color=hover_color,
            fg_color=fg_color,
            corner_radius=1,
            width=1390
            
        )
        Exitbutton.place(anchor="center", relx=0.5, rely=0.92)
class AppliReview(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.bg_image = ctk.CTkImage(
            light_image=Image.open(background_URL),
            dark_image=Image.open(background_URL),
            size=(1545, 850)
        )
        bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.big_boi_panel = ctk.CTkFrame(self,height=750,width=1400,border_width=5,border_color="gold",fg_color="#050521")
        self.big_boi_panel.place(anchor="center",relx=0.5,rely=0.5)
        label = ctk.CTkLabel(self.big_boi_panel, text="BANK", font=("Arial", 58), text_color=text_color,bg_color=bg_text_color)
        label.place(anchor="center", relx=0.5, rely=0.08)

        self.NameLabel = ctk.CTkLabel(self.big_boi_panel, text="ENTER YOUR NAME : ", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color)
        self.NameEntry = ctk.CTkEntry(self.big_boi_panel,border_color="gold",corner_radius=1,bg_color=bg_text_color,width=500,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30))
        self.NameEntry.place(anchor="center", relx=0.585, rely=0.5)
        self.NameLabel.place(anchor="center", relx=0.28, rely=0.5)


        def check_user():
            namee = self.NameEntry.get()
            client_id = DB_connection.get_client_info_id(namee)
            if client_id == False:
                ErrorLabel.configure(text="SORRY! WE COULDN'T FIND A FORUM WITH THAT NAME!")
            else:
                checker= DB_connection.check_if_application_exists(client_id)
                if checker == []:
                    ErrorLabel.configure(text="SORRY! WE COULDN'T FIND A FORUM WITH THAT NAME!")
                else:
                    checker = DB_connection.Review_Single_Application_status(client_id)
                    if checker == "PENDING":
                        ErrorLabel.configure(text="YOUR FORUM IS STILL PENDING REVIEW!")
                    if checker == "REJECTED":
                        ErrorLabel.configure(text="SORRY! YOUR SUBMISSION WAS REJECTED!")
                    if checker == "APPROVED":
                        checker2 = DB_connection.temp_pass_get(client_id)
                        checker3 = DB_connection.application_personal_id_get(client_id)
                        ErrorLabel.configure(text=f"""YOUR SUBMISSION WAS ACCEPTED!\nYOUR ACCOUNT ID : {checker3}\nYOUR TEMPORARY PASSWORD :  {checker2}   """)




        SubmitButton = ctk.CTkButton(self.big_boi_panel,text="CHECK", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color,hover_color=hover_color,fg_color=fg_color,command=check_user,border_color="gold",border_width=5)
        SubmitButton.place(anchor="center", relx=0.85, rely=0.5)
        ErrorLabel = ctk.CTkLabel(self.big_boi_panel, text="", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color,fg_color=fg_color)
        ErrorLabel.place(anchor="center", relx=0.5, rely=0.6)


        def exitingappli():
            self.NameEntry.delete(0,"end")
            ErrorLabel.configure(text="")
            self.controller.show_frame("ApplicationMainScreen")

        Exitbutton = ctk.CTkButton(
            self.big_boi_panel, 
            text="EXIT",
            font=("Arial",20,"bold"),
            command=exitingappli,
            bg_color=bg_text_color,
            text_color=text_color,
            hover_color=hover_color,
            fg_color=fg_color,
            width=1390,
            corner_radius=1
        )
        Exitbutton.place(anchor="center", relx=0.5, rely=0.97)

class AppliReviewAdmin(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.bg_image = ctk.CTkImage(
            light_image=Image.open(background_URL),
            dark_image=Image.open(background_URL),
            size=(1545, 850)
        )
        bg_image_thing = ctk.CTkImage(
            light_image=Image.open("D:/opera gx downloads/image (3).png"),
            dark_image=Image.open("D:/opera gx downloads/image (3).png"),
            size=(1545, 850)
        )
        bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.big_boi_panel = ctk.CTkFrame(self,height=750,width=1400,border_width=5,border_color="gold",fg_color="#050521")
        self.big_boi_panel.place(anchor="center",relx=0.5,rely=0.5)
        label = ctk.CTkLabel(self.big_boi_panel, text="BANK", font=("Arial", 58), text_color=text_color,bg_color=bg_text_color)
        label.place(anchor="center", relx=0.5, rely=0.08)

        label1 = ctk.CTkLabel(self.big_boi_panel,text="SUBMISSIONS AWAITING REVIEW", font=("Arial", 40), text_color=text_color,bg_color=bg_text_color)
        label1.place(anchor="center", relx=0.5, rely=0.15)
        self.E1rrorLabel = ctk.CTkLabel(self.big_boi_panel, text="", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color)
        self.E1rrorLabel.place(anchor="center", relx=0.5, rely=0.92)
        def Display_forums():
            for widget in self.application_box.winfo_children():
                widget.destroy()
            info = DB_connection.review_client_info()
            appli = DB_connection.review_applications()
            for i in range(len(info)):
                if appli[i][2] == "PENDING":
                    card = ctk.CTkFrame(self.application_box, fg_color="#2b2b2b", corner_radius=8)
                    card.pack(fill="x", pady=8, padx=5, side="top")
                    info_text = f" {appli[i][0]} |  {info[i][1]} |  {info[i][2]} | {info[i][3]} | {info[i][4]} | {info[i][5]} | {appli[i][2]}"
                    info_label = ctk.CTkLabel(card,text=info_text, font=("Arial", 24), text_color=text_color)
                    info_label.pack(side="left", padx=15, pady=10)
               
        self.application_box = ctk.CTkScrollableFrame(self.big_boi_panel,label_text=f"ID    NAME     D.O.B     GENDER   NATIONALITY   JOB   YEARLY   INCOME   STATUS ",label_font=("Arial",20),width=900,height=400,corner_radius=15,fg_color="#1e1e1e",border_color="gold",border_width=2)
        self.application_box.place(anchor="center", relx=0.5, rely=0.55)
        self.RefreshButton = ctk.CTkButton(self.big_boi_panel,border_color="gold",text="REFRESH",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,border_width=5,corner_radius=1,command=Display_forums)
        self.RefreshButton.place(anchor="center", relx=0.9, rely=0.3)
        self.ID_entry = ctk.CTkEntry(self.big_boi_panel,border_color="gold",corner_radius=1,bg_color=bg_text_color,width=10,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30))
        self.ID_entry.place(anchor="center", relx=0.9, rely=0.4)
        self.temp_pass_label = ctk.CTkEntry(self.big_boi_panel,placeholder_text="enter a temporary password for the client",border_color="Gold",border_width=2,bg_color=bg_text_color,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30),width=560)
        self.personal_id_label = ctk.CTkEntry(self.big_boi_panel,placeholder_text="enter a personal ID for the client",border_color="Gold",border_width=2,bg_color=bg_text_color,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30),width=500)
        def preapprdecision():
            self.giant_friggin_frame = ctk.CTkLabel(self,image=bg_image_thing,text="")
            self.giant_friggin_frame.place(x=0,y=0,relwidth=1, relheight=1)
            self.confirmButton = ctk.CTkButton(self.giant_friggin_frame,border_color="gold",text="Confirm",font=("Arial",30),fg_color="#00C300",bg_color=bg_text_color,hover_color="#007600",corner_radius=1)
            self.temp_pass_label = ctk.CTkEntry(self.giant_friggin_frame,placeholder_text="enter a temporary password for the client",border_color="Gold",border_width=2,bg_color=bg_text_color,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30),width=560)
            self.personal_id_label = ctk.CTkEntry(self.giant_friggin_frame,placeholder_text="enter a personal ID for the client",border_color="Gold",border_width=2,bg_color=bg_text_color,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30),width=500)
            self.personal_id_label.place(anchor="center", relx=0.5, rely=0.5,)
            self.temp_pass_label.place(anchor="center", relx=0.5, rely=0.6,)
            self.confirmButton.configure(command=apprdecision)
            self.confirmButton.place(anchor="center", relx=0.5, rely=0.7)
        def apprdecision():
            password = self.temp_pass_label.get()
            personal_id = self.personal_id_label.get()
            if personal_id != None:
                personal_id_with_check = DB_connection.personal_id_check(personal_id)
                if personal_id_with_check == []:
                    id_gette = self.ID_entry.get()
                    try:
                        id_getter = int(id_gette)
                        if id_getter != None and password != None and personal_id != None:
                            DB_connection.application_decision(id_getter,"APPROVED")
                            DB_connection.temp_pass_set(id_getter,password)
                            DB_connection.application_personal_id_set(id_getter,personal_id)
                            DB_connection.add_client_acc(personal_id,id_getter,password)
                            self.E1rrorLabel.configure(text=f"SUBMISSION ID : {id_getter} WAS ACCEPTED!")
                            self.personal_id_label.destroy()
                            self.temp_pass_label.destroy()
                            self.confirmButton.destroy()
                            self.ID_entry.delete(0,"end")
                            self.giant_friggin_frame.destroy()
                            Display_forums()
                        else:
                            self.E1rrorLabel.configure(text="PLEASE ENTER AN ID!")
                    except ValueError:
                        self.E1rrorLabel.configure(text=f"PLEASE ENTER A VALID ID!")
                else:
                    self.E1rrorLabel.configure(text=f"THIS ID IS ALREADY TIED TO ANOTHER ACCOUNT, TRY A DIFFERENT ID!")
        def rejdecision():
            id_gette = self.ID_entry.get()
            try:
                id_getter = int(id_gette)
                if id_getter != None:
                    DB_connection.application_decision(id_getter,"REJECTED")
                    self.E1rrorLabel.configure(text=f"SUBMISSION ID : {id_getter} WAS REJECTED!")
                    self.ID_entry.delete(0,"end")
                    Display_forums()
                else:
                    self.E1rrorLabel.configure(text="PLEASE ENTER AN ID!")
            except ValueError:
                self.E1rrorLabel.configure(text=f"PLEASE ENTER A VALID ID!")
        self.confirmButton = ctk.CTkButton(self.big_boi_panel,border_color="gold",text="Confirm",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1,border_width=5)
        self.approveButton = ctk.CTkButton(self.big_boi_panel,command=preapprdecision,border_color="gold",text="APPROVE",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1,border_width=5)
        self.approveButton.place(anchor="center", relx=0.9, rely=0.5)

        self.denyButton = ctk.CTkButton(self.big_boi_panel,command=rejdecision,border_color="gold",text="DENY",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1,border_width=5)
        self.denyButton.place(anchor="center", relx=0.9, rely=0.6)
        self.giant_friggin_frame = None
        def exitingappli():
            self.ID_entry.delete(0,"end")
            self.E1rrorLabel.configure(text="")
            self.controller.show_frame("AdminMainScreen")
        Exitbutton = ctk.CTkButton(
            self.big_boi_panel, 
            text="EXIT",
            font=("Arial",20,"bold"),
            command=exitingappli,
            bg_color=bg_text_color,
            text_color=text_color,
            hover_color=hover_color,
            fg_color=fg_color,
            width=1390,
            corner_radius=1
        )
        Exitbutton.place(anchor="center", relx=0.5, rely=0.97)
class AdminClientCenterScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.bg_image = ctk.CTkImage(
            light_image=Image.open(background_URL),
            dark_image=Image.open(background_URL),
            size=(1545, 850)
        )
        bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.big_boi_panel = ctk.CTkFrame(self,height=750,width=1400,border_width=5,border_color="gold",fg_color="#050521")
        self.big_boi_panel.place(anchor="center",relx=0.5,rely=0.5)
        label = ctk.CTkLabel(self.big_boi_panel, text="BANK", font=("Arial", 58), text_color=text_color,bg_color=bg_text_color)
        label.place(anchor="center", relx=0.5, rely=0.08)

        label1 = ctk.CTkLabel(self.big_boi_panel, text="CLIENT CENTER PLATFORM", font=("Arial", 40), text_color=text_color,bg_color=bg_text_color)
        label1.place(anchor="center", relx=0.5, rely=0.15)

        EntryButton = ctk.CTkButton(self.big_boi_panel,border_color="gold",command=lambda: controller.show_frame("AdminClientDisplayAll"),text="DISPLAY ALL CLIENT ACCOUNTS",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1,border_width=5)
        EntryButton.place(anchor="center", relx=0.5, rely=0.45)
        checkButton = ctk.CTkButton(self.big_boi_panel,border_color="gold",text="DISPLAY AN ACCOUNT'S DETAILS",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1,command=lambda: controller.show_frame("AdminClientDisplaySingle"),border_width=5)
        checkButton.place(anchor="center", relx=0.5, rely=0.55)
        Entry1Button = ctk.CTkButton(self.big_boi_panel,border_color="gold",command=lambda: controller.show_frame("AdminMessageDisplayAll"),text="CHECK SUPPORT TICKETS",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1,border_width=5)
        Entry1Button.place(anchor="center", relx=0.5, rely=0.65)
        check1Button = ctk.CTkButton(self.big_boi_panel,border_color="gold",text="CREDIT CARD PLATFORM",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1,command=lambda: controller.show_frame("AppliReview"),border_width=5)
        check1Button.place(anchor="center", relx=0.5, rely=0.75)
        Exitbutton = ctk.CTkButton(
            self.big_boi_panel, 
            text="EXIT",
            font=("Arial",20,"bold"),
            command=lambda: controller.show_frame("AdminMainScreen"),
            bg_color=bg_text_color,
            text_color=text_color,
            hover_color=hover_color,
            fg_color=fg_color,
            width=1390,
            corner_radius=1
        )
        Exitbutton.place(anchor="center", relx=0.5, rely=0.97)
class AdminClientDisplayAll(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.bg_image = ctk.CTkImage(
            light_image=Image.open(background_URL),
            dark_image=Image.open(background_URL),
            size=(1545, 850)
        )
        bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.big_boi_panel = ctk.CTkFrame(self,height=750,width=1400,border_width=5,border_color="gold",fg_color="#050521")
        self.big_boi_panel.place(anchor="center",relx=0.5,rely=0.5)
        label = ctk.CTkLabel(self.big_boi_panel, text="BANK", font=("Arial", 58), text_color=text_color,bg_color=bg_text_color)
        label.place(anchor="center", relx=0.5, rely=0.08)

        label1 = ctk.CTkLabel(self.big_boi_panel,text="ALL CLIENT ACCOUNTS", font=("Arial", 40), text_color=text_color,bg_color=bg_text_color)
        label1.place(anchor="center", relx=0.5, rely=0.15)
        self.E1rrorLabel = ctk.CTkLabel(self.big_boi_panel, text="", font=("Arial", 20), text_color=text_color,bg_color=bg_text_color)
        self.E1rrorLabel.place(anchor="center", relx=0.5, rely=0.92)
        def Display_forums():
            for widget in self.application_box.winfo_children():
                widget.destroy()
            info = DB_connection.review_clients()
            lock = ""
            for i in range(len(info)):
                if info[i][4] == 0:
                    lock = "UNLOCKED"
                if info[i][4] == 1:
                    lock = "LOCKED"
                name = DB_connection.get_client_name(info[i][2])
                card = ctk.CTkFrame(self.application_box, fg_color="#2b2b2b", corner_radius=8)
                card.pack(fill="x", pady=8, padx=5, side="top")
                info_text = f"      {info[i][0]}     |      {info[i][1]}     |      {name}     |     {lock}"
                info_label = ctk.CTkLabel(card,text=info_text, font=("Arial", 24), text_color=text_color)
                info_label.pack(side="left", padx=15, pady=10)
               
        self.application_box = ctk.CTkScrollableFrame(self.big_boi_panel,label_text=f"ID          PERSONAL       ID         NAME         LOCK",label_font=("Arial",20),width=650,height=400,corner_radius=15,fg_color="#1e1e1e",border_color="gold",border_width=2)
        self.application_box.place(anchor="center", relx=0.5, rely=0.55)
        self.RefreshButton = ctk.CTkButton(self.big_boi_panel,border_color="gold",text="REFRESH",font=("Arial",30),fg_color=bg_text_color,bg_color=bg_text_color,hover_color="grey",corner_radius=1,command=Display_forums)
        self.RefreshButton.place(anchor="center", relx=0.9, rely=0.3)
        self.ID_entry = ctk.CTkEntry(self.big_boi_panel,border_color="gold",corner_radius=1,bg_color=bg_text_color,width=10,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30))
        self.ID_entry.place(anchor="center", relx=0.9, rely=0.4)
        def lockAcc():
                id_gette = self.ID_entry.get()
                try:
                    id_getter = int(id_gette)
                    if id_getter != None:
                        DB_connection.client_acc_lock(id_getter)
                        self.E1rrorLabel.configure(text=f"CLIENT ACCOUNT WITH ID : {id_getter} IS NOW LOCKED!")
                        self.ID_entry.delete(0,"end")
                        Display_forums()
                    else:
                        self.E1rrorLabel.configure(text="PLEASE ENTER AN ID!")
                except ValueError:
                    self.E1rrorLabel.configure(text=f"PLEASE ENTER A VALID ID!")
        def unlockAcc():
                id_gette = self.ID_entry.get()
                try:
                    id_getter = int(id_gette)
                    if id_getter != None:
                        DB_connection.client_acc_unlock(id_getter)
                        self.E1rrorLabel.configure(text=f"CLIENT ACCOUNT WITH ID : {id_getter} IS NOW UNLOCKED!")
                        self.ID_entry.delete(0,"end")
                        Display_forums()
                    else:
                        self.E1rrorLabel.configure(text="PLEASE ENTER AN ID!")
                except ValueError:
                    self.E1rrorLabel.configure(text=f"PLEASE ENTER A VALID ID!")
        def delAcc():
                self.ConfirmdeleteButton.destroy()
                self.DenydeleteButton.destroy()
                id_gette = self.ID_entry.get()
                try:
                    id_getter = int(id_gette)
                    if id_getter != None:
                        DB_connection.delete_client_acc(id_getter)
                        self.E1rrorLabel.configure(text=f"CLIENT ACCOUNT WITH ID : {id_getter} WAS DELETED!")
                        self.ID_entry.delete(0,"end")
                        Display_forums()
                    else:
                        self.E1rrorLabel.configure(text="PLEASE ENTER AN ID!")
                except ValueError:
                    self.E1rrorLabel.configure(text=f"PLEASE ENTER A VALID ID!")
        def deny_del():
            self.ConfirmdeleteButton.destroy()
            self.DenydeleteButton.destroy()
            Display_forums()
        def display_options():
            self.ConfirmdeleteButton = ctk.CTkButton(self.big_boi_panel,command=delAcc,border_color="gold",text="CONFIRM",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1)
            self.DenydeleteButton= ctk.CTkButton(self.big_boi_panel,command=deny_del,border_color="gold",text="DENY",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1)
            self.DenydeleteButton.place(anchor="center", relx=0.6, rely=0.5)
            self.ConfirmdeleteButton.place(anchor="center", relx=0.4, rely=0.5)
        self.approveButton = ctk.CTkButton(self.big_boi_panel,command=lockAcc,border_color="gold",text="LOCK",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1)
        self.approveButton.place(anchor="center", relx=0.9, rely=0.5)

        self.denyButton = ctk.CTkButton(self.big_boi_panel,command=unlockAcc,border_color="gold",text="UNLOCK",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1)
        self.denyButton.place(anchor="center", relx=0.9, rely=0.6)

        self.deleteButton = ctk.CTkButton(self.big_boi_panel,command=display_options,border_color="gold",text="DELETE",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1)
        self.deleteButton.place(anchor="center", relx=0.9, rely=0.7)
        self.ConfirmdeleteButton = ctk.CTkButton(self.big_boi_panel,command=delAcc,border_color="gold",text="CONFIRM",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1)
        self.DenydeleteButton= ctk.CTkButton(self.big_boi_panel,command=deny_del,border_color="gold",text="CANCEL",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1)
        def exitingappli():
            self.ID_entry.delete(0,"end")
            self.E1rrorLabel.configure(text="")
            self.controller.show_frame("AdminClientCenterScreen")
        Exitbutton = ctk.CTkButton(
            self.big_boi_panel, 
            text="EXIT",
            font=("Arial",20,"bold"),
            command=exitingappli,
            bg_color=bg_text_color,
            text_color=text_color,
            hover_color=hover_color,
            fg_color=fg_color,
            width=1390,
            corner_radius=1
        )
        Exitbutton.place(anchor="center", relx=0.5, rely=0.97)
class AdminClientDisplaySingle(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.bg_image = ctk.CTkImage(
            light_image=Image.open(background_URL),
            dark_image=Image.open(background_URL),
            size=(1545, 850)
        )
        bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.big_boi_panel = ctk.CTkFrame(self,height=750,width=1400,border_width=5,border_color="gold",fg_color="#050521")
        self.big_boi_panel.place(anchor="center",relx=0.5,rely=0.5)
        label = ctk.CTkLabel(self.big_boi_panel, text="BANK", font=("Arial", 58), text_color=text_color,bg_color=bg_text_color)
        label.place(anchor="center", relx=0.5, rely=0.08)
        label1 = ctk.CTkLabel(self.big_boi_panel,text="SINGLE ACC INFO PLATFORM", font=("Arial", 40), text_color=text_color,bg_color=bg_text_color)
        label1.place(anchor="center", relx=0.5, rely=0.15)
        Exitbutton = ctk.CTkButton(
            self.big_boi_panel, 
            text="EXIT",
            font=("Arial",20,"bold"),
            command=lambda:controller.show_frame("AdminClientCenterScreen"),
            bg_color=bg_text_color,
            text_color=text_color,
            hover_color=hover_color,
            fg_color=fg_color,
            width=1390,
            corner_radius=1
            )
        Exitbutton.place(anchor="center", relx=0.5, rely=0.97)
        self.E1rrorLabel = ctk.CTkLabel(self.big_boi_panel, text="", font=("Arial", 26), text_color=text_color,bg_color=bg_text_color)
        self.E1rrorLabel.place(anchor="center", relx=0.5, rely=0.9)
        self.database_id_Button = ctk.CTkButton(self.big_boi_panel)
        self.personal_ID_Button = ctk.CTkButton(self.big_boi_panel)
        self.confirmButton = ctk.CTkButton(self.big_boi_panel)
        self.personal_id_entry = ctk.CTkEntry(self.big_boi_panel)
        self.database_id_entry = ctk.CTkEntry(self.big_boi_panel)
        self.exit_info_button = ctk.CTkButton(self.big_boi_panel)
        self.info_label = ctk.CTkLabel(self.big_boi_panel)
        self.cancelButton = ctk.CTkButton(self.big_boi_panel)
        def reset_display():
            self.E1rrorLabel.configure(text="")
            self.database_id_Button.destroy() 
            self.personal_ID_Button.destroy() 
            self.confirmButton.destroy()
            self.cancelButton.destroy()
            self.personal_id_entry.destroy()
            self.database_id_entry.destroy()
            self.exit_info_button.destroy()
            self.info_label.destroy()
            self.check_button = ctk.CTkButton(self,command=Display_check_options,border_color="gold",text="CHECK",font=("Arial",30),fg_color=bg_text_color,bg_color=bg_text_color,hover_color="grey",corner_radius=1)
            self.check_button.place(anchor="center",relx=0.5,rely=0.5)
            self.database_id_Button = ctk.CTkButton(self.big_boi_panel)
            self.personal_ID_Button = ctk.CTkButton(self.big_boi_panel)
            self.confirmButton = ctk.CTkButton(self.big_boi_panel)
            self.cancelButton = ctk.CTkButton(self.big_boi_panel)
            self.personal_id_entry = ctk.CTkEntry(self.big_boi_panel)
            self.database_id_entry = ctk.CTkEntry(self.big_boi_panel)
            self.exit_info_button = ctk.CTkButton(self.big_boi_panel)
            self.info_label = ctk.CTkLabel(self.big_boi_panel)

        def Display_check_options():
            self.check_button.destroy()
            self.confirmButton.configure(border_color="gold",text="Confirm",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1,border_width=5)
            self.cancelButton.configure(border_color="gold",text="Cancel",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1,border_width=5)
            self.database_id_Button.configure(command=database_id_entry,border_color="gold",text="DATABASE ID",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1,border_width=5)
            self.personal_ID_Button.configure(command=personal_id_entry,border_color="gold",text="PERSONAL ID",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1,border_width=5)
            self.personal_ID_Button.place(anchor="center", relx=0.4, rely=0.5)
            self.database_id_Button.place(anchor="center", relx=0.6, rely=0.5)
        self.check_button = ctk.CTkButton(self.big_boi_panel,command=Display_check_options,border_color="gold",text="CHECK",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1,border_width=5)
        self.check_button.place(anchor="center",relx=0.5,rely=0.5)
        def personal_id_entry():
            self.check_button.destroy()
            self.database_id_Button.destroy()
            self.personal_ID_Button.destroy()
            self.personal_id_entry.configure(placeholder_text="enter the client's personal ID",border_color="Gold",border_width=2,bg_color=bg_text_color,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30),width=500)
            self.personal_id_entry.place(anchor="center", relx=0.5, rely=0.5,)
            self.confirmButton.configure(command=info_get_personal)
            self.confirmButton.place(anchor="center", relx=0.5, rely=0.6)
            self.cancelButton.configure(command=reset_display)
            self.cancelButton.place(anchor="center", relx=0.5, rely=0.7)
        def database_id_entry():
            self.database_id_Button.destroy()
            self.personal_ID_Button.destroy()
            self.database_id_entry.configure(placeholder_text="enter the client's database ID",border_color="Gold",border_width=2,bg_color=bg_text_color,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30),width=500)
            self.database_id_entry.place(anchor="center", relx=0.5, rely=0.5)
            self.confirmButton.configure(command=info_get_database)
            self.confirmButton.place(anchor="center", relx=0.5, rely=0.6)
            self.cancelButton.configure(command=reset_display)
            self.cancelButton.place(anchor="center", relx=0.5, rely=0.7)
        def info_get_database():
            d_id = self.database_id_entry.get()
            lock = ""
            try:
                id_getter = int(d_id)
                if id_getter != None:
                    checker = DB_connection.database_id_check(id_getter)
                    if checker != []:
                        self.cancelButton.destroy()
                        center_info = DB_connection.client_center_singular_databaseID(id_getter)
                        details_info = DB_connection.client_info_singular(center_info[0][2])
                        if center_info[0][4] == 0:
                            lock = "UNLOCKED"
                        else:
                            lock = "LOCKED"
                        if center_info[0][7] == None:
                            info_text = f"DATABASE ID : {center_info[0][0]} || PERSONAL ID : {center_info[0][1]} || PERSONAL INFORMATION ID : {center_info[0][2]}\n\n               PERSONAL INFORMATION\n====================================\nNAME : {details_info[0][1]} || D.O.B : {details_info[0][2]} || GENDER : {details_info[0][3]}\n\nNATIONALITY : {details_info[0][4]} || JOB : {details_info[0][5]} || YEARLY INCOME : {details_info[0][3]}\n\nLOCK : {lock} || REMAINING LOGIN ATTEMPTS : {center_info[0][5]} || CURRENT BALANCE : {center_info[0][6]}"
                        else:
                            if center_info[0][10] == 0:
                                c_lock = "UNLOCKED"
                            else:
                                c_lock = "LOCKED"
                            info_text = f"DATABASE ID : {center_info[0][0]} || PERSONAL ID : {center_info[0][1]} || PERSONAL INFORMATION ID : {center_info[0][2]}\n\n               PERSONAL INFORMATION\n====================================\nNAME : {details_info[0][1]} || D.O.B : {details_info[0][2]} || GENDER : {details_info[0][3]}\n\nNATIONALITY : {details_info[0][4]} || JOB : {details_info[0][5]} || YEARLY INCOME : {details_info[0][3]}\n\nLOCK : {lock} || REMAINING LOGIN ATTEMPTS : {center_info[0][5]} || CURRENT BALANCE : {center_info[0][6]}\n\nCREDIT CARD ID : {center_info[0][7]} || CREDIT LIMIT : {center_info[0][8]} || CURRENT CREDIT BALANCE : {center_info[0][9]}\n\nCREDIT CARD LOCK : {c_lock}"
                        self.info_label.configure(text=info_text, font=("Arial", 24), text_color=text_color,bg_color=bg_text_color,fg_color=bg_text_color)
                        self.exit_info_button.configure(command=reset_display,border_color="gold",text="CLOSE",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1,border_width=5)
                        self.info_label.place(anchor="center",relx=0.5,rely=0.5)
                        self.exit_info_button.place(anchor="center",relx=0.5,rely=0.8)
                    else:
                        self.E1rrorLabel.configure(text="NO CLIENT WITH THAT ID EXISTS!")

            except ValueError:
                self.E1rrorLabel.configure(text="PLEASE ENTER A VALID ID!")
        def info_get_personal():
            d_id = self.personal_id_entry.get()
            lock = ""
            try:
                id_getter = str(d_id)
                if id_getter != None:
                    self.cancelButton.destroy()
                    checker = DB_connection.personal_id_check(id_getter)
                    if checker != []:
                        center_info = DB_connection.client_center_singular_personalID(id_getter)
                        details_info = DB_connection.client_info_singular(center_info[0][2])
                        if center_info[0][4] == 0:
                            lock = "UNLOCKED"
                        else:
                            lock = "LOCKED"
                        if center_info[0][7] == None:
                            info_text = f"DATABASE ID : {center_info[0][0]} || PERSONAL ID : {center_info[0][1]} || PERSONAL INFORMATION ID : {center_info[0][2]}\n\n               PERSONAL INFORMATION\n====================================\nNAME : {details_info[0][1]} || D.O.B : {details_info[0][2]} || GENDER : {details_info[0][3]}\n\nNATIONALITY : {details_info[0][4]} || JOB : {details_info[0][5]} || YEARLY INCOME : {details_info[0][3]}\n\nLOCK : {lock} || REMAINING LOGIN ATTEMPTS : {center_info[0][5]} || CURRENT BALANCE : {center_info[0][6]}"
                        else:
                            if center_info[0][10] == 0:
                                c_lock = "UNLOCKED"
                            else:
                                c_lock = "LOCKED"
                            info_text = f"DATABASE ID : {center_info[0][0]} || PERSONAL ID : {center_info[0][1]} || PERSONAL INFORMATION ID : {center_info[0][2]}\n\n               PERSONAL INFORMATION\n====================================\nNAME : {details_info[0][1]} || D.O.B : {details_info[0][2]} || GENDER : {details_info[0][3]}\n\nNATIONALITY : {details_info[0][4]} || JOB : {details_info[0][5]} || YEARLY INCOME : {details_info[0][3]}\n\nLOCK : {lock} || REMAINING LOGIN ATTEMPTS : {center_info[0][5]} || CURRENT BALANCE : {center_info[0][6]}\n\nCREDIT CARD ID : {center_info[0][7]} || CREDIT LIMIT : {center_info[0][8]} || CURRENT CREDIT BALANCE : {center_info[0][9]}\n\nCREDIT CARD LOCK : {c_lock}"
                        self.info_label.configure(text=info_text, font=("Arial", 24), text_color=text_color,bg_color=bg_text_color,fg_color=bg_text_color)
                        self.exit_info_button.configure(command=reset_display,border_color="gold",text="CLOSE",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1,border_width=5)
                        self.info_label.place(anchor="center",relx=0.5,rely=0.5)
                        self.exit_info_button.place(anchor="center",relx=0.5,rely=0.8)
                    else:
                        self.E1rrorLabel.configure(text="NO USER WITH THAT ID EXISTS!")


            except ValueError:
                self.E1rrorLabel.configure(text="PLEASE ENTER A VALID ID!")
class ClientCenterScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # 1. Apply the exact same background image INSIDE this screen too
        self.bg_image = ctk.CTkImage(
            light_image=Image.open(background_URL),
            dark_image=Image.open(background_URL),
            size=(1545, 850)
        )
        bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        label = ctk.CTkLabel(self, text="BANK", font=("Arial", 58), text_color=text_color,bg_color=bg_text_color)
        label.place(anchor="center", relx=0.5, rely=0.08)
        # 2. Add your interactive widgets on top of the image
        label1 = ctk.CTkLabel(self, text="CLIENT CENTER PLATFORM", font=("Arial", 40), text_color=text_color,bg_color=bg_text_color)
        label1.place(anchor="center", relx=0.5, rely=0.15)

        EntryButton = ctk.CTkButton(self,border_color="gold",command=lambda: controller.show_frame("AdminClientDisplayAll"),text="DISPLAY ALL CLIENT ACCOUNTS",font=("Arial",30),fg_color=bg_text_color,bg_color=bg_text_color,hover_color="grey",corner_radius=1)
        EntryButton.place(anchor="center", relx=0.5, rely=0.35)
        checkButton = ctk.CTkButton(self,border_color="gold",text="DISPLAY AN ACCOUNT'S DETAILS",font=("Arial",30),fg_color=bg_text_color,bg_color=bg_text_color,hover_color="grey",corner_radius=1,command=lambda: controller.show_frame("AdminClientDisplaySingle"))
        checkButton.place(anchor="center", relx=0.5, rely=0.45)
        Entry1Button = ctk.CTkButton(self,border_color="gold",command=lambda: controller.show_frame("AppliReviewAdmin"),text="CHECK SUPPORT TICKETS",font=("Arial",30),fg_color=bg_text_color,bg_color=bg_text_color,hover_color="grey",corner_radius=1)
        Entry1Button.place(anchor="center", relx=0.5, rely=0.55)
        check1Button = ctk.CTkButton(self,border_color="gold",text="CREDIT CARD PLATFORM",font=("Arial",30),fg_color=bg_text_color,bg_color=bg_text_color,hover_color="grey",corner_radius=1,command=lambda: controller.show_frame("AppliReview"))
        check1Button.place(anchor="center", relx=0.5, rely=0.65)
        Exitbutton = ctk.CTkButton(
            self, 
            text="EXIT",
            command=lambda: controller.show_frame("AdminMainScreen"),
            bg_color=bg_text_color,
            text_color=text_color,
            hover_color="grey",
            fg_color="dark red",
            corner_radius=1
        )
        Exitbutton.place(anchor="center", relx=0.92, rely=0.8)

class ClientCenterLoginScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.bg_image = ctk.CTkImage(
            light_image=Image.open(background_URL),
            dark_image=Image.open(background_URL),
            size=(1545, 850)
        )
        bg_image_thing = ctk.CTkImage(
            light_image=Image.open("D:/opera gx downloads/image (3).png"),
            dark_image=Image.open("D:/opera gx downloads/image (3).png"),
            size=(1545, 850)
        )
        bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.big_boi_panel = ctk.CTkFrame(self,height=750,width=1400,border_width=5,border_color="gold",fg_color="#050521")
        self.big_boi_panel.place(anchor="center",relx=0.5,rely=0.5)
        label = ctk.CTkLabel(self.big_boi_panel, text="BANK", font=("Arial", 58), text_color=text_color,bg_color=bg_text_color)
        label.place(anchor="center", relx=0.5, rely=0.08)

        label1 = ctk.CTkLabel(self.big_boi_panel, text="CLIENT LOGIN", font=("Arial", 40), text_color=text_color,bg_color=bg_text_color)
        label1.place(anchor="center", relx=0.5, rely=0.15)
        self.E1rrorLabel = ctk.CTkLabel(self.big_boi_panel, text="", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color)
        self.E1rrorLabel.place(anchor="center", relx=0.5, rely=0.85)
        self.attemptsLabel = ctk.CTkLabel(self.big_boi_panel, text="", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color)
        self.attemptsLabel.place(anchor="center", relx=0.5, rely=0.75)
        self.submitMessageLabel = ctk.CTkLabel(self.big_boi_panel, text="", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color)
        self.submitMessageLabel.place(anchor="center", relx=0.8, rely=0.85)
        def reset_screen():
            self.personal_id_entry.delete(0,"end")
            self.password_entry.delete(0,"end")
        def login():
            personal_id = self.personal_id_entry.get()
            password = self.password_entry.get()
            password = str(password)
            if personal_id == "":
                self.E1rrorLabel.configure(text="PLEASE ENTER AN ID!")
            elif password == "":
                self.E1rrorLabel.configure(text="PLEASE ENTER A PASSWORD!")
            else:
                IDchecker = DB_connection.personal_id_check(personal_id)
                if IDchecker == []:
                    self.E1rrorLabel.configure(text="WE COULDN'T FIND AN ACCOUNT WITH THAT ID, PLEASE TRY AGAIN!")
                    reset_screen()
                else:
                    attempts = DB_connection.client_get_remaining_login_attempts(personal_id)
                    if attempts > 0:
                        checker = DB_connection.client_password_check(personal_id,password)
                        if checker == "valid":
                            reset_screen()
                            session_data["client_id"] = personal_id
                            DB_connection.client_login_attempts_set(personal_id,3)
                            DB_connection.application_record_delete_personal_id(personal_id)
                            self.E1rrorLabel.configure(text="")
                            self.attemptsLabel.configure(text="")
                            controller.show_frame("ClientMainScreen")
                        if checker == "invalid":
                            reset_screen()
                            self.E1rrorLabel.configure(text="INCORRECT PASSWORD OR ID! TRY AGAIN!")
                            attempts -= 1
                            loginattemptstext = f"REMAINING LOGIN ATTEMPTS : {attempts}"
                            self.attemptsLabel.configure(text=loginattemptstext)
                            DB_connection.client_login_attempts_set(personal_id,attempts)
                    elif attempts <= 0:
                            reset_screen()
                            DB_connection.client_acc_login_lock(personal_id)
                            self.E1rrorLabel.configure(text="YOUR ACCOUNT IS LOCKED, PLEASE CONTACT OUR ADMINS FOR SUPPORT.", text_color="red")
                            if self.message_button is None:
                                self.message_button = ctk.CTkButton(
                                self.big_boi_panel,
                                border_color=text_color,
                                command=message,
                                text="contact support",
                                font=("Arial", 30),
                                fg_color=fg_color,
                                bg_color=bg_text_color,
                                hover_color=hover_color,
                                corner_radius=1,
                                border_width=5
                            )
                            self.message_button.place(anchor="center", relx=0.7, rely=0.65)
        def message():
                self.giant_friggin_frame = ctk.CTkLabel(self,image=bg_image_thing,text="")
                self.giant_friggin_frame.place(x=0,y=0,relwidth=1, relheight=1)
                self.submit_message_button = ctk.CTkButton(self.giant_friggin_frame,border_color=text_color,command=submit_message,text="SEND",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1)
                self.ReasonEntry = ctk.CTkOptionMenu(self.giant_friggin_frame,corner_radius=1,bg_color=bg_text_color,width=400,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30),dropdown_fg_color=bg_text_color,dropdown_hover_color=hover_color,dropdown_font=("Arial", 30),values=["ACCOUNT LOCK","FORGOT PASSWORD","FORGOT PERSONAL ID"])
                self.message_entry = ctk.CTkEntry(self.giant_friggin_frame,placeholder_text="     enter your message ",border_color="gold",fg_color=bg_text_color,bg_color=bg_text_color,font=("Arial",30),text_color=text_color,width=450)
                self.submit_message_button = ctk.CTkButton(self.giant_friggin_frame,border_color=text_color,command=submit_message,text="SEND",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1)
                self.ReasonEntry.place(anchor="center",relx=0.5,rely=0.3)
                self.message_entry.place(anchor="center",relx=0.5,rely=0.4)
                self.submit_message_button.place(anchor="center",relx=0.5,rely=0.5)
        def submit_message():
            time = dt.now()
            time = time.strftime('%Y/%m/%d | %I:%M %p')
            personal_id = self.personal_id_entry.get()
            Reasonchoice = self.ReasonEntry.get()
            message = self.message_entry.get()
            DB_connection.client_add_support_message(personal_id,Reasonchoice,message,time)
            self.ReasonEntry.destroy()
            self.message_entry.destroy()
            self.submit_message_button.destroy()
            self.giant_friggin_frame.destroy()
            self.E1rrorLabel.configure(text="")
            self.message_button.destroy()
            self.message_button = ctk.CTkButton(
                                self.big_boi_panel,
                                border_color=text_color,
                                command=message,
                                text="contact support",
                                font=("Arial", 30),
                                fg_color=fg_color,
                                bg_color=bg_text_color,
                                hover_color=hover_color,
                                corner_radius=1,
                                border_width=5)
        self.message_button = ctk.CTkButton(
                                self.big_boi_panel,
                                border_color=text_color,
                                command=message,
                                text="contact support",
                                font=("Arial", 30),
                                fg_color=fg_color,
                                bg_color=bg_text_color,
                                hover_color=hover_color,
                                corner_radius=1,
                                border_width=5)
        self.message_button.place(anchor="center", relx=0.7, rely=0.65)

        self.giant_friggin_frame = None
        self.submit_message_button = None
        self.ReasonEntry = None
        self.message_entry = None
        self.message_button = ctk.CTkButton(
                                self.big_boi_panel,
                                border_color=text_color,
                                command=message,
                                text="contact support",
                                font=("Arial", 30),
                                fg_color=fg_color,
                                bg_color=bg_text_color,
                                hover_color=hover_color,
                                corner_radius=1,
                                border_width=5)
        self.personal_id_entry = ctk.CTkEntry(self.big_boi_panel,placeholder_text="     ENTER YOUR PERSONAL ID ",border_color="gold",fg_color=bg_text_color,bg_color=bg_text_color,font=("Arial",30),text_color=text_color,width=500)
        self.personal_id_entry.place(anchor="center",relx=0.5,rely=0.45)
        self.password_entry = ctk.CTkEntry(self.big_boi_panel,placeholder_text="   ENTER YOUR PASSWORD ",border_color="gold",fg_color=bg_text_color,bg_color=bg_text_color,font=("Arial",30),text_color=text_color,width=450)
        self.password_entry.place(anchor="center",relx=0.5,rely=0.55)
        self.submit_button = ctk.CTkButton(self.big_boi_panel,border_color=text_color,command=login,text="LOGIN",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,corner_radius=1,border_width=5)
        self.submit_button.place(anchor="center",relx=0.5,rely=0.65)
        def exit_func():
            reset_screen()
            self.E1rrorLabel.configure(text="")
            self.attemptsLabel.configure(text="")
            controller.show_frame("MainScreen")
        Exitbutton = ctk.CTkButton(
            self.big_boi_panel, 
            text="EXIT",
            font=("arial",20,"bold"),
            command=exit_func,
            bg_color=bg_text_color,
            text_color=text_color,
            hover_color=hover_color,
            fg_color=fg_color,
            width=1390,
            corner_radius=1,
        )
        Exitbutton.place(anchor="center", relx=0.5, rely=0.97)

class AdminMessageDisplayAll(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.bg_image = ctk.CTkImage(
            light_image=Image.open(background_URL),
            dark_image=Image.open(background_URL),
            size=(1545, 850)
        )
        bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.big_boi_panel = ctk.CTkFrame(self,height=750,width=1400,border_width=5,border_color="gold",fg_color="#050521")
        self.big_boi_panel.place(anchor="center",relx=0.5,rely=0.5)
        label = ctk.CTkLabel(self.big_boi_panel, text="BANK", font=("Arial", 58), text_color=text_color,bg_color=bg_text_color)
        label.place(anchor="center", relx=0.5, rely=0.08)

        label1 = ctk.CTkLabel(self.big_boi_panel,text="ALL CLIENT ACCOUNTS", font=("Arial", 40), text_color=text_color,bg_color=bg_text_color)
        label1.place(anchor="center", relx=0.5, rely=0.15)
        self.E1rrorLabel = ctk.CTkLabel(self.big_boi_panel, text="", font=("Arial", 26), text_color=text_color,bg_color=bg_text_color)
        self.E1rrorLabel.place(anchor="center", relx=0.5, rely=0.92)
        def Display_forums():
            for widget in self.application_box.winfo_children():
                widget.destroy()
            info = DB_connection.admin_read_support_messages()
            for i in range(len(info)):
                time = info[i][4]
                card = ctk.CTkFrame(self.application_box, fg_color="#2b2b2b", corner_radius=8)
                card.pack(fill="x", pady=8, padx=5, side="top")
                info_text = f"      {info[i][0]}     |      {info[i][1]}     |      {info[i][2]}     |     {info[i][3]}     |     {time}"
                info_label = ctk.CTkLabel(card,text=info_text, font=("Arial", 16), text_color=text_color)
                info_label.pack(side="left", padx=15, pady=10)
        def display_options():
            checker = self.ID_entry.get()
            if checker != "" and checker != None:
                self.box = ctk.CTkLabel(self.big_boi_panel,width=700,height=30,fg_color="black",bg_color="black",text="",)
                self.ConfirmdeleteButton = ctk.CTkButton(self.big_boi_panel,command=delAcc,border_color="gold",text="CONFIRM",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,border_width=5,corner_radius=1)
                self.DenydeleteButton= ctk.CTkButton(self.big_boi_panel,command=deny_del,border_color="gold",text="CANCEL",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,border_width=5,corner_radius=1)
                self.DenydeleteButton.place(anchor="center", relx=0.6, rely=0.5)
                self.ConfirmdeleteButton.place(anchor="center", relx=0.4, rely=0.5)
                self.box.place(anchor="center", relx=0.5, rely=0.5,relheight=0.2)
            else:
                self.E1rrorLabel.configure(text="ENTER AN ID TO DELETE!")
        def delAcc():
                self.ConfirmdeleteButton.destroy()
                self.DenydeleteButton.destroy()
                self.box.destroy()
                id_gette = self.ID_entry.get()
                try:
                    id_getter = int(id_gette)
                    if id_getter != None:
                        DB_connection.delete_support_ticket(id_getter)
                        self.E1rrorLabel.configure(text=f"TICKET WITH ID : {id_getter} HAS BEEN DELETED!")
                        self.ID_entry.delete(0,"end")
                        Display_forums()
                    else:
                        self.E1rrorLabel.configure(text="PLEASE ENTER AN ID!")
                except ValueError:
                    self.E1rrorLabel.configure(text=f"PLEASE ENTER A VALID ID!")
        self.deleteButton = ctk.CTkButton(self.big_boi_panel,command=display_options,border_color="gold",text="DELETE",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,border_width=5,corner_radius=1)
        self.deleteButton.place(anchor="center", relx=0.92, rely=0.6)
        def deny_del():
            self.ConfirmdeleteButton.destroy()
            self.DenydeleteButton.destroy()
            self.box.destroy()
        self.box = ctk.CTkLabel(self.big_boi_panel,width=500,height=300,fg_color="black",bg_color="black")
        self.ConfirmdeleteButton = ctk.CTkButton(self.big_boi_panel,command=delAcc,border_color="gold",text="CONFIRM",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,border_width=5,corner_radius=1)
        self.DenydeleteButton= ctk.CTkButton(self.big_boi_panel,command=deny_del,border_color="gold",text="CANCEL",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,border_width=5,corner_radius=1)
        self.application_box = ctk.CTkScrollableFrame(self.big_boi_panel,label_text=f"ID          PERSONAL ID         REASON         MESSAGE         TIME",label_font=("Arial",20),width=850,height=400,corner_radius=15,fg_color="#1e1e1e",border_color="gold",border_width=2)
        self.application_box.place(anchor="center", relx=0.5, rely=0.55)
        self.RefreshButton = ctk.CTkButton(self.big_boi_panel,border_color="gold",text="REFRESH",font=("Arial",30),fg_color=fg_color,bg_color=bg_text_color,hover_color=hover_color,border_width=5,corner_radius=1,command=Display_forums)
        self.RefreshButton.place(anchor="center", relx=0.92, rely=0.2)
        self.ID_entry = ctk.CTkEntry(self.big_boi_panel,border_color="gold",corner_radius=1,bg_color=bg_text_color,width=20,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30))
        self.ID_entry.place(anchor="center", relx=0.92, rely=0.3)

        Exitbutton = ctk.CTkButton(
            self.big_boi_panel, 
            text="EXIT",
            font=("Arial",20,"bold"),
            command=lambda: controller.show_frame("AdminClientCenterScreen"),
            bg_color=bg_text_color,
            text_color=text_color,
            hover_color=hover_color,
            fg_color=fg_color,
            width=1390,
            corner_radius=1
        )
        Exitbutton.place(anchor="center", relx=0.5, rely=0.97)

class ClientMainScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.personal_info = ""
        self.bg_image = ctk.CTkImage(
            light_image=Image.open(background_URL),
            dark_image=Image.open(background_URL),
            size=(1545, 850)
        )
        bg_image_thing = ctk.CTkImage(
            light_image=Image.open("D:/opera gx downloads/image (3).png"),
            dark_image=Image.open("D:/opera gx downloads/image (3).png"),
            size=(1545, 850)
        )
        bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        def show_main_screen():
            self.welcome_panel.configure(self,height=200,width=1400,border_width=5,border_color="gold",fg_color="#050521")
            self.balance_panel.configure(self,height=600,width=400,border_width=5,border_color="gold",fg_color="#050521")
            self.history_panel.configure(self,height=600,width=600,border_width=5,border_color="gold",fg_color="#050521")
            self.transfer_panel.configure(self,height=600,width=400,border_width=5,border_color="gold",fg_color="#050521")
            self.welcome_panel.place(anchor="center",relx=0.5,rely=0.15)
            self.transfer_panel.place(anchor="center",relx=0.825,rely=0.62)
            self.history_panel.place(anchor="center",relx=0.5,rely=0.62)
            self.balance_panel.place(anchor="center",relx=0.175,rely=0.62)
            Exitbutton = ctk.CTkButton(self,text="EXIT",font=("Arial",20,"bold"),command=exit_func,bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=390)
            Exitbutton.place(anchor="center", relx=0.825, rely=0.953)
            self.settings_button = ctk.CTkButton(self,command=lambda :self.controller.show_frame("ClientSettingsScreen"),text="SETTINGS",font=("Arial",20,"bold"),bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=299)
            self.settings_button.place(anchor="center", relx=0.595, rely=0.953)
            self.cards_button = ctk.CTkButton(self,command=lambda :self.controller.show_frame("ClientCardsScreen"),text="CARDS",font=("Arial",20,"bold"),bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=299)
            self.cards_button.place(anchor="center", relx=0.405, rely=0.953)
            self.info_button = ctk.CTkButton(self,command=show_main_screen,text="HOME",font=("Arial",20,"bold"),bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=390)
            self.info_button.place(anchor="center", relx=0.175, rely=0.953)
            self.history_box = ctk.CTkScrollableFrame(self.history_panel,label_text=f"PROCESS  |  AMOUNT  |  TIME",label_font=("Arial",20),corner_radius=10,fg_color="#050521",border_color="gold",border_width=10,width=550,height=430,label_fg_color="#0f0f53")
            self.history_box.place(anchor="center", relx=0.5, rely=0.48)
            self.transfer_button = ctk.CTkButton(self.transfer_panel,command=transfer_confirmation,corner_radius=0,text="TRANSFER",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200)
            self.deposit_button = ctk.CTkButton(self.balance_panel,command=deposit,corner_radius=0,text="DEPOSIT",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200)
            self.withdraw_button = ctk.CTkButton(self.balance_panel,command=withdraw,text="WITHDRAW",corner_radius=0,text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200)
            self.withdraw_all_button = ctk.CTkButton(self.balance_panel,command=withdraw_all,corner_radius=0,text="WITHDRAW ALL FUNDS",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=390)
            self.welcome_label.destroy()
            self.balance_label.destroy()
            self.welcome_label= ctk.CTkLabel(self.welcome_panel, font=("Arial", 50), text_color=text_color,bg_color="#050521",fg_color=bg_text_color,corner_radius=10)
            self.welcome_label.place(anchor="center",relx=0.5,rely=0.5)
            self.balance_label= ctk.CTkLabel(self.balance_panel,bg_color="#050521",fg_color=bg_text_color,corner_radius=10, text="CLICK THE HOME BUTTON...PLS", font=("Arial", 35), text_color=text_color)
            self.balance_label.place(anchor="center",relx=0.5,rely=0.18)
            self.deposit_button.place(anchor="center",relx=0.27,rely=0.38)
            self.withdraw_button.place(anchor="center",relx=0.73,rely=0.38)
            self.withdraw_all_button.place(anchor="center",relx=0.5,rely=0.44)
            self.balance_error_box.place(anchor="center",relx=0.5,rely=0.7)
            personal_id = session_data["client_id"]
            self.personal_info = DB_connection.client_center_singular_personalID(personal_id)
            name = DB_connection.get_client_name(self.personal_info[0][2])
            welcome_text = f"WELCOME, {name}!"
            balance_text = f"""
 ACCOUNT BALANCE 
______________
{self.personal_info[0][6]} $
"""
            self.welcome_label.configure(text=welcome_text)
            self.balance_label.configure(text=balance_text)
            self.history_box = ctk.CTkScrollableFrame(self.history_panel,label_text=f"PROCESS  |  AMOUNT  |  TIME",label_font=("Arial",20),corner_radius=10,fg_color="#050521",border_color="gold",border_width=10,width=550,height=430,label_fg_color="#0f0f53")
            self.history_box.place(anchor="center", relx=0.5, rely=0.48)
            self.transfer_id_entry = ctk.CTkEntry(self.transfer_panel,text_color=text_color,bg_color=bg_text_color,fg_color="#0F0F42",border_color="gold",border_width=4,placeholder_text="       transferee ID",width=380,height=100,font=("Arial",24,"bold"))
            self.transfer_id_entry.place(anchor="center",relx=0.5,rely=0.3)
            self.transfer_button = ctk.CTkButton(self.transfer_panel,command=transfer_confirmation,corner_radius=0,text="TRANSFER",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=300,height=100)
            self.transfer_button.place(anchor="center",relx=0.5,rely=0.5)
            Display_forums()
        self.welcome_panel = ctk.CTkFrame(self,height=200,width=1400,border_width=5,border_color="gold",fg_color="#050521")
        self.balance_panel = ctk.CTkFrame(self,height=600,width=400,border_width=5,border_color="gold",fg_color="#050521")
        self.history_panel = ctk.CTkFrame(self,height=600,width=600,border_width=5,border_color="gold",fg_color="#050521")
        self.transfer_panel = ctk.CTkFrame(self,height=600,width=400,border_width=5,border_color="gold",fg_color="#050521")
        self.welcome_panel.place(anchor="center",relx=0.5,rely=0.15)
        self.transfer_panel.place(anchor="center",relx=0.825,rely=0.62)
        self.history_panel.place(anchor="center",relx=0.5,rely=0.62)
        self.balance_panel.place(anchor="center",relx=0.175,rely=0.62)

        


        self.settings_button = ctk.CTkButton(self,command=lambda: self.controller.show_frame("ClientSettingsScreen"),text="SETTINGS",font=("Arial",20,"bold"),bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=299)
        self.settings_button.place(anchor="center", relx=0.595, rely=0.953)
        self.cards_button = ctk.CTkButton(self,command=lambda :self.controller.show_frame("ClientCardsScreen"),text="CARDS",font=("Arial",20,"bold"),bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=299)
        self.cards_button.place(anchor="center", relx=0.405, rely=0.953)
        self.info_button = ctk.CTkButton(self,command=show_main_screen,text="HOME",font=("Arial",20,"bold"),bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=390)
        self.info_button.place(anchor="center", relx=0.175, rely=0.953)
        welcome_text = f"WELCOME!"
        self.history_box = ctk.CTkScrollableFrame(self.history_panel,label_text=f"PROCESS  |  AMOUNT  |  TIME",label_font=("Arial",20),corner_radius=10,fg_color="#050521",border_color="gold",border_width=10,width=550,height=430,label_fg_color="#0f0f53")
        self.history_box.place(anchor="center", relx=0.5, rely=0.48)
        def Display_forums():
            for widget in self.history_box.winfo_children():
                widget.destroy()
            info = DB_connection.client_read_personal_balance_history(self.personal_info[0][1])
            for i in range(len(info)):
                card = ctk.CTkFrame(self.history_box, fg_color="#2b2b2b", corner_radius=8)
                card.pack(fill="x", pady=8, padx=5, side="top")
                info_text = f"      {info[i][2]}     |      {info[i][3]}     |      {info[i][4]}"
                info_label = ctk.CTkLabel(card,text=info_text, font=("Arial", 18), text_color=text_color)
                info_label.pack(side="left", padx=15, pady=10)
        self.welcome_label = ctk.CTkLabel(self.welcome_panel, text=welcome_text, font=("Arial", 35), text_color=text_color,bg_color=bg_text_color)
        self.welcome_label.place(anchor="center",relx=0.5,rely=0.5)
        self.balance_label = ctk.CTkLabel(self.balance_panel, text="CLICK THE HOME BUTTON...PLS", font=("Arial", 20), text_color=text_color,bg_color="#050521",fg_color=bg_text_color,corner_radius=4)
        self.balance_label.place(anchor="center",relx=0.5,rely=0.2)
        self.balance_error_box = ctk.CTkFrame(self.balance_panel,height=250,width=390,border_color="gold",fg_color="#060630",border_width=4)
        self.history_label = ctk.CTkLabel(self.history_box,text="PROCESS  |  AMOUNT  |  TIME",bg_color="#050521",fg_color=bg_text_color,corner_radius=10,font=("Arial", 35), text_color=text_color)
        self.transfer_id_entry = ctk.CTkEntry(self.transfer_panel,text_color=text_color,bg_color=bg_text_color,fg_color="#060630",border_color="gold",border_width=4,placeholder_text="transfree ID",width=600,height=80,font=("Arial",18,"bold"))
        def transfer_confirmation():
            def destroy_entry_menu():
                self.confirm_button.destroy()
                self.cancel_button.destroy()
                self.id_check.destroy()
                self.giant_friggin_frame.destroy()
            def transfer_deposit():
                def confirm():
                    amount_a = self.amount_entry.get()
                    try:
                        amount = float(amount_a)
                        old_amount = DB_connection.client_get_balance(self.personal_info[0][0])
                        if amount > old_amount:
                            self.MenuErrorLabel.configure(self.giant_friggin_frame,text="INSUFFICIENT BALANCE, YOU DO NOT HAVE ENOUGH FUNDS TO WITHDRAW THAT AMOUNT")
                        else:
                            new_amount = old_amount - amount
                            DB_connection.client_set_balance(new_amount,self.personal_info[0][0])
                            old_amount1 = DB_connection.client_get_balance(id_checker[0][0])
                            new_amount1 = old_amount1+amount
                            DB_connection.client_set_balance(new_amount1,id_checker[0][0])
                            time = dt.now()
                            time = time.strftime('%Y/%m/%d | %I:%M %p')
                            DB_connection.client_add_balance_history(id_checker[0][1],f"TRANSFER FROM {self.personal_info[0][1]}",amount,time)
                            DB_connection.client_add_balance_history(self.personal_info[0][1],f"TRANSFER TO {id_checker[0][1]}",amount,time)
                            destroy_entry_menu()
                            show_main_screen()
                    except ValueError:
                        self.MenuErrorLabel.configure(self.giant_friggin_frame,text="PLEASE ENTER VALID DIGITS!")
                def cancel():
                    destroy_entry_menu()
                self.giant_friggin_frame = ctk.CTkLabel(self,image=bg_image_thing,text="")
                self.giant_friggin_frame.place(x=0,y=0,relwidth=1, relheight=1)
                self.amount_entry= ctk.CTkEntry(self.giant_friggin_frame,text_color=text_color,bg_color=bg_text_color,fg_color="#060630",border_color="gold",border_width=4,placeholder_text="    ENTER THE AMOUNT     ",width=600,height=80,font=("Arial",30,"bold"))
                self.amount_entry.place(anchor="center",relx=0.5,rely=0.5)
                self.confirm_button=ctk.CTkButton(self.giant_friggin_frame,command=confirm,corner_radius=0,text="CONFIRM",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200,height=40)
                self.cancel_button=ctk.CTkButton(self.giant_friggin_frame,command=cancel,corner_radius=0,text="CANCEL",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200,height=40)
                self.confirm_button.place(anchor="center",relx=0.4,rely=0.6)
                self.cancel_button.place(anchor="center",relx=0.6,rely=0.6)
                self.MenuErrorLabel = ctk.CTkLabel(self.giant_friggin_frame,bg_color="#050521",fg_color="black",text="",font=("Arial",30,"bold"),corner_radius=5,text_color=text_color)
                self.MenuErrorLabel.place(anchor="center",relx=0.5,rely=0.7)
            def cancel():
                destroy_entry_menu()
            def confirm():
                destroy_entry_menu()
                transfer_deposit()
            transfree_id = self.transfer_id_entry.get()
            id_checker = DB_connection.client_center_singular_personalID(transfree_id)
            self.giant_friggin_frame = ctk.CTkLabel(self,image=bg_image_thing,text="")
            self.giant_friggin_frame.place(x=0,y=0,relwidth=1, relheight=1)
            self.id_check= ctk.CTkLabel(self.giant_friggin_frame,text_color=text_color,bg_color=bg_text_color,fg_color="#060630",text="",width=600,height=80,font=("Arial",30,"bold"))
            self.id_check.place(anchor="center",relx=0.5,rely=0.5)
            self.confirm_button=ctk.CTkButton(self.giant_friggin_frame,command=confirm,corner_radius=0,text="CONFIRM",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200,height=40)
            self.cancel_button=ctk.CTkButton(self.giant_friggin_frame,command=cancel,corner_radius=0,text="CANCEL",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200,height=40)
            if id_checker != []:
                if id_checker[0][1] == self.personal_info[0][1]:
                    self.id_check.configure(text=f"...seriously? transferring to yourself?...")
                    self.cancel_button.configure(text="sorry....",command=destroy_entry_menu)
                    self.cancel_button.place(anchor="center",relx=0.5,rely=0.6)
                else:
                    transfree_name = DB_connection.get_client_name(id_checker[0][2])
                    self.id_check.configure(text=f"account found : {transfree_name}\nIs this the person you are looking for?")
                    self.confirm_button.place(anchor="center",relx=0.4,rely=0.6)
                    self.cancel_button.place(anchor="center",relx=0.6,rely=0.6)
            else:
                self.id_check.configure(text=f"no account with that ID exists!")
                self.cancel_button.configure(text="EXIT",command=destroy_entry_menu)
                self.cancel_button.place(anchor="center",relx=0.5,rely=0.6)
        def destroy_entry_menu():
            self.confirm_button.destroy()
            self.cancel_button.destroy()
            self.amount_entry.destroy()
            self.giant_friggin_frame.destroy()
        def deposit():
            def confirm():
                amount_a = self.amount_entry.get()
                try:
                    amount = float(amount_a)
                    old_amount = DB_connection.client_get_balance(self.personal_info[0][0])
                    new_amount = old_amount+amount
                    DB_connection.client_set_balance(new_amount,self.personal_info[0][0])
                    time = dt.now()
                    time = time.strftime('%Y/%m/%d | %I:%M %p')
                    DB_connection.client_add_balance_history(self.personal_info[0][1],"DEPOSIT",amount,time)
                    destroy_entry_menu()
                    show_main_screen()
                except ValueError:
                   self.MenuErrorLabel.configure(self.giant_friggin_frame,text="PLEASE ENTER VALID DIGITS!")
            def cancel():
                destroy_entry_menu()
            self.giant_friggin_frame = ctk.CTkLabel(self,image=bg_image_thing,text="")
            self.giant_friggin_frame.place(x=0,y=0,relwidth=1, relheight=1)
            self.amount_entry= ctk.CTkEntry(self.giant_friggin_frame,text_color=text_color,bg_color=bg_text_color,fg_color="#060630",border_color="gold",border_width=4,placeholder_text="    ENTER THE AMOUNT     ",width=600,height=80,font=("Arial",30,"bold"))
            self.amount_entry.place(anchor="center",relx=0.5,rely=0.5)
            self.confirm_button=ctk.CTkButton(self.giant_friggin_frame,command=confirm,corner_radius=0,text="CONFIRM",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200,height=40)
            self.cancel_button=ctk.CTkButton(self.giant_friggin_frame,command=cancel,corner_radius=0,text="CANCEL",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200,height=40)
            self.confirm_button.place(anchor="center",relx=0.4,rely=0.6)
            self.cancel_button.place(anchor="center",relx=0.6,rely=0.6)
            self.MenuErrorLabel = ctk.CTkLabel(self.giant_friggin_frame,bg_color="#050521",fg_color="black",text="",font=("Arial",30,"bold"),corner_radius=5,text_color=text_color)
            self.MenuErrorLabel.place(anchor="center",relx=0.5,rely=0.7)
        def withdraw_all():
            def confirm():
                amount = DB_connection.client_get_balance(self.personal_info[0][0])
                time = dt.now()
                time = time.strftime('%Y/%m/%d | %I:%M %p')
                DB_connection.client_add_balance_history(self.personal_info[0][1],"FULL WITHDRAW",amount,time)
                DB_connection.client_set_balance(0,self.personal_info[0][0])
                destroy_entry_menu()
                show_main_screen()
            def cancel():
                destroy_entry_menu()
            self.giant_friggin_frame = ctk.CTkLabel(self,image=bg_image_thing,text="")
            self.giant_friggin_frame.place(x=0,y=0,relwidth=1, relheight=1)
            self.confirm_button=ctk.CTkButton(self.giant_friggin_frame,command=confirm,corner_radius=0,text="CONFIRM",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200,height=40)
            self.cancel_button=ctk.CTkButton(self.giant_friggin_frame,command=cancel,corner_radius=0,text="CANCEL",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200,height=40)
            self.confirm_button.place(anchor="center",relx=0.4,rely=0.6)
            self.cancel_button.place(anchor="center",relx=0.6,rely=0.6)
            self.MenuErrorLabel = ctk.CTkLabel(self.giant_friggin_frame,bg_color="#050521",fg_color="black",text="",font=("Arial",30,"bold"),corner_radius=5,text_color=text_color)
            self.MenuErrorLabel.place(anchor="center",relx=0.5,rely=0.7)
        def withdraw():
            def confirm():
                amount_a = self.amount_entry.get()
                try:
                    amount = float(amount_a)
                    old_amount = DB_connection.client_get_balance(self.personal_info[0][0])
                    if amount > old_amount:
                        self.MenuErrorLabel.configure(self.giant_friggin_frame,text="INSUFFICIENT BALANCE, YOU DO NOT HAVE ENOUGH FUNDS TO WITHDRAW THAT AMOUNT")
                    else:
                        new_amount = old_amount - amount
                    DB_connection.client_set_balance(new_amount,self.personal_info[0][0])
                    time = dt.now()
                    time = time.strftime('%Y/%m/%d | %I:%M %p')
                    DB_connection.client_add_balance_history(self.personal_info[0][1],"WITHDRAW",amount,time)
                    destroy_entry_menu()
                    show_main_screen()
                except ValueError:
                   self.MenuErrorLabel.configure(self.giant_friggin_frame,text="PLEASE ENTER VALID DIGITS!")
            def cancel():
                destroy_entry_menu()
            self.giant_friggin_frame = ctk.CTkLabel(self,image=bg_image_thing,text="")
            self.giant_friggin_frame.place(x=0,y=0,relwidth=1, relheight=1)
            self.amount_entry= ctk.CTkEntry(self.giant_friggin_frame,text_color=text_color,bg_color=bg_text_color,fg_color="#060630",border_color="gold",border_width=4,placeholder_text="    ENTER THE AMOUNT     ",width=600,height=80,font=("Arial",30,"bold"))
            self.amount_entry.place(anchor="center",relx=0.5,rely=0.5)
            self.confirm_button=ctk.CTkButton(self.giant_friggin_frame,command=confirm,corner_radius=0,text="CONFIRM",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200,height=40)
            self.cancel_button=ctk.CTkButton(self.giant_friggin_frame,command=cancel,corner_radius=0,text="CANCEL",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200,height=40)
            self.confirm_button.place(anchor="center",relx=0.4,rely=0.6)
            self.cancel_button.place(anchor="center",relx=0.6,rely=0.6)
            self.MenuErrorLabel = ctk.CTkLabel(self.giant_friggin_frame,bg_color="#050521",fg_color="black",text="",font=("Arial",30,"bold"),corner_radius=5,text_color=text_color)
            self.MenuErrorLabel.place(anchor="center",relx=0.5,rely=0.7)
        self.transfer_button = ctk.CTkButton(self.transfer_panel,command=transfer_confirmation,corner_radius=0,text="TRANSFER",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200)
        self.deposit_button = ctk.CTkButton(self.balance_panel,command=deposit,corner_radius=0,text="DEPOSIT",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200)
        self.withdraw_button = ctk.CTkButton(self.balance_panel,command=withdraw,text="WITHDRAW",corner_radius=0,text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200)
        self.withdraw_all_button = ctk.CTkButton(self.balance_panel,command=withdraw_all,corner_radius=0,text="WITHDRAW ALL FUNDS",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=390)
        self.amount_entry = ctk.CTkEntry(self)
        self.confirm_button = ctk.CTkButton(self)
        self.cancel_button = ctk.CTkButton(self)
        self.giant_friggin_frame = None
        self.MenuErrorLabel = None
        self.id_check= None
        
        def exit_func():
            self.welcome_label.destroy()
            self.balance_label.destroy()
            for widget in self.history_box.winfo_children():
                widget.destroy()
            self.controller.show_frame("ClientCenterLoginScreen")
        Exitbutton = ctk.CTkButton(self,text="EXIT",font=("Arial",20,"bold"),command=exit_func,bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=390)
        Exitbutton.place(anchor="center", relx=0.825, rely=0.953)

class ClientSettingsScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.personal_info = ""
        self.bg_image = ctk.CTkImage(
            light_image=Image.open(background_URL),
            dark_image=Image.open(background_URL),
            size=(1545, 850)
        )
        bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_image_thing = ctk.CTkImage(
            light_image=Image.open("D:/opera gx downloads/image (3).png"),
            dark_image=Image.open("D:/opera gx downloads/image (3).png"),
            size=(1545, 850)
        )
        label = ctk.CTkLabel(self, text="BANK", font=("Arial", 58), text_color="white",bg_color="black")
        label.place(anchor="center", relx=0.5, rely=0.08)
        def exit_func():
            if self.info_label:
                self.info_label.destroy()
                self.controller.show_frame("ClientCenterLoginScreen")
            else:
                self.controller.show_frame("ClientCenterLoginScreen")
        def display_info():
            d_id = self.personal_info[0][1]
            checker = DB_connection.personal_id_check(d_id)
            details_info = DB_connection.client_info_singular(self.personal_info[0][2])
            if self.personal_info[0][4] == 0:
                lock = "UNLOCKED"
            else:
                lock = "LOCKED"
            info_text = f"DATABASE ID : {self.personal_info[0][0]}\nPERSONAL ID : {self.personal_info[0][1]}\nPERSONAL INFORMATION ID : {self.personal_info[0][2]}\n\n               PERSONAL INFORMATION\n=============================================\n\nNAME : {details_info[0][1]}\nD.O.B : {details_info[0][2]}\nGENDER : {details_info[0][3]}\nNATIONALITY : {details_info[0][4]}\nJOB : {details_info[0][5]}\nYEARLY INCOME : {details_info[0][3]}\nLOCK : {lock}\nREMAINING LOGIN ATTEMPTS : {self.personal_info[0][5]}"
            self.info_label= ctk.CTkLabel(self.big_boi_panel,text=info_text, font=("Arial", 24), text_color=text_color,bg_color=bg_text_color,fg_color=bg_text_color,height=600,width=700)
            self.info_label.place(anchor="center",relx=0.5,rely=0.5)
        def new_pass():
            def new_pass_confirmed():
                DB_connection.client_password_change(self.personal_info[0][1],pass_checker2)
                self.new_pass_entry.destroy()
                self.new_pass_entry_confirm.destroy()
                self.giant_friggin_frame.destroy()
                self.submit_pass_button.destroy()
                self.ErrorLabel.destroy()
            pass_checker1 = self.new_pass_entry.get()
            pass_checker2 = self.new_pass_entry_confirm.get()
            if pass_checker1 == pass_checker2:
                self.ErrorLabel.configure(text="")
                new_pass_confirmed()
            else:
                self.ErrorLabel.configure(text="PASSWORDS DO NOT MATCH!")
        def pass_check():
            password = self.pass_entry.get()
            if password != "":
                checker = DB_connection.client_password_check(self.personal_info[0][1],password)
                if checker == "valid":
                    self.ErrorLabel.configure(text="")
                    self.pass_entry.destroy()
                    self.submit_pass_button.destroy()
                    self.new_pass_entry = ctk.CTkEntry(self.giant_friggin_frame,placeholder_text="     enter your new password ",border_color="gold",fg_color=bg_text_color,bg_color=bg_text_color,font=("Arial",30),text_color=text_color,width=450)
                    self.new_pass_entry_confirm = ctk.CTkEntry(self.giant_friggin_frame,placeholder_text="     enter the password again ",border_color="gold",fg_color=bg_text_color,bg_color=bg_text_color,font=("Arial",30),text_color=text_color,width=450)                
                    self.new_pass_entry.place(anchor="center",relx=0.5,rely=0.4)
                    self.new_pass_entry_confirm.place(anchor="center",relx=0.5,rely=0.5)
                    self.submit_pass_button = ctk.CTkButton(self.giant_friggin_frame,border_color=text_color,command=new_pass,text="CONFIRM",font=("Arial",30),fg_color="#2EAD00",bg_color=bg_text_color,hover_color="#1C6A00",corner_radius=1)
                    self.submit_pass_button.place(anchor="center",relx=0.5,rely=0.6)
                if checker == "invalid":
                    self.ErrorLabel.configure(text="INCORRECT PASSWORD!")
            else:
                self.ErrorLabel.configure(text="ENTER YOUR PASSWORD!")
        def cancel_first_screen():
            self.giant_friggin_frame.destroy()
            self.ErrorLabel.destroy()
            self.submit_message_button.destroy()
            self.pass_entry.destroy()
            self.cancel_button.destroy()
        def change_pass():
            self.giant_friggin_frame = ctk.CTkLabel(self,image=bg_image_thing,text="")
            self.giant_friggin_frame.place(x=0,y=0,relwidth=1, relheight=1)
            self.ErrorLabel = ctk.CTkLabel(self.giant_friggin_frame, text="", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color)
            self.ErrorLabel.place(anchor="center", relx=0.5, rely=0.7)
            self.submit_pass_button = ctk.CTkButton(self.giant_friggin_frame,border_color=text_color,command=pass_check,text="CONFIRM",font=("Arial",30),fg_color="#2EAD00",bg_color=bg_text_color,hover_color="#1C6A00",corner_radius=1)
            self.cancel_button = ctk.CTkButton(self.giant_friggin_frame,border_color=text_color,command=cancel_first_screen,text="CANCEL",font=("Arial",30),fg_color="#771202",bg_color=bg_text_color,hover_color="#3B0000",corner_radius=1)
            self.pass_entry = ctk.CTkEntry(self.giant_friggin_frame,placeholder_text="     enter your old password ",border_color="gold",fg_color=bg_text_color,bg_color=bg_text_color,font=("Arial",30),text_color=text_color,width=450)
            self.pass_entry.place(anchor="center",relx=0.5,rely=0.4)
            self.submit_pass_button.place(anchor="center",relx=0.4,rely=0.5)
            self.cancel_button.place(anchor="center",relx=0.6,rely=0.5)

        def message():
                self.giant_friggin_frame = ctk.CTkLabel(self,image=bg_image_thing,text="")
                self.giant_friggin_frame.place(x=0,y=0,relwidth=1, relheight=1)
                self.submit_message_button = ctk.CTkButton(self.giant_friggin_frame,border_color=text_color,command=submit_message,text="SEND",font=("Arial",30),fg_color="#2EAD00",bg_color=bg_text_color,hover_color="#1C6A00",corner_radius=1)
                self.ReasonEntry = ctk.CTkOptionMenu(self.giant_friggin_frame,corner_radius=1,bg_color=bg_text_color,width=400,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30),dropdown_fg_color=bg_text_color,dropdown_hover_color="grey",dropdown_font=("Arial", 30),values=["ACCOUNT LOCK","FORGOT PASSWORD","FORGOT PERSONAL ID"],button_color="#D4AF37",button_hover_color="#AA820A")
                self.message_entry = ctk.CTkEntry(self.giant_friggin_frame,placeholder_text="     enter your message ",border_color="gold",fg_color=bg_text_color,bg_color=bg_text_color,font=("Arial",30),text_color=text_color,width=450)
                self.ReasonEntry.place(anchor="center",relx=0.5,rely=0.3)
                self.message_entry.place(anchor="center",relx=0.5,rely=0.4)
                self.submit_message_button.place(anchor="center",relx=0.5,rely=0.5)
        def submit_message():
            time = dt.now()
            time = time.strftime('%Y/%m/%d | %I:%M %p')
            personal_id = self.personal_info[0][1]
            Reasonchoice = self.ReasonEntry.get()
            message = self.message_entry.get()
            DB_connection.client_add_support_message(personal_id,Reasonchoice,message,time)
            self.ReasonEntry.destroy()
            self.message_entry.destroy()
            self.submit_message_button.destroy()
            self.giant_friggin_frame.destroy()
        def show_settings_screen():
            Exitbutton = ctk.CTkButton(self,text="EXIT",font=("Arial",20,"bold"),command=exit_func,bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=390)
            personal_id = session_data["client_id"]
            Exitbutton.place(anchor="center", relx=0.825, rely=0.953)
            self.personal_info = DB_connection.client_center_singular_personalID(personal_id)
            self.big_boi_panel.place(anchor="center",relx=0.63,rely=0.55)
            self.small_boi_panel.place(anchor="center",relx=0.175,rely=0.55)
            self.account_info_button.place(anchor="center",relx=0.5,rely=0.3)
            self.change_password_button.place(anchor="center",relx=0.5,rely=0.5)
            self.request_support_button.place(anchor="center",relx=0.5,rely=0.7)
        self.big_boi_panel = ctk.CTkFrame(self,height=720,width=1000,border_width=5,border_color="gold",fg_color="#050521")
        self.small_boi_panel = ctk.CTkFrame(self,height=720,width=400,border_width=5,border_color="gold",fg_color="#050521")
        self.settings_button = ctk.CTkButton(self,command =show_settings_screen,text="SETTINGS",font=("Arial",20,"bold"),bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=300)
        self.settings_button.place(anchor="center", relx=0.6, rely=0.953)
        self.cards_button = ctk.CTkButton(self,command=lambda: self.controller.show_frame("ClientCardsScreen"),text="CARDS",font=("Arial",20,"bold"),bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=300)
        self.cards_button.place(anchor="center", relx=0.405, rely=0.953)
        self.info_button = ctk.CTkButton(self,command=lambda: self.controller.show_frame("ClientMainScreen"),text="HOME",font=("Arial",20,"bold"),bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=390)
        self.info_button.place(anchor="center", relx=0.175, rely=0.953)
        Exitbutton = ctk.CTkButton(self,text="EXIT",font=("Arial",20,"bold"),command=lambda: self.controller.show_frame("ClientCenterLoginScreen"),bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=390)
        Exitbutton.place(anchor="center", relx=0.825, rely=0.953)
        self.account_info_button = ctk.CTkButton(self.small_boi_panel,command=display_info,text="ACCOUNT INFORMATION",font=("Arial",26,"bold"),bg_color="#0B032C",hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=300,border_color="#0B032C",border_width=5,height=100)
        self.change_password_button = ctk.CTkButton(self.small_boi_panel,command=change_pass,text="CHANGE PASSWORD",font=("Arial",26,"bold"),bg_color="#0B032C",hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=320,border_color="#0B032C",border_width=5,height=100)
        self.request_support_button = ctk.CTkButton(self.small_boi_panel,command=message,text="REQUEST SUPPORT",font=("Arial",26,"bold"),bg_color="#0B032C",hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=320,border_color="#0B032C",border_width=5,height=100)
        self.submit_message_button = ctk.CTkButton(self,border_color=text_color,command=submit_message,text="SEND",font=("Arial",30),fg_color="#2EAD00",bg_color=bg_text_color,hover_color="#1C6A00",corner_radius=1)
        self.ReasonEntry = ctk.CTkOptionMenu(self,corner_radius=1,bg_color=bg_text_color,width=400,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30),dropdown_fg_color=bg_text_color,dropdown_hover_color="grey",dropdown_font=("Arial", 30),values=["ACCOUNT LOCK","FORGOT PASSWORD","FORGOT PERSONAL ID"],button_color="#D4AF37",button_hover_color="#AA820A")
        self.message_entry = ctk.CTkEntry(self,placeholder_text="     enter your message ",border_color="gold",fg_color=bg_text_color,bg_color=bg_text_color,font=("Arial",30),text_color=text_color,width=450)
        self.message_button = ctk.CTkButton(self,border_color=text_color,command=message,text="contact support",font=("Arial",30),fg_color="#134AB7",bg_color=bg_text_color,hover_color="#0C3E78",corner_radius=1)
        self.giant_friggin_frame = None
        self.info_label = None
        self.pass_entry=None
        self.submit_pass_button = None
        self.new_pass_entry = None
        self.new_pass_entry_confirm = None
        self.ErrorLabel =None
        self.cancel_button =None

class ClientCardsScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.personal_info = ""
        self.bg_image = ctk.CTkImage(
            light_image=Image.open(background_URL),
            dark_image=Image.open(background_URL),
            size=(1545, 850)
        )
        bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        c_card_image = ctk.CTkImage(
            light_image=Image.open("c:/users/lenovo-a/OneDrive/Pictures/Screenshots/Screenshot 2026-05-29 231253.png"),
            dark_image=Image.open("c:/users/lenovo-a/OneDrive/Pictures/Screenshots/Screenshot 2026-05-29 231253.png"),
            size=(300, 200)
        )
        d_card_image = ctk.CTkImage(
            light_image=Image.open("c:/Users/lenovo-a/OneDrive/Pictures/Screenshots/Screenshot 2026-05-29 231722.png"),
            dark_image=Image.open("c:/Users/lenovo-a/OneDrive/Pictures/Screenshots/Screenshot 2026-05-29 231722.png"),
            size=(300, 200)
        )
        bg_image_thing = ctk.CTkImage(
            light_image=Image.open("D:/opera gx downloads/image (3).png"),
            dark_image=Image.open("D:/opera gx downloads/image (3).png"),
            size=(1545, 850)
        )
        label = ctk.CTkLabel(self, text="BANK", font=("Arial", 58), text_color="white",bg_color="black")
        label.place(anchor="center", relx=0.5, rely=0.08)

        def exit_func():
            if self.credit_card_apply_button != None:
                self.credit_card_apply_button.destroy()
            if self.debit_card_apply_button != None:
                self.debit_card_apply_button.destroy()
            if self.debit_deposit_button != None:
                self.debit_deposit_button.destroy()
            if self.debit_withdraw_button != None:
                self.debit_withdraw_button.destroy()
            if self.debit_withdraw_all_button != None:
                self.debit_withdraw_all_button.destroy()
            if self.credit_withdraw_button != None:
                self.credit_withdraw_button.destroy()
            if self.credit_withdraw_all_button != None:
                self.credit_withdraw_all_button.destroy()
            self.c_card.configure(text="")
            self.d_card.configure(text="")
            self.controller.show_frame("ClientCenterLoginScreen")
        def show_screen():
            personal_id = session_data["client_id"]
            self.personal_info = DB_connection.client_center_singular_personalID(personal_id)
            self.personal_info = DB_connection.client_center_singular_personalID(personal_id)
            if self.personal_info[0][7] != None:
                self.debit_deposit_button = ctk.CTkButton(self.right_panel,command=debit_deposit,text="DEPOSIT",text_color=text_color,bg_color=bg_text_color,font=("Arial",20,"bold"),hover_color=hover_color,fg_color=fg_color,border_color="#FFFFFF",border_width=5,corner_radius=1,width=200,height=20)        
                self.debit_withdraw_button = ctk.CTkButton(self.right_panel,command=debit_withdraw,text="WITHDRAW",text_color=text_color,bg_color=bg_text_color,font=("Arial",20,"bold"),hover_color=hover_color,fg_color=fg_color,border_color="#FFFFFF",border_width=5,corner_radius=1,width=200,height=20)        
                self.debit_withdraw_all_button = ctk.CTkButton(self.right_panel,command=debit_withdraw_all,text="WITHDRAW ALL",text_color=text_color,bg_color=bg_text_color,font=("Arial",20,"bold"),hover_color=hover_color,fg_color=fg_color,border_color="#FFFFFF",border_width=5,corner_radius=1,width=200,height=20)                
                self.debit_balance_label = ctk.CTkLabel(self.right_panel,text=f"{self.personal_info[0][8]}$",text_color="#FFFFFF",font=("Arial",26,"bold"))
                self.d_card.configure(text=self.personal_info[0][7])
                self.debit_deposit_button.place(anchor="center",relx=0.5,rely=0.6)
                self.debit_withdraw_button.place(anchor="center",relx=0.5,rely=0.7)
                self.debit_withdraw_all_button.place(anchor="center",relx=0.5,rely=0.8)
                self.debit_balance_label.place(anchor="center",relx=0.5,rely=0.5)
            else:
                self.debit_card_apply_button = ctk.CTkButton(self.right_panel,command=debit_apply,text="APPLY FOR A DEBIT CARD!",text_color=text_color,bg_color=bg_text_color,font=("Arial",20,"bold"),hover_color=hover_color,fg_color=fg_color,border_color="#FFFFFF",border_width=5,corner_radius=1,width=200,height=20)        
                self.d_card.configure(text="YOU DO NOT OWN A DEBIT CARD!",font=("Arial",16,"bold"))
                self.debit_card_apply_button.place(anchor="center",relx=0.5,rely=0.5)
            if self.personal_info[0][10] != None:
                self.c_card.configure(text=self.personal_info[0][10])
                self.credit_withdraw_button = ctk.CTkButton(self.left_panel,text="WITHDRAW",text_color=text_color,bg_color=bg_text_color,font=("Arial",20,"bold"),hover_color=hover_color,fg_color=fg_color,border_color="#FFFFFF",border_width=5,corner_radius=1,width=200,height=20)        
                self.credit_withdraw_all_button = ctk.CTkButton(self.left_panel,text="WITHDRAW ALL",text_color=text_color,bg_color=bg_text_color,font=("Arial",20,"bold"),hover_color=hover_color,fg_color=fg_color,border_color="#FFFFFF",border_width=5,corner_radius=1,width=200,height=20)                
                self.credit_withdraw_button.place(anchor="center",relx=0.5,rely=0.5)
                self.credit_withdraw_all_button.place(anchor="center",relx=0.5,rely=0.6)
            else:
                self.credit_card_apply_button = ctk.CTkButton(self.left_panel,command=credit_apply,text="APPLY FOR A CREDIT CARD!",text_color=text_color,bg_color=bg_text_color,font=("Arial",20,"bold"),hover_color=hover_color,fg_color=fg_color,border_color="#FFFFFF",border_width=5,corner_radius=1,width=200,height=20)
                self.c_card.configure(text="YOU DO NOT OWN A CREDIT! CARD!",font=("Arial",16,"bold"))
                self.credit_card_apply_button.place(anchor="center",relx=0.5,rely=0.5)
            self.credit_card_card.place(anchor="center",relx=0.5,rely=0.25)
            self.debit_card_card.place(anchor="center",relx=0.5,rely=0.25)
            self.c_card.place(anchor="center",relx=0.5,rely=0.5)
            self.d_card.place(anchor="center",relx=0.5,rely=0.5)
        def destroy_entry_menu():
            self.confirm_button.destroy()
            self.cancel_button.destroy()
            self.amount_entry.destroy()
            self.giant_friggin_frame.destroy()
        def debit_deposit():
            def confirm():
                amount_a = self.amount_entry.get()
                try:
                    amount = float(amount_a)
                    old_amount = DB_connection.debit_balance_get(self.personal_info[0][7])
                    new_amount = old_amount[0][0]+amount
                    DB_connection.debit_balance_set(new_amount,self.personal_info[0][7])
                    time = dt.now()
                    time = time.strftime('%Y/%m/%d | %I:%M %p')
                    DB_connection.client_add_debit_history(self.personal_info[0][1],self.personal_info[0][7],"DEPOSIT",amount,time)
                    destroy_entry_menu()
                    show_screen()
                except ValueError:
                   self.MenuErrorLabel.configure(self.giant_friggin_frame,text="PLEASE ENTER VALID DIGITS!")
            def cancel():
                destroy_entry_menu()
            self.giant_friggin_frame = ctk.CTkLabel(self,image=bg_image_thing,text="")
            self.giant_friggin_frame.place(x=0,y=0,relwidth=1, relheight=1)
            self.amount_entry= ctk.CTkEntry(self.giant_friggin_frame,text_color=text_color,bg_color=bg_text_color,fg_color="#060630",border_color="gold",border_width=4,placeholder_text="    ENTER THE AMOUNT     ",width=600,height=80,font=("Arial",30,"bold"))
            self.amount_entry.place(anchor="center",relx=0.5,rely=0.5)
            self.confirm_button=ctk.CTkButton(self.giant_friggin_frame,command=confirm,corner_radius=0,text="CONFIRM",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200,height=40)
            self.cancel_button=ctk.CTkButton(self.giant_friggin_frame,command=cancel,corner_radius=0,text="CANCEL",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200,height=40)
            self.confirm_button.place(anchor="center",relx=0.4,rely=0.6)
            self.cancel_button.place(anchor="center",relx=0.6,rely=0.6)
            self.MenuErrorLabel = ctk.CTkLabel(self.giant_friggin_frame,bg_color="#050521",fg_color="black",text="",font=("Arial",30,"bold"),corner_radius=5,text_color=text_color)
            self.MenuErrorLabel.place(anchor="center",relx=0.5,rely=0.7)
        def debit_withdraw():
            def confirm():
                amount_a = self.amount_entry.get()
                try:
                    amount = float(amount_a)
                    old_amount = DB_connection.debit_balance_get(self.personal_info[0][7])
                    if old_amount < amount:
                        self.MenuErrorLabel.configure(text="YOU DO NOT HAVE ENOUGH FUNDS!")
                    else:
                        new_amount = old_amount[0][0]-amount
                        DB_connection.debit_balance_set(new_amount,self.personal_info[0][7])
                        time = dt.now()
                        time = time.strftime('%Y/%m/%d | %I:%M %p')
                        DB_connection.client_add_debit_history(self.personal_info[0][1],self.personal_info[0][7],"WITHDRAW",amount,time)
                        destroy_entry_menu()
                        show_screen()
                except ValueError:
                   self.MenuErrorLabel.configure(self.giant_friggin_frame,text="PLEASE ENTER VALID DIGITS!")
            def cancel():
                destroy_entry_menu()
            self.giant_friggin_frame = ctk.CTkLabel(self,image=bg_image_thing,text="")
            self.giant_friggin_frame.place(x=0,y=0,relwidth=1, relheight=1)
            self.amount_entry= ctk.CTkEntry(self.giant_friggin_frame,text_color=text_color,bg_color=bg_text_color,fg_color="#060630",border_color="gold",border_width=4,placeholder_text="    ENTER THE AMOUNT     ",width=600,height=80,font=("Arial",30,"bold"))
            self.amount_entry.place(anchor="center",relx=0.5,rely=0.5)
            self.confirm_button=ctk.CTkButton(self.giant_friggin_frame,command=confirm,corner_radius=0,text="CONFIRM",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200,height=40)
            self.cancel_button=ctk.CTkButton(self.giant_friggin_frame,command=cancel,corner_radius=0,text="CANCEL",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200,height=40)
            self.confirm_button.place(anchor="center",relx=0.4,rely=0.6)
            self.cancel_button.place(anchor="center",relx=0.6,rely=0.6)
            self.MenuErrorLabel = ctk.CTkLabel(self.giant_friggin_frame,bg_color="#050521",fg_color="black",text="",font=("Arial",30,"bold"),corner_radius=5,text_color=text_color)
            self.MenuErrorLabel.place(anchor="center",relx=0.5,rely=0.7)
        def debit_withdraw_all():
            def confirm():
                amount = DB_connection.debit_balance_get(self.personal_info[0][7])
                time = dt.now()
                time = time.strftime('%Y/%m/%d | %I:%M %p')
                DB_connection.client_add_debit_history(self.personal_info[0][1],self.personal_info[0][7],"FULL WITHDRAW",amount,time)
                DB_connection.client_set_balance(0,self.personal_info[0][0])
                destroy_entry_menu()
                show_screen()
            def cancel():
                destroy_entry_menu()
            self.giant_friggin_frame = ctk.CTkLabel(self,image=bg_image_thing,text="")
            self.giant_friggin_frame.place(x=0,y=0,relwidth=1, relheight=1)
            self.confirm_button=ctk.CTkButton(self.giant_friggin_frame,command=confirm,corner_radius=0,text="CONFIRM",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200,height=40)
            self.cancel_button=ctk.CTkButton(self.giant_friggin_frame,command=cancel,corner_radius=0,text="CANCEL",text_color=text_color,bg_color="#050521",font=("Arial",20,"bold"),hover_color="#0c0c3e",fg_color="#0f0f53",width=200,height=40)
            self.confirm_button.place(anchor="center",relx=0.4,rely=0.6)
            self.cancel_button.place(anchor="center",relx=0.6,rely=0.6)
            self.MenuErrorLabel = ctk.CTkLabel(self.giant_friggin_frame,bg_color="#050521",fg_color="black",text="",font=("Arial",30,"bold"),corner_radius=5,text_color=text_color)
            self.MenuErrorLabel.place(anchor="center",relx=0.5,rely=0.7)
        def confirm_debit_apply():
            reason = self.reason_debit_apply.get()
            if reason != None and reason != "":
                DB_connection.client_apply_debit(self.personal_info[0][2],self.personal_info[0][1],reason)
                self.giant_friggin_frame.destroy()
                self.reason_debit_apply.destroy()
                self.apply_debit_button_confirm.destroy()
                self.error_debit.destroy()
            else:
                self.error_debit.configure(text="PLEASE ENTER A REASON!")
        def debit_apply():
            self.giant_friggin_frame = ctk.CTkLabel(self,image=bg_image_thing,text="")
            self.giant_friggin_frame.place(x=0,y=0,relwidth=1, relheight=1)
            self.reason_debit_apply = ctk.CTkEntry(self.giant_friggin_frame,text_color=text_color,bg_color=bg_text_color,fg_color=fg_color,border_color="gold",border_width=4,placeholder_text="    REASON FOR THE CARD    ",width=600,height=80,font=("Arial",30,"bold"))
            self.reason_debit_apply.place(anchor="center",relx=0.5,rely=0.5)
            self.apply_debit_button_confirm = ctk.CTkButton(self.giant_friggin_frame,text="APPLY",font=("Arial",20,"bold"),bg_color=bg_text_color,text_color=text_color,hover_color=hover_color,fg_color=fg_color,corner_radius=1,width=360,command=confirm_debit_apply)
            self.apply_debit_button_confirm.place(anchor="center",relx=0.5,rely=0.6)
            self.error_debit = ctk.CTkLabel(self.giant_friggin_frame, text="", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color)
            self.error_debit.place(anchor="center",relx=0.5,rely=0.7)
        def confirm_credit_apply():
            reason = self.reason_credit_apply.get()
            limit = self.credit_limit_choice.get()
            if limit == "5000":
                limit = 5000.0
            elif limit == "10000":
                limit = 10000.0
            elif limit == "15000":
                limit = 15000.0 
            elif limit == "20000":
                limit = 20000.0     
            if reason != None and reason != "":
                DB_connection.client_apply_credit(self.personal_info[0][2],self.personal_info[0][1],reason,limit)
                self.giant_friggin_frame.destroy()
                self.reason_credit_apply.destroy()
                self.apply_credit_button_confirm.destroy()
                self.error_credit.destroy()
                self.credit_limit_choice.destroy()
            else:
                self.error_debit.configure(text="PLEASE ENTER A REASON!")
        def credit_apply():
            self.giant_friggin_frame = ctk.CTkLabel(self,image=bg_image_thing,text="")
            self.giant_friggin_frame.place(x=0,y=0,relwidth=1, relheight=1)
            self.reason_credit_apply = ctk.CTkEntry(self.giant_friggin_frame,text_color=text_color,bg_color=bg_text_color,fg_color=fg_color,border_color="gold",border_width=4,placeholder_text="    REASON FOR THE CARD    ",width=600,height=80,font=("Arial",30,"bold"))
            self.reason_credit_apply.place(anchor="center",relx=0.5,rely=0.5)
            self.credit_limit_choice = ctk.CTkOptionMenu(self.giant_friggin_frame,corner_radius=1,bg_color=bg_text_color,width=400,text_color=text_color,fg_color=fg_color,font=("Arial", 30),dropdown_fg_color=fg_color,dropdown_hover_color=hover_color,dropdown_font=("Arial", 30))
            info_id = self.personal_info[0][2]
            peros_info = DB_connection.client_info_singular(info_id)
            yearly_income = peros_info[0][6]
            if yearly_income <= 5000:
                self.credit_limit_choice.configure(values=["5000"])
            elif yearly_income <= 10000:
                self.credit_limit_choice.configure(values=["5000","10000"])
            elif yearly_income <= 50000:
                self.credit_limit_choice.configure(values=["5000","10000","15000"])
            elif yearly_income <= 100000:
                self.credit_limit_choice.configure(values=["5000","10000","15000","20000"])
            self.credit_limit_choice.place(anchor="center",relx=0.5,rely=0.6)
            self.apply_credit_button_confirm = ctk.CTkButton(self.giant_friggin_frame,text="APPLY",font=("Arial",20,"bold"),bg_color=bg_text_color,text_color=text_color,hover_color=hover_color,fg_color=fg_color,corner_radius=1,width=360,command=confirm_credit_apply)
            
            self.apply_credit_button_confirm.place(anchor="center",relx=0.5,rely=0.7)
            self.error_credit = ctk.CTkLabel(self.giant_friggin_frame, text="", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color)
            self.error_credit.place(anchor="center",relx=0.5,rely=0.7)
        self.left_panel = ctk.CTkFrame(self,height=720,width=700,border_width=5,border_color="gold",fg_color="#050521")
        self.right_panel = ctk.CTkFrame(self,height=720,width=700,border_width=5,border_color="gold",fg_color="#050521")
        self.credit_card_card = ctk.CTkFrame(self.left_panel,width=310,height=210,border_color="#FFFFFF",fg_color="#050521",border_width=10)
        self.debit_card_card = ctk.CTkFrame(self.right_panel,width=310,height=210,border_color="#FFFFFF",fg_color="#050521",border_width=10)
        self.c_card = ctk.CTkLabel(self.credit_card_card,image=c_card_image,text_color="#FFFFFF",text="98234692",font=("Arial",26,"bold"))
        self.d_card = ctk.CTkLabel(self.debit_card_card,image=d_card_image,text="400304324",text_color=text_color,font=("Arial",26,"bold"))

        self.left_panel.place(anchor="center",relx=0.275,rely=0.55)
        self.right_panel.place(anchor="center",relx=0.715,rely=0.55)
        self.settings_button = ctk.CTkButton(self.right_panel,command=lambda: self.controller.show_frame("ClientSettingsScreen"),text="SETTINGS",font=("Arial",20,"bold"),bg_color=bg_text_color,text_color=text_color,hover_color=hover_color,fg_color=fg_color,corner_radius=1,width=360)
        self.settings_button.place(anchor="center", relx=0.27, rely=0.97)
        self.cards_button = ctk.CTkButton(self.left_panel,text="CARDS",command=show_screen,font=("Arial",20,"bold"),bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=360)
        self.cards_button.place(anchor="center", relx=0.73, rely=0.97)
        self.info_button = ctk.CTkButton(self.left_panel,command=lambda: self.controller.show_frame("ClientMainScreen"),text="HOME",font=("Arial",20,"bold"),bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=360)
        self.info_button.place(anchor="center", relx=0.27, rely=0.97)
        self.credit_card_apply_button = ctk.CTkButton(self.left_panel,command=credit_apply,text="APPLY FOR A CREDIT CARD!",text_color=text_color,bg_color=bg_text_color,font=("Arial",20,"bold"),hover_color=hover_color,fg_color=fg_color,border_color="#FFFFFF",border_width=5,corner_radius=1,width=200,height=20)
        self.debit_card_apply_button = ctk.CTkButton(self.right_panel,command=debit_apply,text="APPLY FOR A DEBIT CARD!",text_color=text_color,bg_color=bg_text_color,font=("Arial",20,"bold"),hover_color=hover_color,fg_color=fg_color,border_color="#FFFFFF",border_width=5,corner_radius=1,width=200,height=20)        
        self.debit_deposit_button = ctk.CTkButton(self.right_panel,command=debit_deposit,text="DEPOSIT",text_color=text_color,bg_color=bg_text_color,font=("Arial",20,"bold"),hover_color=hover_color,fg_color=fg_color,border_color="#FFFFFF",border_width=5,corner_radius=1,width=200,height=20)        
        self.debit_withdraw_button = ctk.CTkButton(self.right_panel,command=debit_withdraw,text="WITHDRAW",text_color=text_color,bg_color=bg_text_color,font=("Arial",20,"bold"),hover_color=hover_color,fg_color=fg_color,border_color="#FFFFFF",border_width=5,corner_radius=1,width=200,height=20)        
        self.debit_withdraw_all_button = ctk.CTkButton(self.right_panel,command=debit_withdraw_all,text="WITHDRAW ALL",text_color=text_color,bg_color=bg_text_color,font=("Arial",20,"bold"),hover_color=hover_color,fg_color=fg_color,border_color="#FFFFFF",border_width=5,corner_radius=1,width=200,height=20)                
        self.credit_withdraw_button = ctk.CTkButton(self.left_panel,text="WITHDRAW",text_color=text_color,bg_color=bg_text_color,font=("Arial",20,"bold"),hover_color=hover_color,fg_color=fg_color,border_color="#FFFFFF",border_width=5,corner_radius=1,width=200,height=20)        
        self.credit_withdraw_all_button = ctk.CTkButton(self.left_panel,text="WITHDRAW ALL",text_color=text_color,bg_color=bg_text_color,font=("Arial",20,"bold"),hover_color=hover_color,fg_color=fg_color,border_color="#FFFFFF",border_width=5,corner_radius=1,width=200,height=20)                
        self.amount_entry = ctk.CTkEntry(self)
        self.confirm_button = ctk.CTkButton(self)
        self.cancel_button = ctk.CTkButton(self)
        self.giant_friggin_frame = None
        self.MenuErrorLabel = None
        self.id_check= None
        self.reason_debit_apply = None
        self.error_debit = None
        self.apply_debit_button_confirm = None
        self.reason_credit_apply = None
        self.error_credit = None
        self.apply_credit_button_confirm = None
        self.credit_limit_choice = None
        self.debit_balance_label = None
        Exitbutton = ctk.CTkButton(self.right_panel,text="EXIT",font=("Arial",20,"bold"),command=exit_func,bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=360)
        Exitbutton.place(anchor="center", relx=0.73, rely=0.97)

class AdminCreditReview(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.bg_image = ctk.CTkImage(
            light_image=Image.open(background_URL),
            dark_image=Image.open(background_URL),
            size=(1545, 850)
        )
        bg_image_thing = ctk.CTkImage(
            light_image=Image.open("D:/opera gx downloads/image (3).png"),
            dark_image=Image.open("D:/opera gx downloads/image (3).png"),
            size=(1545, 850)
        )
        bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.big_boi_panel = ctk.CTkFrame(self,height=750,width=1400,border_width=5,border_color="gold",fg_color="#050521")
        self.big_boi_panel.place(anchor="center",relx=0.5,rely=0.5)
        self.giant_friggin_frame = ctk.CTkLabel(self,image=bg_image_thing,text="")
        label = ctk.CTkLabel(self.big_boi_panel, text="BANK", font=("Arial", 58), text_color=text_color,bg_color=bg_text_color)
        label.place(anchor="center", relx=0.5, rely=0.08)

        label1 = ctk.CTkLabel(self.big_boi_panel,text="ALL CREDIT CARD REQUESTS", font=("Arial", 40), text_color=text_color,bg_color=bg_text_color)
        label1.place(anchor="center", relx=0.5, rely=0.15)
        self.E1rrorLabel = ctk.CTkLabel(self.big_boi_panel, text="", font=("Arial", 24), text_color=text_color,bg_color=bg_text_color)
        self.E1rrorLabel.place(anchor="center", relx=0.5, rely=0.93)
        def Display_forums():
            for widget in self.application_box.winfo_children():
                widget.destroy()
            info = DB_connection.cards_application_forum_read()
            for i in range(len(info)):
                if info[i][5] == True:
                    status = "APPROVED"
                if info[i][5] == False:
                    status = "REJECTED"
                if info[i][5] == None:
                    status = "PENDING"
                if info[i][5] == None and info[i][3] == None:
                    pass
                else:
                    card = ctk.CTkFrame(self.application_box, fg_color="#2b2b2b", corner_radius=8)
                    card.pack(fill="x", pady=8, padx=5, side="top")
                    info_text = f"      {info[i][0]}     |      {info[i][2]}     |      {info[i][3]}     |     {info[i][4]}     |     {status}"
                    info_label = ctk.CTkLabel(card,text=info_text, font=("Arial", 20), text_color=text_color)
                    info_label.pack(side="left", padx=15, pady=10)
                
        self.application_box = ctk.CTkScrollableFrame(self.big_boi_panel,label_text=f"ID          ACCOUNT ID         REASON         CREDIT LIMIT         STATUS",label_font=("Arial",20),width=700,height=400,corner_radius=15,fg_color="#1e1e1e",border_color="gold",border_width=5)
        self.application_box.place(anchor="center", relx=0.5, rely=0.55)
        self.RefreshButton = ctk.CTkButton(self.big_boi_panel,border_color="gold",text="REFRESH",font=("Arial",30),fg_color=bg_text_color,bg_color=bg_text_color,hover_color="grey",corner_radius=1,command=Display_forums,border_width=5)
        self.RefreshButton.place(anchor="center", relx=0.9, rely=0.3)
        self.ID_entry = ctk.CTkEntry(self.big_boi_panel,border_color="gold",corner_radius=1,bg_color=bg_text_color,width=50,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30),placeholder_text="ID")
        self.ID_entry.place(anchor="center", relx=0.9, rely=0.4)
        self.card_id_entry = ctk.CTkEntry(self.giant_friggin_frame,placeholder_text="enter an ID for the card",border_color="Gold",border_width=2,bg_color=bg_text_color,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30),width=500)
        self.error_label = ctk.CTkLabel

        def preapprdecision():
            checker = self.ID_entry.get()
            if checker == None or checker == "":
                self.E1rrorLabel.configure(text="PLEASE ENTER A VALID ID!")
            else:
                self.giant_friggin_frame = ctk.CTkLabel(self,image=bg_image_thing,text="")
                self.giant_friggin_frame.place(x=0,y=0,relwidth=1, relheight=1)
                self.confirmButton = ctk.CTkButton(self.giant_friggin_frame,border_color="gold",text="Confirm",font=("Arial",30),fg_color="#00C300",bg_color=bg_text_color,hover_color="#007600",corner_radius=1)
                self.card_id_entry = ctk.CTkEntry(self.giant_friggin_frame,placeholder_text="enter an ID for the card",border_color="Gold",border_width=2,bg_color=bg_text_color,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30),width=500)
                self.card_id_entry.place(anchor="center", relx=0.5, rely=0.5,)
                self.confirmButton.configure(command=apprdecision)
                self.confirmButton.place(anchor="center", relx=0.5, rely=0.7)
        def apprdecision():
            self.error_label = ctk.CTkLabel(self.giant_friggin_frame, text="", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color)
            self.error_label.place(anchor="center",relx=0.5,rely=0.6)
            card_id = self.card_id_entry.get()
            if card_id != None and card_id != "":
                checker = DB_connection.credit_id_check(card_id)
                if checker == False:
                    database_id = self.ID_entry.get()
                    DB_connection.credit_request_review_admin(database_id,True,card_id)
                    Display_forums()
                    self.giant_friggin_frame.destroy()
                    self.confirmButton.destroy()
                    self.card_id_entry.destroy()
                    self.error_label.destroy()
                if checker == True:
                    self.error_label.configure(text="ID ALREADY IN USE!")
            else:
                self.error_label.configure(text="PLEASE ENTER AN ID!")
        def rejdecision():
            id_gette = self.ID_entry.get()
            try:
                id_getter = int(id_gette)
                if id_getter != None:
                    DB_connection.credit_request_review_admin(id_getter,False,0)
                    self.E1rrorLabel.configure(text=f"SUBMISSION ID : {id_getter} WAS REJECTED!")
                    self.ID_entry.delete(0,"end")
                    Display_forums()
                else:
                    self.E1rrorLabel.configure(text="PLEASE ENTER AN ID!")
            except ValueError:
                self.E1rrorLabel.configure(text=f"PLEASE ENTER A VALID ID!")
        self.confirmButton = ctk.CTkButton(self.big_boi_panel,border_color="gold",text="Confirm",font=("Arial",30),fg_color="#050049",bg_color=bg_text_color,hover_color="#080036",corner_radius=1)
        self.approveButton = ctk.CTkButton(self.big_boi_panel,command=preapprdecision,border_color="gold",text="APPROVE",font=("Arial",30),fg_color="#050049",bg_color=bg_text_color,hover_color="#080036",corner_radius=1,border_width=5,width=200)
        self.approveButton.place(anchor="center", relx=0.9, rely=0.5)
        
        self.denyButton = ctk.CTkButton(self.big_boi_panel,command=rejdecision,border_color="gold",text="DENY",font=("Arial",30),fg_color="#050049",bg_color=bg_text_color,hover_color="#080036",corner_radius=1,border_width=5,width=200)
        self.denyButton.place(anchor="center", relx=0.9, rely=0.6)
        def exitingappli():
            self.ID_entry.delete(0,"end")
            self.E1rrorLabel.configure(text="")
            self.controller.show_frame("AdminMainScreen")
        Exitbutton = ctk.CTkButton(self.big_boi_panel,text="EXIT",font=("Arial",20,"bold"),command=exitingappli,bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=1390)
        Exitbutton.place(anchor="center",relx=0.5,rely=0.971)

class AdminDebitReview(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller


        self.bg_image = ctk.CTkImage(
            light_image=Image.open(background_URL),
            dark_image=Image.open(background_URL),
            size=(1545, 850)
        )
        bg_image_thing = ctk.CTkImage(
            light_image=Image.open("D:/opera gx downloads/image (3).png"),
            dark_image=Image.open("D:/opera gx downloads/image (3).png"),
            size=(1545, 850)
        )
        bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.big_boi_panel = ctk.CTkFrame(self,height=750,width=1400,border_width=5,border_color="gold",fg_color="#050521")
        self.big_boi_panel.place(anchor="center",relx=0.5,rely=0.5)
        self.giant_friggin_frame = ctk.CTkLabel(self,image=bg_image_thing,text="")
        label = ctk.CTkLabel(self.big_boi_panel, text="BANK", font=("Arial", 58), text_color=text_color,bg_color=bg_text_color)
        label.place(anchor="center", relx=0.5, rely=0.08)

        label1 = ctk.CTkLabel(self.big_boi_panel,text="ALL DEBIT CARD REQUESTS", font=("Arial", 40), text_color=text_color,bg_color=bg_text_color)
        label1.place(anchor="center", relx=0.5, rely=0.15)
        self.E1rrorLabel = ctk.CTkLabel(self.big_boi_panel, text="", font=("Arial", 24), text_color=text_color,bg_color=bg_text_color)
        self.E1rrorLabel.place(anchor="center", relx=0.5, rely=0.93)
        def Display_forums():
            for widget in self.application_box.winfo_children():
                widget.destroy()
            info = DB_connection.cards_application_forum_read()
            for i in range(len(info)):
                if info[i][7] == True:
                    status = "APPROVED"
                if info[i][7] == False:
                    status = "REJECTED"
                if info[i][7] == None:
                    status = "PENDING"
                if info[i][7] == None and info[i][6] == None:
                    pass
                else:
                    card = ctk.CTkFrame(self.application_box, fg_color="#2b2b2b", corner_radius=8)
                    card.pack(fill="x", pady=8, padx=5, side="top")
                    info_text = f"      {info[i][0]}     |      {info[i][2]}     |     {info[i][6]}     |     {status}"
                    info_label = ctk.CTkLabel(card,text=info_text, font=("Arial", 20), text_color=text_color)
                    info_label.pack(side="left", padx=15, pady=10)
               
        self.application_box = ctk.CTkScrollableFrame(self.big_boi_panel,label_text=f"ID          ACCOUNT ID         REASON         STATUS",label_font=("Arial",20),width=700,height=400,corner_radius=15,fg_color="#1e1e1e",border_color="gold",border_width=5)
        self.application_box.place(anchor="center", relx=0.5, rely=0.55)
        self.RefreshButton = ctk.CTkButton(self.big_boi_panel,border_color="gold",text="REFRESH",font=("Arial",30),fg_color=bg_text_color,bg_color=bg_text_color,hover_color="grey",corner_radius=1,command=Display_forums,border_width=5)
        self.RefreshButton.place(anchor="center", relx=0.9, rely=0.3)
        self.ID_entry = ctk.CTkEntry(self.big_boi_panel,border_color="gold",corner_radius=1,bg_color=bg_text_color,width=50,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30),placeholder_text="ID")
        self.ID_entry.place(anchor="center", relx=0.9, rely=0.4)
        self.card_id_entry = ctk.CTkEntry(self.giant_friggin_frame,placeholder_text="enter an ID for the card",border_color="Gold",border_width=2,bg_color=bg_text_color,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30),width=500)
        self.error_label = ctk.CTkLabel
        def preapprdecision():
            checker = self.ID_entry.get()
            if checker == None or checker == "":
                self.E1rrorLabel.configure(text="PLEASE ENTER A VALID ID!")
            else:
                self.giant_friggin_frame = ctk.CTkLabel(self,image=bg_image_thing,text="")
                self.giant_friggin_frame.place(x=0,y=0,relwidth=1, relheight=1)
                self.confirmButton = ctk.CTkButton(self.giant_friggin_frame,border_color="gold",text="Confirm",font=("Arial",30),fg_color="#00C300",bg_color=bg_text_color,hover_color="#007600",corner_radius=1)
                self.card_id_entry = ctk.CTkEntry(self.giant_friggin_frame,placeholder_text="enter an ID for the card",border_color="Gold",border_width=2,bg_color=bg_text_color,text_color=text_color,fg_color=bg_text_color,font=("Arial", 30),width=500)
                self.card_id_entry.place(anchor="center", relx=0.5, rely=0.5,)
                self.confirmButton.configure(command=apprdecision)
                self.confirmButton.place(anchor="center", relx=0.5, rely=0.7)
        def apprdecision():
            self.error_label = ctk.CTkLabel(self.giant_friggin_frame, text="", font=("Arial", 35), text_color=text_color,bg_color=bg_text_color)
            self.error_label.place(anchor="center",relx=0.5,rely=0.6)
            card_id = self.card_id_entry.get()
            if card_id != None and card_id != "":
                checker = DB_connection.credit_id_check(card_id)
                if checker == False:
                    database_id = self.ID_entry.get()
                    DB_connection.debit_request_review_admin(database_id,True,card_id)
                    Display_forums()
                    self.giant_friggin_frame.destroy()
                    self.confirmButton.destroy()
                    self.card_id_entry.destroy()
                    self.error_label.destroy()
                if checker == True:
                    self.error_label.configure(text="ID ALREADY IN USE!")
            else:
                self.error_label.configure(text="PLEASE ENTER AN ID!")
        def rejdecision():
            id_gette = self.ID_entry.get()
            try:
                id_getter = int(id_gette)
                if id_getter != None:
                    DB_connection.debit_request_review_admin(id_getter,False,0)
                    self.E1rrorLabel.configure(text=f"SUBMISSION ID : {id_getter} WAS REJECTED!")
                    self.ID_entry.delete(0,"end")
                    Display_forums()
                else:
                    self.E1rrorLabel.configure(text="PLEASE ENTER AN ID!")
            except ValueError:
                self.E1rrorLabel.configure(text=f"PLEASE ENTER A VALID ID!")
        self.confirmButton = ctk.CTkButton(self.big_boi_panel,border_color="gold",text="Confirm",font=("Arial",30),fg_color="#050049",bg_color=bg_text_color,hover_color="#080036",corner_radius=1)
        self.approveButton = ctk.CTkButton(self.big_boi_panel,command=preapprdecision,border_color="gold",text="APPROVE",font=("Arial",30),fg_color="#050049",bg_color=bg_text_color,hover_color="#080036",corner_radius=1,border_width=5,width=200)
        self.approveButton.place(anchor="center", relx=0.9, rely=0.5)
        
        self.denyButton = ctk.CTkButton(self.big_boi_panel,command=rejdecision,border_color="gold",text="DENY",font=("Arial",30),fg_color="#050049",bg_color=bg_text_color,hover_color="#080036",corner_radius=1,border_width=5,width=200)
        self.denyButton.place(anchor="center", relx=0.9, rely=0.6)
        def exitingappli():
            self.ID_entry.delete(0,"end")
            self.E1rrorLabel.configure(text="")
            self.controller.show_frame("AdminMainScreen")
        Exitbutton = ctk.CTkButton(self.big_boi_panel,text="EXIT",font=("Arial",20,"bold"),command=exitingappli,bg_color=bg_text_color,text_color=text_color,hover_color="#0c0c3e",fg_color="#0f0f53",corner_radius=1,width=1390)
        Exitbutton.place(anchor="center",relx=0.5,rely=0.971)
app = App()
app.mainloop()
DB_connection.close_connection()