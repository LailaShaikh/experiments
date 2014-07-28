def class_decorator(func):
    def inner(instance): #'self' parameter implicitly passed
        if instance.person_name == 'nava':
            print "He is a handsome guy..why do you want to know his citizen type?"
        else:
            func(instance)
    return inner
    



class Person(object):
    def __init__(self, name, age):
        self.person_name = name
        self.age = age
        
    #@class_decorator
    def find_citizen_type(self):
        if self.age > 18:
            print "%s is citizen" %(self.person_name)
        elif self.age < 18:
            print "%s may be an adult" %(self.person_name)



#output

'''
In [1]: from class_decorator import Person, class_decorator

In [2]: p = Person('nava',20)

In [3]: p.find_citizen_type()
nava is citizen

In [4]: Person.find_citizen_type = class_decorator(Person.find_citizen_type)

In [5]: p.find_citizen_type()
He is a handsome guy..why do you want to know his citizen type?

'''
