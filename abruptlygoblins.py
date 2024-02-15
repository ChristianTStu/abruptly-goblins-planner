# Instructions: Step 1
gamers_list = []

# Instructions: Step 2
def add_gamer(gamer):
    if list(gamer.keys()) == ['name', 'availability']:
        gamers_list.append(gamer)

add_gamer({'name': 'Kimberly', 'availability': ['Monday', 'Tuesday', 'Friday']})
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]})
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]})
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]})
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]})
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]})
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]})
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]})
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]})


