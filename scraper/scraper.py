from lxml import html
import requests

class SimpleScraper():
  """
  A simple scraper for sites that aren"t heavily javascripted

  Args:
    schema (dict): A schema to introduce scraping
  """

  def __init__(self, schema):
    self.schema = schema

  def scrape(self, url=None):
    """
    The main scraping function

    Args:
      url (str, optional): url to scrape. If not given, the one in schema.url
        will be used
    """
    if url is None:
      url = self.schema["url"]
    response = requests.get(url)
    page_elem = html.fromstring(response.text)
    return self._scrape(page_elem, self.schema["objects"])

  def _scrape(self, page_elem, objects, parent_obj={}):
    result = {}
    for obj in objects:
      if obj.get("children"):
        children = self._scrape(page_elem, obj.get("children"), obj)
        result[obj["name"]] = children
      else:
        xpath = parent_obj.get("xpath", "") + obj["xpath"]
        children_elems = page_elem.xpath(xpath)
        result[obj["name"]] = [child_elem.text_content() for child_elem in children_elems]
    return result

  def scrape_multiple(self, urls=[]):
    """
    Scrapes multiple urls

    Args:
      urls (:obj: list of str): List of urls to scrape
    """
    return [self.scrape(url) for url in urls]
