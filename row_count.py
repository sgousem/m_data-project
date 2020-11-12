import os
import csv
import glob
path = os.getcwd()
os.chdir(os.path.join(path,'CDATA'))
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
total_rows = 0
for file_name in all_filenames:
    with open(file_name, 'r',encoding='utf-8') as csvfile:
        csvwriter = csv.reader(csvfile)
        total_rows+= sum(1 for row in csvwriter)
print(total_rows)