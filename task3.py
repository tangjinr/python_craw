import random
import sys

from blackbox import BlackBox

input_filename = sys.argv[1]
stream_size = int(sys.argv[2])
num_of_asks = int(sys.argv[3])
output_filename = sys.argv[4]

SEED = 553
MAX_NUMBER = 100000
seq_number = 0
user_list = []


def update_user_list(stream_users):
    global seq_number
    for s in stream_users:
        random_num = random.randint(0, MAX_NUMBER)
        seq_number = seq_number + 1
        random_num_mod = random_num % seq_number
        if random_num_mod >= stream_size:
            continue
        random_num = random.randint(0, MAX_NUMBER)
        user_list[random_num % stream_size] = s


def fixed_size_sampling():
    global seq_number
    bx = BlackBox()
    random.seed(SEED)
    output = open(output_filename, "w")
    output.write("seqnum,0_id,20_id,40_id,60_id,80_id" + "\n")

    for index in range(num_of_asks):
        stream_users = bx.ask(input_filename, stream_size)
        if index == 0:
            seq_number = stream_size
            user_list.extend(stream_users)
        else:
            update_user_list(stream_users)
        output.write(
            str(seq_number) + "," + str(user_list[0]) + "," + str(user_list[20]) + "," + str(user_list[40]) + "," + str(
                user_list[60]) + "," + str(user_list[80]) + "\n")


if __name__ == '__main__':
    fixed_size_sampling()
