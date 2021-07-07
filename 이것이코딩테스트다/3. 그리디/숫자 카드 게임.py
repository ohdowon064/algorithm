n, m = map(int, input().split())
cards = []

# card = -999
# index = 0
# for i in range(n):
#     numbers = list(map(int, input().split()))
#     cards.append(numbers)
#     if min(numbers) > card:
#         card = min(numbers)
#         index = i
#
# print(min(cards[index]))

card = -999
for i in range(n):
    numbers = list(map(int, input().split()))
    card = max(min(numbers), card)

print(card)