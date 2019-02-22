# CAM2 - Image Database
# Author: Haoran Wang
# Purpose: Given a CSV file, file names and bucket name as input, return a TAR file with images compressed in it.

import pandas as pd
import subprocess as sp
import datetime

csv_file_name = "sample.csv"
host_name = "myminio"

ts = datetime.datetime.now()
folder_name = ts.strftime("%Y-%m-%d") + "_" + ts.strftime("%I.%M.%S_%p")

# Read in CSV as a data frame
# Fill in two lists, file_names and bucket_name
df = pd.read_csv(csv_file_name, sep=',', header=0, engine='python')
file_names = df.File_Names.tolist()
bucket_name = df.Bucket_Name.tolist()

# Check if two lists are valid before proceeding
error = 0
error_message = "Please Fix CSV Before Proceeding"
for i in range(file_names.__len__()):
    if isinstance(file_names[i], str) == False or isinstance(bucket_name[i], str) == False or file_names[i] == "" or \
            bucket_name[i] == "":
        error = 1


# Make bucket downloadable
def policy_download_cmd():
    for i in range(bucket_name.__len__()):
        cmd = "mc policy download " + host_name + "/" + bucket_name[i] + "/"
        returned_output = sp.call(cmd, shell=True)
        print(returned_output)


# Create folder
def mkdir_cmd():
    cmd = "mkdir " + folder_name
    # print(cmd)
    returned_output = sp.call(cmd, shell=True)
    print(returned_output)


# Download Files by running cp command
def cp_cmd():
    for i in range(file_names.__len__()):
        cmd = "mc cp " + host_name + "/" + bucket_name[i] + "/" + file_names[i] + " ./" + folder_name
        returned_output = sp.call(cmd, shell=True)
        print(returned_output)


# Compress the folder and deliver a .tar file
def tar_cmd():
    cmd = "tar -cvf " + folder_name + ".tar " + folder_name
    returned_output = sp.call(cmd, shell=True)
    print(returned_output)


if __name__ == '__main__':

    if error == 1:
        print(error_message)

    else:

        # Make all files downloadable
        policy_download_cmd()

        # Make a folder named with timestamp
        mkdir_cmd()

        # Download images to that folder
        cp_cmd()

        # Compress folder
        tar_cmd()
