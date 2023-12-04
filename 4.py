def AddOddEven(values):
    even = sum(val for val in values if val % 2 == 0)
    odd = sum(val for val in values if val % 2 != 0)
    
    print(f"Even Sum: {even}\nOdd Sum: {odd}")

VALUES = [13, 17, 12, 6, 9]
AddOddEven(VALUES)
