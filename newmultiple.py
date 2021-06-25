def numberlinejump(x1,v1,x2,v2):
    # 1 act, two kangaroos
    if v2 == v1 and x2 != x1:
        return ('NO')
    elif x1 == x2 and v2 != v1:
        return ('NO')
    elif x2 > x1 and v2 > v1:
        return ('NO')
    elif x1 > x2 and v1 > v2:
        return ('NO')
    if (x1 - x2) % (v2 - v1) == 0:
        return 'YES'
    else:
        return 'NO'
    # elif x1+v1>x2+v2 and v1>v2:
    #     return 'NO'
    # elif x2+v2>x1+v1 and v2>v1:
    #     return 'NO'
    # else:
    #     return('YES')
    # for i in range(10000):
    #     if x1+v1==x2+v2:
    #         return 'YES'
    #     x1+=v1
    #     x2+=v2
    # return 'NO'