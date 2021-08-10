import csv
import time
import psutil

def main():
    old_value = 0;
    with open('data.csv','w',newline='')as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Day_Time','data_used','Percent_change'])
        while True:
            new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
            thewriter.writerow([time.ctime(),convert_to_mbit(new_value),convert_to_mbit(new_value-old_value)])
            old_value = new_value
            time.sleep(1)

def convert_to_gbit(value):
    ''' Humanise the output to less digits. '''
    return value/1024./1024./1024.*8

def convert_to_mbit(value):
    '''Humanise the output to less digits. '''
    return value/1024./1024.

main()

