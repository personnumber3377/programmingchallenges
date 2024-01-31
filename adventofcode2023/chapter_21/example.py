
LOOP_COUNT = 20

def get_neig(pos: tuple) -> list:
    return [tuple((pos[0]-1, pos[1])), tuple((pos[0]+1, pos[1])), tuple((pos[0], pos[1]-1)), tuple((pos[0], pos[1]+1))] # Non-diagonal neighbours only.

def render_positions(positions: set):
    mat = [["." for _ in range(20)] for _ in range(20)]
    for pos in positions:
        print(pos)
        mat[pos[1]][pos[0]] = "#"
    for line in mat:
        print("".join(line))
    return

def main() -> int:
    
    visited = set([tuple((10,10))])
    new_positions = [tuple((10,10))] # Initialize with the one position
    for i in range(LOOP_COUNT):
        # Main loop.
        # Get new spots.
        new_new = []
        for pos in new_positions: # optimization. no need to loop over positions which aren't new.
            neighbours = get_neig(pos)
            for neig in neighbours:
                #if neig not in visited: # No need to check. the "add" method doesn't do anything if element already is in set.
                assert isinstance(neig, tuple)
                visited.add(neig)
                new_new.append(neig)
        new_positions = new_new
        # Render.
        print("visited == "+str(visited))
        render_positions(visited)

    return 0

if __name__=="__main__":
    exit(main())
