def task3(minimum,maximum,divisor):
    diviList = list()
    for i in range(minimum,maximum):
        if i%divisor ==0:
            diviList.append(i)

    total = sum(diviList)
    print(total)


task3(0,10,2)