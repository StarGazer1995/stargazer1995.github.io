---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4HSK6LS%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T101202Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIHBoEEYY0MS4%2B%2F3fTksImUj2vm%2FVY%2FqA3hYXM%2FQtOdaPAiAYrnfcK1O83zogZ7Gnz%2FCHwAGvGkcaQrs3Fb%2FykVILHyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMExUmBh50BrS9giz4KtwDBxEzAHwbhmLHWqPZ2Pux8J4ORLURiYCFK8acBmqPhmkbin2NUKVPeUPu22QRjURLBVsmxDTR6ug0m019m2DN%2BID5JOmUful9yLH1Zk1wU2Guj9aQbyRSaxlqu5DKjaPL0ziEUqrWtHf5t0Nk2ArvWzhHqdsZUQfJtN8v9N3uxdhHUD2hYbjrm0pOGc%2FCAcC7f1m7IuvyU9Gsjc6R2P7%2BUa7HzJUn9wbhM8%2FUZOlTizXuwfJ0uWcfQCm31fhJ6D9OjuGYdxikdVlVj0qzFN8d4gtSadIId0pcQU1ImVTFkKHPYMV35BAKZGgANRDuTV8EB7CIrrmWzfjZNPvQPNFiNX%2FC0aTRHrVSQcXlnxqcNAnCePhVzAuf80J4CjuHFbQBx5OCEX1t4VD1BYg40fUu%2BsupQqao4uVEzpIqKPINSPhI8WYVmFYA5DpieSLdC8s6QFHdt2QUJ4T%2FrUYjJO9KwH795lDrqvIrYpM8%2BSDkPwvfZYYKN3zZA4%2F6T1AkgCGe%2Farkci%2BrpRiRLtCaLdHT8bjBlsDMZCkONGDoTm%2FIy4IsHPI0iPnrY0M1YdGjww%2BcKcyBCyVZx3RuMQ99rpiAUPZjLkYI6vYW2FILPCP4iV%2BiWtklpnyV5snfnr8wy9iq1AY6pgFdLC9R9aIEBtByibWIaKOUga2z6Gsh7RidGIv8ESUHlG9nmGbc3gPrWve%2F21eiUxbkbwKhkoyM3uWd24u1kErn2lzMyS4gNkdb%2FOnDt%2Fhkm8%2B4OwdlWIXnlOsI2Pen6Wfp3PoDwob7nHdnneq6dAbuDszZBrKVRpLDKsQtYfycaDNxQRJxjx188xq%2FPkxIU0w7HSSslc1ogzO6rYS0G%2BwkEB%2FtmX5F&X-Amz-Signature=baa0f0fba45c00fe2b17d4c3763f5b97aaded411d4b1ea3986179fbe964a483f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
