import itertools
from Tabris import generate_sequences, generate_A_sequence, generate_Y_sequence 
from Hashim import estimate_parameters

def main(S):
    A, Y = generate_sequences(S)
    s1 = S[0]
    s2 = S[1]
    s3 = S[2]
    s4 = S[3]

    rand_best_model, max_prob = estimate_parameters(A, Y, s1, s1, s3, s4)

    return rand_best_model, max_prob