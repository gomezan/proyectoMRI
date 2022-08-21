from __future__ import print_function, division, absolute_import, unicode_literals

import os
import shutil
import numpy as np
import logging

import tensorflow as tf

from DCSRNyunzeman.tf_dcsrn.dcsrn import DCSRN,Trainer
from DCSRNyunzeman.tf_dcsrn.image_util import MedicalImageDataProvider

output_path = r"C:\Users\Estudiante\Documents\datasetMRI\snapchat"
# path of dataset, here is the HCP dataset
dataset_HCP = r"C:\Users\Estudiante\Documents\datasetMRI\Aug"

#preparing data loading, you may want to explicitly note the glob search path on you data 
data_provider = MedicalImageDataProvider()

print("\ndata_provider initialization over.\n")

# setup & training
net = DCSRN(channels=1)

print("\nGraph set over.\n")

trainer = Trainer(net)

print("\nBegin to train.\n")

path = trainer.train(data_provider, output_path, restore = True)

print("\nTraining process is over.\n")

# verification, randomly test 4 images
test_provider = MedicalImageDataProvider()
test_x, test_y = test_provider(4)
result = net.predict(path, test_x)