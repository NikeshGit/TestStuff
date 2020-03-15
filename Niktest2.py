#  save a file module.py - this is a module which can be imported
#  a group of modules is a package. This is a directory and can be imported in the same way. The only requirement is that the folder has a file in it called "__init__.py" - can be empty or execute something
#  python loads the modules, first from sys.path, and continues through this until it loads the file. To see this, in repl do "import sys" and "sys.path"
#  if you write something and try to import, it won't load unless you are in the directory or you append the path to sys.path: "sys.path.append("/Users/Nik/PYModules")"
#  if you execute a directory "python3 PYModules", then python complains that no "__Main__.py" file exists. If you create this as a new file, this will execute the code in this file. So this can be entry point to your app



#  callable objects
#  so functions, methods and classes (by the init method) are callable - you run functionName() to call it
#  class instances (the object initialised) can also be made callable using the __call__ 


class Resolver:

    def __init__(self):
        self._cache = ()

    def __call__(self):  #  this will allow the instance to be executed like a function and be callable: "x = Niktest2.Resolver()"... "x()"
        return "This is called for the instance like a function"


#  conditional expressions make if/else nicer. value if condition else othervalue
def conditionalExp(x):
    return "value" if x == True else "no value"


#  anonymous functions - lambda functions
def lambExp():
    lstNames = ["Nik","Nil","Sur","Rit","Ran","Mah","Via","Nya","Mur"]
    return sorted(lstNames, key=lambda name: name[-1])  #  the second part accepts a function to define how to sort - in this case, by the last letter


#  variable list of arguments using *args  "returnArgs("a","s","g","t",1,5)"
def returnArgs(*args):
    print(args)
    for i in args:
        print(i)


#  can also pass variable arguments as keyword arguments which breaks it down into key value pairs "Niktest2.returnKWArgs(name="Nik", age=40, hobby="python!")"
def returnKWArgs(**kwargs):
    print(kwargs)
    for i in kwargs:
        print(i)

#  when you are doing things in the REPL, you may want to reload the module if changes have been made. Do this by "import importlib"... importlib.reload(module)

#  inner/local functions - functions can be nested and used within the scope of the outer function. Rememeber that def just defines it
def sortey(strings): #  call this outer function with a list of strings (sortey(["hello","nikesh","you","animal"]))
     def lastl(s):  #  for each string it will return the last letter and use that in the key, but wont execute until called by the key - so similar to inline lambda
             return s[-1]
     return sorted(strings, key=lastl)

#  a function can also return another function. If defined in its scope, it can return it to a variable. This won't execute it until you call the variable.
#  so on below example, calling function x will define and return y into a variable. if we then call y, only then will it execute it

def x(a):  #  closures. These are useful when using function factories - generating functions. Local functions can be returned list other variables
     def y(b): # the inner function won't execute until you create an object for x and pass in the parameter for the inner. The inner will hold onto the variables needed and closes over it to keep it alive  - closure
             print(a + b)
     return y  
#  e.g. run "a = x("Hello")" which will return the inner function ... "a(" Nikesh")"  which will execute it holding onto the outer parameter... "a(" Nilesh")"   the first parameter will be held until the inner is called so can execute multiple times with different inner parameter
#  since its a function factory, we can then call the outer again and create another function e.g. "b = x("Bye")" ... b(" Nikesh"). The factory has created a hello function taking parameters and a goodbye one


#  decorators - a way to modify/extend an existing function without changing it. Take a function as an argument and return one. can be done on all callable objects - classes/methods
#  @my_decorator is added to decorate a function which will pass the function object tagged to the decorator function. 
#  The decorator function can then do some additional stuff and then returns it back and binds it to the original function

def morning():
    return("dias")

def evening():
    return("noches")

def afternoon():
    return("tardes")

#  now say if all 3 needed to be updated to put buenos in front of them... this could be disruptive to existing users of functions and require changes in multiple places so
#  we can just add a decorator and tag each function to call it - useful for logging extensions, etc

def buenos_decorator(f):  #  name of decorator taking function as input
    def wrap(*args, **kwargs):  #  new inner function taking variable arguments passed
        x = f(*args, **kwargs)  #  call original function with those args passed
        return "buenos " + x  #  make any updates/extensions
    return wrap  #  return the wrapper function

@buenos_decorator
def morning2():
    return("dias")

@buenos_decorator
def evening2():
    return("noches")

@buenos_decorator
def afternoon2():
    return("tardes")


#  decorators can be used to flag @staticmethod or @classmethod (a method at the class level) - both are similar with small differences and use class when in doubt
class ShippingContainer:
    next_serial = 1000  #  this is a class attribute

    def __init__(self, ownercode, contents):  #  this initialises a new instance with its own instance variables
        self._ownercode = ownercode
        self._contents = contents
        self._serial = ShippingContainer._get_next_serial()  #can call class methods or variables using the classname. format
        self._elephant = "Bob"

    @classmethod  #  this is a decorator to flag that this is a method to implement the static class method which works on the class attribute. We could have used a @staticmethod too if this wasnt associated with the class
    def _get_next_serial(cls):  #  _ at start indicates that this is an internal implementation
        result = cls.next_serial  #  instead of self, pass cls
        cls.next_serial += 1
        return result

    #  encapsulation on attributes can be accomplished with getters and setters using decorators (both will have the name of the attribute)
    #  property() is a built-in function that creates and returns a property object. The signature of this function is: property(fget=None, fset=None, fdel=None, doc=None)
    #  where, fget is function to get value of the attribute, fset is function to set value of the attribute, fdel is function to delete the attribute and doc is a string (like a comment)

    @property  #  getter is flagged by @property decorator. This method can now be called like an attribute: "x.elephant"
    def elephant(self):
        return self._elephant

    @elephant.setter  #  setter is flagged by @attribute.setter. This method can now be called like an attribute: "x.elephant = "Dumbo"" (not "x.elephant("Dumbo")"
    def elephant(self, value):
        if type(value) == str:   #  now we can apply logic to the setter - i.e. is it a string
            self._elephant = value
        else:
            self._elephant = "Nelly"

    def __str__(self):  #  overridding the str magic will allow this to be printed either by: "str(x)" or "print(x)" for a client
        return f"{str(self._ownercode)}, {str(self._contents)}"

    def __repr__(self):  #  overriding the repr magic will allow this to be printed by: "repr(x)". This should be a representation of the object creation for a developer
        return f"ShippingContainer(ownercode={self._ownercode},contents={self._contents})"

    #  import Decimal module to help with financing calcs else it will not round calculations correctly
    #  import datetime module for dates. e.g. datetime.date.today() will give todays date



def readFi():  #  the way to use resources is to open the resource, do something with it and then close it
    inputFile = open("input.json", "r")  #  open resource (enter)
    obj = json.load(inputFile)  #  do something (code block)
    hobbyList = obj["Hobbies"]  
    inputFile.close()  #  close it (exit)
    print(hobbyList)

    #  but this is better accomplished by using context managers - i.e. using with which does all of this
    with open("input.json", "r") as f:
        obj = json.load(f)
    hobbyList = obj["Hobbies"]
    print(hobbyList)

    #context managers can be defined as new classes as required and implement the __enter__ and __exit__ magics


class simpleContextManager:  #  this is a simple example of creating a context manager. an example of a use case is a database connection to commit transactions
    def __enter__(self):
        print("simpleContextManager.__enter__()")  #  does this first
        return("work done")  #  the return statement is given to the block and bound to the as variable

    def __exit__(self, exc_type, exc_val, exctb):
        if exc_type is None:
            print("close anything no longer needed")
        else:
            print(f"simpleContextManager.__exit__(exc_type = {exc_type}, exc_val = {exc_val}, exctb = {exctb})")  #  these exceptions will be None unless there is an error
                                                                                        #  which will set exc_type to ValueError, exc_val to "wrong!" and exctb to the traceback object
                                                                                        
def callContectManager():
    readFi()
    with simpleContextManager() as x:
      # raise ValueError("wrong!")  #  add this line to raise an error in the with block 
        print(x)

#  introspection - to inspect things
#  type(x) -> to return type information
#  dir(X) -> to return all attribute names and methods for an instance


