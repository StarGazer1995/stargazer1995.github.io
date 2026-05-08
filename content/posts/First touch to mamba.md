---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S36VESDV%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T170150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIHQ%2FXP8EGrTBJiz%2BLAXss7074h0fFgjh3wSQy8H1hzjuAiBANOh2HOxJ3dhz6s%2FqO5pczuin6vIaueXBjFXdgqvVvyqIBAjS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIa7eaGYCIDPcka8KKtwDuFY%2BbQDdtvq%2BLP6b4qMFtdyjqgzKOFFiH2LvsbEVPCf2UnnIfzEOwpBbkx6a5EgCY4KiL0urvXbyF1w7vowJOQAIzksB7D3bPZY3AwIyiOcTwwvoPlm7Fwj3IkH3OnjWByctCO1hP3SNyQV4D8%2BFw%2FxyB058apP2ziKTXj4jKEM%2F%2BlI6JgZ9VntX1PVUZ6exj9%2BB6SKqAOMCeAAD9gruvfvUQk73Io%2Fd%2BphKNqzD91V0%2FYj46DaZlRI4noxOlaIy%2F7XkUrU4mYxxDOtG30VuAwhL%2FuMJE7qaAO3Ev9gz3MhmyF%2BGNWnYWhdk%2FgePVjfqiAJo%2FXPeml6ThJuqNfnCgpgZml0Tyz8sjwbh4BF37SiHlpT2%2FXmdlKww8Fv5b6Vl2iw9em795hbUKCt4nuTWUgZ%2F0z0lyKQ7LbwKi0sGqObgKqS6%2Fjx6YOVvnWhTzSo0%2BMUuRxZdzRltxFL10846gee2BLKL3guhQ9zTQUZHOaPpTke%2FTQkm%2FjArntegZeVSXVDz3rlL8iaZa5h7U9QqFJcXCNy1tt%2FugnN%2BXQX7QqR7K6796V66zy06zV5I87a01eSpwQkwxbg6NQBC9sfJykcGNVA00XbdsOQ6NDNOy5xiq8Gsq6fWoZTVid8w5aD4zwY6pgHU3MakTV5T6hgHAkp8yoxujGejE8yB1USVNFbXh0w4%2F%2FCNY8lZpLoR%2BJcWX67GBqqvPWE%2Bxkn%2FP7dPJgpAJmhDFQ6NeHleoejB%2FOBAOztWKXr3y9PqJ7o4ckcZy2LqYGH8GvZBpuIwxzxw4sfIRNXn0GvvX4zvJNx3PAxPBtT%2FJoSxL3BByq%2BNARaaEsnQxuQoTYTORfom5x8U3S8C%2FuZufSzjRHBM&X-Amz-Signature=bc2069b8f4e8e7fdddd6deef7e4b93f80f20e7288c49756c4d6ef3dd5ebbd84d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
