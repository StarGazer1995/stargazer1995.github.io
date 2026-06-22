---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QE4WXTXR%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T215512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCICZGdIDk8XAignGV3FVCEQzb%2FHiKU027BiSeztb6iWBRAiAdR17faJlSxne26frUYGhAV%2BJFI0yJ5V94lumBTZfxcSr%2FAwgLEAAaDDYzNzQyMzE4MzgwNSIMx6c%2FjDgyVK3r0%2F3CKtwDDEJYIxipnkJ9fS6g0%2FjOp6jIX0KxO25qvPLx5RaKwijcgv42v4t4Ns%2FCmYRdrJKg4LOnfxoOqE1xRqyY9nd4gFZbWUWpqIp4gZ%2B6HeXVe7W4rFb9HUFOlp6Ke5PrWmk1NqSe0qeSfyDOxvNm6gszakUx7oo6jn2BOqdYIlzzHmwg9rm%2FxLr%2FXH%2FXKhMQXweAXx0W2ZPZlwkF6hh5hRbsv%2Fyz0mKTc2bJMNyD%2FSg7ey8KlwVzw2SrJMzGWZzMKTN7bWefx6zzVog%2BKPTsUsM59MY%2FjJTxi7yxSk%2BvCi5vn0ExoavWTW2JYWpN%2Fu5vMPTFZveIhekpQlKG0FemGfiyLx0Fn4osyjf1Br8qKgNLtZNfNeDhuDazpgrfyTlBuQAodjgl7mvIX1YXhgT5FmtY8CDSDXK09RqHKEhIWznFFRESXfetFqPJuXA0HvT6lAyGIYWrk1w90Hj3vcaYMDfLeT776wkea98eRDPunt5BgGyXCF3y847ynHN6gU6LmilqWa0DWGs%2BZYqqMgbnm2XGcsZbN%2FgJDB4g0%2BoeOAiYT38QUvUXy%2BCAgJnk0iJmMp0%2BqGX4z8DqWqU61JPCet964sMZb7m1VeEuHkZVf%2FETyiZJJw4zgCeM5u5K5BUwkvrl0QY6pgEl01ki8Ohqt%2FkGa4eEqTww4n%2Bdq8Uyx6HxHzAT%2FzH5bBQmpQTfCwA6V%2Bo%2BveZeC6FxM0UzqkzThOCDcTF2Fr2eGSpRA1KIfuk8iw160QTbY94%2B8NnpC0L2ZkMhQEIx8MHEbL%2BNDrDQm7ZWYEpnPguW8D353LGUZIofpnyzmL3Oo12X1zpMSmRWb%2F6y36%2FjNXQqCIrPM9l7f78HLih9Ek2d3cuK3rgB&X-Amz-Signature=595f63f1def9800fa3d610992652f09c1327454054390b448139cc45c40c6c16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
