"""Nik test module built in playground""" #use docstrings to put documentation on the api. Call help(module name) to get that in python3 live mode
import json #import modules needed
from requests import get #import just the function needed. import this will return the zen of python - lol

count = 0 #global variable
 
def runThis(url): #define a function, with parameters to be passed in
    """fetch time of a region"""
    x = 10 #variable assignment is dynamic - it is defined at runtime not compile time
    y = "hello" #strings are immutable objects, so if you make y=x and change x, y wont change as still pointing to other object. if y value is changed, old object is orphaned and garbage collected

    r = [2,4,6] #this is a list. lists are mutable so if you make s = r and update s[1] = 4, then both r and s will change

    if y == "hi": #for statement
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
    print(line + "\n" + message)

def updateCounter(c):
    #count = c #going back to the global variable called count. This will only create a new local variable unless you refer to the global one
    global count #use global to reference the global variable. this will update the global count variable so when printed using printCounter it works as you'd expect
    count = c


def printCounter():
    print(count) #try printing global variable once set

