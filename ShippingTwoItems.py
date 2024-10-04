from typing import List, Tuple


# Time: O(n^2), Space: O(1)
def longTaskA(items: List[Tuple[float, str]], p2500):
    n = len(items)
    for i in range(n):
        for j in range(i+1, n):
            if items[i][0] + items[j][0] == p2500:
                return [items[i], items[j]]
    return None


# Time: O(n), Space:O(n)
def taskA(items: List[Tuple[float, str]], p2500: float):
    # mapItems stores index: complement value, element: location(index) in Items
    mapItems = {}
    for index, item in enumerate(items):
        price: float = item[0]
        # print(price)
        targetPrice = p2500 - price
        # print('Target Price is:', targetPrice)
        if targetPrice in mapItems:
            # items[mapItems[targetPrice] returns the index of the complement in the original items list
            return [items[mapItems[targetPrice]], item]
        # Add the current item price into the HashMap
        mapItems[price] = index
    return None

