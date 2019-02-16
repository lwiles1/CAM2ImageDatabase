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
@click.argument('query', nargs=-1)
def get(query):
  """
  This search and returns results to the given query.
  """
  click.echo(query)
  # TODO Get query

# POST Request: send folder and optional csv file
@rest.command(context_settings={"ignore_unknown_options": True})
@click.argument('folder', type=click.Path(exists=True, dir_okay=True, allow_dash=True))
@click.argument('csv', required=False, type=click.Path(exists=False))
def post(folder, csv):
  """
  This uploads a folder of images and possibly the csv.
  """
  # Make sure folder and file are appropriate
  if not os.path.isdir(folder):
    raise(click.BadParameter("Image directory not found or not a directory.", param_hint=folder))
  if csv != None:
    if not os.path.isfile(csv):
      raise(click.BadParameter("csv file not found or not a file.", param_hint=csv))
    if not csv.endswith('.csv'):
      raise(click.BadParameter("File is not a csv file."))

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

# Request: DELETE
@rest.command(context_settings={"ignore_unknown_options": True})
def delete():
  """
  DELETE request
  """

if __name__ == '__main__':
  rest()
