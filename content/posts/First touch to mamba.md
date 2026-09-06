---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZMUBR4C%2F20260906%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260906T013643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJIMEYCIQD8RivAo%2BOMcL0UtjcUJa63TYvl6NeyjMWRdwQ88JFMagIhAKsZJDjg38wLznO0z6yitza97Tcpy5YdkjYTIvv%2FvCsZKv8DCBsQABoMNjM3NDIzMTgzODA1IgxxGYJaNnaV%2Be6ypVMq3AMv%2FfesYiQRQgy%2BFg%2FALQSx6HeJ%2FF5sa0QdWh1fNI20EDgh%2Fagco%2FGNiSYkukt68VmBKmjINXsqhlaNFFowOdh1huEqjmP6xUz41dJqJQvQPjT8cugiL5tFJwWQWDrpICUn0szTnUU9Ibe8wJOu3IbOioQ3azmGrLVIUkvpi1Uurxq3oG2I985Ro2Ix8it1k%2ByI67UtYYcBOjSC10oGPb79K077YpbXPd73fYXHZ7xdgEM0gTIPqXuK%2BkxcwdmUIRFnZmI1U17L4NhgFt8ra2sQ%2Bmw9YoXg3E4DLjdMkf5Jk8fJmB3nr0KnoR3%2FHM9qfe237g9Y1CWHVCbQ6hLnLlnjc%2BxMKePWDWXOf1f6ocmIpahA7YMW5%2B5f0eNtEEsKWKExxNMYfw8JmERZiIkv8%2B0bpr71HciYlP8cO2JFJtgOthVlxILpv%2BdcZpJzPipZiwayGk%2BVgC1K0OwLZq3M%2FAb6iTijC%2BG6OiKVrYFcMxjUC3KiG4npZb7R4yFlss70Wrix8wP61dydbnlxQIkt46pof8nJV0wKuVPO6dZgC50wCtSUws6UE1WIFomYoJ9Qv9TT7xzUr42wOdDGTkg1mubLJ8xu4gLFnRH%2Bk5fNBKFNSW4YyKqY3F1ijjKAejChhvPUBjqkASHlgw%2BdoJ7iNsK%2Fjei4Q3j7eA0Ja3wm%2Bwz3mt7bNNabp8jnbwOJIyTXMiHgqWh6le7sudIGfGhnFrtHBRS8w5wGlxeFtBiYTqBRenlECa8YaiUszHIwHxrzx8QGdu0wBHJmSIAj9vNM5K%2B6az29INxkktpY%2FmVvFYTRaf7emHghEqxHV4X6FdEwwhw2cm4UdishprFy8gtvN2gGVu%2B0P3X7hA72&X-Amz-Signature=26520df0aa76baf440eef7e304a928eb86e84c355a9d3b9397a6120a3ba80b25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
