import pdb
def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    for snack in person["favourites"]["snacks"]:
        if snack == food:
            return True
    else:
        return False

def add_friend(person,newfriend):
    person["friends"].append(newfriend)

def remove_friend(person, enemy):
    person["friends"].remove(enemy)

def total_money(people):
    sum = 0
    for person in people:
        sum = sum + person["monies"]
    return sum

def l_money(lender,lendee,amount):
    lender["monies"] - amount
    lendee["monies"] + amount
    return lender["monies"]
    return lendee["monies"]

def all_favourite_foods(people):
    
    all_foods = [] 
    for person in people:
        for food in person["favourites"]["snacks"]:
            all_foods.append(food)
    return all_foods

def find_no_friendends(people):
    losers = []
    for person in people:
        if person["friends"]==[]:
            losers.append(person)
    return losers

    









    

