import os
import csv

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


with open('nyc_traffic_sample.csv', mode='w') as csv_file:
    fieldnames = ['File_Names', 'Bucket_Name']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for file in files("./minio_test_server/nyc"):
        writer.writerow({'File_Names': file, 'Bucket_Name': 'nyc'})



