import click
import os

# Create command group based off HTTP requests
@click.group()
def rest():
  """
  Command Line Interface for Image Database
  """
  pass

# GET Request: results corresponding to given query
@rest.command(context_settings={"ignore_unknown_options": True})
@click.argument('features', nargs=-1)
# TODO Get by image ID as well
def get(features):
  """
  Search by Camera ID or by features. Returns results of given query.
  """
  click.echo(features)
  # TODO Get query

# POST Request: send folder and optional csv file
@rest.command(context_settings={"ignore_unknown_options": True})
@click.argument('folder', required=True, type=click.Path(exists=True,
                                          dir_okay=True,
                                          allow_dash=True))
@click.argument('csv', required=False, type=click.Path(exists=True, dir_okay=False))
def post(folder, csv):
  """
  This uploads a folder of images and possibly the csv.
  """
  # Make sure folder and file are appropriate
  if not os.path.isdir(folder):
    raise(click.BadParameter("Image directory not found or not a directory.", param_hint=folder))
  if csv != None and not csv.endswith('.csv'):
    raise(click.BadParameter("File is not a csv file.", param_hint=csv))

  # TODO folder is the directory of images and csv is the csv file if it exists
  if csv != None:
    #TODO create csv for image directory and push to db
    click.echo(folder)
    click.echo(csv)
  else:
    #TODO check if csv is appropriate and push to db
    click.echo(folder)

# Request: PUT 
@rest.command(context_settings={"ignore_unknown_options": True})
def put():
  """
  PUT request
  """

if __name__ == '__main__':
  rest()
