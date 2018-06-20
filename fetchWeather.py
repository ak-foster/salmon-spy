import requests
from lxml import etree

# TODO: get API key to replace "Your_Key"
url = 'https://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?lat=58.7551&lon=-156.548&product=time-series&begin=2018-01-01T00:00:00&end=2019-06-01T00:00:00&maxt=maxt&mint=mint'
resp = requests.get(url)
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('Received {}'.format(resp.status_code))

def parseBookXML(resp):
    """Read API response and parse XML"""

    context = etree.iterparse(resp)
    temp_dict = {}
    temp = []
    for action, elem in context:
        if not elem.text:
            text = "None"
        else:
            text = elem.text
        print (elem.tag + " => " + text)
        temp_dict[elem.tag] = text
        if elem.tag == "value":
            temp.append(temp_dict)
            temp_dict = {}
    return temp

if __name__ == "__main__":
    parseBookXML(resp.content)
