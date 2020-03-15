import json

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


class simpleContextManager:  #  this is a simple example of creating a context manager
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

if __name__ == "__main__":
    callContectManager()


