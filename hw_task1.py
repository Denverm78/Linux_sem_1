# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в ее выводе
# и False в противном случае. Передаваться должна только одна строка, разбиение вывода
# использовать не нужно

import subprocess

def check_text(command, text):
    result = subprocess.run(args=command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    result_out = result.stdout
    if text in result_out and result.returncode == 0:
        return True
    else:
        return False

if __name__ == '__main__':

    result_check1 = check_text('cat /etc/os-release','22.04.1')
    result_check2 = check_text('ls','task5.py')
    print(result_check1, result_check2)