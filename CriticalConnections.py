import copy

def criticalConnection(numOfWarehouses, numOfRoads, roads):
    
    connectionDict = {}
    criticalRoads = []
    
    for i in range(numOfWarehouses):
        connectionDict[i + 1] = []

    for i in range(len(roads)): 
        tempDict = copy.deepcopy(connectionDict)
        tempStorage = roads[:]
        tempStorage.pop(i) 
        
        for j in range(len(tempStorage)):
            #not considering case where warehouse isnt in roads list
            # if tempStorage[j][0] not in list(tempDict.keys()) or tempStorage[j][1] not in list(tempDict.keys()):
                # return criticalRoads

            tempDict[tempStorage[j][0]].append(tempStorage[j][1])
            tempDict[tempStorage[j][1]].append(tempStorage[j][0])

        if isConnected(tempDict) == False:
            criticalRoads.append(roads[i])
        tempDict = {}
    
    return criticalRoads

def isConnected(dict, warehousesReached = None, startWarehouse = None):
    
    if warehousesReached == None:
        warehousesReached = set()
        
    warehouses = list(dict.keys())

    if not startWarehouse:
        startWarehouse = warehouses[0]

    warehousesReached.add(startWarehouse)
    if len(warehousesReached) != len(warehouses):
        for temp in dict[startWarehouse]:
            if temp not in warehousesReached:
                if isConnected(dict, warehousesReached, temp):
                    return True
    else:
        return True

    return False


print(criticalConnection(6,5,[[1,2], [2, 3], [3,4], [4,5], [6,3]]))
