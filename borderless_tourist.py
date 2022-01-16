#Project was facilitated by Codeacademy and created by me. I do not take credit for the functionality of this program.

destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]

#finding the index of destination to be used for future functions.
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index
   
#saving the index of users destination. in this case, the traveler input would be the test_traveler variable.
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

#creating the list attractions by looping through every destination in the list destinations (which is defined in the begining of script.py) and adding an empty list ([]) within a larger list called attractions ([[], [], [], [], [], []])
attractions = [[] for destination in destinations]

#designed to add attractions to the empty lists in attractions. try: except SyntaxError: is new. the interpeter will see try: and then observe the following code, if the code has any error besides the SyntaxError, it will display an error message. If there is a SyntaxError, then then interepreter will in this case return nothing. hense "except SyntaxError: return "
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
  except SyntaxError:
    return

#adding to our attractions list.
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#a function designed to take in a destination and list of interests as inputs. The function then finds the index of the destination via use of the get_destination_index() function.
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interests = []

  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]

    for interest in interests:
        if interest in attraction_tags:
          # 49. only appending the first element of possible_attraction    because we dont wont the user to see the tags hence: possible_attraction[0].
          attractions_with_interests.append(possible_attraction[0])
  return attractions_with_interests

la_art = find_attractions("Los Angeles, USA", ['art'])

#creation of new function designed to 
def get_attractions_for_traveler_interests(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)

  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "

  for i in range(len(traveler_attractions)):
    if traveler_attractions[-1] == traveler_attractions[i]:
      interests_string += "the " + traveler_attractions[i] + "."
    else:
      interests_string += "the " + traveler_attractions[i] + ", "
  return interests_string

smiles_france = get_attractions_for_traveler_interests(['Nikki Bush', 'Cairo, Egypt', ['museum']])

print(smiles_france)
