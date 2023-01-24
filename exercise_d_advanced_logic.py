# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

for number in numbers:
    if number % 2 == 0:
        print (number)


# 2. Print the difference between the largest and smallest value:

numbers2 = numbers
numbers2.sort()

smallest_number = numbers2[0]
largest_number = numbers2[-1]

difference = largest_number - smallest_number
print(difference)


# 3. Print True if the list contains a 2 next to a 2 somewhere.

print(numbers)
#check how muany times '2' appears in list
print(numbers.count(2))

#check index of 1st instance
first_index_of_2 = numbers.index(2)
print(first_index_of_2)

#as there are only 2 instances, reverse list to check other index
numbers_rev = numbers
numbers_rev.reverse()

print(numbers_rev)

second_index_of_2 = numbers_rev.index(2)
print(second_index_of_2)

#index of 2nd instance needs to be adjusted to correct index - re reversed

length = len(numbers)
print(length)

adjusted_second_index = length - 1 - second_index_of_2
print(adjusted_second_index)

# instances are next to each other if difference between indexes equals '1'

if adjusted_second_index - first_index_of_2 == 1:
    print(True)
else:
    print(False)







# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 







