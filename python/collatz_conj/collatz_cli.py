import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 6000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    # Send data
    il = raw_input("Enter the integers and comma as delimiter like --> 1,2,3,4: ")
    print >>sys.stderr, 'sending "%s"' % il
    sock.send(il)
    expect_msg = len('The maximum cycle length is :  for  ')
    data = ''
    res = ''
    while '\n' not in data:
        data = sock.recv(16)
        res += data
    
    print "***" * 5
    print res
    print "***" * 5

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
