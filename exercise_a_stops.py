stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list

print('Add "Edinburgh Waverley" to the end of the list\n')
stops.append('Edinburgh Waverly')
print(stops)
print('\n')

#2. Add "Glasgow Queen St" to the start of the list

print('Add "Glasgow Queen St" to the start of the list\n')
stops.insert(0,'Glasgow Queen Street')
print(stops)
print('\n')


#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")

print('Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow"\n')
stops.insert(4, 'Polmont')
print(stops)
print('\n')

#4. Print out the index position of "Linlithgow"

print('Print out the index position of "Linlithgow"\n')
position = stops.index('Linlithgow')
print(f'"Linlithgow" is the index {position}')
print('\n')


#5. Remove "Livingston" from the list using its name

print('Remove "Livingston" from the list using its name\n')
stops.remove('Livingston')
print(stops)
print('\n')

#6. Delete "Cumbernauld" from the list by index

print('Delete "Cumbernauld" from the list by index\n')
stops.pop(2)
print(stops)
print('\n')

#7. Print the number of stops there are in the list

print('Print the number of stops there are in the list\n')
number_stops = len(stops)
print(f'The number of stops is {number_stops}')
print('\n')

#8. Sort the list alphabetically

print('Sort the list alphabetically\n')
stops.sort()
print(stops)
print('\n')

#9. Reverse the positions of the stops in the list

print('Reverse the positions of the stops in the list\n')
stops.reverse()
print(stops)
print('\n')

#10 Print out all the stops using a for loop

print('Print out all the stops using a for loop\n')

for stop in stops:
    print(stop)
print('\n')


# PythonMethods
# https://docs.python.org/3/tutorial/datastructures.html
# quiz
# https://docs.google.com/forms/d/e/1FAIpQLSc0FNd66FGGdtQMRC6_fx5r3mp6zGA3EP2e1VoImdqS2FcAiA/viewform
