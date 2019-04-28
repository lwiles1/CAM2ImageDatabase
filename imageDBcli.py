import click
import csv
import time
import datetime
import os

# Global variable to check if user is admin
isAdmin = False

# Help page can be displayed with '-h' or '--help'
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

# Create the group of commands called 'rest' which includes 'get', 'post', 'put', and 'delete'
@click.group()
def rest():
  """
  Command Line Interface for Image Database
  """
  pass

# GET Request: Downloads results corresponding to given query
# '--download' is a flag that allows users to choose if they want to download the files or not
@rest.command('get', short_help = 'Query database by camera ID or by a list of features')
@click.option('-d', '--download', is_flag=True, help='Option to download as csv')
@click.option('-lat', '--latitude', nargs=1, type=float, help='Latitude of camera location.')
@click.option('-long', '--longitude', nargs=1, type=float, help='Longitude of camera location.')
@click.option('-city', '--city', nargs=1, help='City of camera location.')
@click.option('-s', '--state', nargs=1, help='State of camera locaiton.')
@click.option('-c', '--country', nargs=1, help='Country of camera locaiton.')
@click.option('-cid', '--camid', nargs=1, help='ID of the camera.')
@click.option('-date', '--date', nargs=1, help='The date format is YYYY-MM-DD. Date the image was taken.')
@click.option('-st', '--start_time', nargs=1, help='The time format is HH:mm:ss. Time the image was taken.')
@click.option('-et', '--end_time', nargs=1, help='The time format is HH:mm:ss. Time the image was taken.')
@click.option('-feat', '--features', multiple=True, help='Put searchable features in \' \'.')
def get(download, latitude, longitude, city, state, country, camid, date, start_time, end_time, features):
  """
  Query database through list of specified features
  """
  if latitude is None and longitude is None and city is None and state is None and country is None and camid is None and date is None and start_time is None and end_time is None and features == ():
    raise(click.UsageError("No arguments passed. Please try again."))
  if latitude != None and (latitude < -90 or latitude > 90):
    raise(click.BadParameter("Latitude value should be within range -90 to +90.", param_hint=latitude))
  if longitude != None and (longitude < -180 or longitude > 180):
    raise(click.BadParameter("Longitude value should be within range -90 to +90.", param_hint=longitude))
  if city != None and not city.isalpha():
    raise(click.BadParameter("City value should be alphabets only.", param_hint=city))
  if state != None and not state.isalpha():
    raise(click.BadParameter("State value should be alphabets only.", param_hint=state))
  if country != None and not country.isalpha():
    raise(click.BadParameter("Country value should be alphabets only.", param_hint=country))
  if date != None:
    try:
      datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
      raise(click.BadParameter("Date value should be formatted YYYY-MM-DD.", param_hint=date))
  if (start_time is not None and end_time is None) or (start_time is None and end_time is not None):
    raise(click.UsageError("Please enter the value for start and end time. Cannot enter only one."))
  elif start_time is not None and end_time is not None:
    try:
      datetime.datetime.strptime(start_time, "%H:%M:%S")
    except ValueError:
      raise(click.BadParameter("Start time value should be formatted HH:MM:SS.", param_hint=start_time))
    try:
      datetime.datetime.strptime(end_time, "%H:%M:%S")
    except ValueError:
      raise(click.BadParameter("End time value should be formatted HH:MM:SS.", param_hint=end_time))

  #TODO pass in arugments to command
  pass

# POST Request: send folder and optional csv file
@rest.command('post', short_help='Uploads a folder of images and an optional .csv features file') 
@click.argument('folder', required=True, type=click.Path(exists=True, dir_okay=True, allow_dash=True))
@click.argument('csv', required=False, type=click.Path(exists=True, dir_okay=False))
def post(folder, csv):
  """Uploads a folder of images and an optional .csv features file
  
  FOLDER  Name of directory with images

  [CSV]   (Optional argument) .csv file with features
  """
  if isAdmin:
    # Make sure folder and file are appropriate
    if not os.path.isdir(folder):
      raise(click.BadParameter("Image directory not found or not a directory.", param_hint=folder))
    if csv != None and not csv.endswith('.csv'):
      raise(click.BadParameter("File is not a csv file.", param_hint=csv))

    if csv != None:
      #TODO create csv for image directory and push to db
      click.echo(folder)
      click.echo(csv)
    else:
      #TODO check if csv is appropriate and push to db
      click.echo(folder)
  else:
    raise(click.UsageError("Not admin. Permission denied."))

# Request: PUT 
@rest.command('put', short_help='Update a camera ID with a .csv file')
@click.argument('camID', required=True, type=click.Path(allow_dash=True))
@click.argument('csv', required=True, type=click.Path(exists=True, dir_okay=False))
def put(camID, csv):
  """Update a camera ID with a .csv file
  
  CAMID   Name of camera ID

  CSV     .csv file with features
  """
  if isAdmin:
    if csv and not csv.endswith('.csv'):
      raise(click.BadParameter("File is not a csv file.", param_hint=csv))
  else:
    raise(click.UsageError("Not admin. Permission denied."))

# Request: DELETE 
@rest.command('delete', short_help='Remove a camera ID')
@click.argument('camID', required=True)
def delete(camID):
  """Remove a camera ID
  
  CAMID   Name of camera ID
  """
  if isAdmin:
    pass
  else:
    raise(click.UsageError("Not admin. Permission denied."))

# Check if the user is an admin
def checkAdmin():
  global isAdmin

  # Get $USER environment variable
  user = os.environ['USER']
  
  # See if user exists in users.csv file
  f = open('users.csv')
  csv_f = csv.reader(f)
  for row in csv_f:
    if row[0] == user:
      isAdmin = True
      break

if __name__ == '__main__':
  checkAdmin()
  rest()
