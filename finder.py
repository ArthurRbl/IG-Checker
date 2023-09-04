import codecs

notFollowing = []
notFollowingMeBack = []

txtFollowers = codecs.open("followers.txt", "r", "utf-8")
txtFollowing = codecs.open("following.txt", "r", "utf-8")

txtFollowers = txtFollowers.read()
txtFollowing = txtFollowing.read()

def nameCleaner(rawName):
    name = ""
    i = 0
    while rawName[i] != "<":
        name = name + rawName[i]
        i+=1
    return name

def nameFinder(txt):
    list = []
    id = -10
    while id != -1:
        id += 10
        id = txt.find('<span class="_aacl _aaco _aacw _aacx _aad7 _aade" dir="auto">', id)
        if id != -1:
            list.append(nameCleaner(txt[id+61:id+100]))
    return list

listFollowers = nameFinder(txtFollowers)
listFollowing = nameFinder(txtFollowing)

"""
print("Followers : \n")
print(listFollowers)
print("\n\nFollowing : \n")
print(listFollowing)
"""

for i in range(len(listFollowing)):
    if listFollowing[i] not in listFollowers:
        notFollowingMeBack.append(listFollowing[i])

for i in range(len(listFollowers)):
    if listFollowers[i] not in listFollowing:
        notFollowing.append(listFollowers[i])

#print(notFollowingMeBack)
#prtin(notFollowing)

print("Not following me back : \n\n")
for i in range(len(notFollowingMeBack)):
    print(str(i+1) + ". " + notFollowingMeBack[i])

print("\n\nI dont follow : \n\n")
for i in range(len(notFollowing)):
    print(str(i+1) + ". " + notFollowing[i])

print("\n\n" + str(len(notFollowingMeBack)) + " users are note following me back and I dont follow " + str(len(notFollowing)) + " users.")
