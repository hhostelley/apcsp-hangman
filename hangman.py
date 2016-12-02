from googleplaces import GooglePlaces, types, lang
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

YOUR_API_KEY = 'AIzaSyCzUJbo-SRdXzrHX5FitEHDiPi071UNbgg'

google_places = GooglePlaces(YOUR_API_KEY)

def choose_answer():
    print "\nChoose a category: Fast Food(a), Stores(b), or Schools(c)"
    flush()
    answer = raw_input()
    return answer

def flush():
        sys.stdout.flush()

def Game():
    print "WELCOME TO: Super Radical Hangman Go"
    print "\nPlease input location (ex: 10585 Mountian Vista Ridge, Highlands Ranch, CO)"
    flush()
    location = raw_input()
    flush()
    answer = choose_answer()
    valid_input = False

    while valid_input == False:
        if answer == 'a':
            place_type = 'Fast food'
            valid_input = True
        elif answer == 'b':
            place_type = 'Stores'
            valid_input = True
        elif answer == 'c':
            place_type = 'Schools'
            valid_input = True
        else:
            print "\nInput (",answer,") not valid. Please try again."
            answer = choose_answer()

    flush()

    query_result = google_places.nearby_search(
        location=location, keyword=place_type,
        radius=12000, rankby='distance')


    for place in query_result.places:
        print "--"
        print place.name
        print place.geo_location
        print place.place_id
        print "\n"
        place.get_details()
        print place.website
        print "\n"

Game()
