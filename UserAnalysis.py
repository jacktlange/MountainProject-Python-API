# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:14:34 2019

@author: Jack
"""

from MountainProjectPublicAPI import *

def getAllTicks(privateKey, userId):
    maxTicksReturned = 200
    tickIndex = 0
    ticks = []
    while True:
        ticksQuery = getTicks(privateKey, email = "jacktlange@gmail.com", startPos = tickIndex)["ticks"]
        ticks.extend(ticksQuery)
        tickIndex += maxTicksReturned
        if len(ticksQuery) != 200:
            break
    return ticks

#take ticks as an array of route IDs
def ticksToRoutes(privateKey, ticks):
    routes = []
    separator = ","
    i = 0
    maxRouteQuery = 100
    tickIds = list(map(lambda x: str(x["routeId"]), ticks))
    while i < len(ticks):
        routeIds = separator.join(tickIds[i:i + maxRouteQuery])
        i += maxRouteQuery
        routes.extend(getRoutes(privateKey, routeIds)["routes"])
#fewer routes may be returned than the number of ticks because duplicate ticks in the same 100
#only return one route
    return routes
    
def sent(tick):
    if tick["leadStyle"] == "Flash" or tick["leadStyle"] == "Redpoint" or tick["leadStyle"] == "Onsight":
        return True
    else:
        return False
        
def gradePyramid(privateKey, userEmail):
    groupedGrades = {"5.10-":["5.10a","5.10a/b", "5.10-", "5.10b",
                               "5.10a PG13","5.10a/b PG13", "5.10- PG13", "5.10b PG13",
                               "5.10a R","5.10a/b R", "5.10- R", "5.10b R",],
                               
                     "5.10":["5.10", "5.10b/c",
                              "5.10 PG13", "5.10b/c PG13"
                              "5.10 R", "5.10b/c R"],
                      
                     "5.10+":["5.10c", "5.10+","5.10c/d", "5.10d",
                               "5.10c PG13", "5.10+ PG13","5.10c/d PG13", "5.10d PG13",
                               "5.10c R", "5.10+ R","5.10c/d R", "5.10d R"],
                     "5.11-":["5.11a","5.11a/b", "5.11-", "5.11b",
                               "5.11a PG13","5.11a/b PG13", "5.11- PG13", "5.11b PG13",
                               "5.11a R","5.11a/b R", "5.11- R", "5.11b R",],
                               
                     "5.11":["5.11", "5.11b/c",
                              "5.11 PG13", "5.11b/c PG13"
                              "5.11 R", "5.11b/c R"],
                      
                     "5.11+":["5.11c", "5.11+","5.11c/d", "5.11d",
                               "5.11c PG13", "5.11+ PG13","5.11c/d PG13", "5.11d PG13",
                               "5.11c R", "5.11+ R","5.11c/d R", "5.11d R"],
                               
                     "5.12-":["5.12a","5.12a/b", "5.12-", "5.12b",
                               "5.12a PG13","5.12a/b PG13", "5.12- PG13", "5.12b PG13",
                               "5.12a R","5.12a/b R", "5.12- R", "5.12b R",],
                     "5.12":["5.12", "5.12b/c",
                              "5.12 PG13", "5.12b/c PG13"
                              "5.12 R", "5.12b/c R"],
                      
                     "5.12+":["5.12c", "5.12+","5.12c/d", "5.12d",
                               "5.12c PG13", "5.12+ PG13","5.12c/d PG13", "5.12d PG13",
                               "5.12c R", "5.12+ R","5.12c/d R", "5.12d R"],
                               
                    "5.13-":["5.13a","5.13a/b", "5.13-", "5.13b",
                               "5.13a PG13","5.13a/b PG13", "5.13- PG13", "5.13b PG13",
                               "5.13a R","5.13a/b R", "5.13- R", "5.13b R",],
                     "5.13":["5.13", "5.13b/c",
                              "5.13 PG13", "5.13b/c PG13"
                              "5.13 R", "5.13b/c R"],
                      
                     "5.13+":["5.13c", "5.13+","5.13c/d", "5.13d",
                               "5.13c PG13", "5.13+ PG13","5.13c/d PG13", "5.13d PG13",
                               "5.13c R", "5.13+ R","5.13c/d R", "5.13d R"],
                    }
                     
    user = getUser(privateKey, userEmail)
    ticks = getAllTicks(privateKey, str(user["id"]))
    #filter ticks for redpoint, flash, onsight
    sentTicks = list(filter(sent, ticks))
    tradDates = {}
    sportDates = {}
    
    sentRoutes = ticksToRoutes(privateKey, sentTicks)
    #sort sent routes by grade, print out number at each grade
    sentRoutesByGrade = {}
    for route in sentRoutes:
        grade = route["rating"]
        if grade in sentRoutesByGrade:
            sentRoutesByGrade[grade].append(route)
        else:
            sentRoutesByGrade[grade] = []
            sentRoutesByGrade[grade].append(route)
    for gradeGroup,value in groupedGrades.items():
        sentRoutes = []
        for grade in value:
                
            if grade in sentRoutesByGrade:
                sentRoutes.extend(sentRoutesByGrade[grade])
        
        print(gradeGroup)
        print("sent routes " + str(len(sentRoutes)))
        print(list(map(lambda x: x["name"],sentRoutes)))
        
def climbingStyles(privateKey, userEmail):
    user = getUser(privateKey, userEmail)
    ticks = getAllTicks(privateKey, str(user["id"]))
    #group ticks by date - dictionary
    ticksByDate = {}
    for tick in ticks:
        tickDate = tick["date"]
        if tickDate in ticksByDate:
            ticksByDate[tickDate].append(tick)
        else:
            ticksByDate[tickDate] = []
            ticksByDate[tickDate].append(tick)
   
    #translate ticks into routes
    typeCounter = {"trad": 0, "sport": 0, "mixed": 0}
    for date,ticks in ticksByDate.items():
        #todo: want a more efficient way to do this translation
        routes = ticksToRoutes(privateKey, ticks)
        tickTypes = list(map(lambda x: x["type"], routes))
        if "Trad" in tickTypes and "Sport" not in tickTypes:
            typeCounter["trad"] += 1
        if "Trad" not in tickTypes and "Sport" in tickTypes:
            typeCounter["sport"] += 1
        if "Trad" in tickTypes and "Sport" in tickTypes:
            typeCounter["mixed"] += 1
    print(typeCounter)

    
