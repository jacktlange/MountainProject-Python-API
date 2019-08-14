import requests
import json

### Return genral user information as JSON dictionary
### args: 
###     - key: your private key
###     - userId: Id of user to return
###     - email: email of user to return
### returns: genral user information as JSON dictionary
baseURL = "https://www.mountainproject.com/data/"
def getUser(key, userId="", email=""):
    if userId == "" and email != "":
        queryString =  "get-user?email=" + email
    elif userId != "" and email == "":
        queryString =  "get-user?userId=" + userId
    else:
        raise Exception("Supply only a userId or email, not both")
    queryURL = baseURL + queryString + "&key=" + key
    response = requests.get(queryURL)
    return json.loads(response.text)

### Returns up to 200 of the user's most recent ticks.
### args: 
###     - key: your private key
###     - userId: Id of user to return
###     - email: email of user to return
###     - startPos: The starting index of the list to return. Defaults to 0.
### returns: Users ticks as JSON dictionary
def getTicks(key, userId="", email="", startPos=0):
    if userId == "" and email != "":
        queryString =  "get-ticks?email=" + email + "&" + str(startPos)
    elif userId != "" and email == "":
        queryString =  "get-ticks?userId=" + userId + "&" + str(startPos)
    else:
        raise Exception("Supply only a userId or email, not both")
    queryURL = baseURL + queryString + "&key=" + key
    response = requests.get(queryURL)
    return json.loads(response.text)
    
### Returns up to 200 of the user's TODOs
### args: 
###     - key: your private key
###     - userId: Id of user to return
###     - email: email of user to return
###     - startPos: The starting index of the list to return. Defaults to 0.
### returns: User's TODOs as JSON dictionary
def getToDos(key, userId="", email="", startPos=0):
    if userId == "" and email != "":
        queryString =  "get-to-dos?email=" + email + "&" + str(startPos)
    elif userId != "" and email == "":
        queryString =  "get-to-dos?userId=" + userId + "&" + str(startPos)
    else:
        raise Exception("Supply only a userId or email, not both")
    queryURL = baseURL + queryString + "&key=" + key
    response = requests.get(queryURL)
    return json.loads(response.text)
    
### Returns details for up to 200 routes.
### args: 
###     - key: your private key
###     - routeIds: A comma-separated list of route IDs, up to 100
### returns: details for up to 200 routes as JSON dictionary
def getRoutes(key, routeIDs):
    queryString = "get-routes?routeIds=" + routeIDs
    queryURL = baseURL + queryString + "&key=" + key
    response = requests.get(queryURL)
    return json.loads(response.text)
    
### Returns routes for a given query
### args: 
###     - key: your private key
###     - lat - Latitude for a given area
###     - lon - Longitude for a given area
###     - maxDistance: Max distance, in miles, from lat, lon. Default: 30. Max: 200.
###     - maxResults:  Max number of routes to return. Default: 50. Max: 500.
###     - minDiff:  Min difficulty of routes to return, e.g. 5.6 or V0.
###     - maxDiff:  Max difficulty of routes to return, e.g. 5.10a or V2.
### returns: details for up to 200 routes as JSON dictionary
def getRoutesForLatLon(key, lat, lon, maxDistance=30, maxResults=50, minDiff="5.0", maxDiff="5.16"):
    queryString = "get-routes-for-lat-lon?" + "lat=" + str(lat) + "&lon=" + str(lon) + "&maxDistance=" + str(maxDistance) + "&maxResults=" + str(maxResults) + "&minDiff=" + minDiff + "&maxDiff=" + maxDiff
    queryURL = baseURL + queryString + "&key=" + key
    print(queryURL)
    response = requests.get(queryURL)
    return json.loads(response.text)

    

