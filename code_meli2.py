def func_to_help_validate_national_code(a):
    if len(a) == 10 and a.isdigit():
        control = int(a[-1])
        sum = 0
        count = 0
        for i in range(10, 1, -1):
            sum += i * int(a[count])
            count += 1
        count = sum % 11
        if count < 2 and count == control:
            return True
        elif count >= 2:
            count = 11 - count
            if count == control:
                return True


a = "1234567899"
print(func_to_help_validate_national_code(a))