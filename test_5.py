from question import *
#первая
def check_question(question):
    last_letter = question.find("#")
    cut_question = question[0:last_letter] #хранится вопрос
    right_answer = question[last_letter + 1] #срез, сам ответ

    
    answer = input(cut_question)

    if answer == right_answer:
        return 1
    else:
        return 0
    
def estimation(point):
    if point < 2:
        return "На данный момент мы не готовы рассмотреть Вас как потенциального кандидата на должность."
    elif point > 4:
        return "Вы прошли тестирование! Ждём Вас на следующем этапе собеседования!"
    else:
        return "Пройдите дополнительную подготовку и возвращайтесь снова!"
