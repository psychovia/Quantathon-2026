import random
def estimate_parameters(possible_A_seqs, possible_Y_seqs, s1, s2, s3, s4):
    target_S = (s1, s2, s3, s4)
    models = [(0,0), (0,1), (1,0), (1,1)]
    likelihoods=[]

    total_combs = len(possible_A_seqs) * len(possible_Y_seqs)

    for alpha, sigma in models:
        valid_num = 0

        for A_Seq in possible_A_seqs:
            for Y_Seq in possible_Y_seqs:
                S_i = 0
                Y_prev = 0
                matches = True

                for i in range(4):
                    A_i = A_seq[i]
                    Y_i = Y_seq[i]

                    S_change = alpha * A_n + sigma * (Y_i - Y_prev)
                    S_i += delta_S

                    if S_i != target_S[i]:
                        match = False
                        break

                    Y_prev = Y_i

                if match:
                    valid_num += 1
        likelihoods[(alpha, sigma)] = valid_num/total_combs

    
    
    max_prob = max(likelihoods.values())

    best_models = [model for model, p in likelihoods.items() if p == max_prob]

    rand = len(best_models)
    rand_best_model = best_models[random.randint(0,len(best_models - 1))]

    return rand_best_model, max_prob


