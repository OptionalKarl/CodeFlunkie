import math
import itertools

def split(word): # function to split the possible combinations into an array
    return [char for char in word]

AvailableLengths = [0.5,0.8,1,1.2,1.5,1.8] # hardcoded - but the list of available rods
Cubewidth = 2.5 # hardcoded - but the dimension of the cube to place on rods
Maxvar = math.ceil(Cubewidth / min(AvailableLengths)) # the maximum number of smaller rods you would require
base = 0 #used to build a string and build different itertions
FinalIterations = [] # prepare array ahead of time
success = 0 # counter for whether combination is valid

for i in range (1,Maxvar): # based on maxvar, build the string to extrapolate all possible combinations. e.g. 01234, 0123456
    base = str(base) + str(i)
base = str(base) + str(Maxvar)

print(base)
print("\n")

a = [''.join(i) for i in itertools.combinations_with_replacement(base, len(AvailableLengths))] # first pass that gets an ordered list icluding repeated characters, generating a list of combinations

b = [''.join(i) for i in itertools.permutations(base, len(AvailableLengths))] # second pass that gets an unordered list, but does not included repeated characters

# take lists a & b and pull them together removing duplicates
duplicate = set(a)
unordered = set(b)
notfoundperm = unordered - duplicate
FullList = a + list(notfoundperm)


for  element in FullList:
    totallength = 0
    multipliers = split(element)
    for i in (0,len(AvailableLengths)-1): # go through the iteration and build the total length of all rods using that iteration
        totallength = int(totallength) + int(multipliers[i]) * AvailableLengths[i]
    if totallength > Cubewidth: # if the iteration results in a length greater than the width of the box
        success = 0
        for i in (0, len(AvailableLengths)-1): # for each possible rod length, check whether reducing by 1 rod length, it is no longer big enough
            if totallength - AvailableLengths[i] < Cubewidth:
                success = success + 1 # increase by 1 for each rod that COULD be removed 
        if success == 1: # if the length is only exceeded by 1 rod of any length, this is a valid combination
            FinalIterations.append(element) # add to final list

print (len(FullList))
print (len(FinalIterations))