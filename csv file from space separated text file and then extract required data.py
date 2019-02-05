# -*- coding: utf-8 -*-

import sys, os, csv
from time import strftime
logfile=input("Enter the file name with extension:")
newlogfile = "%s_%s.csv" % (logfile,strftime("%Y_%m_%d_ %H_%M_%S"))
with open(logfile,'r') as logf, open(newlogfile,'w') as nlogf:
    nlogf.writelines(lineI.replace(':' if lineI[0]=='#' else ' ', ',')
                  for lineI in logf)
csv_file = newlogfile
with open(csv_file, 'r') as csvfile:
    for line in csvfile.readlines():
        array = line.split(',')
        first_item = array[0]
    num_columns = len(array)
    csvfile.seek(0)
    reader = csv.reader(csvfile, delimiter=',')
    included_cols = [0, 4, 6, 7, 9]
    newfile = "%s_organised.csv" % (newlogfile)
    with open(newfile,'w') as nfile:
        writer=csv.writer(nfile)
        for row in reader:
            content = list(row[i]for i in included_cols)
            writer.writerow(content)
