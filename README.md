This package is a wrapper for the Mountain Project public data API: https://www.mountainproject.com/data. 

Install using: pip install MountainProjectPublicAPI

Required packages: json, requests


Example usage can be found at: https://github.com/jacktlange/MountainProject-User-Analysis


Available functions:

### getUser(key, userId="", email="")
    Return genral user information as JSON dictionary
    args: 
         - key: your private key
        - userId: Id of user to return
        - email: email of user to return
    return: genral user information as JSON dictionary

### getTicks(key, userId="", email="", startPos=0)
    Return up to 200 of the user's most recent ticks.
    args: 
        - key: your private key
        - userId: Id of user to return
        - email: email of user to return
        - startPos: The starting index of the list to return. Defaults to 0.
    returns: Users ticks as JSON dictionary

### getToDos(key, userId="", email="", startPos=0)
     Return up to 200 of the user's TODOs
     args: 
         - key: your private key
         - userId: Id of user to return
         - email: email of user to return
         - startPos: The starting index of the list to return. Defaults to 0.
     returns: User's TODOs as JSON dictionary

### getRoutes(key, routeIDs)
     Return details for up to 200 routes.
     args: 
         - key: your private key
         - routeIds: A comma-separated list of route IDs, up to 100
     returns: details for up to 200 routes as JSON dictionary
     
### getRoutesForLatLon(key, lat, lon, maxDistance=30, maxResults=50, minDiff="5.0", maxDiff="5.16")
     Return routes for a given query
     args: 
         - key: your private key
         - lat - Latitude for a given area
         - lon - Longitude for a given area
         - maxDistance: Max distance, in miles, from lat, lon. Default: 30. Max: 200.
         - maxResults:  Max number of routes to return. Default: 50. Max: 500.  
         - minDiff:  Min difficulty of routes to return, e.g. 5.6 or V0.
         - maxDiff:  Max difficulty of routes to return, e.g. 5.10a or V2.
     returns: details for up to 200 routes as JSON dictionary
   

    


