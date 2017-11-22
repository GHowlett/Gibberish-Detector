#!/usr/bin/python

import pickle
import gib_detect_train
import os

gib_model_file = os.path.join(os.path.dirname(__file__),'gib_model.pki')
model_data = pickle.load(open(gib_model_file, 'rb'))
model_mat = model_data['mat']
threshold = model_data['thresh']

def is_gibberish(string):
    return gib_detect_train.avg_transition_prob(string, model_mat) <= threshold

if __name__ == "__main__":
    print 'threshold: ' + str(threshold)
    while True:
        input = raw_input()
        prob = gib_detect_train.avg_transition_prob(input, model_mat)
	print('prob: ' + str(prob))
        print('gibberish? ' + str(is_gibberish(input)))

