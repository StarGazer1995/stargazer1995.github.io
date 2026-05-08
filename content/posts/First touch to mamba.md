---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642CG7OPD%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T190322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIAy3m%2BqVyP%2BteozS0Ua9ANhN3nGWstyIACNm7WxGZlJ7AiBippkBlHdHh3wN9S97%2B6MmUOTG8gNmPKCq76UzxzxRfCqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMA6XYszGjKoUPqlbSKtwDSmkT7dLZd%2B7AiCBPhVqHrP8R1v0TYbTNs%2FkfpGJKk5gVjCT4AXK3NNJfKJHnn9Lal8oq6B41VoFZCE9q7VeCWwwSEtei%2BXcJpZx8MYfaOtWb6HzN6scRx5dfZEANlXAfCJVDOuHcYkoNkotNKMLTLF1KMsHvv4povf4aycI2aoA7tMHZpYydzntQhYrLlAf0kEi%2Bj0gzEMAv7Curgm%2BSj%2Fol6E0VSaTFrwO1CwpXQTVtsv2jIiYT6abQu9K%2FWvU8iFw7eIBw636kiR4F3yWSFuMK%2FzEA9rfJkdqoync9IYvEx3wiV47cZ%2FxRhbVSvHzxXakVl8vV6%2FxhvX9GbWaHzLeWinSsQmiHPIZq8q%2FIAoUKekAnpKDMgMgJAr9iip1gGrvfgzvbK1%2By%2BvoCQn6G1iwI94XrcicKmcJdx0aHEPCLup20pA0LO5oKhWvtw5Zy%2FTLD5VFIh%2B19dlzaK2YpJ6gfiM%2FCa5UcU4ueSvE6nKwxRMglBzt2PVgmcc3a2W1UQLKmLli1SrykA2Biq2VYLnh%2FSKTX2Ss0jIUVty6ZovuFDAwsvn5N2Lb1%2FP51MwEiiRNu5Eqp8h1FMz9IovJ4rPeoEA7Fg8XaKk5bOpPoyp3o46eKSqbYRgCgQ64w5MH4zwY6pgG65wmoSfxxuRkMOsfREhz0xe8TT%2B7qnDQrztRJans%2FcuSqXldUy3q3Y4epKEdiCXTTEaiKEONz6KPuJhUWjlAtPB0beqIekxKUnbpVzLExPqNbxZjOIH0RxepuJKOmxxEQqCnaZSmTnqQpJ1E1Bpmq1%2Fnl96nF76bPH2S88%2FXnpK%2F%2Bk2KK%2Bmt9H1ZoQCCBy3noOTNHPoeDTXyzNqgJc1zQWMDlQPUt&X-Amz-Signature=598218a2a6eef2b5d2afbfe809bcf5536ad20ab8e9ff7a050b8bdeb25b6d70e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
