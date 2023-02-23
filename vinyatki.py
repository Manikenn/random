result = []
def divider(a, b):
    try:
        if a < b:
            raise ValueError("a must be greater than or equal to b")
        if b > 100:
            raise IndexError("b must be less than or equal to 100")
        return a/b
    except (ValueError, IndexError) as e:
        print(type(e).__name__ + ": " + str(e))
        return None

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
for key in data:
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(result)