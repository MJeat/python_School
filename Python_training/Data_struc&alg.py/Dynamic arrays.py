# Dynamic array: a type of data structure that is used for storage. Unlike static array, which have fixed size and capacity, dynamic array has flexible size and capacity need to change if needed.
# dynamic array is like a magical box for your toys that can grow bigger or smaller as you need it!
#Dynamic array: is called list in python. 


#Exercise 1:

heros=['spider man','thor','hulk','iron man','captain america']

heros.append('black panther')

print(len(heros))
print(heros)

heros.remove('black panther')
print(heros)

heros.insert(3, 'black panther')
print(heros)

heros[1:3] = ['doc strange'] # To replace thor and hulk with doc. number one does not count so it counts 2 and 3 which will be replaced by doc. 
print(heros)

#-------------------------------------------------------------------------------------------------
# Exercise 2:

cost = [2200,2350,2600,2130,2190]

print('In Feb, how many dollars you spent extra compare to January?: ', cost[1]-cost[0])
print('Find out your total expense in first quarter (first three months) of the year: ', cost[0]+cost[2]+ cost[1])


print('Find out if you spent exactly 2000 dollars in any month: ', 2000 in cost)

cost.append(1980)
print(cost)


new_cost = cost[3]-200
cost[3] = new_cost
print(cost)
 
# [2200, 2350, 2600, 1930, 2190, 1980]