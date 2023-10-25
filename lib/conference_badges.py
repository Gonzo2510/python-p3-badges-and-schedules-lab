def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(badge_maker(name))
    return badges

    #badges = [badge_maker(name) for name in names]
    
def assign_rooms(names):
    greeting_with_room_assignments = []
    count = 1
    for name in names:
        greeting_with_room_assignments.append(f"Hello, {name}! You'll be assigned to room {count}!")
        count += 1
    return greeting_with_room_assignments

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for room in assign_rooms(names):
        print(room)
