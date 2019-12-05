"""OOP is to be consumed with moderation."""
a = 2
b = 2
element = 8
for i in range(element - 1):
    a, b = b, a + b
print(a)
