def digit_root(num):
    if isinstance(num, int) and num > 0 and num <= 10**7:
        while num >= 10:
            num = sum(int(digit) for digit in str(num))
        return num