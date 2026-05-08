---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQBM5EFR%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T204610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIH3DT%2FMEiN7%2BS%2FJQbW6yRPkMrNOgVdxSPI%2FJsn%2BH3roSAiBqN3mAkyvEXjCRO2gn1RdLbJAAL3PRHacRCKVRf%2FxgNiqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrCM1XUrZj5eiv9Z6KtwDBIqtNEwOIry1a%2B0QckF7YAVvnZviBnL3031N11SDKuLW0yGhxsYpkc%2Bq14eggkfbIfqGEAaizeP5j2Pe0J6XKv1HA2OmlkFbr2B0GjmJSleCx2lV8F22Q6frAfdsrFSU9FrZ2XZ%2Ft53e5c5epPlseXToxH0rVfEW6CJG1fZqBLct54Ls8M40sCCvhH59sWg8IAsf8Ddodaq95u%2FhcOGgYP%2B11XiEj3TrDxgy9yq9m8DA4fnz0WA3m8gTM6StDTi7XKjL1OErjHP4Rn%2BUqYFbYrVemG087fAR7JSikV4bkx0ANsDFYyPkqyeaZC2cT8qz1NzT4aVcUN4q5N86fAWcRQGaYJwpA%2BtPSZl23Cip1dGB8HhKRD9miFcTdlZrowKcT5ekIm6QpZmWn9ex8ugo4l6V9hJA0xy4hN3gH6CqESaGUHpJPDwx8XvJutVWjfXzw9IOSbIiiem1EQMjngGNHraX6Vp%2BZpj0VeATbxgNO6QMV%2BEeQWyFozkUC0E9eKm9Ccl2VHOrk%2Fa93K%2F9H4IkntdMxHgT4TqZIO%2BcWZzLuRiPmN8dY7R4vgodf%2Brf%2FoeUMz5m535odzSdPiDzSrM5fJyVk2cgDl4yk5V3hoo%2BdY8sZX4%2B7aKk8MlGXkswxev4zwY6pgET8s4Z7CLwBmH07o0eR2GmbMbcIsfmremUbMKW1bHD53YYjEiZCt08kanBJTEorGLPUR25ZXZ4SpYJLYMmdP7RRu2l51bKgsQOdY0LZ%2Fi5KdmlaZnjrSJtPXgp97VF3%2F95OlFGCFq6EdE4s26xENloKjgfhZnZFVr3rgwiqm7lqGeniBbQhLdZSqVLtmjfFT7hSY7Y6sy%2BoRfRm5C%2FmGEtfjyIawpQ&X-Amz-Signature=2d181b877a4499816646e4a7a09a19064f433ab90c1b6fc9258c167c7c99a823&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
