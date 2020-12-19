import sqlite3
conn = sqlite3.connect(r"C:\Users\79190\programmers\discord\3 опросник(невозможен)\answer_user.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
try:
    cursor.execute('''CREATE TABLE answer(number_answer ,id_user, answer_1, answer_2, answer_3, answer_4, answer_5)''')
except:
    pass
class sql_test:
    #есть ли такой юзер
    @staticmethod
    def chek_user_questions(id_user):
        sql=f"SELECT number_answer FROM answer WHERE id_user = {id_user}"
        number_answer = cursor.execute(sql).fetchone()
        if number_answer==None:
            return("Юзера нет")
        elif int(number_answer[0])<5:
            return("Юзер не ответил на все вопросы")
        elif int(number_answer[0])==5: 
            return("Юзер уже ответил")
    #какой вопрос
    @staticmethod
    def chek_number_question(id_user):
        sql=f"SELECT number_answer FROM answer WHERE id_user = {id_user}"
        number = cursor.execute(sql).fetchone()[0]
        return number
    #замена ответа+некст вопрос
    @staticmethod
    def update_answer(id_user,answer,number):
        #оюбновление вопроса
        sql=f'UPDATE answer SET answer_{number+1} = ? WHERE id_user = ?'
        cursor.execute(sql, (answer, id_user))
        #обновление номера вопроса
        sql=f'UPDATE answer SET number_answer = ? WHERE id_user = ?'
        cursor.execute(sql, (number+1, id_user))
        conn.commit() 
    #отправка всех ответов
    @staticmethod
    def chek_answer(id_user):
        sql = f"select answer_1,answer_2,answer_3,answer_4,answer_5 from answer where id_user == {id_user}"
        return(cursor.execute(sql).fetchone())
    #добавление нового юзера
    @staticmethod
    def app_new(id_user):
        cursor.execute(f"""INSERT INTO answer VALUES ('0' ,{id_user}, '', '','','', '')""")
        conn.commit() 

