import json

def load_data():
    """ Loads a JSON file """
    with open("animals_data.json", "r") as handle:
        return json.load(handle)

animals_data = load_data()


def get_animal_data(animals_data):
    """ unpack data from the json-file """
    for animal in animals_data:
        name = animal.get("name")
        diet = animal.get("characteristics", {}).get("diet", "Unknown")
        location = animal.get("characteristics").get("location",{}.get("location", "unknown"))
        type = animal.get("characteristics", {}).get("type", "Unknown")

        print(f"Name: {name}")
        print(f"Diet: {diet}")
        print(f"Location: {location}")
        print(f"Type: {type}")
        print("\n")

get_animal_data(animals_data)
