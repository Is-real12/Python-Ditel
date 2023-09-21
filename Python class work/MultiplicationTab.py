count = 1
oneTimesMul = 1

for i in range(1, 13):
    print()
    for dum in range(1, 21):
        print(f"{i: > 2} x {dum:>2} = {i * dum:^4}", end=" ")
        # print(i ," * " ,dum ,'=', i*dum,"   ", end=' ')

    # or print(f"{i>2} x {j:>2} = {i*j: 4}", end=" ")
