import numpy as np
import matplotlib.pyplot as plt

#17
print(np.random.rand(1))
#18
print(np.random.normal(0, 1, 15))
#19
print(np.arange(15,56)[1:-1])
#20
for i in np.nditer(np.arange(0,12).reshape(3,4)):
    print(i)
#21
print(np.linspace(5, 50, 10))
#22
a = np.arange(21)
a[(a>=9)&(a<=15)] *= -1
print(a)
#23
print(np.random.randint(0, 11, 5))
#24
print(np.array([2,3])*np.array([4,4]))
#25
print(np.arange(10,22).reshape(3,4))
#26
print(np.arange(0,12).reshape(3,4).shape)
#27
print(np.identity(3))
#28
a = np.ones((10,10))
a[1:-1, 1:-1] = 0
print(a)
#29
print(np.diag([1,2,3,4,5]))
#30
a = np.zeros((4,4))
a[::2, 1::2] = 1
a[1::2, ::2] = 1
print(a)
#31
print(np.random.random((3,3,3)))
print(np.random.rand(3,3,3))
#32
a = np.arange(1,101).reshape(10,10)
print(np.sum(a))
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))
#33
a1 = np.arange(0,6).reshape(2,3)
a2 = np.arange(0,6).reshape(3,2)
print(np.dot(a1, a2))
#34
a1 = np.arange(0,12).reshape(4,3)
a2 = np.array([1,2,3])
print(a1)
print(a2)
for r in range(len(a1)):
    a1[r,:] += a2
print(a1)
#35
a1 = np.arange(0,12).reshape(4,3)
print(a1)
np.save("35.npy", a1)
a2 = np.load("35.npy")
print(a2)
print(np.array_equal(a1, a2))
#36

#37

#38

#39
l = [1,2,3,4,5,6]
a = np.array(l)
print(type(l), type(a), type(a.tolist()))
#40
x = np.arange(0.0, 2*np.pi, 0.01)
y = np.sin(x)
# plt.plot(x,y)
# plt.show()
#41
df = np.float32(32.0)
f = df.item()
print(type(df), type(f))
#42
#43
a1 = np.array([[1,2,np.nan], [np.nan,3,4]])
print(np.isnan(a1))
#44
print(np.array_equal([1,2,3], [1,2,3]))
#45
#46
#47
print(np.random.rand(40))
#48
print(np.random.normal(200,7,40).reshape(8,5))
print(np.random.randn(8,5) * 7 + 200)
#49
print(np.random.choice(7, 5, p=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]))
print(np.random.choice(7, 5, replace=False, p=[0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]))
#50
a1 = np.random.randint(1,100,16).reshape(4,4)
a2 = a1[::-1]
print(a1)
print(a2)
#51
print(np.zeros((5,6)))
#52
a1 = np.random.randint(1,100,16).reshape(4,4)
print(a1)
print(np.sort(a1, axis=0))
print(np.sort(a1, axis=1))
#53
a1 = np.arange(0,16).reshape(4,4)
print([a1>5])
#54
a1 = np.arange(0,16).reshape(4,4)
print(np.where(a1 == 3, 1024, a1))
#55
a1 = np.arange(0,16).reshape(4,4)
print(np.zeros_like(a1))
#56
#57
#58
a1 = np.random.randint(1,100,16).reshape(4,4)
a2 = a1[::-1, ::-1]
print(a1)
print(a2)
#59
print(np.array([[0,1],[2,3]]) * np.array([[3,2],[1,0]]))