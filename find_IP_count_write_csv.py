# 1. Find the IP in the log file
# 2. Find the IP count in the log file
# 3. Write the Ip and count in the output.csv
# Please refer the log file for the content

import re
from collections import *
import csv


# To find the IP and its count in the log file


def ip_and_count(filename):
    with open(filename) as file1:
        log = file1.read()
        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ip = re.findall(regexp, log)
        return Counter(ip)


def write(count):
    with open('output.csv', 'w') as file2:
        headers = ['IP', 'Count']
        writer = csv.writer(file2)
        writer.writerow(headers)
        for i in count:
            writer.writerow((i, count[i]))


if __name__ == '__main__' :
    write(ip_and_count('log'))
