---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XINT2Z4%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T161440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHbiX5hsdfrlSP3cI%2FjxF%2Be1TYnpemKpku3w%2Bw2sSsOAAiA2%2FZTbs28ekW%2BbvzTEzsaMKbeRYG%2FIlqP5XUN7w2qOjSqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcM2Uxrpa%2BL1X%2F%2F0hKtwDx%2F7mfFKgLWCahUhfBnLmiRKiiq5G6bgdaxI%2FDZ%2BV3NKyh9432EstaWaKlqA1OAHyDvbpDk8nv10Phuazz20ZrJXjwJMXC1UGxPTSDz9DnqGEI%2Bhx9YgEYk8MAc9kCM0lA5bqCG5KByNC6JKB1wvMdkG%2FJzfljiXDGtjTNXvI59SYevAFaiUlC0azlbwiDmCLQXp6uxyrAlG56pdjquWXKSmQn6G%2F%2BTkoDEuDkAWBWpccIGnqnlVQvwAmNDHwHYQ379tHrFbZBZe%2FBQMH%2FCArag0khHH9EyHCXmVuuLUgwTM0u7hm0q7KpRNfCsfpOCxG7T2kgRTfB56jk1g5piZTxAj092BYVTTOJ7isyKGXRaCGFgSaQxJ9SFeAnqQ5YJrLUf41QsTQPBLhY4CiPZf4e%2Fv6TnPj9%2BLzkNY56PgsApRBYTWjXsN1F8JJPklseCWJAyjETH5JE0kzyBwwiRiHGb240H3dIWGdBxte0u6F35cwcqFRU85DyO47CX6%2FR%2B0zJGm0GUzx%2By6uROYOdW1%2F4YWqMeccqJhEkxJW64v%2BrU33W6YNEwDbkuI6qvHqBSJ%2FRQ4iQl7OAGvbHWurKqqSefBoN2WI8J7%2BLaQQCHpTOegDIrIY6j9GGF5wMUIw1biO0gY6pgHd6iS1uM5VGUx85qID4PmTxplazTmZYxZH3bgTLoyZCM%2F3sjdlz0Si0YJIHzqh0QvIewvZb1Gzoy%2F0JJTcGu53St3g8Aw7tHCcUzMViWO%2BEOSz6Ro2X7v2a4Xp52ui5ZGIL1A8xD3uVE7l42xzqT8B0q4C8WnAozDSwSN%2BC044OC9Df98rk6TRz14BWODFN%2FCVWvBuZBzwhSeKqk5Al5lcIZlKsY4H&X-Amz-Signature=8db063431d95680dbaaf09c5e5fc3d52aa61f027af11f2c477174fc380b5f229&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
