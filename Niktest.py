"""Nik test module built in playground""" #use docstrings to put documentation on the api. Call help(module name) to get that in python3 live mode
import json #import modules needed
from requests import get #import just the function needed. import this will return the zen of python - lol

count = 0 #global variable
 
def runThis(url): #define a function, with parameters to be passed in
    """fetch time of a region"""
    x = 10 #variable assignment is dynamic - it is defined at runtime not compile time
    y = "hello" #strings are immutable objects, so if you make y=x and change x, y wont change as still pointing to other object. if y value is changed, old object is orphaned and garbage collected

    r = [2,4,6] #this is a list. lists are mutable so if you make s = r and update s[1] = 4, then both r and s will change

    if y == "hi": #for statement. This demonstrates the importance if indentation
        print("this wont print")

    inputFile = open("input.json", "r") #open file in read mode. later in write mode
    outputFile = open("output.txt", "w")

    obj = json.load(inputFile) #uses json module to loop through in list
    for hobby in obj['Hobbies']: #for loop
        outputFile.write(hobby + "\n") #this is a comment with a hash character

    inputFile.close() #remember to close any open streams
    outputFile.close()

    response = get(url) #an example of a http request to an api. since we imported just get from requests, fully qualified name is not required
    obj2 = json.loads(response.text)
    return (str(obj2['timezone']) + "/n" + str(obj2['utc_datetime'])) #return from the function


def printTime(timer):
    """print the time""" #api comments shown on help(modulename) or help(modulename.functionname)
    print(timer) #print statement


def main():
    """main method to get a time"""
    x = runThis("http://worldtimeapi.org/api/timezone/Europe/London") #just a comment to say all parameters are passed by ref, not by val
    printTime(x)


if __name__ == '__main__': #this will ensure it always runs if required
    main()



def banner(message, border="-"):  #passed the 2nd parameter with a default (so its optional). rule: always use immutable objects for defaults
    line = len(message) * border
    print(line + "\n" + message + "\n" + line)

def updateCounter(c):
    #count = c #going back to the global variable called count. This will only create a new local variable unless you refer to the global one
    global count #use global to reference the global variable. this will update the global count variable so when printed using printCounter it works as you'd expect
    count = c

def callBanner():
    banner(message="hello friend", border="@") #passing parameters by name rather than position

def printCounter():
    print(count) #try printing global variable once set

def reviewCollections():
    #tuple - immutable sequence of objects (using brackets)
    t=("Nikesh",1,3.55) 
    t[0]
    len(t)
    for item in t: #print each item in a loop
        print(item)
    if 1 in t: #look for a specific item
        print("its in there")

    #strings
    len('hello')
    colors=';'.join(['red','orange','green','pink']) #join is more efficient than + and has additional power - e.g. join each element in a list with a separator
    print(colors)
    colors.split(';') #split the string based on a value in the string and put it in list format
    'hellofriend'.partition('of') #partition a string on a value into 3 - before, at and after
    "this is an {0} of a format {1}!".format("example","string")    #can use format to insert variables into a string based on position
    "this is an {eg} of a format {type}".format(eg="example",type="string")  # or based on named variables
    eg = "example"
    type = "string"
    f"this is an {eg} of a format {type} using f-strings with {printTime('functioncall')}" #f-strings are less verbose and can pass variables in as well as functions

    #lists
    newList=[1,2,3,4,5,6] #list with square brackets
    newList[0] #index from start returns 1
    newList[-1] #index from end returns 6
    newList[2:5] #can slice up a list returns 3, 4, 5
    newList.index(4) #returns position of the indexed value
    newList.remove(4) #removes a value from the list based on value
    newList.reverse() #reverses the list
    newList.sort() #sorts the list

    #dictionaries - key and value pairs
    newDict = {1:"this",2:"is",3:"a",4:"dictionary"} #curly braces with key:value
    newDict[4] #returns value at key
    newDict.update({2:'was'}) #update the value at a key
    for key in newDict:
        print(f"{key} => {newDict[key]}")   #can loop through dictionary using for loop. easy to return the value using f-string and pass the function

    #sets - can be used to take a set (which will remove duplicates) and compare against another set
    set1 = {"nik","rita","nils","viaan"}
    set2 = {"nils","viaan","surina","nyal"}
    set1
    set2
    set1.add("murtle") #adds new value to set
    set1.union(set2) #bring back the union of 2 sets
    set1.intersection(set2) #those in set1 and in set 2
    set1.difference(set2) #everything in first set and not in second set
    set1.symmetric_difference(set2) #in first set or second set but not both
    set3 = {"nik","rita","murtle"}
    set3.issubset(set1) #checks if a set is a subset of another - this will return true

def exceptionManagement(xx): #demonstrates exception when you pass a non integer or non number string
    """this is an example of working with exceptions"""
    try:
        x = int(xx)
        return x
    except ValueError:  #you can see the type of error in the failed call stack
        print("conversion failed")
        return -1

