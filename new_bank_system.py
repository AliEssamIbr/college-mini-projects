import sqlite3 as sq
from datetime import datetime as dt
class BANK():
    def __init__(self):
        self.__module = sq.connect("Bank_system.db")
        self.__cursor = self.__module.cursor()

        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS client_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        D_O_B TEXT NOT NULL,
        gender TEXT NOT NULL,
        nationality TEXT NOT NULL,
        job TEXT NOT NULL,
        yearly_income FLOAT NOT NULL)""")

        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS application_forum(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id TEXT,
        status TEXT NOT NULL,
        temp_pass TEXT,
        client_center_id TEXT,
        FOREIGN KEY (client_id) REFERENCES client_info(id))""")

        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS client_center(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        personal_client_id TEXT,
        client_info TEXT,
        password TEXT NOT NULL,
        lock BOOLEAN,
        pass_attempts INTEGER,
        balance FLOAT NOT NULL,
        debit_card_id TEXT,
        debit_card_balance FLOAT,
        debit_card_lock BOOLEAN,                      
        credit_card_id TEXT,
        cred_bal_limit FLOAT,
        remaining_cred_balance FLOAT,
        credit_card_lock BOOLEAN,
        FOREIGN KEY (client_info) REFERENCES client_info(id))""")


        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS user_balance_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        personal_client_id TEXT,
        process TEXT NOT NULL,
        amount FLOAT NOT NULL,
        time TEXT NOT NULL,
        FOREIGN KEY (personal_client_id) REFERENCES client_center(id)
        )""")

        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS user_credit_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        personal_client_id TEXT,
        card_id TEXT,
        process TEXT NOT NULL,
        amount FLOAT NOT NULL,
        time TEXT NOT NULL,
        FOREIGN KEY (personal_client_id) REFERENCES client_center(id))""")

        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS user_debit_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        personal_client_id TEXT,
        card_id TEXT,
        process TEXT NOT NULL,
        amount FLOAT NOT NULL,
        time TEXT NOT NULL,
        FOREIGN KEY (personal_client_id) REFERENCES client_center(id))""")

        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS client_messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        personal_client_id TEXT NOT NULL,
        reason TEXT NOT NULL,
        message TEXT,
        time TEXT NOT NULL,
        FOREIGN KEY (personal_client_id) REFERENCES client_center(id)
        )""")

        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS cards_application_forum(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_info_id TEXT,
        client_center_id TEXT,
        credit_reason TEXT,
        credit_limit FLOAT,
        credit_status BOOLEAN,
        debit_reason TEXT,
        debit_status BOOLEAN,
        FOREIGN KEY (client_info_id) REFERENCES client_info(id),
        FOREIGN KEY (client_center_id) REFERENCES client_center(personal_client_id))""")

        #"inventory table is not neccecary, it's only here to demonstrate the purchase functionality"

        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS user_inventory(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id TEXT,
        item TEXT NOT NULL,
        FOREIGN KEY (client_id) REFERENCES client_center(id))""")
        self.__module.commit()
    
    
    def close_connection(self):
        self.__module.close()
    
    def get_client_info_id(self,name):
        self.__cursor.execute("SELECT id FROM client_info WHERE name = ?",(name,))
        rows = self.__cursor.fetchall()
        if rows:
            return rows[0][0]
        else:
            return False


    def add_application(self,Name,DOB,Gender,Natio,Job,YrIncome):
        if Name == "" or DOB== "" or Gender== "" or Natio == "" or Job == "" or YrIncome == "":
            return False
        else:
            try:
                Yearly = float(YrIncome)
            except ValueError:
                return "INCORRECT YRINCOME"
            self.__cursor.execute("INSERT INTO client_info (name,D_O_B,gender,nationality,job,yearly_income) VALUES (?,?,?,?,?,?)",(Name,DOB,Gender,Natio,Job,Yearly,))
            self.__module.commit()
            client_id = self.get_client_info_id(Name)
            self.__cursor.execute("INSERT INTO application_forum (client_id,status) VALUES (?,?)",(client_id,"PENDING",))
            self.__module.commit()
            return True
    def review_applications(self):
        self.__cursor.execute("SELECT * FROM application_forum")
        rows = self.__cursor.fetchall()
        return rows
    def review_client_info(self):
        self.__cursor.execute("SELECT * FROM client_info")
        rows = self.__cursor.fetchall()
        return rows
    def check_if_application_exists(self,id):
        self.__cursor.execute("SELECT * FROM application_forum WHERE id = ?",(id,))
        s = self.__cursor.fetchall()
        return s
    def Review_Single_Application_status(self,id):
        self.__cursor.execute("SELECT status FROM application_forum WHERE id = ?",(id,))
        s = self.__cursor.fetchall()
        return s[0][0]
    def temp_pass_get(self,id):
        self.__cursor.execute("SELECT temp_pass FROM application_forum WHERE id = ?",(id,))
        s = self.__cursor.fetchall()
        return s[0][0]
    def temp_pass_set(self,id,password):
        self.__cursor.execute("UPDATE application_forum SET temp_pass = ? WHERE id = ?",(password,id,))
        self.__module.commit()
    def application_decision(self,id,decision):
        self.__cursor.execute("UPDATE application_forum SET status = ? WHERE id = ?",(decision,id,))
        self.__module.commit()
        if decision == "APPROVED":
            return True
        if decision == "REJECTED":
            return False
    def application_personal_id_set(self,id,personal_id):
        self.__cursor.execute("UPDATE application_forum SET client_center_id = ? WHERE id = ?",(personal_id,id,))
        self.__module.commit()
    def application_personal_id_get(self,id):
        self.__cursor.execute("SELECT client_center_id FROM application_forum WHERE id = ?",(id,))
        s = self.__cursor.fetchall()
        return s[0][0]
    def application_record_delete(self,id):
        self.__cursor.execute("DELETE FROM application_forum WHERE id = ?",(id,))
        self.__module.commit()
    def application_record_delete_personal_id(self,id):
        self.__cursor.execute("DELETE FROM application_forum WHERE client_center_id = ?",(id,))
        self.__module.commit()
    def personal_id_check(self,id):
        self.__cursor.execute("SELECT id FROM client_center WHERE personal_client_id = ?",(id,))
        s = self.__cursor.fetchall()
        if s == []:
            return s
        else:
            return s[0][0]
    def database_id_check(self,id):
        self.__cursor.execute("SELECT id FROM client_center WHERE id = ?",(id,))
        s = self.__cursor.fetchall()
        if s == []:
            return s
        else:
            return s[0][0]
    def add_client_acc(self,personal_client_id,client_info_id,password,):
        self.__cursor.execute("INSERT INTO client_center (personal_client_id,client_info,password,lock,pass_attempts,balance,debit_card_id,debit_card_balance,debit_card_lock,credit_card_id,cred_bal_limit,remaining_cred_balance,credit_card_lock) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",(personal_client_id,client_info_id,password,False,3,0,None,0.0,False,None,0.0,0.0,False))
        self.__module.commit()
    def review_clients(self):
        self.__cursor.execute("SELECT * FROM client_center")
        rows = self.__cursor.fetchall()
        return rows
    def get_client_name(self,id):
        self.__cursor.execute("SELECT name FROM client_info WHERE id = ?",(id,))
        rows = self.__cursor.fetchall()
        return rows[0][0]
    def client_acc_lock(self,id):
        self.__cursor.execute("UPDATE client_center SET lock = ? WHERE id = ?",(True,id,))
        self.__cursor.execute("UPDATE client_center SET pass_attempts = ? WHERE id = ?",(0,id,))
        self.__module.commit()
    def client_acc_unlock(self,id):
        self.__cursor.execute("UPDATE client_center SET lock = ? WHERE id = ?",(False,id,))
        self.__cursor.execute("UPDATE client_center SET pass_attempts = ? WHERE id = ?",(3,id,))
        self.__module.commit()
    def client_center_singular_databaseID(self,id):
        self.__cursor.execute("SELECT * FROM client_center WHERE id = ?",(id,))
        s = self.__cursor.fetchall()
        return s
    def client_center_singular_personalID(self,id):
        self.__cursor.execute("SELECT * FROM client_center WHERE personal_client_id = ?",(id,))
        s = self.__cursor.fetchall()
        return s
    def client_info_singular(self,id):
        self.__cursor.execute("SELECT * FROM client_info WHERE id = ?",(id,))
        rows = self.__cursor.fetchall()
        return rows
    def delete_client_acc(self,id):
        self.__cursor.execute("DELETE FROM client_center WHERE id = ?",(id,))
        self.__module.commit()
    def client_password_check(self,id,password):
        self.__cursor.execute("SELECT password FROM client_center WHERE personal_client_id = ?",(id,))
        rows = self.__cursor.fetchall()
        if rows[0][0] == password:
            return f"valid"
        else:
            return f"invalid"
    def client_get_remaining_login_attempts(self,id):
        self.__cursor.execute("SELECT pass_attempts FROM client_center WHERE personal_client_id = ?",(id,))
        rows = self.__cursor.fetchall()
        return rows[0][0]
    def client_login_attempts_set(self,id,attempts):
        self.__cursor.execute("UPDATE client_center SET pass_attempts = ? WHERE personal_client_id = ?",(attempts,id,))
        self.__module.commit()
    def client_add_support_message(self,id,reason,message,time):
        self.__cursor.execute("INSERT INTO client_messages (personal_client_id,reason,message,time) VALUES (?,?,?,?)",(id,reason,message,time,))
        self.__module.commit()
    def admin_read_support_messages(self):
        self.__cursor.execute("SELECT * FROM client_messages")
        rows = self.__cursor.fetchall()
        return rows
    def admin_read_specefic_support_messages(self,personal_id):
        self.__cursor.execute("SELECT * FROM client_messages WHERE personal_client_id = ?",(personal_id,))
        rows = self.__cursor.fetchall()
        return rows
    def delete_support_ticket(self,id):
        self.__cursor.execute("DELETE FROM client_messages WHERE id = ?",(id,))
        self.__module.commit()
    def client_acc_login_lock(self,id):
        self.__cursor.execute("UPDATE client_center SET lock = ? WHERE personal_client_id = ?",(True,id,))
        self.__module.commit()
    def client_set_balance(self,amount,id):
        self.__cursor.execute("UPDATE client_center SET balance = ? WHERE id = ?",(amount,id,))
        self.__module.commit()
    def client_get_balance(self,id):
        self.__cursor.execute("SELECT balance FROM client_center WHERE id = ?",(id,))
        amount = self.__cursor.fetchall()
        return(amount[0][0])
    def client_add_balance_history(self,personal_client_id,process,amount,time):
        self.__cursor.execute("INSERT INTO user_balance_history (personal_client_id,process,amount,time) VALUES (?,?,?,?)",(personal_client_id,process,amount,time,))
        self.__module.commit()
    def client_read_personal_balance_history(self,id):
        self.__cursor.execute("SELECT * FROM user_balance_history WHERE personal_client_id = ?",(id,))
        rows = self.__cursor.fetchall()
        return rows
    def client_password_change(self,id,new_password):
        self.__cursor.execute("UPDATE client_center SET password = ? WHERE personal_client_id = ?",(new_password,id,))
        self.__module.commit()
    def client_apply_credit(self,info_id,center_id,reason,limit):
        self.__cursor.execute("SELECT * FROM cards_application_forum WHERE client_center_id = ?",(center_id,))
        s = self.__cursor.fetchall()
        if s != []:
            self.__cursor.execute("UPDATE cards_application_forum SET credit_reason =? ,credit_limit = ? ,credit_status = ? WHERE client_center_id = ?",(reason,limit,None,center_id,))
            self.__module.commit()
        else:
            self.__cursor.execute("INSERT INTO cards_application_forum (client_info_id,client_center_id,credit_reason,credit_limit,credit_status) VALUES (?,?,?,?,?)",(info_id,center_id,reason,limit,None,))
            self.__module.commit()

    def client_apply_debit(self,info_id,center_id,reason):
        self.__cursor.execute("SELECT * FROM cards_application_forum WHERE client_center_id = ?",(center_id,))
        s = self.__cursor.fetchall()
        if s != []:
            self.__cursor.execute("UPDATE cards_application_forum SET debit_reason = ?,debit_status = ? WHERE client_center_id = ?",(reason,None,center_id,))
            self.__module.commit()
        else:
            self.__cursor.execute("INSERT INTO cards_application_forum (client_info_id,client_center_id,debit_reason,debit_status) VALUES (?,?,?,?)",(info_id,center_id,reason,None,))
            self.__module.commit()

    def cards_application_forum_read(self):
        self.__cursor.execute("SELECT * FROM cards_application_forum")
        s = self.__cursor.fetchall()
        return s
    
    def credit_request_review_admin(self,id,decision,card_id):
        if decision == True:
            self.__cursor.execute("UPDATE cards_application_forum SET credit_status = ? WHERE id = ?",(True,id,))
            self.__cursor.execute("SELECT credit_limit FROM cards_application_forum WHERE id = ?",(id,))
            cred_limit = self.__cursor.fetchall()
            self.__cursor.execute("SELECT client_center_id FROM cards_application_forum WHERE id = ?",(id,))
            personal_id = self.__cursor.fetchall()
            limit = cred_limit[0][0]
            P_id = personal_id[0][0]
            self.__cursor.execute("UPDATE client_center SET credit_card_id = ?, cred_bal_limit = ?,remaining_cred_balance = ?,credit_card_lock = ? WHERE personal_client_id = ?",(card_id,limit,limit,False,P_id,))
            self.__module.commit()
            return "A"
        if decision == False:
            self.__cursor.execute("UPDATE cards_application_forum SET credit_status = ? WHERE id = ?",(False,id,))
            self.__module.commit()

    def debit_request_review_admin(self,id,decision,card_id=0):
        if decision == True:
            self.__cursor.execute("UPDATE cards_application_forum SET debit_status = ? WHERE id = ?",(True,id,))
            self.__cursor.execute("SELECT client_center_id FROM cards_application_forum WHERE id = ?",(id,))
            personal_id = self.__cursor.fetchall()
            self.__cursor.execute("UPDATE client_center SET debit_card_id = ?, debit_card_balance = ?,debit_card_lock = ? WHERE personal_client_id = ?",(card_id,0,False,personal_id[0][0],))
            self.__module.commit()
        if decision == False:
            self.__cursor.execute("UPDATE cards_application_forum SET debit_status = ? WHERE id = ?",(False,id,))
            self.__module.commit()
    def credit_id_check(self,id):
        self.__cursor.execute("SELECT * FROM client_center WHERE credit_card_id = ?",(id,))
        s = self.__cursor.fetchall()
        if s == []:
            return False
        else:
            return True   
    def debit_id_check(self,id):
        self.__cursor.execute("SELECT * FROM client_center WHERE debit_card_id = ?",(id,))
        s = self.__cursor.fetchall()
        if s == []:
            return False
        else:
            return True     
    def debit_balance_set(self,amount,id):
        self.__cursor.execute("UPDATE client_center SET debit_card_balance = ? WHERE debit_card_id = ?",(amount,id,))
        self.__module.commit()
    def debit_balance_get(self,id):
        self.__cursor.execute("SELECT debit_card_balance FROM client_center WHERE debit_card_id = ?",(id,))
        s = self.__cursor.fetchall()
        return s
    def credit_balance_set(self,amount,id):
        self.__cursor.execute("UPDATE client_center SET remaining_cred_balance = ? WHERE credit_card_id = ?",(amount,id,))
        self.__module.commit()
    def credit_balance_get(self,id):
        self.__cursor.execute("SELECT remaining_cred_balance FROM client_center WHERE credit_card_id = ?",(id,))
        s = self.__cursor.fetchall()
        return s
    def client_add_debit_history(self,personal_client_id,card_id,process,amount,time):
        self.__cursor.execute("INSERT INTO user_debit_history (personal_client_id,card_id,process,amount,time) VALUES (?,?,?,?,?)",(personal_client_id,card_id,process,amount,time,))
        self.__module.commit()
    def client_add_credit_history(self,personal_client_id,card_id,process,amount,time):
        self.__cursor.execute("INSERT INTO user_credit_history (personal_client_id,card_id,process,amount,time) VALUES (?,?,?,?,?)",(personal_client_id,card_id,process,amount,time,))
        self.__module.commit()































































#TIME SPENT ON THIS PROJECT : 3 HOURS

#started at 5~ 2026-5-16
#Stopped at 8~ 2026-5-16

#started at 5 2026-5-18
#Paused at 7:10 2026-5-18
#Unpaused at 7:20
#stopped at 11:20

#started at 7:10 PM 2026-5-19
#paused at 8:20 PM 
#unpaused at 10 PM
#stopped at 11 PM (FUCK THE "ADD CLIENT" STUFF, FUCK ALL OF IT!)

#started at 7:22 PM 2026-5-20
#paused at 8:07 PM
#UNPAUSED AT 8:30 PM
#stopped at 10:45 PM 2026-5-20 (ok ok, makin some progress but its still fuckin annoying, 750 lines tho sooo.. y e a h..)

#4 to 6:45 2026-5-27 (EID)
#from 9 to 11:16


#11:55 AM 2026-5-29
#paused at 1:45
#unpaused at 4
#paused at 6:20
#unpaused at 10:50 PM
#stopped at 12 AM

#3:20 PM 2026-5-30
#paused at 5 PM
#unpaused at 9:30 PM
#finished at 12:30 AM

#started at 8:10 2026-5-31