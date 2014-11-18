import sys


def mycallback(frame, event, arg):
    print "event is %s" %event
    print "args are %s" %arg
    print "current exe line filename: %s" %frame.f_code.co_name
    print "current execution line: %s" %frame.f_lineno
    print "caller line no: %s" %frame.f_back.f_lineno
    print "caller file name: %s" %frame.f_back.f_code.co_name

    return mycallback 

def function(arg1, arg2):
    print "Input: ",arg1, arg2
    return arg1 + arg2

sys.settrace(mycallback)
print function(4,5)
sys.settrace(None)
