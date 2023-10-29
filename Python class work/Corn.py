gog = "google.com"


# dict1 += gog
# print(dict(dict1)
# )
def count(gog):
    dict1 = {}
    for i in gog:
        count = gog.count(i)
        dict1.setdefault(i, count)
    return dict1


gog = "google.com"

print(count(gog))
