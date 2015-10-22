class Node(object):
    def __init__(self, _ele, _next):
        self.val = _ele
        self.next = _next
    

class LinkedQueue(object):
    def __init__(self):
        self.qhead = None
        self.qtail = None
        self.size = 0

    def enqueue(self, val):
        curr_node = Node(val, None)
        if not self.is_empty():
            self.qtail.next = curr_node
        else:
            self.qhead = curr_node
        self.qtail = curr_node

    def dequeue(self):
        if not self.is_empty():
            if self.qhead == self.qtail:
                self.qtail = self.qhead.next
            self.qhead = self.qhead.next
       
        else:
            print "queue is empty dude!"
            raise BaseException('Empty :(')

    def print_q(self):
        tmp_q = self.qhead
        #print tmp_q
        while tmp_q is not None:
            print "%s --->" % tmp_q.val,
            tmp_q = tmp_q.next
        print "NULL"

    def is_empty(self):
        #print self.qhead, self.qtail
        return True if self.qhead is None and self.qtail is None  else False


if __name__ == '__main__':
    print "Initial Q"
    lq = LinkedQueue()
    print "Enquing 5"
    lq.enqueue(5)
    print "Enquing 10"
    lq.enqueue(10)
    print "Enquing 6"
    lq.enqueue(6)
    print "Enquing 15"
    lq.enqueue(15)
    print "Enquing 9"
    lq.enqueue(9)

    lq.print_q()
   
    print "Dequing"
    lq.dequeue()

    lq.print_q()

    print "Dequing"
    lq.dequeue()

    lq.print_q()

    print "popping"
    lq.dequeue()

    lq.print_q()

    print "popping"
    lq.dequeue()

    lq.print_q()

    print "popping"
    lq.dequeue()

    lq.print_q()

    print "popping"
    lq.dequeue()
    lq.print_q()
