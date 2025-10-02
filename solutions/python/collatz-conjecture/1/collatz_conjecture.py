# define steps function
def steps(num):
    # while num = 1 appear , loop break
    if num < 1:
        raise ValueError("Only positive integers are allowed")
    n_all = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        n_all += 1
    return n_all
