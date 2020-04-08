# From wiki page


def max_subarray(numbers):
    best_sum = 0  # or: float('-inf')
    best_start = best_end = 0  # or: None
    current_sum = 0
    for current_end, x in enumerate(numbers):
        if current_sum <= 0:
            # Start a new sequence at the current element
            current_start = current_end
            current_sum = x
        else:
            # Extend the existing sequence with the current element
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1  # the +1 is to make 'best_end' exclusive

    return best_sum, best_start, best_end


# examplr 1:
# list = [631, -583, -975]

# example 2: -5, -1, -4, -7

# example 3: 34, -50, 42, 14, -5, 86


some_list = [34, -50, 42, 14, -5, 86]

result = max_subarray(some_list)

print(result)
