from sys import argv

name, first, second, third, fourth = argv

print "Script name is:", name
print "Your first argument is:", first
print "Your second argument is:", second
print "Your third argument is:", third
print "Your fourth argument is:", fourth


# Alternatively we can access "argv" argument list directly using range. For exmaple:

# Print all arguments except script name
print argv[1:]

# Print second argument
print argv[2]

# Print second and third argument
print argv[2:4]

# Print last argument
print argv[-1]
