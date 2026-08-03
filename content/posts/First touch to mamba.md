---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTBHHSRJ%2F20260803%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260803T124855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJGMEQCIFtGSpdWJKByYxD9yBvn3D2zk4O9Y%2Fb6FR8%2FY4A3xjkqAiBTaq5jiMoEZ2iAGNxD3SQoGfvDdrZV0edmLnjukJf4vyqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEpJjXBOwFXl%2BAoVLKtwDrK%2FeAPQgHDynN2MlmCpVOXtVAnLbKS2Lr%2FzNTc1IygygW%2BKbIKj2taJGsa8J7KkZ4ocS1jhqYZthY4Uav1FIWzcLuwWuQ5Qk6%2FqNO5ueIn2neCf3WAXJY2StvhkPwGJVignI%2F9nuA%2BWUUmfcwVcnOBPtyfnC%2BOXw9w6nxUsi2ZZlIp9VwUymgOIg%2BaXwGA4yg8ZbSv%2FQ2XJtvl5YzUN9fo43VO2aE0QG%2F2X8EKporyEHSxfrX%2FildlKwrjz93JIJEuq6g4LbPVLuwubc%2B%2F%2FkfKe9ZLZ7796D4Ix5L%2B7zqhK%2FoaRCUurDFgiQrsxXGJ%2F6z2b3CwyOVT2LZ0HMOPHofxSduhEiozJy02KZH2QPBcT5uNwccTeOG8nNj9lCmKaJGMgt7e7XOVQbksY76eVjFTy5N3W9bwGgFUQQ6OTBgOL9TuLFApZQYXX4%2Bqe1gtD8kEjG6JN3FastkRxcd1f6zHAHQiQpHCkZmVggxNzrs3GuLcAfSgimvdfSIhJgUFZYoDH44rj%2Fjyx5pAHRGPhP7zYAvdkWnSp0kSqf7OELCV8F5QuYvB%2B6E8xbWYQtWwxtp5ae6pVSNAhzNBV6IAG701FZgvN8aLl26TAuSpVl%2BctXx%2FNNwc97oHrE96Iwvv7B0wY6pgFArkcXQ4pI%2BhVOsu96LZAIqyJ7JQtRdTyFhltYJ28anepIvFhjls7RaKoYIqri7JfncSjOuwDRgZuJqXoyiTqC0WipBhHtyeRcrs7E5poeC3ZRmagwjf%2Bl15FoS78RujRm0Dyf8WGylXp2TwNn5PrUm4GvbPR33Ia5QW%2B9ZUjkX0ruyW5d0n3sFKMhJn29CWHV%2FWGrQ%2BRtiWBbO9ZWJg06Tc8Xu5Rn&X-Amz-Signature=39adc39952ea8bfda3bd2b0271412391023d072c929a5bdd26d526f8b4c1c5ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
