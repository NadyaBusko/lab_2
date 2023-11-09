def generator():
    for el in (10, 20, 30):
        yield el


g = generator()
print(g)

for el in g:
    print(el)
