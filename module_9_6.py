"""Генератор"""


def all_variants(text):
    bum = len(text)
    for i in range(1, bum + 1):
        for k in range(bum - i + 1):
            yield text[k:k + i]


# def all_variants(text):
#     bum = len(text)
#     for i in range(bum):
#         for k in range(i + 1, bum + 1):
#             yield text[i:k]


a = all_variants("abc")
for i in a:
    print(i)











# def func_generator(n):
#     i = 0
#     while i != n:
#         yield i
#         i += 1
#
#
# fg = func_generator(10)
# print(fg)
#
# for i in fg:
#     print(i)


# def fibonacci_1(n):
#     result = []
#     a, b = 0, 1
#     for _ in range(n):
#         result.append(a)
#     return result
#
#
# def fibonacci_2(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
# fib_1 = fibonacci_1(n=10)
# print(fib_1)
#
# for value in fib_1:
#     print(value)
#
# fib_2 = fibonacci_2(n=2)
# print(fib_2)
# for value in fib_2:
#     print(value)



# def fibonacci_3():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# for value in fibonacci_3():
#     print(value)
#     if value> 10 ** 6:
#         break

# import time
#
# start = time.time()
#
#
# def read_large_file(file_path):
#     with open(file_path, "r", encoding='utf-8') as file:
#         for line in file:
#             yield line.strip()
#
# for line in read_large_file('large_file.txt'):
#     print(line)
#
#
# fin = time.time()
#
# print((fin-start) * 1000)


