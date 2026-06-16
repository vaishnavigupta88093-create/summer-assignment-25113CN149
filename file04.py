f = open("poem.txt", "r", encoding="utf-8")
data = f.read()

print(data.count("Twinkle"))

f.close()