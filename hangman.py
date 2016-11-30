from googleplaces import GooglePlaces, types, lang
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def flush():
        sys.stdout.flush()

YOUR_API_KEY = 'AIzaSyCzUJbo-SRdXzrHX5FitEHDiPi071UNbgg'

google_places = GooglePlaces(YOUR_API_KEY)

print "WELCOME TO: Super Radical Hangman Go"
print "Please input location (ex: 10585 Mountian Vista Ridge, Highlands Ranch, CO)"
flush()
location = raw_input()
flush()
print "Please input type of place (ex: Cafe)"
flush()
place_type = raw_input()
flush()

query_result = google_places.nearby_search(
        location=location, keyword=place_type,
        radius=20000, types=[types.TYPE_FOOD])


for place in query_result.places:
    print "--"
    print place.name
    print place.geo_location
    print place.place_id
    print "\n"
    place.get_details()
    print place.website
    print "\n"
