from minio import Minio
from minio.error import ResponseError
import sys
import pandas as pd
import subprocess as sp
import time
import datetime


# File name is named after time stamp
ts = datetime.datetime.now()
folder_name = ts.strftime("%Y-%m-%d") + "_" + ts.strftime("%I.%M.%S_%p")


# Create temp folder
def mkdir_cmd():
    cmd = "mkdir " + folder_name
    # print(cmd)
    sp.call(cmd, shell=True)


# Compress the folder and deliver a .tar file
def tar_cmd():
    cmd = "tar -cvf " + folder_name + ".tar " + folder_name
    sp.call(cmd, shell=True)


# Delete temp folder
def rm_cmd():
    cmd = "rm -r " + folder_name
    sp.call(cmd, shell=True)


if __name__ == '__main__':

    minioClient = Minio('localhost:9000', access_key='FX770DGQ10M2ALSRVX3F', secret_key='qCO+rTTAGoPdaf5m39dleP5+vr9f15sCT0RGAbLl', secure=False)

    start_time = time.time()

    # Check parameters before proceeding
    if len(sys.argv) != 2 or isinstance(sys.argv[1], str) is False or sys.argv[1] == "":
        print("Invalid Parameters")
        sys.exit()

    else:
        csv_file_name = sys.argv[1]

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

        # Make a folder named with timestamp
        mkdir_cmd()

        # presigned get object URL for object name, expires in 2 days.
        URLs = list()
        try:
            for i in range(file_names.__len__()):
                URLs.append(minioClient.presigned_get_object('nyc', file_names[i], expires=datetime.timedelta(days=2)))
        # Response error is still possible since internally presigned does get bucket location.
        except ResponseError as err:
            print(err)

        # Download images from url to temp folder
        for i in range(URLs.__len__()):
            cmd = "cd ./" + folder_name + " &&  wget " + URLs[i]
            sp.call(cmd, shell=True)

        # Compress temp folder
        tar_cmd()

        # Delete temp folder
        rm_cmd()

        print("===============================================================")
        print("Finished in --%s-- seconds" % (time.time()-start_time))
