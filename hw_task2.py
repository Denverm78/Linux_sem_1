# Доработать функцию из предыдущего задания таким образом, чтобы у нее появился дополнительный режим работы, 
# в котором вывод разбивается на слова с удалением всех знаков пунктуации 
# (их можно взять из списка string.punctuation модуля string).
# В этом режиме должно проверяться наличие слова в выводе.

import subprocess
import string

def user_menu():
    num_mode = int(input('Введите режим работы:\n 1 - без удаления знаков препинания\n 2 - с удалением: '))
    return num_mode

def check_text(command, text, mode):
    result = subprocess.run(args=command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    result_out = result.stdout
    # print(type(result_out))
    if mode == 2:
        for i in string.punctuation:
            if i in result_out:
                result_out = result_out.replace(i, '')
    print(result_out)
    if text in result_out:
        return True
    else:
        return False


if __name__ == '__main__':
    mode = user_menu()
    result_check1 = check_text('cat /etc/os-release','22.04.1', mode)
    result_check2 = check_text('ls','task4.py', mode)
    result_check3 = check_text('cat /etc/os-release', 'httpswwwubuntucom', mode)
    print(result_check1, result_check2, result_check3)