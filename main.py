# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re
import time, os
def callFunction(a):
    prev=""
    output=""
    for s in a:
        curr=s
        if(curr==prev):
            pass
        else:
            output=output+s
            prev=curr
    return output

path = "myfile.txt"
os.path.getctime(path)

time.ctime()

time.strptime()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = "thisissttringg"
    output = callFunction(a)
    print(output + "  " +a)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
