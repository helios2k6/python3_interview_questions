class Food:
    def __init__(self, name: str, protein: int, carbs: int, fat: int):
        self.name = name
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.category = None

    def calories(self) -> int:
        return (self.fat * 9) + (self.protein * 4) + (self.carbs * 4)

    def __str__(self) -> str:
        return self.name

    def setCategory(self, cat: str) -> None:
        self.category = cat

class SparseCache:
    def __init__(self):
        self.cache = {}

    def tryGet(self, itemNumber: int, protein: int, carbs: int, fat: int):
        if itemNumber not in self.cache or protein not in self.cache[itemNumber] or carbs not in self.cache[itemNumber][protein] or fat not in self.cache[itemNumber][protein][carbs]:
            return (0, 0, 0)
        return self.cache[itemNumber][protein][carbs][fat]

    def insert(self, itemNumber: int, protein: int, carbs: int, fat: int, valueProtein: int, valueCarbs: int, valueFat: int):
        if itemNumber not in self.cache:
            self.cache[itemNumber] = {}
        if protein not in self.cache[itemNumber]:
            self.cache[itemNumber][protein] = {}
        if carbs not in self.cache[itemNumber][protein]:
            self.cache[itemNumber][protein][carbs] = {}
        if fat not in self.cache[itemNumber][protein][carbs]:
            self.cache[itemNumber][protein][carbs][fat] = {}
        self.cache[itemNumber][protein][carbs][fat] = (valueProtein, valueCarbs, valueFat)

    def __str__(self):
        return self.cache.__str__()

def tryGetFromCache(cache: dict, itemNumber: int, protein: int, carbs: int, fat: int):
    if itemNumber not in cache or protein not in cache[itemNumber] or carbs not in cache[itemNumber][protein] or fat not in cache[itemNumber][protein][carbs]:
        return (0, 0, 0)
    return cache[itemNumber][protein][carbs][fat]

def solveKnapsack3D(foods: list, protein: int, carbs: int, fat: int, categoryLimits: dict) -> list:
    # Initialize the cache first
    cache = SparseCache()
    foodCategoryTallies = {}
    for ithFood in range(0, len(foods)):
        food = foods[ithFood]
        if food.category and food.category in categoryLimits:
            if food.category not in foodCategoryTallies:
                foodCategoryTallies[food.category] = 0
            foodCategoryTallies[food.category] += 1
        for p in range(0, protein + 1):
            for c in range(0, carbs + 1):
                for f in range(0, fat + 1):
                    previousValue = cache.tryGet(ithFood - 1, p, c, f)
                    # We will special case protein. We're OK with exceeding protein levels. This isn't true 3D knapsack since we have
                    # special rules in place for specific macros. We also need to respect "food category limits" so that we don't just add
                    # a bunch of protein shakes into the diet. This also complicates our diet plan
                    if food.carbs > c or food.fat > f or (food.category and food.category in categoryLimits and food.category in foodCategoryTallies and foodCategoryTallies[food.category] > categoryLimits[food.category]):
                        # Food exceeds our knapsack limit or has limits placed on it
                        cache.insert(ithFood, p, c, f, previousValue[0], previousValue[1], previousValue[2])
                    else:
                        # Food does not exceed our limit. Decide which is more valuable, keeping the previous food item
                        # or adding our current food item
                        valueWithoutPreviousFood = cache.tryGet(ithFood - 1, p - food.protein, c - food.carbs, f - food.fat)
                        valueWithoutPrevousFoodButWithCurrentFood = (valueWithoutPreviousFood[0] + food.protein, valueWithoutPreviousFood[1] + food.carbs, valueWithoutPreviousFood[2] + food.fat)
                        if previousValue[0] < valueWithoutPrevousFoodButWithCurrentFood[0] or previousValue[1] < valueWithoutPrevousFoodButWithCurrentFood[1] or previousValue[2] < valueWithoutPrevousFoodButWithCurrentFood[2]:
                            cache.insert(ithFood, p, c, f, valueWithoutPrevousFoodButWithCurrentFood[0], valueWithoutPrevousFoodButWithCurrentFood[1], valueWithoutPrevousFoodButWithCurrentFood[2])
                        else:
                            cache.insert(ithFood, p, c, f, previousValue[0], previousValue[1], previousValue[2])

    listOfItems = []
    currentProteinLimit = protein
    currentCarbsLimit = carbs
    currentFatLimit = fat
    for itemNumber in reversed(range(0, len(foods))):
        currentValue = cache.tryGet(itemNumber, currentProteinLimit, currentCarbsLimit, currentFatLimit)
        previousValue = cache.tryGet(itemNumber - 1, currentProteinLimit, currentCarbsLimit, currentFatLimit)

        if currentValue[0] != previousValue[0] or currentValue[1] != previousValue[1] or currentValue[2] != previousValue[2]:
            currentFood = foods[itemNumber]
            listOfItems.append(currentFood)

            # Update the current protein, carbs, and fat limits
            currentProteinLimit -= currentFood.protein
            currentCarbsLimit -= currentFood.carbs
            currentFatLimit -= currentFood.fat

    return listOfItems

def dietCore(foods: list, proteinLimit: int, carbLimit: int, fatLimit: int, categoryLimits: dict):
    print(f"Testing with: ({proteinLimit}, {carbLimit}, {fatLimit})")
    optimalFoods = solveKnapsack3D(foods, proteinLimit, carbLimit, fatLimit, categoryLimits)
    runningProtein = 0
    runningCarbs = 0
    runningFat = 0
    for food in optimalFoods:
        runningProtein += food.protein
        runningCarbs += food.carbs
        runningFat += food.fat
        print(f"{food} | Total Protein: {runningProtein} | Total Carbs: {runningCarbs} | Total Fat: {runningFat}")


def diet0():
    foods = []

    for _ in range(0, 3):
        f = Food("A", 1, 1, 1)
        f.setCategory("A")
        foods.append(f)

    for _ in range(0, 1):
        f = Food("B", 1, 1, 1)
        f.setCategory("B")
        foods.append(f)

    dietCore(foods, 3, 3, 3, {"A": 2})

def diet1():
    foods = []
    # Scrambled Eggs
    for _ in range(0, 3):
        foods.append(Food("Scrambled Eggs (100g)", 11, 2, 12))

    # Muscle Milk
    for _ in range(0, 2):
        shake = Food("Muscle Milk (14 oz)", 25, 9, 5)
        shake.setCategory("Shake")
        foods.append(shake)

    # Bacon
    for _ in range(0, 4):
        foods.append(Food("Bacon (1 Slice)", 3, 0, 3))

    # Orange Juice
    for _ in range(0, 2):
        foods.append(Food("Orange Juice (1/2 cup)", 1, 13, 0))

    # Premier Protein Shake
    for _ in range(0, 2):
        shake = Food("Premier Protein Shake (325 ml)", 30, 5, 3)
        shake.setCategory("Shake")
        foods.append(shake)

    # Hanger Steak
    for _ in range(0, 2):
        foods.append(Food("Hanger Steak (5 oz)", 30, 0, 10))

    # Crispy Chicken Strips
    for _ in range(0, 4):
        foods.append(Food("Crispy Chicken Strips (100 g)", 14, 22, 7.2))

    # Lactaid Milk
    for _ in range(0, 4):
        foods.append(Food("Lactaid Milk (1 cup)", 8, 13, 5))

    dietCore(foods, 160, 166, 101, {"Shake": 2})

diet0()