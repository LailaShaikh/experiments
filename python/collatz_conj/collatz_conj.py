"""
Soln steps:
1.Take list of integers as input from user
2.Apply the collatz conjucture formula to count cycle length for each element in list
3.Findout the maximum cycle length element
4.Do it in parallel processing
5.Return the result
6.write unittest cases

"""

from gevent import socket
from gevent.server import StreamServer

def echo(socket, address):
    print('New connection from %s:%s' % address)
    while True:
        line  = socket.recv(1024)
        if line == 'quit':
            break
       
        if len(line.strip()): 
            il = [int(i) for i in line.strip().split(',') if i != ' ']
            print il
            #max seq result
            res = max(map(find_collatz_cycle_len, il))
            print "The maximum cycle length is : %s" %res
            socket.sendall("The maximum cycle length is : %s" %res)
        

def find_collatz_cycle_len(elem):
    #Assumptions:
    # TODO: The cycle count will not proceed for negative numbers and number 1
    #To optimize the m/y issue instead of stack we can use count variable

    stack = []
    #count  = 1
    def transition(e):
        while e > 1:
            if e % 2 == 0:
                e /= 2
            else:
                e = (3 * e) + 1
            yield e
    
    for i in transition(elem):
        #count += 1
        stack.append(i)
    return len(stack) + 1 #including the last transition to 1
    #return count



def start_work():
    #1.Get input

    il = raw_input("Enter the integers and space as delimiter like --> 1 2 3 4: ")
    il = [int(i) for i in il.split(' ') if i != ' ']
    
    #max seq result
    print max(map(find_collatz_cycle_len, il))


def start_server():
    server = StreamServer(('0.0.0.0', 6000), echo)
    print('Starting echo server on port 6000')
    server.serve_forever()
   

if __name__ == '__main__':
    start_server()
    #start_work()
