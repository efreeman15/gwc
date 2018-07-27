# how to define a cat object.

# ------------------------------
# @@@@@@@ !THIS IS NOT VALID PYTHON CODE.! @@@@@@@
# use this to get a sense of what an object might
# look like in code.
# ------------------------------

# we are writing the blueprint or template that we will fill out
# when we call/create an instance of the Cat object.

# "creating an instance" of this object means filling out this
# blueprint with values specific to the type of cat we want. in the code
# below, all we are doing is writing the template -- we have not
# actually created any Cat objects yet.
object Cat:

    # this function is called automatically
    # when we define a new instance of our class
    def __init__(whiskers, color, size):
        # we can pass it any number of parameters.
        # these will become our attributes

        # assigning our parameters to variables means
        # we will keep track of our object's attributes.
        # it's like saving our attributes.
        w = whiskers
        c = color
        s = size

        # we can also define certain attributes without
        # using parameters. if we define an attribute without
        # parameters, it will be true for ALL instances of
        # that object--in this case, all Cats.
        feline = True
        # so now any Cat will have a True value for the
        # feline attribute. we can't change this attribute
        # without changing our object definition (i.e. we
        # can't change it when we create an instance of Cat.)

    # note that now we are indented outside of our __init__ function,
    # but that we are still inside our Cat object.

    # here we are defining a function (method) that ALL Cat objects
    # have. after we create an instance of our cat, we can call the
    # meow() method by using dot notation. any Cat we create will
    # be able to meow().

    def meow():
        print("Meow!")



    # we could have as many methods as we want, and we can use parameters,
    # just like any other function.
    def eat(food):
        print("The cat ate all of the %s!"%(food))

# now we are unindented out of the class definition body
# we are finished defining our object--our Cat template is done!

# --------------------------------------------------

# you can have multiple instances of an objects.
# using several objects is helpful because you don't have to
# rewrite the same pieces of code over and over again.
# you can then use the objects in several different ways
# in your code. for example, you can have several Cats with different
# colors, sizes, and amounts of whiskers.
# it's a way to make your code more flexible by creating templates
# and filling them out as you go.

# now we are going to call some instances of our Cat objects.
# to do so, we set the object name (in this case, Cat) equal to
# a variable and pass in any parameters that are needed.

# for example, this is how we would create a Cat with 5 whiskers,
# a black color, and a large size. parameters here work basically
# the same way that they do in function calls.

cat1 = Cat(5, "black", "large")
# when we do this, it calls the __init__ function (that's just some
# Python under-the-hood magic) and sets w = 5, c = "black", s = "large".

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
print(cat2.size)    # this would give an error, we would need to say cat2.s
