import torch
import numpy as np

# data =[[1,2],[3,4]]
# x_data= torch.tensor(data)
# np_array =np.array(data)
# x_np=torch.from_numpy(np_array)
# print(x_data)
# print(x_np)

# x_ones= torch.ones_like(x_data)
# x_rand= torch.rand_like(x_data, dtype=torch.float)
# print(x_ones)
# print(x_rand)

n=np.ones(5)
print(n)
t=torch.from_numpy(n)
np.add(n,1,n)
print(t)