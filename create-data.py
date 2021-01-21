from model import simulate
import random
from csv import writer

random.seed(97)

size = 50
unblock_input = list(range(1,size**2+1))
number_of_observation = 10000
header = ["edge_size","total_sites","unblocked_sites"]

with open("data.csv","w") as data_file:
    file_writer = writer(data_file)
    file_writer.writerow(header)

with open("data.csv","a") as data_file:
    file_writer = writer(data_file)

    for i in range(number_of_observation):
        new_row = [size,size**2]
        random.shuffle(unblock_input)
        new_row.append(simulate(size,unblock_input))

        file_writer.writerow(new_row)