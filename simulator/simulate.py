#!/usr/bin/env python3

import json
import requests
import random
import sys
import time

BASE_URL = "http://10.2.108.20:8080"

# Make an API call to increment the count
def car_arrives(garage, level):
    post_data = create_payload(garage, level)
    r = requests.post(ARRIVE_URL, json = post_data)
    print (r.status_code)

# Make an API call to decrement the count
def car_departs(garage, level):
    post_data = create_payload(garage, level)
    r = requests.post(DEPART_URL, json = post_data)
    print (r.status_code)
# Create a JSON string that will be POSTed to the appropriate endpoint
def create_payload(garage, level):
    data = {}
    data['garage'] = garage
    data['lvl'] = level

    print (data)
    return data

state_map = {}
#state_map['Central'] = {}
#state_map['Creekside'] = {}
#state_map['Hilltop'] = {}
#state_map['Prom'] = {}
#
#state_map['Central']['total'] = [20, 30]
#state_map['Creekside']['total'] = [20, 30]
#state_map['Hilltop']['total'] = [30,30,20, 20]
#state_map['Prom']['total'] = [20, 20, 60]
#
#
#state_map['Central']['free'] = [20, 30]
#state_map['Creekside']['free'] = [20, 30]
#state_map['Hilltop']['free'] = [30,30,20, 20]
#state_map['Prom']['free'] = [20, 20, 60]

garages = ['Central', 'Creekside','Prom', 'Hilltop' ]

def try_arrive():
    candidate_garages = []
    for garage in garages:
        for i in state_map[garage]['free']:
            if i != 0 :
                candidate_garages.append(garage)
                break

    if candidate_garages == []:
        return

    #Simulate an arrival in one of the empty garages
    garage_choice = random.choice(candidate_garages)
    garage = garage_choice
    current_level = 0
    garage_level_array = state_map[garage_choice]['free']
    while True:
        #Car arrives at the initial level
        if garage_level_array[current_level] == 0:
            current_level += 1
            continue
        car_arrives(garage, current_level + 1)
        garage_level_array[current_level] -= 1

        higher_available=False
        #Stop if at highest level with free space
        for i in range(current_level + 1, len(garage_level_array)):
            if garage_level_array[i] > 0:
                higher_available = True
        if not higher_available:
            #Stop at this level
            print("Car stopped in garage {0} at level {1}".format(garage_choice, current_level + 1))
            return
        # Else, 20% chance of proceeding to higher level
        toss = random.random()
        if toss >= 0.6:
            print("Car stopped in garage {0} at level {1}".format(garage_choice, current_level + 1))
            return
        # Car decided to go one level above, so decrement from the current count
        car_departs(garage, current_level + 1)
        garage_level_array[current_level] += 1
        current_level += 1

def try_depart():
    # Find a random garage with nonempty space
    candidate_garages = []
    for garage in garages:
        if state_map[garage]['total'] != state_map[garage]['free']:
            candidate_garages.append(garage)
    if candidate_garages == [] :
        return
    garage_choice= random.choice(candidate_garages)
    for i in range(len(state_map[garage_choice]['total'])):
        candidate_levels = []
        if state_map[garage_choice]['total'][i] != state_map[garage_choice]['free'][i]:
            candidate_levels.append(i)

    if candidate_levels == []:
        return
    level_choice = random.choice(candidate_levels)

    #Simulate the car leaving the car
    for i in range(level_choice, 0, -1):
        car_departs(garage_choice, i + 1)
        car_arrives(garage_choice, i)
    car_departs(garage_choice, 1)
    state_map[garage_choice]['free'][level_choice] += 1

    print("Car departed from garage {0} at level {1}".format(garage_choice, level_choice + 1))

def simulate_event():
    garage = random.choice(garages)
    level = random.choice(list(range(3)))
    #TODO Assert - make sure that a car does not leave an empty garage
    #leave_or_arrive = random.choice(['leave', 'arrive'])
    leave_or_arrive = 'arrive'
    if random.random() < 0.7:
        leave_or_arrive = 'arrive'
    else:
        leave_or_arrive = 'depart'

    if leave_or_arrive == 'arrive':
        try_arrive()
    else:
        try_depart()
    for i in garages:
        print(state_map[i]['free'])
    print('***')

def event_loop():
    while True:
        simulate_event()
        time.sleep(1)


def get_state():
    url = BASE_URL + "/read"
    state = requests.get(url).json()
    for gname in state:
        state_map[gname] = {}
        larr = state[gname]['lvlarr']

        state_map[gname]['total'] = []
        state_map[gname]['free'] = []
        for i in larr:
            state_map[gname]['total'].append(i[1])
            state_map[gname]['free'].append(i[2])



if __name__ == '__main__':
    #BASE_URL = sys.argv[1]
    ARRIVE_URL = BASE_URL + "/add"
    DEPART_URL = BASE_URL + "/remove"

    get_state()

    event_loop()
