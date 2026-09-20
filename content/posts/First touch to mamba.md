---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OFCY3FY%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T020103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBxmfVQot%2BKok9Md8dxjCC0l%2BlAUZrnjGjnCDrJysQItAiAcWqIN%2BWLfdZMBRYnMqSPh0KKpsW7QKnnCpT7D2W7Abir%2FAwhqEAAaDDYzNzQyMzE4MzgwNSIMVl13xvRh%2F2jUy96KKtwDOfv3N%2BP2QuSqRvMYID3eGGOZYZE2k85dGrHA1iTTwkR4%2F7WHzac4kJzrpFf6XdBCV04ZCRlBWDInlkENPeSQsPAvKNXFJMxrVwg1k9E0i1%2F4kQMtshxJCccO%2FbFUEuTAJ5YgGOBsfk%2BB6fZ%2B8DBOFghuuZVrsmaVMNceDiEnJca3J7COE6doKZar192zYJR0fA0hqcpalG4%2BeONhW9aXIfypZ2F0Ux2nfXQNa9wdpX6wGE3UGMyqOXshNZTJxvDgtuPAHBnkkX5mFBtaO7E9boFatQvQqm7wJbTdpKe8U9cRgf%2FreoDrBkBMOSNPSUEFyCeDdSslDM3bKcC0otZt8KSLRG8OhI3Vq1tc%2BxYvMYNHr2e5CLDpsIlbh1%2Fkrym3t8TXW8fERvauQM8R%2FmqkTI91DwtJhBH22zyAk06Zxq0QqGLfC7EQ94ZDE%2BaDLS913lSSfBVIyU5VfiIm4oz2lVPm6vU317IryFoJNJNyzSlWvo3F6%2BU2yQwNTlgHxPmkDd6Q1QxRxUl%2FEAYRgLeN7YWgFJWalaEdBbccxOsyI1q4h7QK%2BZPz6NChIYkS%2FMGdQjKOEtcqhmQ6DJSTVeadwzOYNH5foZWc4iGVt%2FSRwQgbEjsoy3n9sMy7lf0w29m81QY6pgFBTMHyk8DlXFCoy06ZX%2F%2FkNBwyj6%2BYmWB4U6EFllt8uGi2MNMMhDuSuWyo7DKMvpIG6noYIUzl2YQi8%2FJxSe%2FkMP7o0gnYQsm9s2gc6BWgjkqfQHuVgKxPs64J2luaJzLCKexGBp%2BQjiI%2FZgM8iYMLLVtp1VTEdIlzeyRrhWAuBNaQl5kxiiYF7Ipj2Ait7QjGJPIFZVBXNclu43d2XRySDGICs23U&X-Amz-Signature=af9639c0dd61fa3982109b8c01c9e886bad7b656e71dea15e9c1c93cd9e64428&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
