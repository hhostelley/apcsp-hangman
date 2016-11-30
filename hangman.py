import googlemaps
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def flush():
    sys.stdout.flush()

print "WELCOME TO: Super Radical Hangman Go"
flush()
print "Please input locaton: (Example: 10585 Mountain Vista Ridge, Highlands Ranch, CO)"
flush()
location = raw_input()
flush()

gmaps = googlemaps.Client(key='AIzaSyCzUJbo-SRdXzrHX5FitEHDiPi071UNbgg')

# Geocoding an address
geocode_result = gmaps.geocode(location)
x = geocode_result[0]
print x['geometry']

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))


# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
