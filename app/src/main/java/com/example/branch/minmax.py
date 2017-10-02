import sys
min = sys.maxint
max = -sys.maxint-1
while True:
    try:
        num = raw_input("Enter a number: ")
        if num == "done":
            break
        num = int(num)
        if num > max:
            max = num
        if num < min:
            min = num
    except:
        print "Invalid input"         
print "Maximum is " + str(max)
print "Minimum is " + str(min)    

