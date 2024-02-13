def generate_fibonacci_num(fib_list, n):
    if len(fib_list) == n:
        return fib_list
    else:
        next_num = fib_list[len(fib_list) - 1] + fib_list[len(fib_list) - 2]
        fib_list.append(next_num)
        return generate_fibonacci_num(fib_list, n)


def short_fib(n):
    if n <= 1:
        return n
    else:
        return short_fib(n - 1) + short_fib(n - 2)


def fibonacci(n):
    fib_list = [0, 1]
    if n == 1:
        return [0]
    elif n == 2:
        return fib_list
    else:
        return generate_fibonacci_num(fib_list, n)

# pre_list = [0, 1]
# fib_list = []
# if len(fib_list) == n - 2:
#     return pre_list + fib_list
# elif n == 1:
#     return [0]
# else:
#     fib_list.append(x)
#     if len(fib_list) == 1:
#         prev_num = 1
#     else:
#         prev_num = fib_list[len(fib_list) - 2]
#     return fibonacci(prev_num + x, n)
