def pad1(n):
    if n == 1:
        res1 = '#\n'
    else:
        res1 = pad1(n-1) + '#'*n + '\n'
    return res1
def pad2(n):
    if n == 1:
        print('#')
    else:
        for i in range(n):
            if i == 0:
                print(' '*n, '#')
            elif i == 1:
                print(' '*(n-i), '# #')
            else:
                print(' ' * (n - i), '#', ' ' * (1 + 2 * (i - 1)-2), '#')
        for i in range(n-2,-1,-1):
            if i == 0:
                print(' '*n, '#')
            elif i == 1:
                print(' '*(n-i), '# #')
            else:
                print(' '*(n-i), '#', ' '*(1+2*(i-1)-2), '#')
def pad3(n):
    for k in range (n):
        if k == 0:
            for i in range(n):
                print(' '*5 + '_ ', end= '')
            print('\n   ', end = '')
            for i in range(n):
                print('_( )__' + ' ',end = '')
                if i == n-1:
                    print('')
            for i in range (n+1):
                print(' ' + '_|' + ' '*4, end = '')
                if i == n:
                    print('')
            print('(_' + ' '*3, end = '')
            for i in range(n):
                print('_ ' + '(_ ', end = '  ')
                if i == n-1:
                    print('')
            print(' |', end = '')
            for i in range(n):
                print('__( )_', end= '|')
                if i == n-1:
                    print('')
        elif k % 2 != 0:
            for i in range(n):
                if i == 0:
                    print(' |_', end = '')
                print('     |_', end = '')
                if i == n -1:
                    print('')
            for i in range(n):
                if i == 0:
                    print('  _)', end = '')
                print(' _   _)', end = '')
                if i == n-1:
                    print('')
            for i in range (n):
                if i ==0:
                    print(' |', end = '')
                print('__( )_|', end='')
                if i == n-1:
                    print('')
        elif k % 2 == 0:
            for i in range (n+1):
                print(' ' + '_|' + ' '*4, end = '')
                if i == n:
                    print('')
            print('(_' + ' '*3, end = '')
            for i in range(n):
                print('_ ' + '(_ ', end = '  ')
                if i == n-1:
                    print('')
            print(' |', end = '')
            for i in range(n):
                print('__( )_', end= '|')
                if i == n-1:
                    print('')
n = int(input())
print(pad1(n))
pad2(n)
pad3(n)