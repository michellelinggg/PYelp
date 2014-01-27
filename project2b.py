import urllib
import string

print"Hi, welcome to The Location Finder."
print "Please enter your city name and state abbreviation followed by" 
print "a colon and the type of place you are looking for"
print "Ex: Berkeley, CA: salon or San Francisco, CA: cheap food"
print "*Please use correct capitalization of city and state names."
continueSearch = True

def replacement(address, theCity, theState, theSearch):
	address = address.replace("berkeley", theCity)
	address = address.replace("CA", theState)
	address = address.replace("indian", theSearch)
	return address

def printAddressandNum(theNames):
	for name in theNames:
		addressfinder = '<img alt="hey"'
		print name + ":"
		addressfinder = addressfinder.replace('hey', name)
		addressfinder = addressfinder.replace("'", "&#39;")
		indexStart = html.find(addressfinder)
		if indexStart == -1:
			firstword = name.split()
			name = name.replace("'", "&#39;")
			addressfinder = addressfinder.replace(name, firstword[0])
			addressfinder = addressfinder.rstrip('"')
			indexStart = html.find(addressfinder)
		indexGo = html.find("<address>", indexStart)
		indexEnd = html.find("</address>", indexGo)
		theAddress = html[indexGo:indexEnd]
		theAddress = theAddress.lstrip("<address>")
		theAddress = theAddress.lstrip()
		theAddress = theAddress.rstrip()
		theAddress = theAddress.split("<br>")
		for item in theAddress:
			print "\t" + item
		indexGo = html.find('<span class="biz-phone">', indexStart)
		indexEnd = html.find("</span>", indexGo)
		theNumber = html[indexGo:indexEnd]
		theNumber = theNumber.lstrip('<span class="biz-phone">')
		theNumber = theNumber.lstrip()
		print "\t" + theNumber


while (continueSearch):
	userInfo = raw_input("Your search: ")
	address = "http://www.yelp.com/search?find_desc=indian&find_loc=berkeley%2C+CA&ns"
	cityAndsearch = userInfo.split(":")
	cityAndstate = cityAndsearch[0].split(",")
	theCity = cityAndstate[0]
	theCity = theCity.split()
	theCity = "+".join(theCity)
	theCity = theCity.lower()
	theState = cityAndstate[1][1:]
	theState = theState.upper()
	theSearch = cityAndsearch[1][1:]
	theSearch = theSearch.split()
	theSearch = "+".join(theSearch)

	address = replacement(address, theCity, theState, theSearch)

	namesOfPlaces = "Reviews on Indian in Berkeley, CA   "
	namesOfPlaces = namesOfPlaces.replace("Indian", cityAndsearch[1][1:].capitalize())
	namesOfPlaces = namesOfPlaces.replace("Berkeley, CA", cityAndsearch[0])


	url = urllib.urlopen(address)
	html = url.read()
	begins = html.find(namesOfPlaces)
	ends = html.find(">", begins)
	theNames = html[begins:ends-1]
	theNames = theNames.lstrip(namesOfPlaces)
	theNames = theNames.split(", ")
	printAddressandNum(theNames)
	url.close()
	continuing = raw_input("Would you like to do another search? Y/N: ")
	if (continuing.lower() == "n"):
		continueSearch = False
print "See ya next time!"

