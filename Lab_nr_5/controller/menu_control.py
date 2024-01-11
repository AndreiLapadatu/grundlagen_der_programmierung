from repository.drinkrepo import DrinkRepo
from repository.cookeddishrepo import CookedDishRepo
from modelle.cookeddish import CookedDish
from modelle.drink import Drink
from controller.datarepo_control import ShowData

cookedDishManager = CookedDishRepo('cookeddish.dat')
drinkManager = DrinkRepo('drink.dat')


def showMenu():
    print("CookedDishes: ")
    ShowData(0)

    print("Drinks: ")
    ShowData(1)


def addCookedDish():
    name = input("Cooked dish: ")
    portionSize = int(input("Size of cooked dish (gram) : "))
    price = int(input("Price (ron) : "))
    prepTime = int(input("Time to cook (min) : "))

    cookedDishes = cookedDishManager.load() if cookedDishManager.load() else []
    cookedDish = CookedDish(name, portionSize, price, prepTime)
    cookedDishes.append(cookedDish)
    cookedDishManager.sort(cookedDishes)


def addDrink():
    name = input("Drink: ")
    portionSize = int(input("Drink size (ml) : "))
    price = int(input("Drink price (ron) : "))
    alcoolVolume = int(input("Alcohol (%) :"))

    drinks = drinkManager.load() if drinkManager.load() else []
    drink = Drink(name, portionSize, price, alcoolVolume)
    drinks.append(drink)
    drinkManager.sort(drinks)


def search():
    name = input("Searched item name: ")
    cookeddishes = cookedDishManager.load() if cookedDishManager else []
    drinks = drinkManager.load() if drinkManager else []
    print('\n')
    if cookeddishes:
        print(" cooked Dishes: ", '\n')
        for idx in range(len(cookeddishes)):
            if name.lower() in cookeddishes[idx].id.lower():
                print(idx, str(cookeddishes[idx]))

    if drinks:
        print("Drinks: ", '\n')
        for idx in range(len(drinks)):
            if name.lower() in drinks[idx].id.lower():
                print(idx, str(drinks[idx]))

        return

    print("no such item found")

def updateItem():
    choose = int(input("""
    Enter the type you want to update:
        1 - cooked Dish
        2 - Drink
    """))
    id = int(input("ID that will be updated: "))
    if choose == 1:
        name = input("New cooked dish: ")
        portionSize = input("New portion size (gram) : ")
        price = input("New dish price (ron) : ")
        prepTime = input("New preparation time (min) : ")
        cookedDish = CookedDish(name,  portionSize, price, prepTime)
        cookedDishManager.update(id, cookedDish)

    else:
        name = input(("New drink: "))
        portionsize = input("New drink size (ml) : ")
        price = input("New price (ron) : ")
        alcoholvolume = input("New alcohol level (%) : ")
        drink = Drink(name, portionsize, price, alcoholvolume)
        drinkManager.update(id, drink)

def showupdatedmenu():
    showMenu()
    updateItem()

def deleteItem():
    choose = int(input("""
    Enter the type you want to update:
        1 - cooked Dish
        2 - Drink
    """))

    id = int(input("ID you want to delete"))

    if choose == 1:
        cookedDishManager.remove(id)
    else:
        drinkManager.remove(id)

def showmenuafterdelete():
    showMenu()
    deleteItem()