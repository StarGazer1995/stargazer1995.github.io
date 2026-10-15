---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VS47LWWQ%2F20261015%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261015T193309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIC%2FYPNmIyCL3oWwl%2BrUHHfBm0CWs5bwHmYioyHrqvn7OAiBMv7bjpFJNv4Ystm6ZYK8ILH%2F0Ldhg9d5jplHyuoj9NyqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4jxXTRwSPwHIoQe1KtwDAcZk2tE%2FYxXQaUfAJr%2BGGzjfPYTUHw7FV1LeNJ5oKKZPSYs2UrZG1t19BEXjKzV61vfrW2GZOSKH0IqdpfzfCryawKC5lud5enqV%2FRsjT1FamNw4zuI0mq%2FrEbKs2kwHumA07iuTEah9a5UeZC%2BkbR39TOQfSycTjQLvy71W2Ig5uAz3OArSZiLULjOz0FFTN%2B44%2F%2F%2BlXD3%2BDT0YTKx5DR8kbj9udDDK7LyPUsBFNW8hImp%2FrLpyywOur92en%2BMgG%2FHFRf%2FV%2BMW7toIGxIpzOBuYXpenOBE5usspumvUnk3xuScgsgQ0t1o8SGvxFvrL2M0DlM4YHHmGWvueYaQtlKGz6dZJEFtqDIFzzZpCBhyFidxlW4oTYqxR9F5AHJ8DCIZGQy033vITFLvwvgWXkLnttsDMKMwyYWgws%2Btbql%2Fwv7YXgBin6oyr%2BscR85T7Gps9G6fQ6yHq%2BSiTzXNw6o%2FT5KJcY5IQ8nqiE%2F72W8vVTPZUQJpzEcXIXOcb6ELRl2nXXtD5KZKj8d1l7IizvA3UdU3PnPh4ADMqmXpxDrlZZLRzzoEWc%2FzHBsbqqk%2FNyZEw25%2F7EyHqpAdQCvFUCDABI2JcrNBl%2BtqsMwBHzTzN4c3L59J7fwHIehsw9tLE1gY6pgEF%2FsUdgaTaq%2B%2F3jVCFo3me5IJHaCDiyuylnA%2BBfp5pfx%2B3Z7JOEAhDHq46cj68CisrUz51wLHGujhJc989eG3QM93g4Piolk5OnN4k8QnkYbLwBOgI12MYeFczaHwKr6Qx1MJtM4Z0CePoVjbV9A1QCeSRY2nX%2Boj%2B2%2Fqk0b5t8dGOcRffq8TXq%2FQlChOQ2vXdYpBoKvCtgplTC%2F1FGoynPAhxo5rj&X-Amz-Signature=7015e7dfc513753e2c37299c4d388545489025995e511961c173ab811d4ea83f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
