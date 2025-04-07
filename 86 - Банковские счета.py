import sys

clients = {}

for line in sys.stdin:
    line = line.split()
    command = line[0]
    if command == 'DEPOSIT':
        client = line[1]
        amount = int(line[2])
        if client not in clients:
            clients[client] = amount
        else:
            clients[client] += amount
    
    if command == 'TRANSFER':
        client_sender = line[1]
        client_reciever = line[2]
        amount = int(line[3])
        if client_sender not in clients:
            clients[client_sender] = -amount
        else:
            clients[client_sender] -= amount

        if client_reciever not in clients:
            clients[client_reciever] = amount
        else:
            clients[client_reciever] += amount

    if command == 'WITHDRAW':
        client = line[1]
        amount = int(line[2])
        if client not in clients:
            clients[client] = -amount
        else:
            clients[client] -= amount
    if command == 'INCOME':
        amount = int(line[1])
        for key in clients.keys():
            clients[key] = int(clients[key] * (1 + 5 / 100)) if clients[key] > 0 else clients[key]
    
    if command == 'BALANCE':
        client = line[1]
        if client in clients:
            print(clients[client])
        else:
            print('ERROR')
