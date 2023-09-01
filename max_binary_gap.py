# A=[-1, -2, 7, 5, 4, 3, 3, 3, 2]
def sol(a):
    binary=bin(a)[2:]
    print(binary)
    gapcount_length=[]
    gap_count=0
    for i in binary:
        if i=='0':
            gap_count+=1
        if i=='1' and gap_count>0:
            gapcount_length.append(gap_count)
            gap_count=0
    print(gapcount_length)
    if gapcount_length:
        return max(gapcount_length)
    else:
        return 0


print(sol(9687685645645324687983487743634635474859549558776673636326737478498987888888888888888888888888888888888888886666666666666654444444477777777777777777777777777777888888888888888888888888888888888888999999999999999999999999999944444444444333333333333333333333333))


