coords = []
# x = 1
# y = -38
# for i in range(13):
#     coords.append([])
#     x = 1
#     y += 39
#     for j in range(13):
#         if j == 0:
#             coords[i].append((x,y))
#         else:
#             x += 39
#             coords[i].append((x,y))

xlist = [1,40,79,117,156,195,233,272,311,349,388,427,464]
ylist = [0,38,77,115,154,193,231,270,309,348,386,425,463]

for i in range(13):
    coords.append([])
    for j in range(13):
        coords[i].append((xlist[j],ylist[i]))
print(coords)

