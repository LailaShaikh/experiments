class MyClass(object):
    good_attr = None
    better_attr = None
    best_attr = None

   # __slots__ = ['good_attr','better_attr']

   
    def __setattr__(self, attr_name, attr_value):
        if not hasattr(self, attr_name):
            raise AttributeError('{} instance has no attribute {!r}'.format(type(self).__name__,attr_name))
            
        super(MyClass, self).__setattr__(attr_name, attr_value)
   

if __name__ == '__main__':
    obj = MyClass()
    #change value of existing attr
    obj.good_attr = "I am good string!"
    print obj.good_attr
    #create new attrbuite which is not existing
    obj.bad_attr = "I am a bad boy"
    print obj.bad_attr


#example 

"""

In [17]: obj = MyClass()

In [18]: obj.
obj.best_attr    obj.better_attr  obj.good_attr    

In [18]: obj.best_attr

In [19]: obj.best_attr = "Super man"

In [20]: obj.best_attr
Out[20]: 'Super man'

In [21]: obj.bad_boy = "Bane"
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-21-73ee407c6091> in <module>()
----> 1 obj.bad_boy = "Bane"

/home/rlx-l004/nava-dropbox/Dropbox/work/experiments/python/setattr.py in __setattr__(self, attr_name, attr_value)
      6     def __setattr__(self, attr_name, attr_value):
      7         if not hasattr(self, attr_name):
----> 8             raise AttributeError('{} instance has no attribute {!r}'.format(type(self).__name__,attr_name))
      9 
     10         super(MyClass, self).__setattr__(attr_name, attr_value)

AttributeError: MyClass instance has no attribute 'bad_boy'

In [22]: obj.__dict__
Out[22]: {'best_attr': 'Super man'}

In [23]: obj.__dict__['bad_boy'] = "bane"

In [24]: obj.bad_boy
Out[24]: 'bane'

if you add __slots__ as class variable there is no more __dict__

"""
