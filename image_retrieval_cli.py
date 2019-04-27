# CAM_HEADER=["Camera_ID", "Country", "State"\
#                 "City", "Latitude", "Longtitude", \
#                 "Resolution_w", "Resolution_h"]
# IV_HEADER=['IV_ID', 'Camera_ID', 'IV_date', 'IV_time', 'File_type', \
# 'File_size', 'Minio_link', 'Dataset', 'Is_processed']


import argparse
import sys
import datetime

'''Function to check if the latitude value is within range'''
def latitude_range_check(lat):
    try:
        lat = float(lat)
        if lat >= -90 and  lat <= 90:
            return True
        raise ValueError
    except ValueError:
        msg = "Given Value({0}) is not valid! Latitude value should be within range -90 to +90.".format(lat)
        raise argparse.ArgumentTypeError(msg)

'''Function to check if the longitude value is within range'''
def longitude_range_check(longitude):
    try:
        longitude = float(longitude)
        if longitude >= -180 and  longitude <= 180:
            return True
        raise ValueError
    except ValueError:
        msg = "Given Value({0}) is not valid! Longitude value should be within range -180 to +180.".format(longitude)
        raise argparse.ArgumentTypeError(msg)

'''Function to check if the input value contains alphabets only'''
def alphabetsonly(astr):
    try:
        if astr.isalpha():
            return True
        raise ValueError
    except ValueError:
        msg = "Given Value({0}) is not valid! Expected alphabets only".format(astr)
        raise argparse.ArgumentTypeError(msg)

'''Function to check if the date was entered in the correct format.'''
def valid_date_type(arg_date_str):
    try:
        return datetime.datetime.strptime(arg_date_str, "%Y-%m-%d")
    except ValueError:
        msg = "Given Date ({0}) not valid! Expected format, YYYY-MM-DD!".format(arg_date_str)
        raise argparse.ArgumentTypeError(msg)

'''Function to check if the time was entered in the correct format.'''
def valid_time_type(arg_time_str):
    try:
        return datetime.datetime.strptime(arg_time_str, "%H:%M:%S")
    except ValueError:
        msg = "Given Time ({0}) not valid! Expected format, HH:MM:SS!".format(arg_time_str)
        raise argparse.ArgumentTypeError(msg)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-lat", "--latitude",action ="store",dest="latitude",
                        help="Latitude of camera location." ,type= latitude_range_check)
    parser.add_argument("-long", "--longitude", action ="store",dest="longitude",type= longitude_range_check,
                        help="Longitude of camera location.")
    parser.add_argument("-city", "--city",action ="store",dest="city",
                        help="Camera Location City",type = alphabetsonly)
    parser.add_argument("-state", "--state",action ="store",dest="state",
                        help="Camera Location State",type=alphabetsonly)
    parser.add_argument("-country", "--country", action ="store",dest="country",
                        help="Camera Location Country",type=alphabetsonly)
    parser.add_argument("-cid", "--camid", action ="store",dest="camera_id",type=int,
                        help="The ID of the Camera")
    parser.add_argument("-date", "--date", action ="store",dest="date",
                        help="The date format is YYYY-MM-DD.Date the image was taken.",type=valid_date_type)
    parser.add_argument("-stime", "--start_time",action ="store",dest="start_time",
                        help="The time format is HH:mm:ss.Time the image was taken.",type=valid_time_type)
    parser.add_argument("-etime", "--end_time",action ="store",dest="end_time",
                        help="The time format is HH:mm:ss.Time the image was taken",type=valid_time_type)
    parser.add_argument("-feature", "--feature", nargs ='+',action="store", dest="feature",
                        help="Features in the image")
    parser.add_argument("-download","--download", action ="store_true", dest= "download", help ="Marks download parameter as true if mentioned else false")

    args = parser.parse_args()
    options = vars(args)
    if len(sys.argv) == 1:
        print("No arguments passed. Please try again.")
        parser.print_help()
    elif options["start_time"] is not None and options["end_time"] is None or options["end_time"] is None and options["start_time"] is not None:
        print("Please enter the value for start and end time. Cannot enter only one.")
        parser.print_help()

if __name__ == '__main__':
    main()
