def print_max_k(in_list, k):
    for i in range(len(some_list) - k + 1):
        cur_max = max(in_list[i:i+k])
        print("max: " + str(cur_max))


from collections import deque

def print_max_k_improved(in_list, k):
    q = deque()
    for i in range(k):
        while q and in_list[i] >= in_list[q[-1]]:
            q.pop()
        q.append(i)

    for i in range(k, len(in_list)):
        print(in_list[q[0]])
        while q and q[0] <= i - k:
            q.popleft()
        while q and in_list[i] >= in_list[q[-1]]:
            q.pop()
        q.append(i)
    print(in_list[q[0]])




some_list = [1, 2, 3, 0, 5, 6]


# print_max_k(some_list, 3)
# print_max_k_improved(some_list, 3)
print(some_list[:-1])