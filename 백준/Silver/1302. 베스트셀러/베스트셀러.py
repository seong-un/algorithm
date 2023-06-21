N = int(input())

books = dict()
for i in range(N):
    book = input()
    if book in books.keys():
        books[book] += 1
    else:
        books[book] = 1

max_book = 0
bestseller = []
for i in books:
    if max_book < books[i]:
        max_book = books[i]
        bestseller = [i]
    elif max_book == books[i]:
        bestseller.append(i)

print(sorted(bestseller)[0])