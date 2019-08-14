# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 16:03:33 2019

@author: Jack
"""

import requests
import json
#private user key
privateKey = '112446503-8924701af82f2e439e9312357672ca8d'
#make an enum for query types and a function for getURL
#def getTicks(userEmail):
#    baseURL = "https://www.mountainproject.com/data/get-ticks?email=" 
#    queryURL = baseURL + userEmail + "&key=" + privateKey
#    response = requests.get(queryURL)
#    queryResultFile = open(userEmail + "_ticks.txt", "w+")
#    queryResultFile.write(response.text)
#    queryResultFile.close()
#    #check for success of query and write
#    return response.text
#    
#def routesFromTicks(ticks):
#    ticks = json.loads(ticks)
#    tickedRoutes = ticks["ticks"]
#    for route in tickedRoutes:
#        print(route["routeId"])
#        
#def routeFromId(Id):
#    baseURL = "https://www.mountainproject.com/data/get-routes?routeIds=" 
#    queryURL = baseURL + Id + "&key=" + privateKey
#    response = requests.get(queryURL)
#    route = json.loads(response.text)["routes"][0]
#    return route
    
### Return genral user information as JSON dictionary
### args: 
###     - key: your private key
###     - userId: Id of user to return
###     - email: email of user to return
### returns: genral user information as JSON dictionary
def getUser(userId="", email=""):
    
### Returns up to 200 of the user's most recent ticks.
### args: 
###     - key: your private key
###     - userId: Id of user to return
###     - email: email of user to return
###     - startPos: The starting index of the list to return. Defaults to 0.
### returns: Users ticks as JSON dictionary
def getTicks(key, userId="", email="", startPos=0):

### Returns up to 200 of the user's TODOs
### args: 
###     - key: your private key
###     - userId: Id of user to return
###     - email: email of user to return
###     - startPos: The starting index of the list to return. Defaults to 0.
### returns: User's TODOs as JSON dictionary
def getToDos(key, userId="", email="", startPos=0):
    
### Returns details for up to 200 routes.
### args: 
###     - key: your private key
###     - routeIds: A comma-separated list of route IDs, up to 100
### returns: details for up to 200 routes as JSON dictionary
def getRoutes(key, routeIDs):
    
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
def getRoutesForLatLon(key, lat, lon, maxDistance=30, maxResults=50, minDiff=5.0, maxDiff=5.16):

def main():
    #routesFromTicks(getTicks("jacktlange@gmail.com"))
    route = routeFromId("105715550")
    print(route["name"])
main()
    
