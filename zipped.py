# *_*coding:utf-8 *_*
L = [1]

A = zip([0] + L, L + [0])

print(A)

A = [(0, 1), (1, 1), (1, 0)]
list = []
for i in A:
    print(i)
    list.append(sum(i))

print(list)
# (0, 1, 1), (1, 1, 0)
# [2, ]

# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L = [sum(i) for i in zip([0]+L, L+[0])]


