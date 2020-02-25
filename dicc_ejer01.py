# data = [
#     {
#         '158233413': {
#             'vintage': {'id': 3582334573, 'year': '2017'},
#             'median': {'amount': 5.39, 'type': 'user'},
#             'price': None
#         },
#     },
#     {
#         '153413': {
#             'vintage': {'id': 158413, 'year': '2019'},
#             'median': {'amount': 8.88, 'type': 'user'},
#             'price': None
#         },
#     },
#     {
#         '1534131212': {
#             'vintage': {'id': 1534131212, 'year': '2020'},
#             'median': {'amount': 9.25, 'type': 'user'},
#             'price': None
#         },
#     },
# ]


# print('Unknown keys - just the first record')
# for record in data[0]:
#     print(data[0][record]['median']['amount'])

# print('Unknown keys - all records')
# for datum in data:
#     for record in datum:
#         print(datum[record]['median']['amount'])

# class Deck:
#     def __init__(self):
#         self.cards = []
#         self.build() # build a deck
 
#     def build(self):
#         for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
#             print(s)
 
# deck = Deck()
# raw = ("")
# table = str.maketrans(
#     "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
# )
# result = raw.translate(table)
# print(result)
import urllib.request
import re
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]
# count = {}
# for c in data:
#     count[c] = count.get(c,0) + 1
# print(count)
print("".join(re.findall(["A-Za-z"], data)))
