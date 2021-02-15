def run_langton(rules, size):
    num = 0

    commands = {}
    grid = []
    grid_coordinates = []
    ant_rot = ''
    ant_dir = 'up'
    ant_pos = [size//2, size//2]

    count = 0


    for letra in rules:
        commands[num] = letra
        num += 1

    for i in range(size):
        linha = []
        for j in range(size):
            linha.append(0)

        grid.append(linha)

    for i in range(size):
        for j in range(size):
            pos = []
            pos.append(i)
            pos.append(j)
            grid_coordinates.append(pos)

    while ant_pos in grid_coordinates:
        ant_rot = ant_set_rotation(grid, commands, ant_pos)
        ant_dir = ant_set_direction(commands, ant_rot, ant_dir)
        ant_walk(ant_pos, ant_dir)
        count += 1

    return count, grid
    
def ant_walk(ant_position, ant_direction):
    if ant_direction == 'up':
        ant_position[1] -= 1

    elif ant_direction == 'down':
        ant_position[1] += 1
    
    elif ant_direction == 'right':
        ant_position[0] -= 1
    
    elif ant_direction == 'left':
        ant_position[0] += 1

def ant_set_rotation(grid, commands, ant_position):
    
    if grid [ant_position[0]] [ant_position[1]] > len(commands.keys()) - 1:
        grid [ant_position[0]] [ant_position[1]] %= len(commands.keys())     

    color = grid[ ant_position[0]] [ant_position[1]]
    grid [ant_position[0]] [ant_position[1]] += 1

    if grid [ant_position[0]] [ant_position[1]] == len(commands.keys()):
        grid[ ant_position[0]] [ant_position[1]] = 0

    return commands[color]

def ant_set_direction(commands, ant_rotation, ant_direction):

    if ant_rotation == 'L':

        if ant_direction == 'up':
            return 'left'

        elif ant_direction == 'down':
            return 'right'
        
        elif ant_direction == 'right':
            return 'up'
        
        elif ant_direction == 'left':
            return 'down'
    
    elif ant_rotation=='R':

        if ant_direction == 'up':
            return 'right'

        elif ant_direction == 'down':
            return 'left'
        
        elif ant_direction == 'right':
            return 'down'
        
        elif ant_direction == 'left':
            return 'up'
    
    elif ant_rotation == '':
        return ant_direction

print(run_langton('RLRR', 51))