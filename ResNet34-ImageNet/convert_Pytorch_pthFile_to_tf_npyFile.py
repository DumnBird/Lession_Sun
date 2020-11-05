import torch
import numpy as np


bin_path = 'F:/resnet34-333f7ec4.pth'
ckpt_path = 'bert_model.ckpt'

dictionary = {}

for var_name, value in torch.load(bin_path).items():


    numpy_value = value.data.numpy()
    if len(numpy_value.shape)==4:
        numpy_value = np.transpose(numpy_value, [2,3,1,0])
    dictionary[var_name] = numpy_value
 
np.save('resnet34.npy', dictionary)




