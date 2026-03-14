import itertools

def generate_sequences(S):
    n = len(S) # 4
    
    A = generate_A_sequence(0, 0, [], n, [])
    Y = generate_Y_sequence(n, [])
    
    return A, Y

def generate_A_sequence(curr_step, curr_X, curr_path, n, A):
        if curr_step == n:
            A.append(curr_path)
            return
        for move in [-1, 1]:
            next_X = curr_X + move
            next_A = (next_X % 5) - 2
            curr_path.append(next_A)
            generate_A_sequence(curr_step+1, next_X, curr_path)


def generate_Y_sequence(n, Y):
    move = [-1, 1]
    Y.append([list(seq) for seq in itertools.product(moves, repeat = n)])
    