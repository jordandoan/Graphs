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
# visited_rooms.add(player.current_room)
# def travel(player):
#     if player.current_room in visited_rooms:
#         return
#     else:
#         visited_rooms.add(player.current_room)
#         room = player.current_room
#         if player.current_room.n_to is not None:
#             player.travel('n')
#             travel(player)
#             player.current_room = room
#             traversal_path.extend(['n','s'])
#         if player.current_room.w_to is not None:
#             player.travel('w')
#             travel(player)
#             player.current_room = room
#             traversal_path.extend(['w', 'e'])
#         if player.current_room.e_to is not None:
#             player.travel('e')
#             travel(player)
#             player.current_room = room
#             traversal_path.extend(['e', 'w'])
#         if player.current_room.s_to is not None:
#             player.travel('s')
#             travel(player)
#             player.current_room = room
#             traversal_path.extend(['s', 'n'])
dirs = {'n_to':'n', 'w_to': 'w', 'e_to':'e', 's_to':'s'}
opposite = {'s':'n', 'w':'e', 'n':'s', 'e':'w'}
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
bfs_travel(player)
# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

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
