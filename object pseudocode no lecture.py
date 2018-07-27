# how to define a cat object.

# THIS IS NOT VALID PYTHON CODE!!!!!!!!!!!!!!!!!!!!!
# THIS IS JUST AN EXAMPLE OF HOW CODE MIGHT LOOK.

# defining the Cat object
object Cat:

    # this function is called automatically
    # when we define a new instance of our class
    def __init__(whiskers, color, size):
        # save our parameters to variables (attributes)
        w = whiskers
        c = color
        s = size

        # define attributes without using parameters
        feline = True

    # new function (method) for ALL Cat objects
    def meow():
        print("Meow!")

    # new method for all Cat objects using parameters
    def eat(food):
        print("The cat ate all of the %s!"%(food))

# now we are unindented out of the class definition body
# we are finished defining our object--our Cat template is done!

# --------------------------------------------------

# create a new instance of our Cat object
# this instance has 5 whiskers, a black color, and a large size
cat1 = Cat(5, "black", "large")

# to access attributes we use a . (period)
print(cat1.s)    # this would print "large"
print(cat1.w)    #this would print 5
print(cat1.f)  # this would print True

# to access methods we also use a .
cat1.meow()     # this would print "Meow!"
cat1.eat("fish")    # this would print "The cat ate all the fish!"
cat1.eat("ice cream")   # would print "The cat ate all the ice cream!"


# now we are going to define a second instance of the Cat object
cat2 = Cat(4, "orange", "medium")

print(cat2.s)    # this would print ("medium")
cat2.meow()     # this would print "Meow!"

# we can do this for as many Cats as we want!
cat3 = Cat(100, "purple", "enormous")
cat4 = Cat(0, "white", "tiny")
cat5 = Cat(10, "spotted", "small")

# we can also do the following to redefine attributes of an existing
# instance of the Cat object:
cat1.s = "small"
print(cat1.s)    # this would print "small" even though it used to be "large"

# ! THE FOLLOWING CODE WILL NOT WORK !
badcat1 = Cat(5, "brown", "medium", False)   # we have not set up a fourth parameter
badcat2 = Cat()    # we have not defined our whiskers, color, and size attributes
badcat3 = (2, "green", "big")   # we have not told Python to use the Cat object

badcat4 = Cat(3, "orange", "tiny") # this is an OK definition
print(badcat4.whiskers)    # this is not defined, we would need to use badcat4.w

