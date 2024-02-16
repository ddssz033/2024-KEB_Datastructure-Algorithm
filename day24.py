def knapsack():
    print("메모이제이션 배열")
    array = [[0 for _ in range(max_weight + 1)] for _ in range(row_count + 1)]
    for row in range(1, row_count + 1):
        print(row, '개 -->', end ='')
        for col in range(1, max_weight + 1):
            if weight[row] > col:
                array[row][col] = array[row-1][col]
            else:
                value1 = money[row] + array[row-1][col-weight[row]]
                value2 = array[row-1][col]
                array[row][col] = max(value1, value2)
            print(f'{array[row][col]:2d}', end ='')
        print()
    return array[row_count][max_weight]

max_weight = 7
row_count = 4
weight = [0,6,4,3,5]
money = [0,13,8,6,12]
