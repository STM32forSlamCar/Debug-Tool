

class DataBase(object):
    """robot database: cmdMsg  feedbackMsg"""
    __instance = None
    __isFirstInit = False

    def __new__(cls):
        if not cls.__instance:
            DataBase.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not self.__isFirstInit:
            self.cmdMsg = []
            self.feedbackMsg = []
            self.__isFirstInit = True
        else:
            pass

# test this class
def test():
    db1 = DataBase()
    db1.cmdMsg = [1.0, 30]
    db1.feedbackMsg = [1.1, 34]

    print("db1->cmdMSg:",db1.cmdMsg)
    print("db1->feedbackMSg:",db1.feedbackMsg)

    db2 = DataBase()
    print("db2->cmdMSg:",db2.cmdMsg)
    print("db2->feedbackMSg:",db2.feedbackMsg)
    
# test()