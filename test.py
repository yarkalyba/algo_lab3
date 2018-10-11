def test(lst):
    lst.append(5)
    return 3

lst = [1, 4, 2]
test(lst)
print(lst)