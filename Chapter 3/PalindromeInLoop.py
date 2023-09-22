for i in range(5):
    user = int(input('enter four integer'))
    each1 = user // 1000
    each2 = user // 100%10
    each3 = user // 10%10
    each4 = user  %10
    print(f'{each1} {each2} {each3} {each4}')