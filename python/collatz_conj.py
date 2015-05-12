"""
Soln steps:
1.Take list of integers as input from user
2.Apply the collatz conjucture formula to count cycle length for each element in list
3.Findout the maximum cycle length element
4.Do it in parallel processing
5.Return the result
6.write unittest cases

"""


def find_collatz_cycle_len(elem):
    #Assumptions:
    # TODO: The cycle count will not proceed for negative numbers and 1
    stack = []
    def transition(e):
        while e > 1:
            if e % 2 == 0:
                e /= 2
            else:
                e = (3 * e) + 1
            yield e
    
    for i in transition(elem):
        stack.append(i)
    return len(stack) + 1 #including the last transition to 1

def start_work():
    #1.Get input
    il = raw_input("Enter the integers and space as delimiter like --> 1 2 3 4: ")
    il = [int(i) for i in il.split(' ') if i != ' ']
    
    #max seq result
    print max(map(find_collatz_cycle_len, il))
   

if __name__ == '__main__':
    start_work()
