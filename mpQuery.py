# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 16:03:33 2019

@author: Jack
"""

#TODO: function headers
import requests
import json
#private user key
privateKey = '112446503-8924701af82f2e439e9312357672ca8d'
#make an enum for query types and a function for getURL
def getTicks(userEmail):
    baseURL = "https://www.mountainproject.com/data/get-ticks?email=" 
    queryURL = baseURL + userEmail + "&key=" + privateKey
    response = requests.get(queryURL)
    queryResultFile = open(userEmail + "_ticks.txt", "w+")
    queryResultFile.write(response.text)
    queryResultFile.close()
    #check for success of query and write
    return response.text
    
def routesFromTicks(ticks):
    ticks = json.loads(ticks)
    tickedRoutes = ticks["ticks"]
    for route in tickedRoutes:
        print(route["routeId"])
        
def routeFromId(Id):
    baseURL = "https://www.mountainproject.com/data/get-routes?routeIds=" 
    queryURL = baseURL + Id + "&key=" + privateKey
    response = requests.get(queryURL)
    route = json.loads(response.text)["routes"][0]
    return route
    
def main():
    #routesFromTicks(getTicks("jacktlange@gmail.com"))
    route = routeFromId("105715550")
    print(route["name"])
main()
    
