hardcoded = [
    [0, 1, 2, 3],
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
]


def with_loops():
    result = []
    for row_index in range(0, 4):
        result.append([])
        for column_index in range(0, 4):
            result[row_index].append(row_index + column_index)

    return result


print(with_loops())
print(with_loops() == hardcoded)
print("-" * 20)

duo_loops = [[i+j for i in range(0, 4)] for j in range(0, 4)]
print(duo_loops)
print(duo_loops == hardcoded)
print("-" * 20)

single_loop = [list(range(x, x+4)) for x in range(0, 4)]
print(single_loop)
print(single_loop == hardcoded)
