def bonus_decorator(func):
    def wrapper(name):
        if counter % 5 == 0:
            result = func(name)
            return result + ' Вы получаете бесплатную плюшку!'
        else:
            return func(name)
    return wrapper


@bonus_decorator
def greeting(name):
    return f"Привет, {name}!"


counter = 0

with open('.\\files\\client.txt', 'r', encoding='utf-8') as clients_file:
    clients = [client.strip('\n') for client in clients_file.readlines()]

for client in clients:
    counter += 1
    print(greeting(client))

client = input()

while client != 'Плюшки кончились':
    counter += 1
    print(greeting(client))
    client = input()
