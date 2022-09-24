def storeword():
    tf = []
    for x in range(4): tf.append("")
    tf[0] = open("eng.txt", "w")
    tf[1] = open("french.txt", "w")
    tf[2] = open("spanish.txt", "w")
    tf[3] = open("jp.txt", "w")
    for x in range(4):
        for y in range(100000):
            tf[x].write(lines[y] + "\n")
    for x in range(4): tf[x].close()

lines = [] 
for x in range(100000): lines.append("")
storeword()
print("completed.")
