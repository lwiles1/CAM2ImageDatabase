# **Purpose**
A python script that will give user the images/videos that are listed in a .csv file.

* Input: a .csv file that contains file names and bucket name as input
* Output: a .tar file that contain the images/videos correspond to the .csv file

Sample Output:
![Result](https://i.ibb.co/GcGXcbg/Screen-Shot-2019-02-22-at-11-56-46-PM.jpg)

## **Usage**
* Start a Minio server, for example
  $ minio server <desired directory>
* Add an alias to that Minio server, by running
  $ mc config host add <HostAlias> <Endpoint> <AccessKey> <SecretKey>
* Run this script
  $ python ./Get_File_From_Minio.py <HostAlias> <FileName>

### **To Do**
* Need to test on larger image/video set.
* Need to test on a remote server.
