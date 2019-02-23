# CAM2 - Image Database
# Author: Haoran Wang
# Purpose: Given a CSV file, file names and bucket name as input, return a TAR file with images compressed in it.

import sys
import pandas as pd
import subprocess as sp
import time
import datetime

# File name is named after time stamp
ts = datetime.datetime.now()
folder_name = ts.strftime("%Y-%m-%d") + "_" + ts.strftime("%I.%M.%S_%p")

# Make bucket downloadable
def policy_download_cmd():
    for i in range(bucket_name.__len__()):
        cmd = "mc policy download " + host_name + "/" + bucket_name[i] + "/"
        returned_output = sp.call(cmd, shell=True)
        print(returned_output)


# Create temp folder
def mkdir_cmd():
    cmd = "mkdir " + folder_name
    # print(cmd)
    sp.call(cmd, shell=True)


# Download Files by running cp command
def cp_cmd():
    for i in range(file_names.__len__()):
        cmd = "mc cp " + host_name + "/" + bucket_name[i] + "/" + file_names[i] + " ./" + folder_name
        returned_output = sp.call(cmd, shell=True)
        print(returned_output)


# Compress the folder and deliver a .tar file
def tar_cmd():
    cmd = "tar -cvf " + folder_name + ".tar " + folder_name
    sp.call(cmd, shell=True)


# Delete temp folder
def rm_cmd():
    cmd = "rm -r " + folder_name
    sp.call(cmd, shell=True)


if __name__ == '__main__':

    start_time = time.time()

    # Check parameters before proceeding
    if len(sys.argv) != 3 or isinstance(sys.argv[1], str) is False or isinstance(sys.argv[2], str) is False or \
            sys.argv[1] == "" or sys.argv[2] == "":
        print("Invalid Parameters")
        sys.exit()

    else:
        host_name = sys.argv[1]
        csv_file_name = sys.argv[2]

        # Read in CSV as a data frame
        # Fill in two lists, file_names and bucket_name
        df = pd.read_csv(csv_file_name, sep=',', header=0, engine='python')
        file_names = df.File_Names.tolist()
        bucket_name = df.Bucket_Name.tolist()

        # Check if two lists are valid before proceeding
        for i in range(file_names.__len__()):
            if isinstance(file_names[i], str) is False or isinstance(bucket_name[i], str) is False or \
                    file_names[i] == "" or bucket_name[i] == "":
                print("Please Fix CSV Before Proceeding")
                sys.exit()

        # Make all files downloadable
        policy_download_cmd()

        # Make a folder named with timestamp
        mkdir_cmd()

        # Download images to that folder
        cp_cmd()

        # Compress temp folder
        tar_cmd()

        # Delete temp folder
        rm_cmd()

        print("===============================================================")
        print("Finished in --%s-- seconds" % (time.time()-start_time))
