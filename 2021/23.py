import functools
import heapq
import itertools

amphipod_energy = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

amphipod_room_col = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8,
}

room_target = {v: k for k, v in amphipod_room_col.items()}

room_locations = [0, 1, 3, 5, 7, 9, 10]


@functools.cache
def is_path_between(start_location, target_location, state):
    direction = 1 if target_location > start_location else -1
    for i in range(start_location + direction, target_location + direction, direction):
        if i in room_locations and state[i] != '.':
            return False
    return True


@functools.cache
def get_neighbours(state, depth_room=2):
    neighbours_with_cost = []
    for location in room_locations:
        amphipod = state[location]
        if amphipod == '.':
            continue
        target_location = amphipod_room_col[amphipod]
        valid_targets = [amphipod * i for i in range(depth_room)]
        target_available = state[target_location] in valid_targets
        target_cost = depth_room - len(state[target_location])
        if not target_available:
            continue
        if is_path_between(location, target_location, state):
            new_state = list(state)
            new_state[location] = '.'
            new_state[target_location] = amphipod + new_state[target_location]
            cost = (target_cost + abs(target_location - location)) * amphipod_energy[amphipod]
            neighbours_with_cost.append((tuple(new_state), cost))
    for location in amphipod_room_col.values():
        room = state[location]
        if room in [room_target[location] * i for i in range(depth_room + 1)]:
            continue
        amphipod = room[0]
        start_cost = depth_room + 1 - len(room)
        target_location = amphipod_room_col[amphipod]
        valid_targets = [amphipod * i for i in range(depth_room)]
        target_available = state[target_location] in valid_targets
        target_cost = depth_room - len(state[target_location])
        if target_available:
            if is_path_between(location, target_location, state):
                new_state = list(state)
                new_state[location] = room[1:]
                new_state[target_location] = amphipod + new_state[target_location]
                cost = (target_cost + abs(target_location - location) + start_cost) * amphipod_energy[amphipod]
                neighbours_with_cost.append((tuple(new_state), cost))
        for target_location in room_locations:
            target_available = state[target_location] == '.'
            if not target_available:
                continue
            if is_path_between(location, target_location, state):
                new_state = list(state)
                new_state[location] = room[1:]
                new_state[target_location] = amphipod
                cost = (abs(target_location - location) + start_cost) * amphipod_energy[amphipod]
                neighbours_with_cost.append((tuple(new_state), cost))
    return neighbours_with_cost


class Heap:
    def __init__(self):
        self.heap = []
        self.entry_finder = {}
        self.counter = itertools.count()

    def heap_push(self, priority, obj):
        if obj in self.entry_finder:
            self.remove(obj)
        count = next(self.counter)
        entry = [priority, count, obj]
        self.entry_finder[obj] = entry
        heapq.heappush(self.heap, entry)

    def remove(self, obj):
        entry = self.entry_finder.pop(obj)
        entry[-1] = None

    def heap_pop(self):
        while self.heap:
            priority, count, obj = heapq.heappop(self.heap)
            if obj is not None:
                del self.entry_finder[obj]
                return priority, obj
        raise KeyError("Pop from an empty heap")


def solve(data):
    state = ('.', '.', data[0], '.', data[1], '.', data[2], '.', data[3], '.', '.')
    goal_state = ('.', '.', "AAAA", '.', "BBBB", '.', "CCCC", '.', "DDDD", '.', '.')
    dists = {}
    visited = set()
    heap = Heap()
    heap.heap_push(0, state)

    while True:
        d, state = heap.heap_pop()
        if state == goal_state:
            return d
        visited.add(state)
        for neighbour, cost in get_neighbours(state, depth_room=4):
            alt = d + cost
            if neighbour not in visited:
                if neighbour not in dists:
                    dists[neighbour] = alt
                    heap.heap_push(alt, neighbour)
                elif alt < dists[neighbour]:
                    dists[neighbour] = alt
                    heap.remove(neighbour)
                    heap.heap_push(alt, neighbour)


data = ["DDDB", "BCBD", "ABAA", "CACC"]

if __name__ == '__main__':
    print(solve(data))
