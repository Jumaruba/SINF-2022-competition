l1 = input().split()
l2 = input().split()
[kx, ky] = [int(l1[0]), int(l1[1])]
[cx, cy] = [int(l2[0]), int(l2[1])]

def diff_positions(k_pos, c_pos):
    [kx, ky] = k_pos
    [cx, cy] = c_pos
    return abs(kx - cx) + abs(ky - cy)

def search(k_pos, c_pos, depth = 0):
    [cx, cy] = c_pos
    queue = [(k_pos,0)]
    visited = [queue[0]]
    while queue:
        ([kx, ky], depth) = queue[0]
        if kx == cx and ky == cy:
            return depth
        queue = queue[1:]
        if [kx, ky] in visited:
            continue
        visited.append([kx, ky])
        knight_moves = [[kx + 1, ky + 2], [kx + 1, ky - 2], [kx - 1, ky + 2], [kx - 1, ky - 2], [kx + 2, ky + 1], [kx + 2, ky - 1], [kx - 2, ky + 1], [kx - 2, ky - 1]]
        knight_moves.sort(key = lambda x: diff_positions(x, c_pos))
        for move in knight_moves:
            queue.append((move, depth + 1))
    return -1

print(search([kx, ky], [cx, cy]))