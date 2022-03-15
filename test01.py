import torch
from torch import einsum
a=torch.randint(0,4,(4,3,2))
#print(a)
b=torch.ones(4,4)
c=torch.ones(6,7,8)
d=torch.ones(3,4)
x,y=torch.randn(5),torch.randn(5)
#z=torch.einsum('ij,ij->ij', a,b)
z=torch.einsum('ijk->ikj',a)

A = torch.randint(1,3,(3,2,1))
l = torch.randint(1,3,(2,2))
r = torch.randint(1,3,(2,1))
print(A)
print(l)
print(r)
z=torch.einsum('bn,anm,bm->ba', l, A, r)
print(z)