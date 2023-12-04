def count(T):
    for i, element in enumerate(T, start=1):
        print(f"Element {i} = {len(element)}")

T = ((2, 1, 9), (5, 6), (8, 3, 1, 5))
count(T)
