def _count_ways(stairs_count, jump_ways, cache):
    if stairs_count < 0:
        return 0

    if stairs_count == 0:
        return 1

    total_ways = 0
    for cur_jump in jump_ways:
        cur_ways_idx = stairs_count - cur_jump
        if cur_ways_idx < 0:
            continue

        cur_ways = cache[cur_ways_idx]
        if not cur_ways:
            cur_ways = _count_ways(cur_ways_idx, jump_ways, cache)
            cache[cur_ways_idx] = cur_ways

        total_ways += cur_ways

    return total_ways


def count_ways(stairs_count, jump_ways):
    cache = [None] * (stairs_count + 1)
    return _count_ways(stairs_count, jump_ways, cache)


print(count_ways(1, [1, 2, 5]))
print(count_ways(2, [1, 2, 5]))
print(count_ways(3, [1, 2, 5]))
print(count_ways(4, [1, 2, 5]))
print(count_ways(5, [1, 2, 5]))
