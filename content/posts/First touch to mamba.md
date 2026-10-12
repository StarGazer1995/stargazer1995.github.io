---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674LMQCPY%2F20261012%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261012T081229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUfAaMZa%2BVFmpnjKOTSqAQfvwZSYuLwx%2F48q4xNAvHVAIhAJaZvH0UCmxYbsPJ5vTGlXRzz6hAF%2F7gRXy3mbuOo2HfKv8DCH8QABoMNjM3NDIzMTgzODA1Igxk5U0Nybx9m8tIokgq3ANkhIuo9lUwr2T1WRP%2BtS09nQnm4e8YigbUXDDWjWlTh%2BWLDpVClslBCZ4lB9xR1%2FZ2nNz88mqhqoDfB69bE%2F7YUpArgV5%2FaN0df5F2r3blYlnDGJY14BleNBlSMdOMzTyV6iy5HSv%2BEcBaeMT6PXRmW7THhubrb35LFnZ%2BJxjhzTGudTK90fjJkjf1dBKV3Hj%2FaRcphN7pd5mewdXU7bziAacncpGGVhZ8PCuN7n8oDwlqt2ZmFjRsN6U6WyTvkNDJj7iFdjqK4tipOEGFw6ZDsAUKssXBg5BwjlDXdJhQKjOdjmxbej9DPoGIH77tXvTlXRUulBd4DoJueWGdtxUYLwfXHDb3ESl4ZVgSo7iDfDEl4kNPc2y95BVvNzGFpBDodO0qsvGCKPJ6RISXkPJPGsHXzNQ%2BD3qlpY180JNPF9PwxsA488mbfYx5n12z8hn3NRh7ZxA6%2FZ3cjsrjXQB2NghBwkXqT%2FrmvL0de7irMyVmq7WVVTjkG9XN5ntpcSjDoUdR6PuXx1gmoBCZVWXPA6rQSWPZaJbceZa39ck4MrGZhJ3z0IkJvGjBOqeFOCqscVhJo5X2yIhFmIcMFVtfpeRFp1WFPL9txjtt2ypBZ3T5QUnVp3Q64q8pxDCF97HWBjqkAS%2FYPsVU0JfIlBWnt5DAP5D2o1o52ER0fCwWmMXgGud8X8rbhG2ikvsLxGtMaZ82CNrf2L0Jhu4Me%2FWUnJUGAXg7rj2bKjXSv1NCw7ccfyjUyDqNL%2BWd3nyghfVIL1TNpnlo9mNbLeUAxDml8TjpYGoyyEczQMFgVUs%2Fh4OaNlRJfuk9LF8Ia%2F26WHPnJUgzNFEzx%2BoFiNcTAR0Jg1w68K9XF22w&X-Amz-Signature=620c0168370015fee6251e3897e8691d5b2ffd47c374dfb52888bf33f278584f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
