x, y, w, h = map(int, input().split())
top = h - y
bottom = h - top
right = w - x
left = w - right
print(min(top, bottom, right, left))
