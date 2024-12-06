import json
import os
from html import escape

print("Saving file to:", os.getcwd())


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


def generate_animal_html():
    with open("animals_template.html", "r") as template_file:
        html_template = template_file.read()
    return html_template

def generate_animal_info(animals_data):
    animals_info = ""
    for animal in animals_data:
        name = escape(animal.get("name", "unknown"))
        diet = escape(animal.get("characteristics", {}).get("diet", "unknown"))
        location = escape(", ".join(animal.get("locations", ["unknown"])))
        type = escape(animal.get("characteristics", {}).get("type", "unknown"))

        animals_info += '<li class="cards__item">\n'
        animals_info += f'  <div class="card__title">{name}</div>\n'
        animals_info += '  <p class="card__text">\n'
        animals_info += f'      <strong>Diet:</strong> {diet}<br/>\n'
        animals_info += f'      <strong>Location:</strong> {location}<br/>\n'
        animals_info += f'      <strong>Type:</strong> {type}<br/>\n'
        animals_info += '  </p>\n'
        animals_info += '</li>\n'

    return animals_info


def write_animal_html(animals_info):
    """Replaces placeholder in the template and writes to a file"""


    animals_info = generate_animal_info(animals_data)
    html_template = generate_animal_html()
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(html_output)
        print("File written successfully to animals.html")

get_animal_data(animals_data)
write_animal_html(animals_data)