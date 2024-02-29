from flask import Flask
from helper import pets  # Importing the pets data from a helper module

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return '''<h1>Adopt a Pet!</h1>
    <p>Browse through the links below to find your new furry friend:</p>
    <ul>
        <li><a href="/animals/dogs">Dogs</a></li>  <!-- Link to the dogs page -->
        <li><a href="/animals/cats">Cats</a></li>  <!-- Link to the cats page -->
        <li><a href="/animals/rabbits">Rabbits</a></li>  <!-- Link to the rabbits page -->
    </ul>                                  
    '''

# Route for displaying a list of animals of a particular type
@app.route('/animals/<pet_type>')
def animals(pet_type):
    pet_list = pets.get(pet_type, [])  # Get the list of pets of the specified type
    html = f'<h1>List of {pet_type}</h1><ul>'  # Start building the HTML content
    for pet_id, pet in enumerate(pet_list):
        # For each pet, create a list item with a link to its details page
        html += f'<li><a href="/animals/{pet_type}/{pet_id}">{pet["name"]}</a></li>'
    html += '</ul>'  # Close the unordered list
    return html  # Return the HTML content

# Route for displaying details of a specific pet
@app.route('/animals/<pet_type>/<int:pet_id>/')
def pet(pet_type, pet_id):
    pet_list = pets.get(pet_type, [])  # Get the list of pets of the specified type
    if pet_id < 0 or pet_id >= len(pet_list):
        # If the requested pet ID is out of range, return a 404 error
        return 'Pet not found', 404

    pet = pet_list[pet_id]  # Get the details of the specified pet
    return f'''
    <h1>{pet["name"]}</h1>
    <img src="{pet["url"]}" alt="{pet["name"]}">  <!-- Display the pet's image -->
    <p>{pet["description"]}</p>  <!-- Display the pet's description -->
    <ul> 
        <li>Breed: {pet["breed"]}</li>  <!-- Display the pet's breed -->
        <li>Age: {pet["age"]}</li>  <!-- Display the pet's age -->
    </ul>
    '''

if __name__ == '__main__':
    # Run the Flask app in debug mode on all available network interfaces
    app.run(debug=True, host="0.0.0.0")
