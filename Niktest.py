"""Nik test module built in playground"""  # use docstrings to put 
                                           # documentation on the api. Call help(module name) to get that in python3 live mode. should be on module, class, method, function
import json  # import modules needed
from requests import get  # import just the function needed. 

                          
# "import this" will return the zen of python - lol
#  if working in REPL, use _ to return the last value
#  PEP8: linting the code for intelliense on coding standards. Import the pep8 linting module. PEP8 is coding standards published by the python community
#  SPHINX: Auto-documentation. Import sphinx to generate documentation. Add a folder to hold the docs and run sphinx-quickstart in that folder. then generate docs using the docstrings in the code 
#  by using sphinx-apidoc -o docs directory      (where the project lives). some updates on the conf.py and finally "make clean html" in the docs directory
#  PIP: package manager. pull in the dependencies you need from other packages from pypi (package index) - go to this (pypi.org) and search for what you want. 
# "python3 -m pip -V" will show version. "python3 -m pip list" will show downloaded packages. "python3 -m pip install json" (will download the package). Always work virtually when installing packages.
#  virtualenvwrapper: Virtual environments. isolated environment for packages so doesnt cause conflicts with other projects. install virtualenv. Add a new directory outside of projects for holding these.
#  run python3 -m virtualenv nameofenv. this will create a VE, with own python interpreter and pip.
#  on linux " . Nik1/bin/activate" (on windows run batch script). This will activate the environment. run "python -V" for version and "pip list" for packages - lot smaller now. install requests. "pip show requests" will show you its now in the ve
#  "deactivate" will bring the VE down.
#  To share the packages needed with team, run "python3 -m pip freeze > requirements.txt" to out put package list to text. Then build environments for any VE with list of packages using "python3 -m pip install -r requirements.txt"

count = 0  # global variable. to refer to this in inner scope, you must define the variable in the inner scope (e.g. function/class with global - else it will just create a new variable)
 
def updateC():
    count = 1 

#calling this and then printing count will print 0

def updateC2():
    global count
    count = 2
 
#calling this and then printing count will print 2 as the global bound variable is updated

def runThis(url):  # define a function, with parameters to be passed
    """fetch time of a region"""
    x = 10  # variable assignment is dynamic - it is defined at runtime not compile time
    y = "hello"  # strings are immutable objects, so if you make y=x and change x, y wont change as still pointing to other object. if y value is changed, old object is orphaned and garbage collected

    r = [2, 4, 6]  # this is a list. lists are mutable so if you make s = r and update s[1] = 4, then both r and s will change

    print(x, y, str(r))
    if y == "hi":  # if statement. This demonstrates the importance if indentation
        print("this wont print")

    inputFile = open("input.json", "r")  # open file in read mode. later in write mode
    outputFile = open("output.txt", "w")

    obj = json.load(inputFile)  # uses json module to loop through in list
    for hobby in obj['Hobbies']:  # for loop
        outputFile.write(hobby + "\n")  # this is a comment with a hash character

    inputFile.close()  # remember to close any open streams
    outputFile.close()

    response = get(url)  # an example of a http request to an api. since we imported just get from requests, fully qualified name is not required
    obj2 = json.loads(response.text)
    return (str(obj2['timezone']) + "/n" + str(obj2['utc_datetime']))  # return from the function


def printTime(timer):
    """print the time"""  # api comments shown on help(modulename) or help(modulename.functionname)
    print(timer)  # print statement


def main():
    """main method to get a time"""
    x = runThis("https://worldtimeapi.org/api/timezone/Europe/London")  # just a comment to say all parameters are passed by ref, not by val
    printTime(x)


if __name__ == '__main__':  # this will ensure it always runs if required
    main()


def banner(message, border="-"):  # passed the 2nd parameter with a default (so its optional). rule: always use immutable objects for defaults
    line = len(message) * border
    print(line + "\n" + message + "\n" + line)


def updateCounter(c):
    # count = c #going back to the global variable called count. This will only create a new local variable unless you refer to the global one
    global count  # use global to reference the global variable. this will update the global count variable so when printed using printCounter it works as you'd expect
    count = c


def callBanner():
    banner(message="hello friend", border="@")  # passing parameters by name rather than position


def printCounter():
    print(count)  # try printing global variable once set


def reviewCollections():
    # tuple - immutable sequence of objects (using brackets)
    t = ("Nikesh", 1, 3.55) 
    t[0]
    len(t)
    for item in t:  # print each item in a loop
        print(item)
    if 1 in t:  # look for a specific item
        print("its in there")

    # strings
    len('hello')
    colors = ';'.join(['red', 'orange', 'green', 'pink'])  # join is more efficient than + and has additional power - e.g. join each element in a list with a separator
    print(colors)
    colors.split(';')  # split the string based on a value in the string and put it in list format
    'hellofriend'.partition('of')  # partition a string on a value into 3 - before, at and after
    "this is an {0} of a format {1}!".format("example", "string")  # can use format to insert variables into a string based on position
    "this is an {eg} of a format {type}".format(eg="example", type="string")  # or based on named variables
    eg = "example"
    type = "string"
    f"this is an {eg} of a format {type} using f-strings with {printTime('functioncall')}"  # f-strings are less verbose and can pass variables in as well as functions

    # lists
    newList = [1, 2, 3, 4, 5, 6]  # list with square brackets
    newList[0]  # index from start returns 1
    newList[-1]  # index from end returns 6
    newList[2:5]  # can slice up a list returns 3, 4, 5
    newList.index(4)  # returns position of the indexed value
    newList.remove(4)  # removes a value from the list based on value
    newList.reverse()  # reverses the list
    newList.sort()  # sorts the list

    # dictionaries - key and value pairs
    newDict = {1: "this", 2: "is", 3: "a", 4: "dictionary"}  # curly braces with key:value
    newDict[4]  # returns value at key
    newDict.update({2: 'was'})  # update the value at a key
    for key in newDict:
        print(f"{key} => {newDict[key]}")  # can loop through dictionary using for loop. easy to return the value using f-string and pass the function
    newDict = {"a": "apple", "b": "banana", "c": "carrot"}  # if both key and value are strings, can unpack them as follows
    for key, val in newDict:
        print(key + '-' + val)

    # sets - can be used to take a set (which will remove duplicates) and compare against another set
    set1 = {"nik", "rita", "nils", "viaan"}
    set2 = {"nils", "viaan", "surina", "nyal"}
    set1
    set2
    set1.add("murtle")  # adds new value to set
    set1.union(set2)  # bring back the union of 2 sets
    set1.intersection(set2)  # those in set1 and in set 2
    set1.difference(set2)  # everything in first set and not in second set
    set1.symmetric_difference(set2)  # in first set or second set but not both
    set3 = {"nik", "rita", "murtle"}
    set3.issubset(set1)  # checks if a set is a subset of another - this will return true


def exceptionManagement(xx):  # demonstrates exception when you pass a non integer or non number string
    """this is an example of working with exceptions"""
    try:
        x = int(xx)  #  but a better way is to handle this upfront by checking the type. Only use exceptions for exceptional things
        return x
    except ValueError:  # you can see the type of error in the failed call stack. Always have an exception class named
        print("conversion failed")
        return -1
    finally:
        print("Any clean up can be performed here - e.g. clearing resources")

#  All Exceptions inherit from Exception Class. To see list, use subclasses magic: "Exception.__subclasses__()"



def shortHandCollections():
    # this is using comprehensions where you can perform some action on each item in a collection and create a new collection
    words = "this is a long sentance to show you what you can do".split()  # puts words in a list
    lenWords = [len(word) for word in words]  # this will create a new list lenWords with the length of each word in words
                                            # written like this: [functiononitem for item in items]
                                            # can do same with sets using curly braces
                                            # and dictionaries: d = {i: i * 2 for i in range(10)}
    print(lenWords)
    countryToCapital = {'UK': 'London', 'Brazil': 'Brasila', 'Spain': 'Madrid', 'Germany': 'Berlin'}
    capitalToCountry = {capital: country for country, capital in countryToCapital.items()}  # makes a new dictionary where the key is the opposite of the other
    return capitalToCountry


def generatorFunction():
    # generator functions - python iterable
    yield 1
    yield 2
    yield 3



class Person():  #  some stuff on collections
    def __init__(self, name, age):
        self._name = name
        self._age = age


class GroupPeops():  #  creating a collection of people. We can create an iterable to loop through, can instantiate the group, add some people to it and for loop through it by either a for loop or next(i)
    def __init__(self, people):
        self._listPeops = people
        self.index = len(self._listPeops)
        self._counter = 0
    
    def __iter__(self):  #  need to implement the __iter__ method
        return self._listPeops
    
    def __next__(self):  #  need to implement the __next__ method to get the next value in the sequence or raise an exception when done
        if self.index == 0:
            raise StopIteration  #  stop the iteration before it errors - i.e. when none left
        else:
            self.index = self.index - 1
            return self._listPeops[self.index]._name

    def __contains__(self, pers):  #  implement contains magic to allow checks for values to occur in new collection: "if 'Nik' in l"
        return any(x for x in self._listPeops if x._name == pers)

    def __len__(self):  #  implement the len magic to be able to return the length of the collection object
        return len(self._listPeops)

    def __getitem__(self, posi):
        return self._listPeops[posi]

    def __eq__(self, group2):
        return self._listPeops == group2._listPeops

# can also override all of the comparison (e.g. __eq__, __lt__, etc) /string (e.g. __str__, __repr__) magics inherited from the Object class (check help(object) )

def main():
    x = Person("Nik", 40)
    y = Person("Nil", 40)
    z = Person("Viaan", 4)
    a = Person("Nyal", 3)
    r = Person("Nik", 40)
    l = GroupPeops([x, y, z, a, r])

    if "Nik" in l:  #  this will call the containts to check if he's in there
        print("In there")

    print(next(l))  #  this will allow the ability to iterate through the collection using the next magic

    print(len(l))  #  this will check the length of the new collection object

    print(l[2])  #  this will call the getitem magic to fetch the item at that point

    k = GroupPeops([x, y, z, a, r])  #  duplicate list for equality checks
    print(l == k)  #  override the equality operator (and this can be extended to the other lt/gt/etc magics) This compares the 2 collections and since the contents are the same, returns true


if __name__ == "__main__":
    main()

#  to convert a list into an iterable, pass "iter(l)" and then can use "next(l)" to get the next value

#  filter is a function that can be used on a list to create a new filtered iterable by passing each item into a function. e.g. "x = filter(isOdd, [1, 2, 3, 4, 5, 6]". can then iterate through it "next(x)"
def isOdd(y):
    if y % 2 == 0:
        return True
    else:
        return False

#  could also accomplish the same using inline functions lambda
#  "y = filter(lambda a : a % 2 == 0, x)"..."next(y)"


def useGenerator():
    """generator"""
    g = generatorFunction()
    print(next(g))  # allows you to iterate over each yield in generator function
    print(next(g))
    print(next(g))


class Phone:  # class definition
    """example of a class definition"""
    # _phoneNumber = 12345  this has been commented out as this would create an attribute shared by all instances which isn't correct. to refer to it, call Phone._phoneNumber (i.e. class name)

    def callSomeone(self, phoneNumber):  # methods are defined like functions but first parameter is self(i.e. the object) but not passed. Initialise: ip = Phone. call: ip.callSomeone(123)
        self._phoneNumber = phoneNumber  # self references the object instance
        print("calling " + str(self._phoneNumber))

    def __init__(self, emergencyNumber, phoneCase):  # there are no constructors in python. Just initialisers which execute first for any new object after the object is created
        self._phoneNumber = emergencyNumber  # any attributes for the object should be defined in the init since this brings them into being (they will be globally available as against self)
        print("just been initialised with number: " + str(self._phoneNumber))  # use _attributeName to avoid clashes with methods and indicate this shouldnt be directly accessed
        self.__pinCode = 1234  # _ in front of attribute does not prevent others from accessing it. To do this add double __ and use getters/setters
        self._phoneCase = phoneCase  # but even this doesnt prevent someone accessing it by: object._class__attribute, e.g. ip._Phone__pinCode (so encapsulation is trusted)

    def setPin(self, val):  # setter method to change private pin
        self.__pinCode = val

    def getPin(self):  # getter method to return private pin
        return self.__pinCode


class PhoneCase:  # this is another class, and is used in the phone class above (see the initialiser). Called like this: ip=Niktest.Phone(999, Niktest.PhoneCase(screenCover=False))
    def __init__(self, material="plastic", screenCover=True):  # now clients of phone dont need to know about phonecase class
        self._material = material
        self._screenCover = screenCover


class IPhone7(Phone):  # inheritence from a base class
    def __init__(self):  # this is a form of method overriding and will overide the initialiser in the base class so to keep it, call it using super()
        super().__init__(999, PhoneCase())  # call parent class methods using super
        print("iPhone7")


class SamsungGalaxy(Phone):  # now that we have 2 types of the Phone class, we can show polymorphism by creating both phone types and putting them in a list of phones:
    def __init__(self):  # ip = iPhone7()... ss = samsungGalaxy()...   phoneList = [ip, ss]...  for phone in phoneList: print(phone.getPin())
        super().__init__(999, PhoneCase())  # parent method still works as both ip and ss are phones. Using Super we can call the init of base class and extend it here
        print("samsung galaxy")

#  multiple inheritence will be a comma-separated base class list "class subclass(baseclass1, baseclass2)"
#  if a subclass has multiple base classes, only the init of the first base class is called
#  if the same method exists in 2 or more bases, which one is called? determined by MRO (method resolution order) to determine where the method exists - starting from first to last class in definition and then their respecitve base classes)
#  can see the order of looking for the method by executing subclass.__mro__. everything inherits from object

def fileIOExamples():
    """This is examples of using resources"""
    openFile = open("input.json", "r")  # opens a file, this is a base library already available
    print(openFile.read())  # reads from the file
    openFile.close()

    openFile = open("input.json,", "w")  # writes to the file (but doesnt retain content - use append for that)
    openFile.write("hello")
    openFile.close()  # must close the file once done

    openFile = open("input.json", "r")  # file object support iteration so can use for loops to go through lines
    for line in openFile:
        print(line)
    openFile.close()  # if there is an error on the file printline, then it will leave the stream open. to prevent this you can use Try: open...  Finally: close() but this is verbose

    with open("input.json", "r") as openFile:  # use with blocks to make it easier to pair opens with close and will clean up resources
        print(openFile.read())


def showingTypeHints(a: int, b: int, c: str) -> int:
    """since python is a dynamically typed language, it doesn't catch type 
    errors until runtime, unlike C#/JAVA that will catch these errors at compile time so add type hints for variables, parameters and return types to help, but they will be ignored by python"""
    print(c)
    return(a+b)
    #can also do collections - like lists: list1[int]


def callHints():
    """hover over this to see typehints"""
    showingTypeHints(1.8, "fgg", 3)


#  unit testing modules
#  test_module name
import unittest  #import the unit test modules


class Person():
    def __init__(self, name: str, age: int):
        self._myName = name
        self._myAge = age
        self._dictNames = {"Rita": 38, "Nil": 40, "Surina": 41}
        self._dictNames.update({self._myName: self._myAge})

    def returnName(self) -> str:
        return self._myName
        
    def lookupName(self, a: str):
        if a in self._dictNames.keys():
            return True
        else:
            return False
        

class test_Person(unittest.TestCase):  #  create test classes that inherit from unittest
    def setUp(self) -> None:           #  set up any required resources so dont need to have these in each test - this runs before each test (see below commented out) 
        self.person1 = Person("Nik", 40)

    def test_returnName(self):
        #  person1 = Person("Nik", 40)  #  not needed due to setup
        self.assertEqual("Nik", self.person1.returnName())  #Assertions will be available for testing
    
#can return this one test quickly in commandline with a testrunner, but really it should be separated into its own module: "python3 -m unittest -v Niktest.test_Person" will run the tests and report them
    def test_findInDictionary(self):
        #  person1 = Person("Nik", 40)  #  not needed due to setup
        self.assertFalse(self.person1.lookupName("Bob"))  #here we have a true/false check
    
    @unittest.skip("Not yet coded")  #this is an annotation to skip a test and it will not run
    def test_ignoreThisTest(self):
        pass

    def tearDown(self) -> None:  #  executed once after each test - can be used to release resources. It will always be run - even if the test fails
        pass


import pytest  #  when running tests, can also import pytest-html. Then create an interactive test report: "python3 -m pytest Niktest.py --html=report.html" "open report.html"

def test_with_pytest(personSetup):  #  a less verbose way is to use pytest testrunner. Import this and then dont need to create a class to inherit from unittest, etc. To run, "python3 -m pytest Niktest.py"
    #  person1 = Person("Nik", 40)
    assert "Nik" == personSetup.returnName()  #  this will give good information about failing tests using the test runner

@pytest.fixture  #  create the setup before each test using annotations for fixture and then inject the object into the test class (as you can see the first line is commented out above)
def personSetup() -> Person:
    person1 = Person("Nikh", 40)
    return person1


#  last part of testing is using doctest which uses doc strings to help validate and document code with the expected result. Run by: "python3 -m doctest Niktest.py -v"
from random import choice

class RollDice():
    """Creates a dice object and returns the number between 1-6 randomly
    >>> a = RollDice()
    >>> a.roll() in ["1", "2", "3", "4", "5", "6"]
    True
    """
    def __init__(self):
        self._roll = 0
        self._numbers = [1, 2, 3, 4, 5, 6]

    def roll(self) -> str:
        self._roll = choice(self._numbers)
        return str(self._roll)


#test doubles - mocks, stubs, fakes. Dependency injection is important here as you are passing in a fake object for the dependency
import unittest

def getHobbies():  #  explicit dependency so refactor to DI and pass a mock for testing
    inputFile = open("input.json", "r")
    obj = json.load(inputFile)
    hobbyList = obj["Hobbies"]
    inputFile.close()
    return hobbyList


def returnAHobby():
    hobbyList = getHobbies()  #  this is now tightly coupled with the getHobbies function so it can't be unit-tested
    for hobby in _hobbyList:
        hobby = hobby + ";"
    return hobby


def returnAHobby2(hobbyList = None):  #  rewriting injecting a dependency in is a better way of having loose coupling and enabling easy unit testing by 
    _hobbyList = hobbyList or getHobbies()  #  passing in a test-double: returnHobby2(["Eating Pizza!","Python"]). By making it an optional argument, it won't break anything for others
    hobbyStr = ""
    for hobby in _hobbyList:
        hobbyStr += hobby + ";"
    return hobbyStr


class test_Hobby(unittest.TestCase):  #  create test classes that inherit from unittest. Run with "python3 -m unittest -v dt1.py"
    def setUp(self) -> None:           #  set up any required resources so dont need to have these in each test - this runs before each test (see below commented out) 
        self._hobbyList = ["Eating Pizza!", "Python"]

    def test_returnHobby2(self):
        self.assertEqual("Eating Pizza!;Python;", returnAHobby2(self._hobbyList))  #Assertions will be available for testing
    


