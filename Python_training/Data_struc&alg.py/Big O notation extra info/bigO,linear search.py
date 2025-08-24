# Linear search = iterate through a collection one element at a time

#Run time complexity: O(n)

#Pros: 
    # fast for searches of small to medium data sets
    # does not need to sorted 
    # useful for data structures that do not have random access (linkedlist)

#Cons: 
    # slow for large data sets


# Here is an example of a linear search that I have been using but never realize it:


cities = ['Tokyo', 'Mumbai', 'Phnom Penh', 'Washington D.C', 'New York']

for city in cities:
  city = input('Enter your city: ')
  if city == 'New York':
    print('City is found!')
    break
  # Indentation for else moved here
else:
    print('No city is found within the list...')

print(cities[4])

#---------------------------------------------------------------
    