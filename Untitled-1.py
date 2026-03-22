# def reverse_triangle_bruteforce(n):
#     for i in range(n):  # i = row index (0 to n-1)
#         spaces = " " * i
#         stars = "*" * (n - i)
#         print(spaces + stars)

# # Example
# reverse_triangle_bruteforce(7)


def reverse_triangle_optimized(n):
    for i in range(n, 0, -1):   # from n down to 1
        print(("*" * i).rjust(n))


print("\nOptimized:")
reverse_triangle_optimized(7)
