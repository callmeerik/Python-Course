# JSON File Handling
import json
import os

def create_file(file):
    with open(file, "w") as f:
        json.dump([], f, indent=4)

def add_items(file, item):
    # 1.load data from file
    with open(file, "r") as f:
        data = json.load(f)
    
    # 2 add item using write mode
    with open(file, "w") as f:
        data.append(item)
        json.dump(data, f, indent=4)


def read_json(file):
    if os.path.exists(file):
        with open(file, "r") as f:
            data = json.load(f)
        for item in data:
            print(f"Name: {item['pizza']} | Size: {item['size']} | Price: ${item['price']}")

def update_json(file, pizza_name):
    if os.path.exists(file):
        with open(file, "r") as f:
            data = json.load(f)
    else:
        print("Error opening file")
    
    for item in data:
        if item["pizza"].lower() == pizza_name.lower():
            new_price = input("Enter the new price: ")
            item["price"] = new_price
            with open(file, "w") as f:
                json.dump(data, f, indent=4)

def delete_json(file):
    
    if not os.path.exists(file):
        print("No existe el archivo. Crea uno primero.")
        return

    with open(file, "r") as f:
        data = json.load(f)

    read_json("menu.json")
    name = input("Ingresa el nombre a eliminar: ")

    new_data = [item for item in data if item["pizza"] != name]

    if len(new_data) == len(data):
        print("❌ Nombre no encontrado.")
    else:
        with open(file, "w") as f:
            json.dump(new_data, f, indent=4)
        print("🗑️ Registro eliminado!")

if __name__ == "__main__":
    #pizza = input("enter pizza name: ")
    #size = input("Enter pizza size: ")
    #price = input("Enter pizza price")
    #item = {"pizza": pizza, "size": size, "price": price}
    #add_items("menu.json", item)
    #read_json("menu.json")
    #update_json("menu.json", "Pepperoni")
    delete_json("menu.json")