time= int(input('별 몇개 쌓을까?'))

for i in range(1,time+1):
    print(' '*(time-i),'*'*(2*i-1))
