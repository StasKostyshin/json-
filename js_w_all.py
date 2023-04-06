import json

a = {}
sozdanie = input('Создать новый файл json: Да или Нет').strip().title()
if sozdanie == 'Да':
    a = {'start':'dict'}
    with open('in.json', 'w', encoding='UTF-8') as file:  # открываем файл на запись присвоив имя file
        json.dump(a, file, indent=0, ensure_ascii=False)
elif sozdanie == 'Нет':
    def in_(a):
        while True:
            b = input("Введите ключ")
            if b == 'стоп':
                break
            c = input('Введите значение')
            print(a)
            a.setdefault(b,c)
            print(a)

            with open('in.json', 'w', encoding='UTF-8') as file: # открываем файл на запись присвоив имя file
                json.dump(a, file, indent=0, ensure_ascii=False) # Записываем объект (goods) в (file) как json
            return in_(a)

    with open('in.json', 'r', encoding='UTF-8') as file:
        d = json.load(file)
        a = a | d

    a = in_(a)
