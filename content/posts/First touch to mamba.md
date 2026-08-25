---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3EANP6U%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T003319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIFY7gKCFoJtXi6A%2BTGN%2FpQhGarWuHTYzsX584QiokWIpAiEA48IdrUXP5ECF%2B2VDylvd9I%2FixNmnx0jIF5f4sfBw5qgqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL4xf4BrO1ijLwgpDircA5szYQsTyzzcDi3uhPMPK4EtYFmGd0Gc%2BGsezshkcd8lYynP1WGEWhM7pHE5ouPVP%2BD13k%2Fbx3siuqQA%2B%2BbEP%2FiYC9pYdMgoBt4Db6hMhsJV3YgU2t7bsuxEWnGTurkB6oURTHDGIpJd%2BorvZpyPubLY0mIStRQFA%2FVytWcYZlVo6xigEPKjp%2FFIvr9kgLa76FvNBVzKbY1vrRSt0KCi%2FbUzOMobgoFuwCUKueUdhxRBTl36x2iHNK34oaP70X4dAN86oYoJcoRhXKLELTS4S3L2oDR2Pq1XnFmtaVBHvYSUd%2ByGmJ7ycHe4isMwtSvoLmES2x%2FEfHVlIM2sA93j9yWzyWZ%2BdLLE%2BVssjnFoXfbFFsXddUSKfVwdzDTXdMo%2F%2FeKqm1dKgwMr1XOvFIRP%2Bd%2FBk8zTnqC750i5IaI6krwPzXdzKZFaBQEG76UaDNNB02E6pb8%2F5j5dfI2qx9favdfzlaseE4e8jrkfHlz2cjXqr2CVlTYzxMAhKjd%2B8xuQGCY53uIPIA5BeNMYbaEv8ZpzH5ayYrIQ7h8udXpA%2BR13SIw9ZpczNTfaeX%2FZYf%2FRHlKCmns30CoMLAeAORTQ6A5q9oCoPnLsKJvVmhUeq4A2%2BWc5tB%2BDfw4u9clFMIqQs9QGOqUBJxvkqeawuz84QU%2FG3hhA%2FaIgWvA1V7ju35CFft80VxmYEneKN%2FAaR2lUk9%2F9IKuu2NHQ7ly5MIKnWKr8dGpuogzldAEcMT4bIMGr5KVAlmwut3GT43mRrhT6q84m38t09iEuFaIcisGB90JlfzkvHKK%2BzjxJH8Vvp2BBfzcwTxJIZQKLJnHSDOgT%2BidV4Vsy0wJQwqxBdmyI7kgnCIYPQjRdm0b2&X-Amz-Signature=59ed33093e34824e926afb2d973caf5a68eabeb51c3accc9cfb8cd5440e12ca2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

From the perceptive of the structure of mamba, this is a discrete selective space machine that runs in linear time using linear space.

lets say, matrix A is a state space matrix for the last system status h(t). we then can calculate the next h(t+1) based on the following equation:

$$
\begin{equation}h(t) = A*h(t-1) + B*x(t)\end{equation}
$$

$$
y = C*h(t)
$$

Where B is a weight for input x(t) and C is the weight for output y.

We define A matrix in a HiPPO matrix manner.

$$
A = \begin{cases} \sqrt{(2n+1)(2k+1)} && everything-below -diagonal \\
n+1 && on-diagonal \\
0 && everything-beyond-diagonal \end{cases}
$$

By doing this, we can use SVD partition for reducing the computing demand.

$$
A=V\Lambda V^* - PQ^T = V(\Lambda - (V^*P)(V^*Q)^*)V
$$

This can be done
