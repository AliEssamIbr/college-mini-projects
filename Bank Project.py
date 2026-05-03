from datetime import datetime

class BANK:
     def __init__(self):
         self.user_data = {}
         self.application_form = {}
         self.admin_data = {
              "Ali" : {
                    "password" : "SaucyBEANZ",
                    "info" : {
                        "first_name" : "Ali",
                        "last_name" : "Essam",
                        "age" : 19,
                        "role" : "the god damn owner/creator",
                        "status" : "fucking awesome B)"
                    }
              }
         }
         self.admin_user_contact = {}
         self.user_credit_card_request = {}
#    ================APPLYING FOR AN ACCOUNT================

#        +user stuff+   

     def user_apply(self,name,age,gender,nationality,job,income):
         x = self.application_form.get(name)
         if not x:
              self.application_form[name] = {
                   "user" : {
                        "info" : {
                            "name" : name,
                            "age" : age,
                            "gender" : gender,
                            "nationality" : nationality,
                            "job" : job,
                            "income" : income
                        },
                        "status" : "pending",
                        "temp_pass" : "",
                        "user_id" : ""
                     }  
                 }      
         if x:
              return "pend"      

     def user_check_pend(self,name):
         z = self.application_form.get(name)
         if not z:
              return "no"
         if z:
              if z["user"]["status"] == True:
                   return "yes"
              elif z["user"]["status"] == False:
                   return "noo"
              else:
                   return "pend"

     def user_id_and_pass(self,name):
         z = self.application_form.get(name)
         return z


#       +admin stuff+

     def admin_check_pending(self,name):
         x = self.application_form.get(name)
         if not x:
              return "no"
         if x:
              z = x["user"]
              return z 

     def admin_aprove_pend(self,name,approval):
         z = approval
         if z == "2":
            self.application_form[name]["user"]["status"] = True
            while True:
               user_id = input("\nplease enter the new USER ID : ")
               temp_user_pass = input("\nplease enter the user's temporary password : ")
               self.application_form[name]["user"]["temp_pass"] = temp_user_pass
               self.application_form[name]["user"]["user_id"] = user_id
               checkerr = module.user_add(user_id,temp_user_pass,name)
               if checkerr == "yes":
                    print("\n\n===Operation successful!===")
                    exit_loop()
                    break       
         elif z == "1":
               self.application_form[name]["user"]["status"] = False
         else:
              self.application_form[name]["user"]["status"] = "pending"

     def application_forum_info_display(self):
              print("\n\n","="*40,sep="")
              for app_id, app_data in self.application_form.items():
                    user = app_data.get("user", {})
                    info = user.get("info", {})

                    if info: 
                         temp_name = info.get("name")
                         temp_age = info.get("age")
                         temp_gender = info.get("gender")
                         temp_natio = info.get("nationality")
                         temp_job = info.get("job")
                         temp_income = info.get("income")
                         temp_status = user.get("status")
                         if temp_status == True:
                              temp_status = "approved"
                         elif temp_status == False:
                              temp_status = "rejected"
                         else:
                              temp_status = "pending"
                         print(f"\n-----------------------------\n=application sheet=\n info;\n"
                              f"Name: {temp_name}\n"
                              f"D.O.B: {temp_age}\n"
                              f"Gender: {temp_gender}\n"
                              f"Nationality: {temp_natio}\n"
                              f"Job: {temp_job}\n"
                              f"Yearly Income: {temp_income}\n"
                              f"Status: {temp_status}")
              exit_loop()

     def admin_application_delete(self,name):
         z = self.application_form.get(name)
         if z:
              self.application_form.pop(name)
              return True
         if not z:
              return False

#    ================MAIN UI/FUNCTIONS================

#  -------------ACCOUNT BASED STUFF-------------

#      V user stuff V

     def user_add(self,user_id,user_password,name):
         z = self.application_form.get(name)
         check = self.user_data.get(user_id)
         if not check:
          self.user_data[user_id] = {
                    "user" : {
                         "info": z["user"]["info"],
                         "password": user_password,
                         "balance" : 0.0,
                         "lock" : False,
                         "pass_attempts" : 3,
                         "history" : {
                              "process" : [],
                              "amount" : [],
                              "time" : []
                              },
                         "credit_card" : {
                              "id_number" : "",
                              "remaining_balance" : 0.0,
                              "limit" : 0,
                              "history" : {
                                   "process" : [],
                                   "amount" : [],
                                   "time" : []
                              },
                         },
                         "inventory" : []
                    }
               }
          return "yes"
         elif check:
              print("\nThis User ID is already in use, try using a different one.")
              return "n"

     def user_login(self, user_id, user_password):
          x = self.user_data.get(user_id)
          if not x:
               return False
          if x["user"]["lock"]: 
               return "locked"
          if x["user"]["pass_attempts"] <= 0:
               x["lock"] = True
               return "locked"
          if x["user"]["password"] == user_password:
               x["user"]["pass_attempts"] = 3 
               cent = x["user"]
               return cent
          else:
               x["user"]["pass_attempts"] -= 1
               if x["user"]["pass_attempts"] <= 0:
                    x["user"]["lock"] = True
                    return "locked" 
               return "no"

     def login_attempt_check(self,user_id):
         checker = self.user_data.get(user_id)
         z = checker["user"]["pass_attempts"]
         if z > 0:  
               return z
         elif z <=0:   
               return "lockee"
           
     def user_info_display_user(self,user_id):
         x = self.user_data.get(user_id)
         if not x:
              return False
         if x:
               
               temp_name =x["user"]["info"]["name"]
               temp_age =x["user"]["info"]["age"]
               temp_gender =x["user"]["info"]["gender"]
               temp_natio =x["user"]["info"]["nationality"]
               temp_job =x["user"]["info"]["job"]
               temp_income = x["user"]["info"]["income"]
               print("-----------------------------------\nhere is the info : \nName : ", temp_name, "\nD.O.B : ", temp_age,"\nGender : ",temp_gender,"\nnationality : ",temp_natio,"\nJob : ",temp_job,"\nYearly Income : ",temp_income, sep="")
               exit_loop()
               return True

     def user_password_change(self,user_id,new_password):
         self.user_data[user_id]["user"]["password"] = new_password
         return True
 
     def history_add(self,user_id,type,amount):
          current_time = datetime.now()
          self.user_data[user_id]["user"]["history"]["process"].append(type)
          self.user_data[user_id]["user"]["history"]["amount"].append(amount)
          self.user_data[user_id]["user"]["history"]["time"].append(current_time)
 
     def history_read(self,user_id):
          checker = self.user_data.get(user_id)
          if not checker:
               print("error")
          else:
               name = checker["user"]["info"]["name"]
               print("             ",name,"'s transaction history\n","-"*50,sep="")
               for process,amount,time in zip(checker["user"]["history"]["process"],checker["user"]["history"]["amount"],checker["user"]["history"]["time"]):
                    print("\n\nProcess : ",process,"\nAmount ($) : ",amount,"\nDate : ",time.strftime('%Y/%m/%d | %I:%M %p'))

     def user_balance_check(self,user_id):
         x = self.user_data.get(user_id)
         return x["user"]["balance"]

     def withdraw(self,user_id,amount):
          checker = self.user_data.get(user_id)
          if not checker:
               return "error"
          elif checker:
               b_checker = checker["user"]["balance"]
               if b_checker == 0:
                    return "empty"
               else:
                    if (b_checker - amount) < 0:
                         return "insufficient"
                    else:
                         self.user_data[user_id]["user"]["balance"] = self.user_data[user_id]["user"]["balance"] - amount
                         return "success" 
     
     def withdraw_all(self,user_id):
          checker = self.user_data.get(user_id)
          if not checker:
               return "error"
          elif checker:
               b_checker = checker["user"]["balance"]
               if b_checker == 0:
                    return "empty"
               else:
                    z = self.user_data[user_id]["user"]["balance"]
                    self.user_data[user_id]["user"]["balance"] = self.user_data[user_id]["user"]["balance"] - self.user_data[user_id]["user"]["balance"]
                    return z
     
     def deposit(self,user_id,amount):
          checker = self.user_data.get(user_id)
          if not checker:
               return "error"
          elif checker:
               self.user_data[user_id]["user"]["balance"] = self.user_data[user_id]["user"]["balance"] + amount
               return "success"
 
     def user_add_messages(self,user_id,message):
          current_datetime = datetime.now()
          checker = self.admin_user_contact.get(user_id)
          if not checker:
            self.admin_user_contact[user_id] = {
            "info" : {
                "messages" : [message,],
                "time" : [current_datetime,]
            }
            }
          else:
            self.admin_user_contact[user_id]["info"]["messages"].append(message)
            self.admin_user_contact[user_id]["info"]["time"].append(current_datetime)
          return True


#      V admin stuff V

     def admin_admin_read(self):
          checker = self.admin_data.get("Ali")
          if checker:
               temp_name =checker["info"]["first_name"]
               temp_name2 =checker["info"]["last_name"]
               temp_age =checker["info"]["age"]
               temp_role =checker["info"]["role"]
               temp_status = checker["info"]["status"]
               print("\n\n","-"*30, "\nFirst Name : ", temp_name,"\nlast Name : ", temp_name2, "\nAge : ", temp_age,"\nRole : ",temp_role,"\nStatus : ",temp_status,"\n","-"*30 ,sep="")
               exit_loop()
               return True
 
     def admin_user_lock(self,user_id):
          z = module.user_info_display(user_id)
          if z == True:
               while True:
                    locking = input("\nwould you like to lock/unlock this user's account?\n      1 - Lock       2 - Unlock\n            0 - EXIT\nEnter : ")
                    if locking == "1":
                         self.user_data[user_id]["user"]["lock"] = True
                         break
                    elif locking == "2":
                         self.user_data[user_id]["user"]["lock"] = False
                         self.user_data[user_id]["user"]["pass_attempts"] = 3
                         break
                    elif locking == "0":
                         break
                    else:
                         print("\nInvalid option, try again")
          elif z == False:
                    print("user not found.")
 
     def user_info_display(self,user_id):
         x = self.user_data.get(user_id)
         if not x:
              return False
         if x:
               
               temp_name =x["user"]["info"]["name"]
               temp_age =x["user"]["info"]["age"]
               temp_gender =x["user"]["info"]["gender"]
               temp_natio =x["user"]["info"]["nationality"]
               temp_job =x["user"]["info"]["job"]
               temp_income = x["user"]["info"]["income"]
               temp_pass = x["user"]["password"]
               if x["user"]["lock"] == True:
                    temp_status = "Locked"
               elif x["user"]["lock"] == False:
                    temp_status = "Unlocked"
               temp_balance = x["user"]["balance"]
               temp_attempt = x["user"]["pass_attempts"]
               print("\nName : ", temp_name, "\nD.O.B : ", temp_age,"\nGender : ",temp_gender,"\nnationality : ",temp_natio,"\nJob : ",temp_job,"\nYearly Income : ",temp_income, sep="")
               print("account password : ",temp_pass,"\ncurrent balance : ",temp_balance,"\naccount status : ",temp_status,"\nRemaining password attempts : ",temp_attempt,sep="")
               return True
 
     def user_DB_display(self):
          print("\n\n","="*40)
          for app_id, app_val in self.user_data.items():
               print("\n---------------------------------\n      account ID : ",app_id,sep="")
               module.user_info_display(app_id)
          exit_loop()
 
     def admin_read_messages(self, user_id):
        booke = self.admin_user_contact.get(user_id)
        if not booke:
            return None
        return booke["info"] 
     
     def admin_read_all_messages(self):
        if not self.admin_user_contact:
            return None
        return self.admin_user_contact

     def user_check_DB(self,user_id,user_password):
         z = self.user_data.get(user_id)   
         if not z:
              return"no"  
         elif z in self.user_data:
              pass_check = user_password
              if pass_check == self.user_data[user_id]["user"]["password"]:
                   info =  z["user"]["info"]
                   return info
              else:
                   return "no"
 
#      V extra stuff V

     def user_inventory_add(self,user_id,item):
          self.user_data[user_id]["user"]["inventory"].append(item)

     def user_display_inventory(self,user_id):
          data = self.user_data.get(user_id)
          while True:
               print("\n\n               INVENTORY\n","+"*40)
               for value in data["user"]["inventory"]:
                    print("-",value)
               exit = input("           0 - EXIT")
               if exit =="0":
                    break
               else:
                    print("invalid option, try again")

     def user_information_unit(self,user_id):
         x = self.user_data.get(user_id)
         if x:
          return x
         else:
              return False

     def user_db_check(self,user_id):
         check = self.user_data.get(user_id)
         if not check:
              return False
         elif check:
              return True


#  -------------CREDIT CARD BASED STUFF-------------

#      V user stuff V

     def user_credit_apply(self,user_id,reason,limit):
              checker = self.user_data[user_id]
              self.user_credit_card_request[user_id] = {
                   "user" : {
                        "info" : {
                            "name" : checker["user"]["info"]["name"],
                            "age" : checker["user"]["info"]["age"],
                            "gender" : checker["user"]["info"]["gender"],
                            "nationality" : checker["user"]["info"]["nationality"],
                            "job" : checker["user"]["info"]["job"],
                            "income" : checker["user"]["info"]["income"]
                        },
                        "status" : "pending",
                        "reason" : reason,
                        "limit" : limit

                     }  
                 }     

     def check_yearly_income(self,user_id):
          checker = self.user_data.get(user_id)
          if checker["user"]["info"]["income"] < 50000:
               return 1
          elif 50000 <= checker["user"]["info"]["income"] < 100000:
               return 2
          elif 100000 <= checker["user"]["info"]["income"] < 500000:
               return 3
          elif checker["user"]["info"]["income"] >= 500000:
               return 4

     def user_credit_apply_check(self,user_id,reason,limit):
          x = self.user_credit_card_request.get(user_id)
          if not x:
               module.user_credit_apply(user_id,reason,limit)
               return "success"
          elif x:
               if x["user"]["status"] == "pending":
                    return "pending"
               elif x["user"]["status"] == True:
                    return True
               elif x["user"]["status"] == False:
                    return False

     def user_display_credit_card(self,user_id):
          info = self.user_data.get(user_id)
          print("\n           credit card info\n","-"*40,"\ncredit card ID : ",info["user"]["credit_card"]["id_number"],"\nremaining funds : ",info["user"]["credit_card"]["remaining_balance"],"\ncredit card limit: ",info["user"]["credit_card"]["limit"],"\n","-"*40,sep="")
  
     def credit_history_add(self,user_id,type,amount):
          current_time = datetime.now()
          self.user_data[user_id]["user"]["credit_card"]["history"]["process"].append(type)
          self.user_data[user_id]["user"]["credit_card"]["history"]["amount"].append(amount)
          self.user_data[user_id]["user"]["credit_card"]["history"]["time"].append(current_time)
  
     def credit_history_read(self,user_id):
          checker = self.user_data.get(user_id)
          if not checker:
               print("no history found")
          else:
               name = checker["user"]["info"]["name"]
               print(name,"'s credit card history\n","-"*30,sep="")
               for process,amount,time in zip(checker["user"]["credit_card"]["history"]["process"],checker["user"]["credit_card"]["history"]["amount"],checker["user"]["credit_card"]["history"]["time"]):
                    print("\n\nProcess : ",process,"\nAmount ($) : ",amount,"\nDate : ",time.strftime('%Y/%m/%d | %I:%M %p'))
 
     def user_check_pend_credit(self,user_id):
          z = self.user_credit_card_request.get(user_id)
          if not z:
               return "no"
          if z:
               if z["user"]["status"] == True:
                    return "yes"
               elif z["user"]["status"] == False:
                     return "noo"
               else:
                    return "pend"
     
     def credit_check(self,user_id,amount):
          checker = self.user_data.get(user_id)
          if not checker:
               return "error"
          elif checker:
               b_checker = checker["user"]["credit_card"]["remaining_balance"]
               if b_checker == 0:
                    return "empty"
               else:
                    if (b_checker - amount) < 0:
                         return "insufficient"
                    else:
                         self.user_data[user_id]["user"]["credit_card"]["remaining_balance"] = self.user_data[user_id]["user"]["credit_card"]["remaining_balance"] - amount
                         return "success" 

#      V admin stuff V
     def admin_aprove_pend_credit(self,user_id,approval):
         if approval == "1":
               self.user_credit_card_request[user_id]["user"]["status"] = False
         elif approval == "2":
               self.user_credit_card_request[user_id]["user"]["status"] = True
               while True:
                    credit_id = input("please enter the new credit card ID : ")
                    limit = self.user_credit_card_request[user_id]["user"]["limit"]
                    checker = module.add_credit_card(user_id,credit_id,limit)
                    if checker == "used":
                         print("ID already in use, try a different one.")
                    elif checker == "success":
                         break
         else:
              self.user_credit_card_request[user_id]["user"]["status"] = "pending"
     
     def add_credit_card(self,user_id,card_number,limit):
          checker = self.user_data.get(user_id)
          if checker:
               if checker["user"]["credit_card"]["id_number"] == card_number:
                    return "used"
               elif checker["user"]["credit_card"]["id_number"] != card_number:
                    self.user_data[user_id]["user"]["credit_card"]["id_number"] = card_number
                    self.user_data[user_id]["user"]["credit_card"]["remaining_balance"] = limit
                    self.user_data[user_id]["user"]["credit_card"]["limit"] = limit
                    return "success"
     
     def admin_credit_pend_check(self,user_id):
          checker = self.user_credit_card_request.get(user_id)
          if not checker:
               return "not found"
          else:
               return checker["user"]
     
     def user_credit_request_display(self):
        if not self.user_credit_card_request:
            print("\n" + "-"*40 + "\nNo credit requests at the moment")
            return

        for user_id in self.user_credit_card_request.keys():
            print("\n" + "-"*23 + f"\nAccount ID : {user_id}")
            self.admin_display_all_credit_requests(user_id)
     
     def user_DB_credit_card_display(self):
        if not self.user_data:
            print("\n\n" + "="*40 + "\n      No credit cards at the moment\n","="*40,sep="")
            return

        for user_id in self.user_data.keys():
            print("\n" + "-"*40,sep="")
            self.admin_display_all_credit_cards(user_id)
                   
     def admin_display_all_credit_requests(self, user_id):
        request_data = self.user_credit_card_request.get(user_id)
        
        if not request_data:
            print("No request found for this user.")
        else:
            name = request_data["user"]["info"]["name"]
            status = request_data["user"]["status"]
            limit = request_data["user"]["limit"]
            
            print("="*40)
            print(f"Name   : {name}")
            print(f"Status : {status}")
            print(f"Limit  : {limit}$")
     
     def admin_display_all_credit_cards(self, user_id):
          request_data = self.user_data.get(user_id)
          if not request_data:
              print("="*80,"\n          there are no active bank accounts at the moment.\n","="*80,sep="")
          else:
               if request_data["user"]["credit_card"]["id_number"] != "":
                    card_id = request_data["user"]["credit_card"]["id_number"]
                    name = request_data["user"]["info"]["name"]
                    funds = request_data["user"]["credit_card"]["remaining_balance"]
                    limit = request_data["user"]["credit_card"]["limit"]
               
                    print("="*40)
                    print("Card ID : ",card_id,sep="")
                    print(f"Name   : ",name,sep="")
                    print(f"Remaining funds : ",funds,sep="")
                    print(f"Limit  : ",limit,sep="")
               else:
                    print("\nAccount ID : ",user_id," does not have any credit cards.",sep="")
     
     def credit_card_request_delete(self,user_id):
          x = self.user_credit_card_request[user_id]
          if x:
               self.user_credit_card_request.pop(user_id)
               return "deleted"
    



#    ================APPLYING FOR AN ACCOUNT================
#        +user stuff+        
def application_function():
     print("\n\n              Application Forum\n","-"*43)
     new_name = input("\nplease enter your full name : ")
     new_age = input("\nplease enter your D.O.B : ")
     new_gender = input("\nplease enter your gender (M/F) : ")
     new_nati = input("\nplease enter your nationality : ")
     new_job = input("\nplease enter your job : ")
     while True:
          income = (input("\nplease enter your yearly income : "))
          try:
               val = int(income)
               break
          except ValueError:
               print("\n<<<====that's not a number, please enter a number!====>>>")
          


     checker = module.user_apply(new_name,new_age,new_gender,new_nati,new_job,val)
     if checker == "pend":
          print("\n\n","-"*120,"\n        you have already applied for an account, please check your submission through our checking function!\n","-"*120,sep="")
     else:
          print("\n\n","-"*120,"\n        your forum has been submitted to our admins, this may take a while so please check back with us later!\n","-"*120,sep="")
     exit_loop()

def application_checker_function():
     print("\n\n         Appliction checking platform\n----------------------------------------------------------")
     print("   Welcome to the application checking platform!")
     checking_name = input("\nplease enter your full name exactly like you did with the application forum!\nEnter : ")
     checker = module.user_check_pend(checking_name)
     if checker == "no":
          print("\n\n","-"*120,"\n      sorry! but it appears you have not applied for a new account, or you might have misspelled your name!\n","-"*120,sep="")
     elif checker == "yes":
          z = module.user_id_and_pass(checking_name)
          print("\n\n","-"*120,"\n      your application was approved!\nhere is your Bank account ID and your temporary password (you must change it after logging in for security reasons)",sep="")
          print("\n   Bank account number : ", z["user"]["user_id"] , "\n    Temporary password : ", z["user"]["temp_pass"],"\n","-"*120,sep="")
     elif checker == "noo":
          print("\n\n","-"*120,"\n           sorry! but it seems your submission was rejected! you can submit another forum if you'd like!\n","-"*120,sep="")
     elif checker == "pend":
          print("\n\n","-"*120,"\n           your application forum is still pending, please check back again later!\n","-"*120,sep="")              
     exit_loop()
#       +admin stuff+

def admin_application_checker():
     while True:
          print("\n\n       admin application platform \n","-"*40,sep="")
          admin_checker_func = (input("please choose one of the programs.\n\n 1 - application review \n 2 - all existing applications \n 3 - delete an application \n\n           0 - EXIT\n\n Enter : "))
          if admin_checker_func == "1":
               print("\n\n","="*60,sep="")
               tempo_name = input("\nplease enter the full name of the forum you want to review : ")
               checker = module.admin_check_pending(tempo_name)
               if checker == "no":
                    print("\n","-"*100,"\napplication forum not found, you might have misspelled the name.\n","-"*100,sep="")
                    exit_loop()
               else:
                    temp_name =checker["info"]["name"]
                    temp_age =checker["info"]["age"]
                    temp_gender =checker["info"]["gender"]
                    temp_natio =checker["info"]["nationality"]
                    temp_job =checker["info"]["job"]
                    temp_income = checker["info"]["income"]
                    while True:
                         print("\nsubmission sheet found, here is the data : \n")
                         print("Name : ", temp_name, "\nD.O.B : ", temp_age,"\nGender : ",temp_gender,"\nnationality : ",temp_natio,"\nJob : ",temp_job,"\nYearly Income : ",temp_income, sep="")
                         approval = (input("\n 1 - reject          2 - approve\n\n         0 - EXIT\n\n Enter : "))
                         if approval == "1" or "2":
                              module.admin_aprove_pend(tempo_name,approval)
                              break
                         elif approval == "0":
                              break
                         else: 
                              print("\ninvalid option, please try again")  
          elif admin_checker_func =="2":
               module.application_forum_info_display()
          elif admin_checker_func == "3":
               admin_application_deletion()
          elif admin_checker_func == "0":
               break
          else:
               print("\ninvalid option, try again.")

def admin_application_deletion():
     user_namee = input("\nEnter the forums submitted name : ")
     z = module.admin_application_delete(user_namee)
     if z == False:
          print("\n===forum not found, try again.===")
     elif z == True:
          print("\n\n===forum removal successful!===")
     exit_loop()


#    ================MAIN UI/FUNCTIONS================

#  -------------ACCOUNT BASED STUFF-------------

#      V user stuff V

def user_ui(user_id):
     tempe = module.user_information_unit(user_id)
     name = tempe["user"]["info"]["name"]
     while True:
          print("\n\n              welcome",name,"\n-----------------------------------")
          user_ui_function = (input("please choose the program you want to use! \n\n       1 - Display account info \n       2 - check balance \n       3 - Credit Card \n       4 - check Transaction History \n       5 - change password \n       6 - inventory \n       7 - SHOP\n\n 0 - EXIT \n            Enter : "))
          if user_ui_function == "0":
               break
          elif user_ui_function =="1":
               module.user_info_display_user(user_id)
          elif user_ui_function == "2":
               while True:
                    B_checker = module.user_balance_check(user_id)
                    print("\n                your current Balance is : ",B_checker," $\n-----------------------------------------------------------------------",sep="")
                    ask = input("1 - deposit funds\n2 - withdraw funds\n3 - withdraw all funds\n4 - send funds to another account\n        0 - EXIT\n Enter : ")
                    if ask == "1":
                         user_deposit(user_id)
                    elif ask == "2":
                         user_withdraw(user_id)
                    elif ask == "3":
                         user_withdraw_all(user_id)
                    elif ask == "4":
                         user_send_funds(user_id)
                    elif ask == "0":
                         break
                    else:
                         print("invalid option, try again.")
          elif user_ui_function == "3":
               user_credit_card_ui(user_id)
          elif user_ui_function == "4":
               module.history_read(user_id)
               exit_loop()
          elif user_ui_function == "5":
               new_pass = input("\nplease enter your new password : ")
               check = module.user_password_change(user_id,new_pass)
               if check == True:
                    print("\npassword changed successfully!")
          elif user_ui_function == "6":
               module.user_display_inventory(user_id)
          elif user_ui_function == "7":
               shop_ui(user_id)
          else:
               print("\ninvalid option, please try again")

def user_log_in():
     while True:
          user_id = input("Please enter your Account's ID : ")
          user_pass = input("Please enter your Account's Password : ")
          c_checker = input("   0 - EXIT       1 - Continue\n         Enter : ")
          if c_checker == "1":
               checker = module.user_login(user_id,user_pass)
               if checker == False:
                    print("\nWe couldn't find your account, Please try again!")
               elif checker == "no":
                    z = module.login_attempt_check(user_id)
                    print("\n===incorrect password, please try again===")
                    print("\n              ===remaining attempts : ", z," ===",sep="")
               elif checker == "locked":
                         print("\nYour bank account is locked, please contact our admins to unlock your account!")
                         exit_loop()
                         break
               else:
                    user_ui(user_id)
                    break
          elif c_checker == "0":
               break
          else:
               print("\ninvalid option, try again.")

def admin_support__user__(user_id):
     message = input("V Please explain your problem in detail, our admins will work on it as soon as possible! V\n")
     check = module.user_add_messages(user_id,message)
     if check == True:
          print("\n           ===report submitted successfully!===")
          exit_loop()
def user_send_funds(user_id):
     temp_user_id_2 = input("\n please enter the ID of the account you want to send funds to : ")
     if user_id == temp_user_id_2:
          print("\n<==you are attempting to send funds to your own account, why would you do that?==>")
     else:
          user_check = module.user_information_unit(temp_user_id_2)
          if user_check == False:
               print("\n/ error / account not found, try again!")
          else:
               name = user_check["user"]["info"]["name"]
               print("account found!\n","Account holder's name : ",name,sep="")
               while True:
                    amount = input("how much would you like to send over? ($)\nEnter : ")
                    try:
                         F_amount = float(amount)
                         break
                    except ValueError:
                         print("\ninvalid amount, try again.")
               U_checker = module.withdraw(user_id,F_amount)
               if U_checker == "error":
                    print("\n              ===operation declined===\n-------------------------------------------\nerror, account not found, contact tech support to fix the issue")
               elif U_checker == "empty":
                    print("\n              ===operation declined===\n-------------------------------------------\nyour account balance is 0 at the moment")
               elif U_checker == "insufficient":
                         print("\n              ===operation declined===\n-------------------------------------------\n you do not have the required amount in your account")
                         while True:
                              confirmation = input("\nwould you like to send all available funds in your account instead?\n1 - Confirm      2 - Decline\nEnter : ")
                              if confirmation == "1":
                                   B_check = module.user_balance_check(user_id)
                                   w_checker = module.withdraw_all(user_id)
                                   if w_checker == "error":
                                        print("\n              ===operation declined===\n-------------------------------------------\nerror, account not found, contact tech support to fix the issue")
                                        break
                                   elif w_checker == "empty":
                                        print("\n              ===operation declined===\n-------------------------------------------\nyour account balance is 0 at the moment")
                                        break
                                   else:
                                        S_checker = module.deposit(temp_user_id_2,B_check)
                                        if S_checker == "error":
                                             print("\n              ===operation declined===\n-------------------------------------------\nerror, account not found, contact tech support to fix the issue")
                                             break
                                        elif S_checker == "success":
                                             id_thingy = "sent funds to account ID : "+temp_user_id_2
                                             id_thingy2 = "received funds from account ID : "+user_id
                                             module.history_add(user_id,id_thingy,w_checker)
                                             module.history_add(temp_user_id_2,id_thingy2,w_checker)
                                             print("\n\n              ===operation successful!===\n      you sent ",B_check," $ from your account to : ",name,sep="")
                                             break
                              elif confirmation == "2":
                                   break
                              else:
                                   print("\ninvalid option, try again")
               elif U_checker =="success":
                    id_thingy = "sent funds to account ID : "+temp_user_id_2
                    id_thingy2 = "received funds from account ID : "+user_id
                    module.history_add(user_id,id_thingy,F_amount)
                    module.history_add(temp_user_id_2,id_thingy2,F_amount)
                    S_checker = module.deposit(temp_user_id_2,F_amount)
                    if S_checker == "error":
                         print("\n              ===operation declined===\n-------------------------------------------\nerror, account not found, contact tech support to fix the issue")
                    elif S_checker == "success":
                         print("\n\n              ===operation successful!===\n           you sent ",F_amount," $ from your account to : ",name,sep="")
def user_withdraw_all(user_id):
     while True:
          check = input("\n\nconfirm you want to withdraw all funds from your account  : \n         1 - Confirm      2 - Cancel\n Enter : ")
          if check == "1":
               checker = module.withdraw_all(user_id)
               if checker == "error":
                    print("\n              ===operation declined===\n-------------------------------------------\n      error, account not found, contact tech support to fix the issue")
                    exit_loop()
                    break
               elif checker == "empty":
                    print("\n              ===operation declined===\n-------------------------------------------\n      your account balance is 0 at the moment")
                    exit_loop()
                    break
               else:
                    module.history_add(user_id,"Full Balance Withdraw",checker)
                    print("\n              ===operation successful!===\n        you withdrew ",checker," $ from your account.",sep="")
                    exit_loop()
                    break
          elif check == "2":
               break
          else:
               print("invalid option, try again")
def user_deposit(user_id):
     while True:
          while True:
               amount = input("\n\nPlease enter the amount of funds you'd like to add to your account's balance ($) : ")
               try:
                    F_amount = float(amount)
                    break
               except ValueError:
                    print("\ninvalid amount, try again.")
          D_check = module.deposit(user_id,F_amount)
          if D_check == "success":
               module.history_add(user_id,"Deposit",F_amount)
               print("\n      ===operation successful!===\n      you deposited ",F_amount," $ into your account.",sep="")
               exit_loop()
               break
          else:
               print("error, check code")
               break
def user_withdraw(user_id):
     while True:
          amount = int(input("\n\n----------------------------------------------------------------\nPlease enter the amount you want to withdraw : "))
          try:
               F_amount = float(amount)
               break
          except ValueError:
               print("\ninvalid amount, try again.")
     checker = module.withdraw(user_id,F_amount)
     if checker == "error":
          print("\n              ===operation declined===\n-------------------------------------------\n      error, account not found, contact tech support to fix the issue")
     elif checker == "empty":
          print("\n              ===operation declined===\n-------------------------------------------\n      your remaining credit is 0 at the moment")
     elif checker == "insufficient":
               print("\n              ===operation declined===\n-------------------------------------------\n      you do not have the required amount in your credit card")
               user_withdraw_all(user_id)
     elif checker =="success":
          module.history_add(user_id,"withdraw",F_amount)
          print("\n           ===operation successful!===\n      you withdrew ",F_amount," $ from your account.",sep="")
     exit_loop()
#      V admin stuff V

def admin_user_ui():
     while True:
          print("\n\n         Admin-user platform\n","="*40,"\n   Welcome to the Admin's platform!",sep="")
          options = input("\n      choose one of the programs : \n\n1 - display all current accounts \n2 - display an accounts details \n3 - lock/unlock user accounts \n4 - check support tickets \n5 - check credit cards \n\n           0 - EXIT \nEnter : ")
          if options == "1":
               module.user_DB_display()
          elif options == "2":
               user_idd = input("\n\nenter the account's ID to continue : ")
               checker = module.user_info_display(user_idd)
               if checker == False:
                    print("\n\n          ///Error///\n         account not found")
                    exit_loop()
               else:
                    while True:
                         History_check = input("\n\nWould you like to check the accounts transaction history?\n             1 - Confirm   2 - Cancel\nEnter : ")
                         if History_check == "1":
                              print("\n\n")
                              module.history_read(user_idd)
                              exit_loop()
                              break
                         elif History_check =="2":
                              break
                         else:
                              print("Invalid option, try again.")
          elif options == "3":
               admin_user_lockk()
          elif options =="4":
               admin_support_ui()
          elif options =="5":
               admin_credit_card_ui()
          elif options == "0":
               break
          else:
               print("\nInvalid option, try again.")

def admin_user_lockk():
     print("="*50)
     user_id_temp = input("Enter the user's account ID to proceed : ")
     module.admin_user_lock(user_id_temp)

def admin_support_ui():
    while True:
        print("\n\n           support tickets\n","="*40,sep="")
        options = input("\n1 - review a support ticket \n2 - delete a support ticket \n3 - display all support tickets\n\n       0 - EXIT\nEnter : ")
        
        if options == "1":
            loc_id = input("enter the user's id : ")
            info = module.admin_read_messages(loc_id)

            if info is None:
                print("\nNo support tickets found for this ID.")
                exit_loop()
            else:
                print(f"\n--- Messages for Account ID: {loc_id} ---")
                for msg, t in zip(info["messages"], info["time"]):
                    readable_time = t.strftime('%Y/%m/%d | %I:%M %p')
                    print(f"[{readable_time}] User: {msg}")
                print("-----------------------------------------------")
        elif options =="3":
               all_data = module.admin_read_all_messages()
               if not all_data:
                    print("\n\nThe support database is currently empty.")
               else:
                print("\n---------- GLOBAL TICKET LOG ----------")
                for user_id, data in all_data.items():
                    print(f"\nUSER ID: {user_id}")
                    print("-" * 20)
                    for msg, t in zip(data["info"]["messages"], data["info"]["time"]):
                        print(f" > [{t.strftime('%Y/%m/%d | %I:%M %p')}] {msg}")
               print("\n-----------------------------------------")
               exit_loop()
        elif options == "2":  
             loc_id = input("Enter user ID to clear tickets: ")
             if loc_id in module.admin_user_contact:
                module.admin_user_contact.pop(loc_id)
                print("Tickets deleted.")
             else:
                print("User not found.")
             exit_loop()
        elif options == "0":
            break
        else:
            print("\nInvalid option, try again")

#      V extra stuff V
def shop_ui(user_id):
     while True:
          while True:
               print("\n\n              Shop\n","="*40,"\n         Welcome to the digital shop!\n         feel free to browse our items!")
               options = input("\n      1 - iPhone     1000$\n      2 - Wrist Watch     35$\n      3 - headphones     60$\n      4 - PowerBank (10k mAh)     24.99$\n      5 - Leather wallet     10$\n      6 - keychain     1$\n      7 - keychain(but more expensive)     10000$\n      8 - cheap perfume     15$\n\n      0 - EXIT\nEnter : ")
               try:
                    val = int(options)
                    if val >= 0 and val < 9:
                         break
               except ValueError:
                    print("invalid option, try again")
          if val == 0:
               break
          else:
               while True:
                    method = input("\n      payment method\n1 - Cash      2 - credit\nEnter : ")
                    try:
                         M_val = int(method)
                         if M_val != 1 or 2:
                              print("please choose one of the options!")
                              break
                    except ValueError:
                         print("invalid option, try again")
               confirm = input("\n1 - Confirm purchase      2 - cancel\nEnter : ")
               try:
                    C_val = int(confirm)
                    if C_val != 1:
                         print("invalid option, try again")
                    elif C_val == 2:
                         break
               except ValueError:
                    print("invalid option, try again")
               match val:
                    case 1:
                         amount = 1000
                         item = "iPhone"
                         if M_val == 1:
                              cash_pay(user_id,amount,item)
                         elif M_val == 2:
                              credit_pay(user_id,amount,item)
                         
                    case 2:
                         amount = 35
                         item = "Wrist Watch"
                         if M_val == 1:
                              cash_pay(user_id,amount,item)
                         elif M_val == 2:
                              credit_pay(user_id,amount,item)
                         
                    case 3:
                         amount = 60
                         item = "Headphones"
                         if M_val == 1:
                              cash_pay(user_id,amount,item)
                         elif M_val == 2:
                              credit_pay(user_id,amount,item)
                         
                    case 4:
                         amount = 24.99
                         item = "PowerBank (10k mAh)"
                         if M_val == 1:
                              cash_pay(user_id,amount,item)
                         elif M_val == 2:
                              credit_pay(user_id,amount,item)
                         
                    case 5:
                         amount = 10
                         item = "Leather Wallet"
                         if M_val == 1:
                              cash_pay(user_id,amount,item)
                         elif M_val == 2:
                              credit_pay(user_id,amount,item)
                         
                    case 6:
                         amount = 1
                         item = "Keychain"
                         if M_val == 1:
                              cash_pay(user_id,amount,item)
                         elif M_val == 2:
                              credit_pay(user_id,amount,item)
                         
                    case 7:
                         amount = 10000
                         item = "keychain(but more expensive)"
                         if M_val == 1:
                              cash_pay(user_id,amount,item)
                         elif M_val == 2:
                              credit_pay(user_id,amount,item)
                         
                    case 8:
                         amount = 15
                         item = "Cheap perfume"
                         if M_val == 1:
                              cash_pay(user_id,amount,item)
                         elif M_val == 2:
                              credit_pay(user_id,amount,item)

def credit_pay(user_id,amount,item):
     Cash_check = module.credit_check(user_id,amount)
     if Cash_check == "error":
          print("              operation declined\n-------------------------------------------\nerror, account not found, contact tech support to fix the issue")
     elif Cash_check == "empty":
                                   print("              Card declined\n-------------------------------------------\nyour remaining credit is 0 at the moment")
     elif Cash_check == "insufficient":
          print("              Card declined\n-------------------------------------------\n you do not have enough credit")
          while True:
               choice = input("\nWould you like to pay with cash instead?\n1 - Confirm       2 - cancel")
               try:
                    val = int(choice)
                    if val == 1:
                         cash_pay(user_id,amount,item)
                    elif val == 2:
                         break
               except ValueError:
                    print("invalid option, try again")
     elif Cash_check =="success":
          module.credit_history_add(user_id,"Purchase",amount)
          module.user_inventory_add(user_id,item)
          print("operation successful!\nyou paid ",amount," $",sep="")
          print("\n")                                     

def cash_pay(user_id,amount,item):
     Cash_check = module.withdraw(user_id,amount)
     if Cash_check == "error":
          print("              operation declined\n-------------------------------------------\nerror, account not found, contact tech support to fix the issue")
     elif Cash_check == "empty":
          print("              operation declined\n-------------------------------------------\nyour account balance is 0 at the moment")
          while True:
               choice = input("\nWould you like to pay with a credit card instead?\n1 - Confirm       2 - cancel")
               try:
                    val = int(choice)
                    if val == 1:
                         credit_pay(user_id,amount,item)
                         break
                    elif val == 2:
                         break
               except ValueError:
                    print("invalid option, try again")
     elif Cash_check == "insufficient":
          print("              operation declined\n-------------------------------------------\n you do not have the required amount in your account")
          z = module.user_information_unit(user_id)
          if z != False:
               if z["user"]["credit_card"]["id_number"] != "":
                    while True:
                         choice = input("\nWould you like to pay with a credit card instead?\n1 - Confirm       2 - cancel")
                         try:
                              val = int(choice)
                              if val == 1:
                                   credit_pay(user_id,amount,item)
                                   break
                              elif val == 2:
                                   break
                         except ValueError:
                              print("invalid option, try again")
     elif Cash_check =="success":
          module.history_add(user_id,"Purchase",amount)
          module.user_inventory_add(user_id,item)
          print("\n","="*40,"operation successful!\nyou paid ",amount," $","="*40,sep="")
          print("\n")

def exit_loop():
     while True:
          exit_loop = input("\n                0 - EXIT\nEnter : ")
          try:
               val_check = int(exit_loop)
               if val_check == 0:
                    break
               else:
                    print("\n===Invalid option, Try again!===\n")
          except ValueError:
               print("\n===Invalid option, Type 0 if you want to exit!===\n")
#  -------------CREDIT CARD BASED STUFF-------------

#      V user stuff V

def request_credit_card(user_id):
     print("\n\n              Credit Card Request\n","-"*40)
     reason = input("\nwhat is the reason behind the credit card request? \n Write : ")
     print("\nbased off of your yearly income, you can apply for a card with one of the following credit limits : \n")
     checker = module.check_yearly_income(user_id)
     if checker == 1:
          print("1 - 5000 $")
     elif checker == 2:
          print("1 - 5000 $\n2 - 10000 $")
     elif checker == 3:
          print("1 - 5000 $\n2 - 10000 $\n3 - 50000 $")
     elif checker == 4:
          print("1 - 5000 $\n2 - 10000 $\n3 - 50000 $\n4 - 100000 $")
     while True:
          choice_pick = input("\nchoice : ")
          if choice_pick == "1":
               z = module.user_credit_apply_check(user_id,reason,5000)
               if z == "success":
                    print("\nRequest sent successfully!")
                    break
               elif z == "pending":
                    print("\nyour previous request is still pending approval, please wait patiently while our admins work on it!")
                    break
               elif z == True:
                    print("\nCongratulations! your request was approved by our admins!\nYou can apply for another card now.")
                    module.credit_card_request_delete(user_id)
                    break
               elif z == False:
                    print("\nyour request was rejected by our admins.\nYou can apply again if you'd like.")
                    module.credit_card_request_delete(user_id)
                    break
          elif choice_pick == "2":
               z = module.user_credit_apply_check(user_id,reason,10000)
               if z == "success":
                    print("\nRequest sent successfully!")
                    break
               elif z == "pending":
                    print("\nyour previous request is still pending approval, please wait patiently while our admins work on it!")
                    break
               elif z == True:
                    print("\nCongratulations! your request was approved by our admins!\nYou can apply for another card now.")
                    module.credit_card_request_delete(user_id)
                    break
               elif z == False:
                    print("\nyour request was rejected by our admins.\nYou can apply again if you'd like.")
                    module.credit_card_request_delete(user_id)
                    break
          elif choice_pick == "3":
               z = module.user_credit_apply_check(user_id,reason,50000)
               if z == "success":
                    print("\nRequest sent successfully!")
                    break
               elif z == "pending":
                    print("\nyour previous request is still pending approval, please wait patiently while our admins work on it!")
                    break
               elif z == True:
                    print("\nCongratulations! your request was approved by our admins!\nYou can apply for another card now.")
                    module.credit_card_request_delete(user_id)
                    break
               elif z == False:
                    print("\nyour request was rejected by our admins.\nYou can apply again if you'd like.")
                    module.credit_card_request_delete(user_id)
                    break
          elif choice_pick == "4":
               z = module.user_credit_apply_check(user_id,reason,100000)
               if z == "success":
                    print("\nRequest sent successfully!")
                    break
               elif z == "pending":
                    print("\nyour previous request is still pending approval, please wait patiently while our admins work on it!")
                    break
               elif z == True:
                    print("\nCongratulations! your request was approved by our admins!\nYou can apply for another card now.")
                    module.credit_card_request_delete(user_id)
                    break
               elif z == False:
                    print("\nyour request was rejected by our admins.\nYou can apply again if you'd like.")
                    module.credit_card_request_delete(user_id)
                    break
          else:
               print("invalid choice, try again.")

def user_credit_card_ui(user_id):
     while True:
          print("\n\n               Credit Card\n","-"*40)
          options = input("\n      1 - display credit card info \n      2 - check credit card history \n      3 - apply for a credit card\n      0 - EXIT\nEnter : ")
          if options == "1":
               module.user_display_credit_card(user_id)
          elif options == "2":
               module.credit_history_read(user_id)
               exit_loop()
          elif options == "3":
               request_credit_card(user_id)
          elif options == "0":
               break
          else:
               print("Invalid options, try again.")


#      V admin stuff V

def admin_add_credit_card_user():
     print("\n            credit card request\n","-"*40)
     user_idd = input("\nplease enter the Account's ID : ")
     checker = module.admin_credit_pend_check(user_idd)
     if checker == "not found":
          print("\nInvalid ID / No request found!\nPlease make sure you entered the right ID!\n")
     else:
          print("\n\n                Request sheet\n","-"*40)
          for id,value in checker["info"].items():
               print("   ",end="")
               print(id,value,sep=" : ")
          print("   reason for request : ",checker["reason"],"\n   requested credit limit : ",checker["limit"],"\n   request status : ",checker["status"],sep="")
          while True:
               approval = input("\n      1 - Reject       2 - approve\n                 0 - EXIT\nEnter : ")
               if approval == "1" or "2":
                    module.admin_aprove_pend_credit(user_idd,approval)
                    break
               elif approval == "0":
                    break
               else:
                    print("Invalid option, try again")

def admin_credit_card_ui():
     print("\n\n          credit card platform\n","-"*40,sep="")
     while True:
          choice = input("\n      choose one of the programs : \n\n1 - display all current credit cards \n2 - display an accounts credit card info \n3 - display all requests \n4 - review a request \n\n         0 - EXIT \nEnter : ")
          try:
               val = int(choice)
          except ValueError:
               print("Invalid choice, try again")
          if val == 1:
               module.user_DB_credit_card_display()
               exit_loop()
          elif val == 2:
               id_input = input("\nPlease enter the Account's ID : ")
               module.admin_display_all_credit_cards(id_input)
               exit_loop()
          elif val ==3:
               module.user_credit_request_display()
               exit_loop()
          elif val == 4:
               admin_add_credit_card_user()
               exit_loop()
          elif val == 0:
               break


module = BANK()
while True:
     print("\n\n                 BANK\n","="*40,sep="")
     main_function = (input("please choose the program you want to use! \n\n       1 - Admin platform \n       2 - User platform \n       3 - Application platform \n\n           0 - EXIT \nEnter : "))
     if main_function == "1":
          while True:
               print("\n\n                Admin platform\n","="*50,sep="")
               print("\n        Welcome to the Admin's platform!")
               admin_function = input("\n            please select an option : \n\n            1 - review applications\n            2 - User Profiles \n\n                 0 - EXIT \nEnter : ")
               if admin_function == "1":
                    admin_application_checker()
               elif admin_function == "2":
                    admin_user_ui()
               elif admin_function == "0":
                    break
               else: 
                    print("\ninvalid option, please try again") 
     elif main_function == "2":
          while True:
               print("\n\n         User platform\n--------------------------------------")
               print("   Welcome to the User platform!")
               user_func = input("\nplease select an option : \n\n 1 - Log in \n 2 - Contact support \n\n 0 - EXIT \n            Enter : ")
               if user_func == "1":
                    user_log_in()
               elif user_func == "2":
                    print("\n\n               contact support\n----------------------------------------------------")
                    user_id = input("\nplease enter your Accounts ID : ")
                    check = module.user_db_check(user_id)
                    if check:
                         admin_support__user__(user_id)
                    elif not check:
                         print("\naccount not found, please try again")
               elif user_func == "0":
                    break
               else:
                    print("\nInvalid option, try again.")
     elif main_function == "3":
          while True:
               print("\n\n         Appliction platform\n------------------------------------------")
               print("   Welcome to the application platform!")
               apply_function = input("\nplease select an option : \n\n 1 - apply for a new account \n 2 - check an existing submission \n\n          0 - EXIT \nEnter : ")
               if apply_function == "0":
                    break
               elif apply_function == "1":
                    application_function()
               elif apply_function == "2":
                    application_checker_function()
               else: 
                    print("\ninvalid option, please try again") 
     elif main_function =="4":
          module.admin_admin_read()
     elif main_function == "0":
          print("\n\n","="*40,"\n","+"*40,"\n      Bank simulation mini project\n              Ali Essam","\n","+"*40,"\n","="*40,"\n\n",sep="")
          break
     else: 
          print("\ninvalid option, please try again") 
# Time spent on the project : 29 hours and 12 minutes