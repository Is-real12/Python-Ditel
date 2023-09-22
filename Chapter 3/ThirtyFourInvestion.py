realMoney = 1000
percent = 7
inputer = int(input('Enter your starting investment: '))
result = 0
for i in range(1, 31):
    result += realMoney * percent / 100
    inputer += result
    print(f'In year {i}       you have {inputer}')

