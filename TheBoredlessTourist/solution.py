#lists
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
attractions = [[] for i in destinations]

#functions
def get_destination_index(destination):
    try:
        destination_index = destinations.index(destination)
        return destination_index
    except ValueError: #error handleing
        return "Destination not found in the list."

def get_traveler_location(traveler):
  traveler_destination = test_traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for possible_attraction in attractions_in_city:
      print(f"Checking attraction: {possible_attraction}")  # Debug print
      attraction_tags = possible_attraction[1]
      for interest in interests:
          if interest in attraction_tags:
              attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_intrests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_intrests)
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around "
  for i in traveler_attractions:
    interests_string += i + ", "
  return interests_string

# add attractions
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#Final statements
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
la_arts = find_attractions("Los Angeles, USA", ['art'])
add_attraction(destinations[2], ['Venice Beach', ['beach']])
print(smills_france)
print(la_arts)
print(test_destination_index)
print(get_destination_index("Paris, France"))
print(attractions)
print(get_destination_index("Hyderabad, India"))