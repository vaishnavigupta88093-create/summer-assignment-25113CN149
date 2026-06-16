def generatetable(n):
    table=""
    for i in range(1,11):
          table += f"{n} * {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt","w",encoding="utf=8") as f:
        f.write(table)

for i in range(2,21):
    generatetable(i)       

