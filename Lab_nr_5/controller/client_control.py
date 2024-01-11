from repository.clientrepo import ClientRepo
from modelle.client import Client
from controller.datarepo_control import ShowData
from repository.orderrepo import OrderRepo

clientManager = ClientRepo('clients.dat')
orderManager = OrderRepo('orders.dat')


def showClients():
    print("Client: ")
    ShowData(2)


def addClient():
    name = input("Clients Name: ")
    adress = input("Clients Address: ")

    clients: list = clientManager.load() if clientManager.load() else []
    client = Client(1, name, adress)
    clients.append(client)
    clientManager.sort(clients)

def updateClients():
    showClients()
    idList = int(input("ID that will be updated: "))
    clients: list = clientManager.load()

    id = clients[idList].id
    name = input("New name: ")
    adress = input("New address: ")
    client = Client(id, name, adress)
    clientManager.update(idList, client)


def deleteClient():
    showClients()
    id = int(input("Enter the id you want to delete: "))
    clientManager.remove(id)
    orderManager.remove(id)
