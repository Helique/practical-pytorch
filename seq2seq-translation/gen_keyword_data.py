import random
data_file = open("data/auto-auto.txt", "w")
dataset = []
for i in range(1000):
    dataset.append("a b c d e")
for i in range(1000):
    dataset.append("a b f d e")
for i in range(1000):
    dataset.append("a b c d k")
for i in range(1000):
    dataset.append("a b c d f")

randomized_dataset = random.sample(dataset, 4000)
for line in randomized_dataset:
    data_file.write("{}\t{}\t{}\n".format(line, line, "1" if "f" in line else "0"))
