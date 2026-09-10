---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKGAY725%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T122658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1jk0FQikx8riyN1z%2FH2ccpbmfZVwYUvEIStTBe4nspAIgIlwvY2zhz52RTtUJiqXhDe3gFROHzKzY%2FbKmCTJvvkYqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBixAwB8ax6YlvRzyyrcA7wHunnHH1%2FkR%2F4BtJHYTQj4fyenSQamWBf%2F8HGRvre8Ly6mZdq851tf8O9dPktJZZe0%2BDF5uOjdNnsnayKMjJ9fR6K7kP1AsEhbrQydBOt8Nl2Y%2F4rCOUaPW2yTRITsq4Oq9VSJhxHLATwD%2BepgZD0Q6ZhNNuFntQ1y5nsjYi4LRWqkKy0X6dyYVjAFBhp0gRv2udI8rwWxrzyGAZqUKeJyoZsCMrQjiQuDXrn0JEGHN%2FTzsybNPPvEKXYz3LpGzVEU9UyqLZdakAOUlKHi10Ui0pwcyrxcMAuC6k2h7YRJ99GjDj82jXSaoXDHIrsBuXj%2BMMCviUOTW6ztSIGdMQ%2BLBUsirJKx%2BiCr2XXiQa2GlAeJSfeQDF485nk%2B0fT6c8%2Bibug7HkV%2FvO8eI0BlR%2FrV4Oc0oU47GpskJEG%2FVQXN4gsEuDZmFTrP7uW3Dn%2Fqv0O%2Faz5OIqyNtgvI2IABjj0wEn5enhdANmhAY2fmkTlDrZkBM6JQWSsR54v0Uf9JFP1rfwOUpMXiFE69zcq6SjTYA%2BRhs6C2WExuixh4%2BVvl%2BABPwN0IGNGm%2FQWtEfHkuAJTw7zXKtEsWQDe%2B2NeWkjQbgzmtdu77bOkueAoe3ZUV4X7JYUBgp%2BA%2FvbQMKeiitUGOqUBvwBju7GBlelGuiC3MLBPkpoZOmfcCc5iLEZVgpbl5Um5PZZagy%2FUh%2BLpQE93RD2NEEjxy2sOVFOVEuVpl%2F1WI2iu7Or2mgD%2FDHUT8YxZugrhEkoHqDQky4J1H%2FZTDI5J5Vfloh9wNDTUhBCUytMJ4lO7HBN3UBKfCE3CnSbjef32561iSI9QKWqET8111mUolKjO1SuPH%2F4MywUOKeN9uRdhcbQH&X-Amz-Signature=48844827d6cc14c057be31450ce8c07594354a67d07ecd91286820ae00aa31c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
