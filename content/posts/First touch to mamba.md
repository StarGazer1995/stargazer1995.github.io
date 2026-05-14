---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646XIWI7G%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T160432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGsUQvSgSrbFkc9bMJw%2F%2BRqjWyVHtQT6ljvMBF1mFo%2BMAiB%2FJnqbICN3eMPAtMA0o7o%2BDj9EktKMHM6CKGYex3XIoCr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMCauXzEZ7pVqls1yoKtwDY1%2BXQ2VG%2FasPINPl82%2BuF5Jzo6Iqs0ZXVj2P3m7hAdzwj7dlda9bcJkWYcC3a1MSFyIsKj6QWrXchGuBCpXKjy4BQKID4qpnfHlcKdwH5clBsKBgPgbpfbFkmfUdNQENDiRaXNnqjakZkJGo13%2BqQCfuGPLJ9EiH0xRpYGdgrA3ZT7PZLQCHfvHycQYhBrrbjhCpu3lnL1Mt%2F47OdqDl600cyl%2B6XuA6LXpinZep6GxyFdPAmOTgDWD%2F3Qg3nz2msuGx6SBpdfu%2BmZp9C2ojX0XD5ZIDoKvzOw%2FFcvCjg%2BxN0qTBAgNiYJht9DQP4P0z7sulAsaWUkFT2PrjN4OtgizJoCqVifBBPN%2BUsTt%2Bar6c%2BTFgtW%2FHR3mZTlyD0Hq9qDJRZxEwazMHxXnZEAqaJxN%2Bn%2BFpoGhynfbpRrpAIehvyym3Hg1a502MHBV19OpGj8GzhlBs6DcKog8QhrhRWzujpyDrTIdHlOcyP26F1lg7Wm%2F1q0wX2dq7ImFdliKXej8u%2BAnSWfTYW1B5JuJ75fkELHVAQQHfIRy%2B316eRZ1CANBB3j7TPde7eO33wKboWohoqc2mqJnLwFTKIG5FTipUixXE8ncy%2BHrfDmMbKFc2%2BZo%2BfKsEkJwXvXswkd2X0AY6pgHEZIJABiXHWFjYkn01%2F5v3BAUmoPIHJhqH68hXkDFDKRHU0MOaKAO8FtGBc%2Fba8p%2BjgeskE5pyutxWWte1IcRd14cTt5lkpDo6ynb0knphqwmK%2B1WyRJ%2FC6Cy8VDHE1P8rsaaEPw4QKVJDmLvotJ343CZpbF3SdI4DSXVYWfmLPQsuCb3Sjknw3QkFdQ8qCLeyjsi3%2FkwCUZLwi7FiyM2NQgkhnFsh&X-Amz-Signature=a2d0a3538d2cff84747d82b1e28c790e9befed6cdf8a8c4912a1de137096a5a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
