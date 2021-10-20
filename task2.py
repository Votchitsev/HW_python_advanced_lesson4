import os
import hashlib

path = os.path.abspath('result_file.txt')


def my_generator(p):
    file = open(p, 'r')
    cursor = 0
    num_of_strings = len(file.readlines())
    while cursor <= num_of_strings:
        result = hashlib.md5(file.readline().encode('utf-8')).hexdigest()
        yield result
        cursor += 1


print(list(my_generator(path)))
