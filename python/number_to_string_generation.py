#Interview problem
#Convert the given number to string
#  like 1234 - One Thousand Two hundred and thirty four
# 234567 - 

#Constants
pos = {4: 'Thousand', 6: 'Lakhs', 3: 'Hundred', 8:'Crore'}

fpos = {'1': 'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', \
        '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine', '0':' '}

spos = {'2': 'Twenty', '3':'Thirty', '4':'Foury','5':'Fifty','6':'Sixty','7':'Seventy','8':'Eighty','9':'Ninty','1':'Ten', '0':' '}

two_digit_pos = {11:'Elevan',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Ninteen'}

s_bits = (2,5,7,9 )


def get_pair_digit_str(n1, n2):
    print "n1=",n1, "n2=",n2
    out = two_digit_pos[n2 * 10 + n1] if n2 == 1 else \
                  spos[str(n2)] + fpos[str(n1)]
    return out

def convert_to_str(num):
    #2,12,11,212
    r = list(str(num))
    out_s = ''
    r.reverse()
    l=[]
    for idx, num in enumerate(r):
        idx += 1
        l.append(num)
        if idx in s_bits:
            n2, n1 = l[-1], l[-2]
            ts = ' And ' + get_pair_digit_str(n1, n2) if idx == 2 else get_pair_digit_str(0, n2)
            out_s = ts +" "+ out_s
        elif pos.has_key(idx):
            out_s = fpos[num]+" "+pos[idx] + out_s
        print out_s

   
if __name__ == '__main__':
    ino = input("Enter the no:")
    #print get_pair_digit_str(1,2)
    #print get_pair_digit_str(4,2)
    #print get_pair_digit_str(1,9)
    #print get_pair_digit_str(2,7)
    convert_to_str(ino)
