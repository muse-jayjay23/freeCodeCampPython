#for i in [2,1,5]:
    #print(i)

    #i loops through the list, will print each consequentially

"""
Iteration to find the smallest number in a list
itervar runs through the list, if smallest = 0 
or is smaller than intercar (number stored already) 
smallest will become itervar
"""
#smallest = None
#print("Before:", smallest)
#for itervar in [3, 41, 12, 9, 74, 15]:
    #if smallest is None or itervar < smallest:
        #smallest = itervar
    #print("Loop:", itervar, smallest)
#print("Smallest:", smallest)

"""
value iterates through the list
count goes through the number of loops in the iterations
sum adds the values of the iterations together
in print statement, sum/count gives average of values
"""
count = 0 
sum = 0
print("Before", count, sum)
for value in [9,41,12,3,74,15]:
    count = count +1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum / count)