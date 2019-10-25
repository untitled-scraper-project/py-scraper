import json
from scraper import SimpleScraper

def scrape(filename=None, schema=None):
  if not filename and not schema:
    raise Exception("A filename or schema has to be provided!")

  if filename:
    with open(filename) as json_file:
      schema = json.load(json_file)

  return SimpleScraper(schema).scrape()
