import core
core.init()
log = False
while True:
    if log:
        print(f'=========================\nЗапустить калькулятор - 1\nСменить аккаунт - 2\nВыйти из программы - exit\n=========================')
        while True:
            do = input('>>> ')
            if do == '1':
                print('---------------------------\nВведите пример\nВыйти - back\n---------------------------')
                while True:
                    calc = input('>>> ')
                    if calc == 'back':
                        print(f'=========================\nЗапустить калькулятор - 1\nСменить аккаунт - 2\nВыйти из программы - exit\n=========================')
                        break
                    else:
                        try:
                            print(f'Ответ - {eval(calc)}\n=========================\nСледующий пример\nВыйти - back\n---------------------------')
                        except NameError:
                            print('Это не пример ((╬◣﹏◢))')
                        except SyntaxError:
                            print('Это не пример ((╬◣﹏◢))')
            elif do == '2':
                log = False
                break
            elif do == 'exit':
                print('Бай Бай')
                core.c.close()
                exit()
    elif log == False:
        print(f'=========================\nВойти       - 1\nРегистрация - 2\nВыйти    - exit\n=========================')
        do = input('>>> ')
        if do == '1':
            log = core.login()
        if do == '2':
            core.registration()
    if do == 'exit':
        print('Бай Бай')
        core.c.close()
        exit()