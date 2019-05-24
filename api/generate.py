import datetime
import json
def genItems(items, price, quantity):
    aList = list()
    totalCost = 0
    for i in range(len(items)):
        aList.append({
            "item": items[i],
            "cost": str(round(price[i], 2)),
            "quantity": str(quantity[i])
        })
        totalCost += round(price[i]*quantity[i], 2)

    return aList, totalCost

def genTrans(vendor, year, month, day, hour, minute, items, price, quantity):
    aList = dict()
    aList["vendor"] = vendor
    dateTime = datetime.datetime(year, month, day, hour, minute)
    aList["date"] = dateTime.strftime('%m/%d/%Y')
    aList["time"] = dateTime.strftime('%H:%M')
    aList["items"], aList["totalCost"] = genItems(items, price, quantity)
    return aList

def makeData():
    aList = list()
    aList.append(genTrans('Regal Theatre', 2019, 4, 16, 20, 3,  ['John Wick 3 IMAX '], [21.38], [1]))
    aList.append(genTrans('KFC', 2019, 4, 17, 12, 33,  ['Mashed Potatos', 'Chicken Wings'], [2.99, 6.99], [1, 1]))
    aList.append(genTrans('City Dogs', 2019, 4, 18, 15, 43,  ['Chilidog', 'Pepsi'], [4.99, 1.99], [1, 1]))
    aList.append(genTrans('Farm Fresh', 2019, 4, 18, 20, 26,  ['Apples', 'Bananas', 'Oranges'], [0.45, 0.56, 0.75], [10, 20, 25]))
    aList.append(genTrans('Amazon', 2019, 4, 19, 12, 37,  ['Kindle Fire'], [29.99], [1]))
    aList.append(genTrans('Best Buy', 2019, 4, 19, 12, 37,  ['Nintendo Switch'], [249.99], [1]))
    aList.append(genTrans('KFC', 2019, 4, 19, 20, 48,  ['French Fries'], [2.99], [2]))
    aList.append(genTrans('CVS Pharmarcy', 2019, 4, 20, 19, 23,  ['Q-Tips', 'Contact Lens Solution'], [5.67, 7.82], [1, 1]))
    aList.append(genTrans('McDonalds', 2019, 4, 21, 12, 0, ['Double Cheeseburger, Snack Wrap, Pepsi'], [1.99, 3.99 , 1.59], [2, 3, 1]))
    aList.append(genTrans('Richmond Gas Works', 2019, 4, 26, 20, 48,  ['Gas'], [15.15], [1]))
    aList.append(genTrans('Richmond Water', 2019, 4, 28, 18, 34,  ['Water'], [17.84], [1]))
    aList.append(genTrans('Comcast', 2019, 4, 28, 23, 18,  ['Internet'], [19.99], [1]))
    aList.append(genTrans('Farm Fresh', 2019, 4, 29, 20, 26,  ['Bread', 'Chips', 'Salsa'], [3.99, 2.99, 9.99], [2, 5, 1]))
    aList.append(genTrans('Dominion', 2019, 4, 29, 20, 12,  ['Power'], [13.53], [1]))
    aList.append(genTrans('Rent', 2019, 4, 29, 17, 12,  ['Rent'], [550.00], [1]))
    aList.append(genTrans('Regal Theatre', 2019, 5, 2, 12, 50,  ['Avengers Endgame'], [10.00], [1]))
    aList.append(genTrans('Panda Express', 2019, 5, 2, 15, 12,  ['Beef and Broccoli', 'Orange Chicken'], [6.99, 6.99], [1, 1]))
    aList.append(genTrans('Chick-Fil-A', 2019, 5, 4, 7, 14,  ['Waffle Fries', 'Chicken Sandwich'], [3.99, 4.99], [2, 1]))
    aList.append(genTrans('Walmart', 2019, 5, 6, 2, 24,  ['Pears', 'Instant Ramen', 'Twix'], [0.60, 0.10, 0.99], [10, 20, 5]))
    aList.append(genTrans('Amazon', 2019, 5, 8, 19, 21,  ['AirPods'], [129.99], [1]))
    aList.append(genTrans('Amazon', 2019, 5, 12, 1, 19,  ['iPhone Chargers'], [19.99], [1]))
    aList.append(genTrans('Panda Express', 2019, 5, 15,19, 56,  ['Beef and Broccoli'], [6.99], [2]))
    aList.append(genTrans('CVS Pharmarcy', 2019, 5, 18, 22, 14,  ['Facewash', 'Shampoo'], [4.99, 7.99], [1, 1]))
    aList.append(genTrans('McDonalds', 2019, 5, 19, 4, 19, ['Happy Meal, Large Fries, Pepsi'], [5.00, 2.00 , 1.50], [3, 2, 1]))
    aList.append(genTrans('Richmond Gas Works', 2019, 5, 19, 3, 45,  ['Gas'], [12.55], [1]))
    aList.append(genTrans('Richmond Water', 2019, 5, 22, 22, 23,  ['Water'], [25.32], [1]))
    aList.append(genTrans('Comcast', 2019, 5, 23, 1, 12,  ['Internet'], [19.99], [1]))
    aList.append(genTrans('Dominion', 2019, 5, 25, 13, 18,  ['Power'], [18.23], [1]))
    aList.append(genTrans('Rent', 2019, 5, 26, 16, 40,  ['Rent'], [550.00], [1]))
    aList.append(genTrans('Cookout', 2019, 5, 23, 1, 12,  ['Burger'], [5.99], [1]))
    aList.append(genTrans('StakeShake', 2019, 5, 25, 13, 18,  ['Coke'], [2.99], [1]))
    aList.append(genTrans('Walmart', 2019, 5, 26, 16, 40,  ['Chips','Cookies'], [10.00,5.00], [1,2]))
    return {
        "transactions": aList
    }

def makeDemo():
    aList = list()
    aList.append(genTrans('Chick-Fil-A', 2019, 6, 23, 1, 12,  ['Burger'], [5.99], [1]))
    aList.append(genTrans('McDonalds', 2019, 6, 25, 13, 18,  ['Coke'], [2.99], [1]))
    aList.append(genTrans('Walmart', 2019, 6, 26, 16, 40,  ['Chips','Cookies'], [10.00,5.00], [1,2]))
    return aList