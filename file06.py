with open("file06nnew.txt", "r",encoding="utf-8") as f:
    data = f.read()

data = data.replace("donkey", "#####")

with open("file06nnew.txt", "w",encoding="utf-8") as f:
    f.write(data)

print("succesfully replaced")