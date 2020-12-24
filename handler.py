import sqlite3
from config import settings
conn = sqlite3.connect(r"answer_user.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
try:
    create_TABLE='''number_answer ,id_user, full_name, right_answer '''
    for numbers in range(1,settings['number_of_questions']+1):
        create_TABLE=create_TABLE+f''',answer_{numbers} '''
    cursor.execute(f'''CREATE TABLE answer({create_TABLE})''')

except:
    pass

class sql_test:
    @staticmethod
    def chek_user_questions(id_user):
        sql=f"SELECT number_answer FROM answer WHERE id_user = {id_user}"
        number_answer = cursor.execute(sql).fetchone()
        if number_answer==None:
            return("Юзера нет")
        elif int(number_answer[0])<settings['number_of_questions']:
            return("Юзер не ответил на все вопросы")
        elif int(number_answer[0])==settings['number_of_questions']: 
            return("Юзер уже ответил")
    @staticmethod
    def chek_number_question(id_user):
        sql=f"SELECT number_answer FROM answer WHERE id_user = {id_user}"
        number = cursor.execute(sql).fetchone()[0]
        return number
    @staticmethod
    def update_answer(id_user,answer,number):
        if answer==settings[f'right_answer_question{number+1}']:
            sql=f"SELECT right_answer FROM answer WHERE id_user = {id_user}"
            right_answer = cursor.execute(sql).fetchone()[0]
            sql=f'UPDATE answer SET right_answer = ? WHERE id_user = ?'
            cursor.execute(sql, (right_answer+1, id_user))
        sql=f'UPDATE answer SET answer_{number+1} = ? WHERE id_user = ?'
        cursor.execute(sql, (answer, id_user))
        sql=f'UPDATE answer SET number_answer = ? WHERE id_user = ?'
        cursor.execute(sql, (number+1, id_user))
        conn.commit() 
    @staticmethod
    def app_new(id_user, full_name):
        create_TABLE=f"'0' ,{id_user}, '{full_name}',0 "
        for i in range(1,settings['number_of_questions']+1):
            create_TABLE=create_TABLE+f",' ' "
        sql=f"INSERT INTO answer VALUES ({create_TABLE})"
        cursor.execute(sql)
        conn.commit() 
    @staticmethod
    def right_answer(id_user):
        sql=f"SELECT right_answer FROM answer WHERE id_user = {id_user}"
        return(cursor.execute(sql).fetchone()[0])
    @staticmethod
    def top_user(top):
        top_user=[]
        sql=f'''SELECT id_user,right_answer FROM answer AS a ORDER BY right_answer DESC LIMIT {top}'''
        for id in cursor.execute(sql):
            top_user.append([id[0],id[1]])
        return(top_user)
