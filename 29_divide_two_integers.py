def divide(self, dividend: int, divisor: int):
    if not dividend:
        return 0
    sign = (1 if (dividend > 0 and divisor > 0 
        or dividend < 0 and divisor < 0) else
        -1)
    dividend, divisor = abs(dividend), abs(divisor)
    if dividend < divisor:
        return 0
    ans, dig = 0, 31
    while dig >= 0:
        if dividend >= divisor << dig:
            dividend -= divisor << dig
            ans += 1 << dig
        dig -= 1
    return sign*ans if -2**31 <= sign*ans <= 2**31-1 else 2**31-1