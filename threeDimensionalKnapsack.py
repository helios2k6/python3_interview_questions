class Food:
    def __init__(self, protein: int, carbs: int, fat: int):
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

    def calories(self) -> int:
        return (self.fat * 9) + (self.protein * 4) + (self.carbs * 4)

def insertIntoCache(cache: dict, itemNumber: int, protein: int, carbs: int, fat: int, valueProtein: int, valueCarbs: int, valueFat: int) -> None:
    if itemNumber not in cache:
        cache[itemNumber] = {}
    if protein not in cache[itemNumber]:
        cache[itemNumber][protein] = {}
    if carbs not in cache[itemNumber][protein]:
        cache[itemNumber][protein][carbs] = {}
    if fat not in cache[itemNumber][protein][carbs]:
        cache[itemNumber][protein][carbs][fat] = {}
    cache[itemNumber][protein][carbs][fat] = (valueProtein, valueCarbs, valueFat)

def tryGetFromCache(cache: dict, itemNumber: int, protein: int, carbs: int, fat: int):
    if itemNumber not in cache or protein not in cache[itemNumber] or carbs not in cache[itemNumber][protein] or fat not in cache[itemNumber][protein][carbs]:
        return (0, 0, 0)
    return cache[itemNumber][protein][carbs][fat]

def solveKnapsack3D(foods: list, protein: int, carbs: int, fat: int) -> list:
    # Initialize the cache first
    cache = {}
    for p in range(0, protein + 1):
        for c in range(0, carbs + 1):
            for f in range(0, fat + 1):
                insertIntoCache(cache, 0, p, c, f, 0, 0, 0)
    
    for ithFood in range(0, len(foods)):
        food = foods[ithFood]
        for p in range(0, protein + 1):
            for c in range(0, carbs + 1):
                for f in range(0, fat + 1):
                    previousValue = tryGetFromCache(cache, ithFood - 1, p, c, f)
                    if food.protein > p or food.carbs > c or food.fat > f:
                        # Food exceeds our knapsack limit
                        insertIntoCache(cache, ithFood, p, c, f, previousValue[0], previousValue[1], previousValue[2])
                    else:
                        # Food does not exceed our limit. Decide which is more valuable, keeping the previous food item
                        # or adding our current food item
                        valueWithoutPreviousFood = tryGetFromCache(cache, ithFood - 1, p - food.protein, c - food.carbs, f - food.fat)
                        valueWithoutPrevousFoodButWithCurrentFood = (valueWithoutPreviousFood[0] + food.protein, valueWithoutPreviousFood[1] + food.carbs, valueWithoutPreviousFood[2] + food.fat)
                        if previousValue[0] < valueWithoutPrevousFoodButWithCurrentFood[0] or previousValue[1] < valueWithoutPrevousFoodButWithCurrentFood[1] or previousValue[2] < valueWithoutPrevousFoodButWithCurrentFood[2]:
                            insertIntoCache(cache, ithFood, p, c, f, valueWithoutPrevousFoodButWithCurrentFood[0], valueWithoutPrevousFoodButWithCurrentFood[1], valueWithoutPrevousFoodButWithCurrentFood[2])
                        else:
                            insertIntoCache(cache, ithFood, p, c, f, previousValue[0], previousValue[1], previousValue[2])

    listOfItems = []
    currentProteinLimit = protein
    currentCarbsLimit = carbs
    currentFatLimit = fat
    for itemNumber in reversed(range(0, len(foods))):
        currentItem = tryGetFromCache(cache, itemNumber, currentProteinLimit, currentCarbsLimit, currentFatLimit)
        previousItem = tryGetFromCache(cache, itemNumber - 1, currentProteinLimit, currentCarbsLimit, currentFatLimit)

        if currentItem[0] != previousItem[0] or currentItem[1] != previousItem[1] or currentItem[2] != previousItem[2]:
            listOfItems.append(itemNumber)

            # Update the current protein, carbs, and fat limits
            currentProteinLimit -= currentItem[0]
            currentCarbsLimit -= currentItem[1]
            currentFatLimit -= currentItem[2]

    return listOfItems

def main():
    foods = [
        Food(2, 3, 1),
        Food(5, 1, 4),
        Food(1, 1, 1),
    ]

    chosenFoods = solveKnapsack3D(foods, 2, 3, 1)
    print(chosenFoods)

main()