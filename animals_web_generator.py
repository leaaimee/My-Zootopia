import json
import os

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


def serialize_animal(animal_obj):
    """Serialize a single animal object into an HTML list item"""
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj.get("name", "Unknown")}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'      <strong>Diet:</strong> {animal_obj.get("characteristics", {}).get("diet", "Unknown")}<br/>\n'
    output += f'      <strong>Location:</strong> {", ".join(animal_obj.get("locations", ["Unknown"]))}<br/>\n'
    output += f'      <strong>Type:</strong> {animal_obj.get("characteristics", {}).get("type", "Unknown")}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'

    return output


def generate_animal_html():
    with open("animals_template.html", "r") as template_file:
        html_template = template_file.read()
    return html_template


def generate_animal_info(animals_data):
    """Generate HTML for all animals"""
    animals_info = ""
    for animal in animals_data:
        animals_info += serialize_animal(animal)
    return animals_info


def write_animal_html(animals_info):
    """Replaces placeholder in the template and writes to a file"""
    animals_info = generate_animal_info(animals_data)
    html_template = generate_animal_html()
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open("animals.html", "w") as output_file:
        output_file.write(html_output)
        print("File written successfully to animals.html")

get_animal_data(animals_data)
write_animal_html(animals_data)


