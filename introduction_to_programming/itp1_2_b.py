def range(a:int, b:int, c:int) -> str:
    if a < b and b < c:
        return "Yes"
    else:
        return "No"

a, b, c = map(int, input().split())
print(range(a, b, c))