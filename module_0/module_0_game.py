#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np

print ('Загружается программа Загадка...\n...\n...\n...\n')


# функция теста
def test_core_v1 ():
    count_ls=[]
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core_v3(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток\n")
    mode_select()

    
# функция игры
def game_core_v3 (number):
    predict_number=50
    predict_range=[1, 101]
    count=1
    number = int(number)
    # цикл сравнения заданного числа с предполагаем
    while number != predict_number:
        if number > predict_number:
            count += 1
            predict_range[0] = predict_number
            print (f'Загаданное число больше {predict_number}')
            predict_number = int(np.mean(predict_range))            
        elif number < predict_number:
            count += 1
            predict_range[1] = predict_number
            print (f'Загаданное число меньше {predict_number}')
            predict_number = int(np.mean(predict_range))        
    print(f'- Я угадал число {number} с {count} раз!\nНеплохо!')
    return count


# функция ввода рандомного числа
def random_number():
    rund_number = np.random.randint(1,101)
    game_core_v3 (rund_number)

    
# функция ввода пользовательского числа
def user_number():    
    #цикл проверки формата ввода
    while True:
        us_number = input ('Загадай мне число от 1 до 100\n')
        if not us_number.isnumeric():
            print ('- Ответь нормально!\n')
        elif not 1 <= int(us_number) <= 100:
            print ('- Ответь нормально!\n')
        else:
            print('Хорошо, давай попробуем.')
            game_core_v3 (us_number)

            
# функция диалога 
def start_game():         
    #цикл проверки формата ввода
    while True:
        answer = str(input ('1 - согласиться, 2 - отказаться \n')) 
        if not answer.isnumeric():
            print ('- Что ты там бормочешь?\n')
        elif not 1 <= int(answer) <= 2:
            print ('- Что ты там бормочешь?\n')
        elif answer == '1':
            print ('- Я в тебе не сомневался!')
            user_number()
        elif answer == '2':
            print ('- Ты мне и не нужен! Я могу сыграть один.')
            random_number()

            
def mode_select():
    print ('Выберите режим загрузки.\n')
    load_mode = str(input ('test\game\n'))
    #цикл проверки формата ввода
    while load_mode != 'test' and load_mode != 'game':
        print ('Ошибка ввода')
        load_mode = str(input ('test\game\n'))
    else:
        if load_mode == 'test':
            print ('Запускается тестовый режим. Количество проверок - 1000 раз')
            test_core_v1 ()
        elif load_mode == 'game':
            print ('Вы входите во дворец Альт-Интеджер и встречаете чародея Рандома.')
                
    print ('- Здравствуй, странник. Я хочу сыграть с тобой в одну игру.')
    start_game()

    
mode_select()


# In[ ]:





# In[ ]:




