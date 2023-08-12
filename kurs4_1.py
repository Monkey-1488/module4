"""
asdfg

a-3
b-1
d-1
f-1
g-1

"""

# def strcounter(s):
#     for sym in set(s):
#         count = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 count += 1
#         print(f'{sym} - {count}')

# strcounter('assdfg')

# # O(N)
# def strcounter(s):
#     sym_dict = {}
#     for sym in s:
#         sym_dict[sym] = 1 + sym_dict.get(sym, 0)

#     for sym, count in sym_dict.items():
#         print(f'{sym} - {count}')

# strcounter('zxc')



# DZ
def is_palindrome(s):
    return s == s[::-1]

input_str = input("Введите строку: ").lower()
input_str = input_str.replace(" ", "")

if is_palindrome(input_str):
    print("True")
else:
    print("False")