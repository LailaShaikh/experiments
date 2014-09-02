def check_proper_parenthesys(open_symbol, close_symbol):
    """
    This function helps to find whether the close symbol is equivalent to the open symbol or not?
    There should be some mechanism to have the open symbol and close symbol mapping either dict format like {'(':'}','[',']','{':'}'}
    or list format what was written
    """
    open_symbol_list = ['{','[','(']
    close_symbol_list = ['}',']',')']
    return open_symbol_list.index(open_symbol) == close_symbol_list.index(close_symbol)

def main(inputString):
    """
    Why do we choose stack?
          Here we have to choose only stack. Since, we have to check the parenthesis are proper or not?
          So, paranthesys order is necessary and we need to take the list of symbols from reverse order after particular incident.
 
          So, retrieving with the reverse order one and only Stack
    
    """
    s = [] #stack
    for ins in inputString:
        if ins in '{[(':
            s.append(ins)
        else:
            try:
                top_str = s.pop()
            except IndexError:
                #mismatch
                return False

            is_matching = check_proper_parenthesys(top_str, ins)
            
            if not is_matching:
                #mismatch found
                return False
        
    return True
                
                

if __name__ == '__main__':

    print main('{[()]()}')
    print main('{{([][])}()}')
    print main('[{()]')


