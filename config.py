settings = {
    'token': 'TOKEN',
    'bot': "Теx. Поддержка",
    'id': ID,
    'prefix': '!',
    #questions
    #to add / remove questions you need to do:
    #1)add / remove the required number of questions by the sample:
    #   'question<numbers>':'<question>',
    #   'True_answer_question<numbers>':'<right_answer>',
    #2)update 'number_of_questions'
    'number_of_questions':3,
    'start_msg_question':'Твой вопрос:',
    'question1':'Первый вопрос',
    'right_answer_question1':'1',
    'question2':'Второй вопрос',
    'right_answer_question2':'2',
    'question3':'Третий вопрос',
    'right_answer_question3':'3',
    'end_test':'Спасибо за прохождение опроса!\nЧтобы узнать результат, напиши !result',
    #!result
    'result_no_user':'Чтобы узнать результаты, нужно пройти опрос.\nНачать опрос можно по команде !start',
    'result_no_end_test':'Чтобы узнать результ, нужно пройти тест до конца! ',
    'result_right_answer_start':'Ты ответил правильно на ',
    'result_right_answer_end':' вопроса',
    #!help
    'title_help':'Команды',
    'value_start':'Начать тест',
    'value_result':'Узнать результаты',
    #!start
    'start_no_end_test':'Закончи тест',
    'user_already_answered':'Ты уже ответил',
    #On messages
    'on_msg_no_user':'Чтобы начать опрос, напиши !start\nЧтобы узнать команды, напиши !help',
    'om_msg_user_already_answered':'Ты уже ответил'
}
