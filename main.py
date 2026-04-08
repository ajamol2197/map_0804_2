# 1
roy = [1, 2, 3, 4, 5]
print(roy)

a = list(map(lambda d: d * 2, roy))
print(a)

# 2
roy = [10, 20, 30, 40]
print(roy)

a = list(map(lambda d: d * 5, roy))
print(a)

# 3
roy = ["apple", "banana", "cherry"]
print(roy)

a = list(map(lambda d: d.upper(), roy))
print(a)

# 4
roy = ["salom", "dunyo", "python"]
print(roy)

a = list(map(lambda d: len(d), roy))
print(a)

# 5
roy = [3, 6, 9, 12]
print(roy)
a = list(map(lambda d: d* d, roy))
print(a)

# 6
roy = ["Ali", "Vali", "Hasan"]
print(roy)

a = list(map(lambda d: f"MR. {d}", roy))
print(a)

# 7
roy = [100, 200, 300]
print(roy)

b = list(map(lambda a: str(a), roy))
print(b)

# 8
roy = ["1", "2", "3", "4"]
print(roy)

a = list(map(lambda d: int(d), roy))
print(a)

# 9
roy = [5, 10, 15, 20]
print(roy)

a = list(map(lambda d: d / 3, roy))
print(a)

# 10
roy = ["hello", "world"]
print(roy)

a = list(map(lambda d: f"{d}!", roy))
print(a)
