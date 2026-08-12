from time import *
from question import *
from test_5 import *

name = input('Введите имя')
start_time = time()
point = check_question(question1)
point = point + check_question(question2)
point = point + check_question(question3) #храним сколько угадали правильных вариантов отв.
point = point + check_question(question4)
point = point + check_question(question5)

end_time = time()
result_time = end_time - start_time
result_time = round(result_time, 2)
result_msg = estimation(point)

print(name)
print(f"Время прохождения теста: {result_time} сек")
print(f"Набрано баллов: {point}")
print(result_msg)
