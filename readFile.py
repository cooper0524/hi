data = []
count = 0
with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print("File read completed! There are", len(data), "records in total!")


strLen = 0
for record in data:
    strLen += len(record.strip())
averageLen = strLen/len(data)
print("The average length of reviews is", averageLen)

new = []
for r in data:
    if len(r) < 100:
        new.append(r)
print("There are", len(new), "records which length less than 100")

good = []
for d in data:
    if "good" in d:
        good.append(d)
print("There are", len(good), "records which contain the word good")

goodList = [d for d in data if "good" in d]
print(len(goodList))

bad = ["bad" in d for d in data]
print(len(bad))

#Count Words
wc = {}
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1

while True:
    keyWord = input("Search >>> ")
    if keyWord == "q":
        break
    elif keyWord in wc:
        print(keyWord, "appears", wc[keyWord], "times.")
    else:
        print(keyWord, "appears 0 time.")
print("Thanks for using this searching app!")