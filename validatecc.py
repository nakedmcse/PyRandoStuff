# Luhns Algortihm to validate CC numbers
def validate_cc(cardnumber:str) -> bool:
    sum = 0
    for i, c in enumerate(cardnumber.replace(' ','')):
        sum += int(c) if i % 2 != 0 else (int(c)*2 if int(c)*2 < 9 else (int(c)*2)-9)
    return sum % 10 == 0


print('4137 8947 1175 5904:', validate_cc("4137 8947 1175 5904"))
print('1234 5678 1234 5678:', validate_cc("1234 5678 1234 5678"))
