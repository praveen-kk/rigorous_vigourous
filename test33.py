from collections import Counter

def stockmerchant(n, ar):

    n = int(input())
    c = Counter(map(int, input().split()))
    ans = 0
    for x in c:
        ans += c[x] // 2
    print(ans)


ar = ['10', '20', '20', '10', '10', '30', '50', '10', '20']
n = '9'
print(stockmerchant(n, ar))
