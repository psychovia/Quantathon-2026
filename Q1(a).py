import itertools
import estimate_parameters from Hashim
import generate_sequences, generate_A_sequence, generate_Y_sequence from Tabris


def main(S):
    A, Y = generate_sequences(S)
    s1 = S[0]
    s2 = S[1]
    s3 = S[2]
    s4 = S[3]

    x, y = estimate_parameters(A, Y, s1, s1, s3, s4)

    return