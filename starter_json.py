import json

#allUsers = {}
allUsers = []
survey = [
    "What is your name?\n",
    "How old are you?\n",
    "What state do you live in?\n"
]
keys = ["name", "age", "state"]

# currentUser[keys[0]] = answer1
# currentUser[keys[1]] = answer2
# currentUser[keys[2]] = answer3
done = False        # new
while not done:     # changed
    currentUser = {}
    i = 0
    for question in survey:
        response = input(question)
        currentUser[keys[i]] = response
        i += 1

    print("Thank you! Please review your answers")
    for key, value in currentUser.items():
        print("{} : {}".format(key,value))

    #allUsers[currentUser["name"]] = currentUser
    allUsers.append(currentUser)
    # this code is new!
    done_input = input("Are you done taking surveys? Type y or n. ").lower()    # new
    if done_input == 'y':
        # done = True
        pass
    else:
        pass


# -----------------------------------------------
# new code here!
# -----------------------------------------------

# need to import json up at the top
# need to make a NEW blank json file in the same directory
# we also need to change our condition so  we can stop collecting data from users

#opens file containng our past results
#"r" means read
f = open("allanswers.json", "r")
# note that this won't open the file visually, just like in our filters file
olddata = json.load(f)
list_of_answers += [olddata]
f.close()       # need to close file after it's opened

#reopen the file in write mode, "w" means write
f = open("allanswers.json", "w")
f.write('[\n')  #this begins our new list
index = 0
for t in list_of_answers:
    # your code goes here!
    # you will need to use json.dump() which writes data to json files (look this oup)
    pass

f.write(']')
f.close()
