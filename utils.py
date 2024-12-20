
def update_map(dynamic_map, new_position, prev_position):
    
    if new_position == prev_position:
        return
    # marking previous position as explored
    if prev_position in dynamic_map:
        dynamic_map[prev_position] = '.'

    # current position as robot position
    dynamic_map[new_position] = 'R'

def print_map(dynamic_map, cell_size = 10):
    if not dynamic_map:
        print("Map is empty!!")
        return
    
    # finding outer bounds of explored map
    min_x = min(coord[0] for coord in dynamic_map.keys())
    max_x = max(coord[0] for coord in dynamic_map.keys())
    min_y = min(coord[1] for coord in dynamic_map.keys())
    max_y = max(coord[1] for coord in dynamic_map.keys())

    
    condensed_map = {}
    for (x, y), value in dynamic_map.items():
        condensed_x = x // cell_size
        condensed_y = y // cell_size
        if (condensed_x, condensed_y) not in condensed_map or value == 'R':
            condensed_map[(condensed_x, condensed_y)] = value

    condensed_min_x = min(coord[0] for coord in condensed_map.keys())
    condensed_max_x = max(coord[0] for coord in condensed_map.keys())
    condensed_min_y = min(coord[1] for coord in condensed_map.keys())
    condensed_max_y = max(coord[1] for coord in condensed_map.keys())

    for y in range(condensed_min_y, condensed_max_y + 1):
        row = []
        for x in range(condensed_min_x, condensed_max_x + 1):
            row.append(condensed_map.get((x, y), '.'))  # Default to unexplored
        print(row)  # Print each row as a Python list

