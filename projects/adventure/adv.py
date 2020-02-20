from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
import collections

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
dirs = {'n_to':'n', 'w_to': 'w', 'e_to':'e', 's_to':'s'}
keys = ['n_to', 'w_to', 'e_to', 's_to']
opposite = {'s':'n', 'w':'e', 'n':'s', 'e':'w'}
traversal_graph = collections.defaultdict(dict)
# def new_travel(room, direction=None, prev=None):
#     if room.id not in traversal_graph:
#         for exit in room.get_exits():
#             traversal_graph[room.id][exit] = '?'
#     if direction and traversal_graph[room.id][direction] == '?':
#         traversal_graph[room.id][direction] = prev.id
#     for dir in keys:
#         #n, w, s, e
#         direction = dirs[dir]
#         if room.get_room_in_direction(direction) is not None:
#             next_room = room.get_room_in_direction(direction)
#             if traversal_graph[room.id][direction] == '?':
#                 traversal_graph[room.id][direction] = next_room.id
#                 traversal_path.append(direction)
#                 new_travel(next_room, opposite[direction], room)
#                 traversal_path.append(opposite[direction])
degrees = {}
def bfs_degrees(room):
    q = collections.deque()
    q.append((player.current_room, player.current_room))
    while q:
        for _ in range(len(q)):
            room, prev = q.popleft()
            if room not in visited_rooms:
                visited_rooms.add(room)
                player.current_room = room
                traversal_path.append(room.id)
                for dir in dirs:
                    if getattr(player.current_room, dir, None) is not None:
                        player.travel(dirs[dir])
                        q.append((player.current_room, room))
                        player.travel(opposite[dirs[dir]])
                player.current_room = prev
                traversal_path.append(player.current_room.id)
def new_travel(room, came_from=None, prev=None):
    if len(traversal_graph) == 500:
        return
    if room.id not in traversal_graph:
        for exit in room.get_exits():
            traversal_graph[room.id][exit] = '?'
    if came_from and traversal_graph[room.id][came_from] == '?':
        traversal_graph[room.id][came_from] = prev.id
    while any(traversal_graph[room.id][dir] == '?' for dir in traversal_graph[room.id]):
        dir = random.choice(keys)
        #n, w, s, e
        direction = dirs[dir]
        if room.get_room_in_direction(direction) is not None:
            next_room = room.get_room_in_direction(direction)
            if traversal_graph[room.id][direction] == '?':
                traversal_graph[room.id][direction] = next_room.id
                traversal_path.append(direction)
                new_travel(next_room, opposite[direction], room)
                if len(traversal_graph) == 500:
                    return
                traversal_path.append(opposite[direction])
# new_travel(player.current_room)
travrooms = [player.current_room.id]
def new_travel2(room, came_from=None, prev=None):
    if len(traversal_graph) == 500:
        return
    if room.id not in traversal_graph:
        for exit in room.get_exits():
            traversal_graph[room.id][exit] = '?'
    if came_from:
        traversal_graph[room.id][came_from] = prev.id
    exits = room.get_exits()
    exits.sort(key=lambda k: len(room.get_room_in_direction(k).get_exits()))
    for direction in exits:
        if room.get_room_in_direction(direction) is not None:
            if traversal_graph[room.id][direction] == '?':
                next_room = room.get_room_in_direction(direction)
                traversal_graph[room.id][direction] = next_room.id
                traversal_path.append(direction)
                travrooms.append(next_room.id)
                new_travel2(next_room, opposite[direction], room)
                if len(traversal_graph) == 500:
                    return
                traversal_path.append(opposite[direction])
                travrooms.append(room.id)
new_travel2(player.current_room)
print(travrooms)
def dfs_travel(player):
    visited_rooms.add(player.current_room)
    for dir in dirs:
        if getattr(player.current_room, dir, None) is not None:
            if getattr(player.current_room, dir) not in visited_rooms:
                room = player.current_room
                player.travel(dirs[dir])
                traversal_path.append(dirs[dir])
                dfs_travel(player)
                player.current_room = room
                traversal_path.append(opposite[dirs[dir]])
# dfs_travel(player)
def bfs_travel(player):
    q = collections.deque()
    q.append((player.current_room, player.current_room))
    while q:
        for _ in range(len(q)):
            room, prev = q.popleft()
            if room not in visited_rooms:
                visited_rooms.add(room)
                player.current_room = room
                traversal_path.append(room.id)
                for dir in dirs:
                    if getattr(player.current_room, dir, None) is not None:
                        player.travel(dirs[dir])
                        q.append((player.current_room, room))
                        player.travel(opposite[dirs[dir]])
                player.current_room = prev
                traversal_path.append(player.current_room.id)
# bfs_travel(player)
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

print(traversal_path)
if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
