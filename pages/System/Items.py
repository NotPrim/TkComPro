def loadItemList(filename: str = "assets/list/ItemList.csv") -> dict:
    temp = dict()
    file = open(filename, "r")
    for line in file:
        name, price = line.split(',')
        temp[name] = int(price)
    return temp


# เรียงลำดับของสินค้าตามคำค้นหา
def searchSort(search: str) -> dict:
    itemSort = list(itemDict.keys())
    for i in range(len(itemSort)):
        for j in range(i+1, len(itemSort)):
            left = itemSort[i].lower()
            right = itemSort[j].lower()
            Lscore = left.find(search.lower())
            Rscore = right.find(search.lower())
            if Lscore == -1 and Rscore == -1:
                if itemSort[j] < itemSort[i]:
                    itemSort[i], itemSort[j] = itemSort[j], itemSort[i]
            elif Rscore >= 0 and Lscore == -1:
                itemSort[i], itemSort[j] = itemSort[j], itemSort[i]
            elif Rscore < Lscore and Rscore != -1:
                itemSort[i], itemSort[j] = itemSort[j], itemSort[i]
    return {k: itemDict[k] for k in itemSort}


itemDict = loadItemList()

if __name__ == "__main__":
    itemDict = searchSort('s')
    for k in itemDict:
        print(f"{k}: {itemDict[k]}")
