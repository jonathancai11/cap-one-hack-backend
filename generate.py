import datetime
import json

def genItems(items, price, quantity):
    aList = list()
    totalCost = 0
    for i in range(len(items)):
        aList.append({
            "item": items[i],
            "cost": price[i],
            "quantity": quantity[i]
        })
        totalCost += price[i]*quantity[i]

    return aList, totalCost

def genTrans(vendor, year, month, day, hour, minute, items, price, quantity):
    aList = dict()
    aList["vendor"] = vendor
    dateTime = datetime.datetime(year, month, day, hour, minute)
    aList["date"] = dateTime.strftime('%m/%d/%Y')
    aList["time"] = dateTime.strftime('%H:%M')
    aList["items"], aList["totalCost"] = genItems(items, price, quantity)
    return aList

aList = list()
aList.append(genTrans('Regal Theatre', 2019, 5, 16, 20, 3,  ['John Wick 3 IMAX '], [21.38], [1]))
aList.append(genTrans('KFC', 2019, 5, 17, 12, 33,  ['Fried Potato', 'Chicken Wings'], [2.99, 6.99], [1, 1]))
aList.append(genTrans('Cafe HotDogs', 2019, 5, 18, 15, 43,  ['Small Hotdog', 'Pepsi'], [2.99, 1.99], [1, 1]))
aList.append(genTrans('Giant Market', 2019, 5, 18, 20, 26,  ['Apple', 'Banana', 'Orange'], [0.45, 0.56, 0.75], [10, 20, 25]))
aList.append(genTrans('Amazon Store', 2019, 5, 19, 12, 37,  ['Kindle Fire'], [29.99], [1]))
aList.append(genTrans('KFC', 2019, 5, 19, 20, 48,  ['Fried Potato'], [2.99], [2]))
aList.append(genTrans('CVS Pharmarcy', 2019, 5, 20, 19, 23,  ['Ear Care', 'Eye Care'], [5.67, 7.82], [1, 1]))
aList.append(genTrans('Mac Donalds', 2019, 5, 21, 12, 0, ['Cheese Burger, Snack Wrap, Pepsi'], [2.0, 3.0 , 1.5], [2, 3, 1]))

with open('history.json', 'w') as fb:
    json.dump(aList, fb, indent= 4)
    

