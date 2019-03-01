# **Purpose**
 Compare three different methods that will give user the images/videos that are listed in a .csv file from Minio storage.

* Input: a .csv file that contains file names and bucket name as input
* Output: a .tar file that contain the images/videos correspond to the .csv file

## **Procedure**
* Start a Minio server, for example
  $ minio server [desired directory]
* Add an alias to that Minio server, by running
  $ mc config host add [HostAlias] [Endpoint] [AccessKey] [SecretKey]
* Run different scripts

  *Use mc find command from Minio Client*
  $ python ./mc_find.py [HostAlias] [CSV_FileName]

  *Use fget_object method from Python API*
  $ python ./fget_object.py [CSV_FileName]

  *Use wget command*
  $ python ./presigned_get_object.py [CSV_FileName]

### **Comparing Result**
1,196 images from "NYC Traffic" dataset on Google Drive
139.9 MB in total

mc_find.py

![result](https://i.ibb.co/H7NVY8S/674cdc87cc24a81516a75d776f8df6fe-full.jpg)

fget_object.py

![result](https://i.ibb.co/VMNLYqk/Screen-Shot-2019-03-01-at-2-02-39-AM.jpg)

presigned_get_object.py

![result](https://i.ibb.co/DGwWZ1F/Screen-Shot-2019-03-01-at-2-23-10-AM.jpg)
