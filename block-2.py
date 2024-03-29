def run():
    clients = {}
    max_bonus_client = 0
    max_bonus_client_name = ""

    with open('.\\files\\test_1.txt', 'r', encoding='utf-8') as cafe_file:
        for customer in cafe_file.readlines():
            clients[customer.split()[0]] = [int(customer.split()[1]), int(customer.split()[1]) // 6]

    for client in clients:
        print(f'Клиенту {client} полагается {clients[client][1]} бонусных чашек кофе')
        if clients[client][1] > max_bonus_client:
            max_bonus_client = clients[client][1]
            max_bonus_client_name = client

    with open('.\\result.txt', 'w', encoding='utf-8') as res:
        res.write(max_bonus_client_name)


if __name__ == "__main__":
    run()
