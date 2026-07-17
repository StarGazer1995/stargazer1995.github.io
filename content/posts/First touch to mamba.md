---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYJONS7T%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T012531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF8OjbmCP6AqEFb%2BZlH4vMRlX6eiurj6pQMrRsO05VgdAiEA3XjzhHvgFFYIFAARDQw93dwBPc30TYjCKlclYSMUgHkq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDIAUBU21cZ1px2NmvyrcA7BqjMU9Uz79FYpkhqi01k33%2F%2BYMnsw7pBS0YOnCvfkdR1aEVXz3p5%2BhAfxmNixtewMh4l5RqoPxKA1q1vfP4qxRvYQjWVG7G%2FD1YSZKFkA4QYk7k4H6rJoK3YWhGr1HMOTbNAGqXBIy%2B4a074%2BUQW0PD1NdScqdpB62m32IOjPtOXVt0Kf%2FVJ93tW4mJlcukWYAMAvHjC8lOXUfKoVT0wZdHeTc8vpxDcY4uQAEUyC%2BJiN87ZNzAXXvXtNjXAvLlJjJJqYQzqIwd4on1151DDr7SkoBXvcfJI3lHvmI3FFidA7YJuyUz65q6vu5VzHV4ylBzPlUVzSIae7b5MEjSfjgPbHc9LkkFrPpJge0ssE%2BVcPCluV9nnT7jiLQ3CzXGgtHVK4jNbJlO2Nq5%2FoUaLqq3%2Fg0ctUwAcfAPuhWZfQsOaUXtbMGgFlK83%2Bn4AUwlCBkSiUd4L4vAcrDzIkrcp%2B%2BVx%2FcR2%2FUOO2nYBt9oT3c1B%2Fj9Bvuvu8S7QV3SnE03s%2FTq7dunSZ5j%2B7RNKjaNkpNxpYg5SfrNEEG2nV3tpnW7dtvd25k8oveDun7IQdssEb9AC65%2BRhD2xBr%2BOujfqQhCtw8WNwJQnJkE1y8JlU2rj6CxGI3Gg1KVTyWMIzw5dIGOqUB9g7mgf2zDq12p%2FCfCTXXFfzPrZmQiQj7csI3poDYHKkaBWEvZ0tBtCEiJK4ZZlMg0KRE9EL777U%2Fu7jeS23NjGF9JivmR2OMH2ROuiu3HUJPG5N3M1qIyFF0k9k9XwqktKmW4AUIbAYukdNYyWSaPH7FtfaKP%2BT81QQzceV5C%2Fs3MSKFlSQxSInGYxE5fb%2BUNvPq7fiPl03MMZDRac0gZWfnWwwB&X-Amz-Signature=e4d03e94ba6b203371ae7d08dcdd5bce8413febf0ee52794907ba7b600f5924d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
