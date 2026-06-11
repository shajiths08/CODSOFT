products = {
    "rice": ["Basmati Rice", "Ponni Rice", "Brown Rice"],
    "oil": ["Sunflower Oil", "Olive Oil", "Coconut Oil"],
    "snacks": ["Lays", "Kurkure", "Doritos"],
    "beverages": ["Coca-Cola", "Pepsi", "Sprite"],
    "dairy": ["Milk", "Butter", "Cheese"],
    "fruits": ["Apple", "Banana", "Orange"],
    "vegetables": ["Potato", "Tomato", "Carrot"],
    "bakery": ["Bread", "Cake", "Cookies"],
    "frozenfoods": ["Frozen Pizza", "Frozen Fries", "Ice Cream"],
    "personalcare": ["Soap", "Shampoo", "Toothpaste"],
    "household": ["Detergent", "Floor Cleaner", "Dishwash Liquid"],
    "electronics": ["Headphones", "Keyboard", "Mouse"],
    "stationery": ["Notebook", "Pen", "Pencil"],
    "babycare": ["Diapers", "Baby Wipes", "Baby Shampoo"],
    "chocolates": ["Dairy Milk", "KitKat", "Snickers"],
    "breakfast": ["Corn Flakes", "Oats", "Muesli"]
}

print("===== SUPERMARKET RECOMMENDATION SYSTEM =====")

print("\nAvailable Categories:")
for category in products:
    print("-", category)

choice = input("\nEnter a category: ").lower().strip()

if choice in products:
    print("\nRecommended Products:")
    for item in products[choice]:
        print("✓", item)
else:
    print("Category not found!")