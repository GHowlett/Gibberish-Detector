import os
from gib_detect_train import train

gib_model_file = os.path.join(os.path.dirname(__file__),'gib_model.pki')
if not os.path.exists(gib_model_file):
	train()

from gib_detect import is_gibberish
	
