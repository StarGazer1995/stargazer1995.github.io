---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SP6BM32H%2F20261016%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261016T124829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIE48AtdcvKs8SrgLF3%2BpsCL18pBERAfL21sMUtGa2Ji%2FAiBu%2BToas9C4yUJ77wamk6uwElnpPlj0mvyg%2FO3uAefEXyqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLMNV4Z4vtWNxz%2FwUKtwDSAyiCH1xSRV3qR%2BsWfZ3lmJCIU7HCSplJlh8u%2BeGCb3AjjRjEjvbBSgjSG5P7b4vPfz9wnWtXkQpDsqPNpR8xW9i0nvSts0lUEkNZlY3S0ByzK1Eqs1nPA2FWVgB9NCb3Sg0iII7r6fXc5SMqeBZkZZEmN0O3p2Q0HUV5kEzuz0k1qpOuQP3oDb2h56sT%2FubHDWfz6WrLozzZJhROK51lcD0%2FKRCW042Sw6ETwMJ0UTzhHJBP7mBEdTkL%2BBXhT9of1WUxN7hVg27b8P6auXsRRl4Qnl4r4XgZuGfP86vApSPLEVQRmFRzMyqxpXmEzKpmDENSZj3IhQQI%2FHpFCU0zDuMGQ6cv7lDakCpZEpMJJxey1zqc6tijY2yMeZhkwlmpNEFaMs%2BtLQQB%2F3pGyC5vf0E9YvyJS%2B2Rb%2B82N3hltRszeUUlLJ%2FPfFP1w8qUHKnaiowPjsWI7Mn1OdmovddljFxSN9Bp3eBQaDU3oqRqRaKL20GHhC0abFL2E943QzQwYtMY909OxFVAfnYILWLkHo9PsrY4fMSvgLejWu7%2BjDv5vhZuPQ2VTmAjSkdCuJxnXNyFdsteX3DoqAavUv519QhDTz%2BgkfP%2B%2F7H7vVgZb5c1IjxQBYiDoM2C04wyaPI1gY6pgFHJvKMhxhRGqZ9OJIcTgV53ISVSxWKCS904caGMxcTI7b1IJU7%2BFIfej%2FVDKrzXt0o21bjI6GGKbb7fC2clH6VSJeisQ7nI4P19cp5CXTh0INgpfmbI1leLBuSdJrY8QQ6ufTPlxc7lP1A8aU%2B55nPgaIwlP2TDXCEAGQxo2dS20XOY0VZhV54colrHYJO3K43Gnx4iKE6ar80wPXUu49R6FXitXcM&X-Amz-Signature=cb9b86228bf5fe174abf030eef4cdb8f7010b914b48af5b285ba913d3e825a6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
