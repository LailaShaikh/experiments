class Node(object):
    def __init__(self, _ele, _next):
        self.val = _ele
        self.next = _next
    

class LinkedStack(object):
    def __init__(self):
        self.stack = None
        self.size = 0

    def push(self, val):
        self.stack = Node(val, self.stack)
        self.size += 1
        
    def pop(self):
        if not self.is_empty():
            self.stack = self.stack.next
            self.size -= 1
        else:
            print "stack is empty dude!"
    
    def print_stack(self):
        tmp_stack = self.stack
        while tmp_stack is not None:
            print "%s --->" % tmp_stack.val,
            tmp_stack = tmp_stack.next
        print "NULL"

    def is_empty(self):
        return True if self.stack is None else False


if __name__ == '__main__':
    print "Initial stack"
    ls = LinkedStack()
    print "Pushing 5"
    ls.push(5)
    print "Pushing 10"
    ls.push(10)
    print "Pushing 6"
    ls.push(6)
    print "Pushing 15"
    ls.push(15)
    print "Pushing 9"
    ls.push(9)

    ls.print_stack()
   
    print "popping"
    ls.pop()

    ls.print_stack()

    print "popping"
    ls.pop()

    ls.print_stack()

    print "popping"
    ls.pop()

    ls.print_stack()

    print "popping"
    ls.pop()

    ls.print_stack()

    print "popping"
    ls.pop()

    ls.print_stack()

    print "popping"
    ls.pop()

    ls.print_stack()
