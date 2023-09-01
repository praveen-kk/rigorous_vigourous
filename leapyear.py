def solution(y):
    if y%4==0:
        if y%100==0:
            if y%400==0:
                return "true"
    return "false"

print(solution(2400))

print ("""
tests
sfasfaf
""")

