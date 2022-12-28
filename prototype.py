import copy


class Prototype:

    def __init__(self) -> None:
        self.objects = {}

    def register(self, name, obj):
        self.objects[name] = obj

    def unregister(self, name, obj):
        del self.objects[name]

    def clone(self, name, **kwds):
        cloned = copy.deepcopy(self.objects.get(name))
        if kwds:
            cloned.__dict__.update(kwds)
        return cloned


def make_prototype(name,obj, **kwds):
    prototype = Prototype()
    prototype.register(name, obj)
    return prototype.clone(name, **kwds)






        