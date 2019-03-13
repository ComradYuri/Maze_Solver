# see mazes.py for collection of mazes
import mazes


def escape(maze):
    # 1. finds player orientation, player coords, and target coords.    lines: 13-22, 126-137
    # 2. uses bread first search to construct a path.                   lines: 23-37, 102-123
    # 3. construct a move set from the coords in path.                  lines: 38-101
    print("\nMaze that has to be solved:\n")
    for row in maze:
        print(row)
    print("\n\n")
    target = get_targetvalues(maze)
    for i, row in enumerate(maze):
        if "^" in row:
            pointer = (0, (i, row.find("^")))
        elif ">" in row:
            pointer = (1, (i, row.find(">")))
        elif "v" in row:
            pointer = (2, (i, row.find("v")))
        elif "<" in row:
            pointer = (3, (i, row.find("<")))
    path = [pointer[1]]
    vertex_and_path = [pointer[1], path]
    bfs_queue = [vertex_and_path]
    moves = []
    visited = set()
    while bfs_queue:
        current_loc, path = bfs_queue.pop(0)
        visited.add(current_loc)
        fields = get_neighbors(current_loc, maze)
        locs = get_neighbors_locs(current_loc)
        for i, v in enumerate(fields):
            if v == " ":
                if locs[i] not in visited:
                    if locs[i] in target:
                        path += [locs[i]]
                        for j in range(len(path) - 1):
                            if path[j][1] < path[j + 1][1]:
                                # went right
                                if pointer[0] == 3:
                                    moves += ["B", "F"]
                                if pointer[0] == 2:
                                    moves += ["L", "F"]
                                if pointer[0] == 1:
                                    moves += ["F"]
                                if pointer[0] == 0:
                                    moves += ["R", "F"]
                                pointer = (1, (path[j]))
                            if path[j][1] > path[j + 1][1]:
                                # went left
                                if pointer[0] == 3:
                                    moves += ["F"]
                                if pointer[0] == 2:
                                    moves += ["R", "F"]
                                if pointer[0] == 1:
                                    moves += ["B", "F"]
                                if pointer[0] == 0:
                                    moves += ["L", "F"]
                                pointer = (3, (path[j]))
                            if path[j][0] < path[j + 1][0]:
                                # went down
                                if pointer[0] == 3:
                                    moves += ["L", "F"]
                                if pointer[0] == 2:
                                    moves += ["F"]
                                if pointer[0] == 1:
                                    moves += ["R", "F"]
                                if pointer[0] == 0:
                                    moves += ["B", "F"]
                                pointer = (2, (path[j]))
                            if path[j][0] > path[j + 1][0]:
                                # went up
                                if pointer[0] == 3:
                                    moves += ["R", "F"]
                                if pointer[0] == 2:
                                    moves += ["B", "F"]
                                if pointer[0] == 1:
                                    moves += ["L", "F"]
                                if pointer[0] == 0:
                                    moves += ["F"]
                                pointer = (0, (path[j]))
                        print("Solved Maze:\n")
                        maze_solved_listed = []
                        for x, m in enumerate(maze):
                            maze_solved_listed.append(
                                [maze[x][y] if (x, y) not in path else "o" for y in range(len(m))]
                                                        )
                        maze_solved_str = []
                        for row in maze_solved_listed:
                            maze_solved_str.append("".join(row))
                        for row in maze_solved_str:
                            print(row)
                        print("""\nMove set:
F = move one step forward
L = turn 90 degrees to left
R = turn 90 degrees to right
B = turn around 180 degrees
                            """)
                        print(moves)
                        return moves
                    else:
                        bfs_queue.append([locs[i], path + [locs[i]]])
    return []


def get_neighbors(pointer, maze):
    try:
        up = maze[pointer[0] - 1][pointer[1]]
        right = maze[pointer[0]][pointer[1] + 1]
        down = maze[pointer[0] + 1][pointer[1]]
        left = maze[pointer[0]][pointer[1] - 1]
        return (up, right, down, left)
    except IndexError:
        return -1


def get_neighbors_locs(pointer):
    up = (pointer[0] - 1, pointer[1])
    right = (pointer[0], pointer[1] + 1)
    down = (pointer[0] + 1, pointer[1])
    left = (pointer[0], pointer[1] - 1)
    return up, right, down, left


def get_targetvalues(maze):
    targets = []
    if maze[0].find(" ") != -1:
        targets.append((0, maze[0].find(" ")))
    for i, row in enumerate(maze):
        if row[0] == " ":
            targets.append((i, 0))
        if row[-1] == " ":
            targets.append((i, len(row) - 1))
    if maze[-1].find(" ") != -1:
        targets.append((len(maze) - 1, maze[-1].find(" ")))
    return targets


escape(mazes.maze15)
escape(mazes.maze24)
