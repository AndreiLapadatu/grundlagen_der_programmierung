from repository.clientrepo import ClientRepo
from repository.drinkrepo import DrinkRepo
from repository.cookeddishrepo import CookedDishRepo
from repository.orderrepo import OrderRepo


def ShowData(Type):
    types = {
        0: CookedDishRepo('cookeddish.dat'),
        1: DrinkRepo('drink.dat'),
        2: ClientRepo('clients.dat'),
        3: OrderRepo('orders.dat')
    }

    repo = types[Type]

    list = repo.load()
    if list:
        for idx in range(len(list)):
            print(idx, str(list[idx]))

    print('\n')
