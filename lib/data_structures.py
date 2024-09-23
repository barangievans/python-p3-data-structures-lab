# data_structures.py

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """Retrieve names from a list of spicy foods."""
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """Return foods with a heat level greater than 5."""
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    """Print all spicy foods formatted with 🌶 emojis."""
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Return the food that matches a specific cuisine."""
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # Return None if no food is found

def print_spiciest_foods(spicy_foods):
    """Print foods with heat level greater than 5 formatted with 🌶 emojis."""
    spiciest = get_spiciest_foods(spicy_foods)
    for food in spiciest:
        heat_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def get_average_heat_level(spicy_foods):
    """Return the average of heat levels in spicy foods."""
    if not spicy_foods:
        return 0
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)

def create_spicy_food(spicy_foods, new_food):
    """Add a new spicy food to the list and return the updated list."""
    spicy_foods.append(new_food)
    return spicy_foods
