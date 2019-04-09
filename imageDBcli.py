import click
import csv
import os

isAdmin = False

# Create command group based off HTTP requests
@click.group()
def rest():
  """
  Command Line Interface for Image Database
  """
  pass

# GET Request: results corresponding to given query
@rest.command(context_settings={"ignore_unknown_options": True})
@click.argument('features', required=False, nargs=-1)
#@click.argument('cameraID', required=True, nargs=1)
# TODO Get by image ID as well
def get(features):#, cameraID):
  """
  Query database by camera ID or by a list of features
  """
  if features == None:# and cameraID == None:
    # Get all
    click.echo("all")
  click.echo(features)
  #click.echo(cameraID)
  # TODO Get query

# POST Request: send folder and optional csv file
@rest.command(context_settings={"ignore_unknown_options": True})
@click.option('--download', is_flag=True)
@click.argument('folder', required=True, type=click.Path(exists=True,
                                          dir_okay=True,
                                          allow_dash=True))
@click.argument('csv', required=False, type=click.Path(exists=True, dir_okay=False))
def post(download, folder, csv):
  """
  Uploads a folder of images and an optional .csv features file
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
    if download:
      click.echo("Download")
  else:
    raise(click.UsageError("Not admin. Permission denied."))

# Request: PUT 
@rest.command(context_settings={"ignore_unknown_options": True})
def put():
  """
  Update a camera ID with a .csv file
  """

# Request: DELETE 
@rest.command(context_settings={"ignore_unknown_options": True})
def delete():
  """
  Remove a camera ID
  """

def checkAdmin():
  global isAdmin

  user = os.environ['USER']
  f = open('users.csv')
  csv_f = csv.reader(f)
  for row in csv_f:
    if row[0] == user:
      isAdmin = True

if __name__ == '__main__':
  checkAdmin()
  rest()
