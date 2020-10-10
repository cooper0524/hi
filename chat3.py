
lines = []
with open("3.txt", "r", encoding="utf-8-sig") as f:
    for line in f:
        lines.append(line.strip())
new = []
for line in lines:
    s = line.split(" ")
    time = s[0][:5]
    name = s[0][5:]
    content = ""
    for l in s[1:]:
        content += l
    new.append(time + " " + name + " " + content)


with open("output3.txt", "w") as f:
    for line in new:
        print(line)
        f.write(line + "\n")
 
    
