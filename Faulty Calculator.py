num_1 = int(input('Enter 1st Number'))
num_2 = int(input('Enter 2nd Number'))
operation = input('Enter Type of operation for example- (*),(/),(+),(-)')

if num_1==45 and num_2 ==3 and operation =="*":
    print(555)
elif num_1==56 and num_2 == 9 and operation =="+":
    print(77)
elif num_1 ==56 and num_2 ==6 and operation =="/":
    print(4)
else:
    if operation =="*":
        print(num_1*num_2)
    elif operation =="+":
        print(num_1+num_2)
    elif operation =="/":
        print(num_1/num_2)
    else:
        print(num_1-num_2)