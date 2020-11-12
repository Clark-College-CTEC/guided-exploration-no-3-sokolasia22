# Guided Exploration No. 3
# Anastasia Sokolov

# generate random library
import random
# make empty list to store rap names from rap-names.txt file
possible_names = []
# open rap-names-output.txt file
outputFile = open('rap-names-output.txt', 'w')
# open rap-names.txt file for read access
# assign file to variable dataFile
with open('rap-names.txt', 'r') as dataFile:
    # iterate through each line in rap-names.txt file
    for name in dataFile:
        # read in a line from file
        # strip off line-feed
        # append name to possible-names list
        possible_names.append(name.rstrip())
# ask the user to input the desired number of rap names
count = int(input('How many rap names would you like to create? '))
# ask user to input the desired number of parts the name should contain
parts = int(input('How many parts should the name contain? '))
# use counted loop to generate number of rap names
for i in range(count):
    # create empty list for rap names
    name_parts = []
    # iterate through list for the number of rap names
    for j in range(parts):
        # generate random number to get rap name from possible_names
        # append generated name from possible_names to name_parts
        name_parts.append(possible_names[random.randint(0, len(possible_names)-1)])\
            # combine contents of name_parts list, seperated with a space
    # add newline to string
    outputFile.write(f"{' '.join(name_parts)}\n")
    # display file in terminal
    print(f"{' '.join(name_parts)}")
# close output file
outputFile.close()
