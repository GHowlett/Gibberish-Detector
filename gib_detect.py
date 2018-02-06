#!/usr/bin/python

import pickle
import gib_detect_train
import os
import sys

gib_model_file = os.path.join(os.path.dirname(__file__),'gib_model.pki')
if not os.path.isfile(gib_model_file): gib_detect_train.train()
model_data = pickle.load(open(gib_model_file, 'rb'))
model_mat = model_data['mat']
threshold = model_data['thresh']

def is_gibberish(string):
    return gib_detect_train.avg_transition_prob(string, model_mat, threshold) <= threshold

if __name__ == "__main__":
    if len(sys.argv) > 1: sys.exit(not is_gibberish(sys.argv[1]))
    
    print('threshold: ' + str(threshold))
    while True:
        input = raw_input()
        prob = gib_detect_train.avg_transition_prob(input, model_mat, threshold)
	print('prob: ' + str(prob))
        print('gibberish? ' + str(is_gibberish(input)))

