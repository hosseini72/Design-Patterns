
# Singleton Decorator
def Singleton(cls):
    __instance = {}
    def getinstance(*args,**kwargs):
        if cls not in __instance:
            __instance[cls] = cls(*args,**kwargs)
        return __instance[cls]
    return getinstance

#Singleton Class
class Singleton_cls(type):
    __instance = None

    def __call__(self, *args, **kwds):
        if self.__instance is None:
            self.__instance= super().__call__(*args, **kwds)
        return self.__instance

