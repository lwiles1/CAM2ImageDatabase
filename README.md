# **Purpose**
A python script that will give user the images/videos that are listed in a .csv file.

* Input: a .csv file that contains file names and bucket name as input
* Output: a .tar file that contain the images/videos correspond to the .csv file

## **Usage**
* Start a Minio server, for example
  $ minio server [desired directory]
* Add an alias to that Minio server, by running
  $ mc config host add [HostAlias] [Endpoint] [AccessKey] [SecretKey]
* Run this script
  $ python ./Get_File_From_Minio.py [HostAlias] [FileName]

### **Current Test**
1,196 images from "NYC Traffic" dataset on Google Drive
139.9 MB in total

![result](https://cdn1.imggmi.com/uploads/2019/2/25/674cdc87cc24a81516a75d776f8df6fe-full.jpg)

#### **To Do**
* Need to test on larger image/video set.
* Need to test on a remote server.
