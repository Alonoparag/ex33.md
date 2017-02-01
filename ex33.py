numbers = []
print "Welcome to the magical printer of numbers."
def printer(limit, increment):
    i = 0
    while i <= limit:
        print "The top i is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now: ", numbers
        if i < limit:
            print "The bottom i is %d" % i
        """else:
            numbers = []
            i = 0
"""

    print "The numbers: "

    for num in numbers:
        print num
loop = "Y"
while loop != "N" or loop != "n":
    if loop != "N" or loop != "n":
        loop = raw_input('>')
    if loop == "Y" or loop == "y":
        print "How many numbers there would be in the group?"
        number = int(raw_input(">"))
        print "At which increment?"
        increment = int(raw_input('>'))
        if increment > number:
            print "ERROR: The increment chosen is larger than the number chosen,"
            print "Please pick an increment lower tha the number chosen"
        else:
            printer(number, increment)
        print "Would you like to try another number?"
        print "Y \\ N ?"
        """del numbers[:]
        i = 0
        loop = raw_input('>')"""
        """elif loop == "N" or loop == "n":
        print "Goodbye!"
        loop = "N"""
    elif loop != "N" or loop != "n":
        print "Character not recognized."
        print "Would you like to try another number?"
        print "Y \\ N ?"
        """del numbers[:]
        i = 0
        loop = raw_input('>')"""
    """del numbers[:]
    i = 0"""
    #loop = raw_input('>')
print "Goodbye!"
