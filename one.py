n = int(input())

if n == 0:
    print(1)
else:
    ans = 0
    place = 1

    while n > 0:
        digit = n % 10

        if digit == 0:
            digit = 1

        ans = ans + digit * place
        place = place * 10
        n = n // 10

    print(ans)
