def small_large_equal(a:int, b:int) -> str:
    if a < b:
        return "a < b"
    elif a >b:
        return "a > b"
    else:
        return "a == b"

a, b = map(int, input().split())
print(small_large_equal(a, b))