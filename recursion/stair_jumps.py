def count_ways(stairs_count, jump_ways):
    if stairs_count < 0:
        return 0
    if stairs_count == 0:
        return 1

    total_ways = 0
    for cur_jump in jump_ways:
        total_ways += count_ways(stairs_count - cur_jump, jump_ways)

    return total_ways


print(count_ways(1, [1, 2, 5]))
print(count_ways(2, [1, 2, 5]))
print(count_ways(3, [1, 2, 5]))
print(count_ways(4, [1, 2, 5]))
print(count_ways(5, [1, 2, 5]))
print(count_ways(5, [1, 2, 3]))
