gamers_list = []

def add_gamer(gamer):
    if list(gamer.keys()) == ['name', 'availability']:
        gamers_list.append(gamer)

def build_daily_frequency_table():
    return {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0
    }

count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer['availability']:
            available_frequency[day] += 1

def find_best_night(availability_table):
    return list(count_availability.keys())[list(count_availability.values()).index(max(count_availability.values()))]

def available_on_night(gamers_list, day):
    available_gamers = []
    for gamer in gamers_list:
        if day in gamer['availability']:
            available_gamers.append(gamer)
    return available_gamers

add_gamer({'name': 'Kimberly', 'availability': ['Monday', 'Tuesday', 'Friday']})
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]})
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]})
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]})
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]})
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]})
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]})
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]})
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]})

calculate_availability(gamers_list, count_availability)

game_night = find_best_night(count_availability)
print(game_night)

attending_game_night = available_on_night(gamers_list, game_night)
print(attending_game_night)