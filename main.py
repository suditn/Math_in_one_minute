import time
import random


def get_divisor(n):
    '''
    :param n: The number
    :return: a divisor of n
    '''

    l = []
    for i in range(1, n+1):
        if n % i == 0:
            l.append(i)
    return random.choice(l)


if __name__ == '__main__':
    ops = ['+', '-', '*', '/']
    start_time = time.time()
    total = 0
    correct = 0
    questions = []
    #while seconds is less than 60
    while time.time() - start_time <= 60:
        a = random.randint(1,99)
        op = random.choice(ops)
        if op == '/':
            #Деление на 0
            b = get_divisor(a)
        else:
            b = random.randint(1,99)

        #Правельный ответ
        a_op_b = '{}{}{}'.format(a, op, b)
        c = int(eval(a_op_b))

        #Ввод ответа

        try:
            ans = int(input('{} = '.format(a_op_b)))
        except:
            ans = ''

        #Проверка ответа
        if time.time() - start_time <=60:
            if c == ans:
                print('Всё верно! времени осталось {} секунд'.format(int(60 - (time.time() - start_time))))
                correct += 1
            else:
                print('Не верно! времени осталось {} секунд'.format(int(60 - (time.time() - start_time))))
            total = total + 1
            questions.append('{} = {}'.format(a_op_b, ans))

    print ('Из {} вопросов твой процент правельных ответов это: {:.2f}%'.format(total, correct / total * 100))
    for q in questions:
        print(q)