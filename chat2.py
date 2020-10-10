
def read_file(filename):
    lines = []
    with open(filename, "r", encoding="utf-8-sig") as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    person = None
    allenWC = 0
    vikiWC = 0
    allenSticker = 0
    allenPic = 0
    vikiSticker = 0
    vikiPic = 0
    for line in lines:
        s = line.split(" ")
        time = s[0]
        name = s[1]
        if name == "Allen":
            if s[2] == "貼圖":
                allenSticker += 1
            elif s[2] == "圖片":
                allenPic += 1
            else:
                for m in s[2:]:
                    allenWC += len(m)
        elif name == "Viki":
            if s[2] == "貼圖":
                vikiSticker += 1
            elif s[2] == "圖片":
                vikiPic += 1
            else:
                for m in s[2:]:
                    vikiWC += len(m)
    print("Allen發了:", allenWC, "個字，", allenSticker, "個貼圖，及", allenPic, "張圖片！")
    print("Viki發了:", vikiWC, "個字，", vikiSticker, "個貼圖，及", vikiPic, "張圖片！")

def write_file(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")

def main():
    lines = read_file("LINE-Viki.txt")
    lines = convert(lines)
    # write_file("output.txt", lines)

main()