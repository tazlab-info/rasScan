import openfoodfacts
import json
try:
    with open("list.json", r) as file:
        list = json.load(file)
except:
    list=[]
api = openfoodfacts.API(user_agent="MyAwesomeApp/1.0")

while True:
    code = input("scannez le produit...")
    product = api.product.get(code)
    try:
        name = product.get("product_name")
        total = [name, product.get("image_url")]
        if total in list:
            print("le produit ",name , "a été supprimer de la liste.")
            list.remove(total)
        else :
            print("le produit ",name , "a été ajouter a la liste.")
            list.append(total)
    except:
        print("produit non conforme")
        pass
    with open("list.json", "w") as file:
        json.dump(list, file)