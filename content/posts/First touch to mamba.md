---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PV2QF4V%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T180940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCICGBJnwUSRI7%2FC89GG8PYZZtZ9PafHmN2AX7pi1ch5gJAiAQmjYU77FmpCPO6NfvXWwm%2Bcc5uJlBKU6HM48P6PYQNiqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLvu1rhodQISnMp5zKtwDrWyqzaK%2BhhOSUf5AiBbKWW3B37GOOHRs61hr%2F7e3tzFcEuhQ1xA6h1vUtKd8v94vfAQyJ5RuA1uwIx%2BuXuacVdbuKXaQEWuItB7KasWuitoHe%2FE1x%2B06bJFYd%2Fi%2FhU4Dkv0Qx9IkUQMLQ24Bz4jhjp6ESm5YW6vOQpmpS6NWSV0pCScF3NJowIhCfNq%2BUu5XylSWqH9clSotwZdTt0hCupOtCfFdC0ncVOd4sUBmTJxoTCthfYUn1kAxbLhesM5K1kLdalaCVVfHhWkQCFtcstbbZ3zqtRKBoS6q9KXKMqyG51MrB5eYiaZYPiRULnPgRugdvB4BbPc5uCjDH7xPo5dMbQ2zc2W%2FBLmsF2l%2Fv7dvOwHV6gtvmyKoMP5oAXNjy%2FobsQO7tYnoGo%2FJP0tlXwVVQhD9sP5%2Bn1iVYUb6ZC65hjHy%2B2spBy%2BeHf1zt8RxM3yp1aJG75SpBcej4E5JsbwfU30rSYUwhNW8KDx2aMUZwqxA%2BqYM1NHXVJ3aJfnMfphdAe5ojZBo78tiirnLawPcPlBVyDGlcnPVFsycgDjhz1pecHfVZo5uVxnOUpzJgMMaygvqQo3BmRd0xHAHh%2BB0KlGCW%2BiuBsJeV2aQezXv9iLzQvE4v8pX8uIwqtq30AY6pgEAL50bq75c26HbnAuQV%2FLryNwL4FSDKF6lYSaRGByCS8Z58tCRcUp5abEGBmNrD4iqVMtP%2FU0gu9vciAl00HROyTAVnLDpa1wuc5Ds2zAo1RrY9CweRUBBU8ip3cZZ12zQQzrmdI%2BJc%2BLJac1fPo58NumkoEnsya3DKy%2Bnn9zuZk5vuBGIIhede6e%2FkTGkHEp199nRIPeYxAQsyyg6yyb5QBpchLTd&X-Amz-Signature=493cedfe11104b162c42169269d8ba0a218589c4806461c790d0e6d44c0e87f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
