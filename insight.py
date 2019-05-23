import json

vendor_cat = {
    "DINING": {'KFC','City Dogs', 'McDonalds'},
    "GROCERY": {'Farm Fresh','CVS Pharmarcy'},
    "ENTERTAINMENT": {'Regal Theatre'},
    "ELECTRONIC": {'Amazon','Best Buy'},
    "UTILITIES": {'Dominion','Richmond Water','Richmond Gas Works', 'Comcast'},
    "RENT": {'Rent'}
}

def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data

def insight_categories(json_file):
    with open(json_file) as readJSON:
        data = json.load(readJSON, object_hook= _byteify)

    cost_cat = dict()
    for vendor in vendor_cat:
        cost_cat[vendor] = 0
    for transaction in data:
        for vendor in vendor_cat:
            print(transaction["vendor"])
            if transaction["vendor"] in vendor_cat[vendor]:
                cost_cat[vendor] += transaction["totalCost"]

    aList = list()
    for category, cost in cost_cat.items():
        aDict = dict()
        aDict[category] = cost
        aList.append(aDict)
    return aList

def make_insight_json(json_file):
    aDict = dict()
    aDict["categories"] = insight_categories(json_file)
    aDict["vendors"] = insight_vendors(json_file)
    # aDict["dates"] = insight_dates(json_file)
    # aDict["specific_cat"] = insight_specific(json_file)

def insight_vendors(json_file):
    Vendor = {} 
    with open(json_file) as json_file:
        data = json.load(json_file, object_hook= _byteify)
        for transaction in data:
            if transaction["vendor"] in Vendor:
                Vendor[transaction["vendor"]] += 1
            else:
                Vendor[transaction["vendor"]] = 1
        
        aList = list()
        for vendor, nBills in Vendor.items():
            aDict = dict()
            aDict[vendor] = nBills
            aList.append(aDict)
    return aList

print(insight_vendors('history.json'))
