print('\t\t\tThe Cocacola Company \n\t\t\t\tWelcome')
i=0
while 1:
    print('\nMenu: \n1. Material Stock Checker\n2. Order Checker\n3. Production Line Performance\n4. Production Line Error Calculator\n5. Exit')
    x=int(input('Please Enter an Option:'))
    if x==1:
        a=input('\nEnter Day: ')
        b=int(input('Enter number of plastic body in stock: '))
        c=int(input('Enter number of caps in stock: '))
        d=int(input('Enter number of cap string in stock: '))
        e=int(input('Enter number of plastic wrapper in stock: '))
        print('On ' + str(a) + ', ' + str(b) + '000 plastic body, ' + str(c) + '000 caps, ' + str(d) + '000 cap string, ' + str(e) + '000 plastic wrappers were on stock.')
    elif x == 2:
        or_b = int(input('\nEnter ordering threshold for plastic body: '))
        or_c = int(input('Enter ordering threshold for caps: '))
        or_d = int(input('Enter ordering threshold for cap string: '))
        or_e = int(input('Enter ordering threshold for plastic wrapper: '))
        if b <= or_b:
            oram_b = or_b - b
            print('\nNumber of plastic bodies to be ordered: ' + str(oram_b))
        else:
            print('Number of plastic bodies to be ordered: 0 ')
        if c <= or_c:
            oram_c = or_c - c
            print('Number of caps to be ordered: ' + str(oram_c))
        else:
            print('Number of caps to be ordered: 0 ')
        if d <= or_d:
            oram_d = or_d - d
            print('Number of cap strings to be ordered: ' + str(oram_d))
        else:
            print('Number of cap strings to be ordered: 0 ')
        if e <= or_e:
            oram_e = or_e - e
            print('Number of plastic wrapper to be ordered: ' + str(oram_e))
        else:
            print('Number of plastic wrapper to be ordered: 0 ')
    elif x==3:
        j=int(input('Enter number of machines active last week: '))
        from array import *
        machine = array('i',[])
        for y in range(j):
            pr=[int(i) for i in input('Enter day-wise production rate for machine '+str(y+1)+': ')]
i+=1