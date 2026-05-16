---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMQRLISA%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T223603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICh%2FbDAu8sjT1X8lRG28MAcb7aeJ%2BIbdhpI2kdfm2FIWAiABhiZYvxSyv1qGUS20vhL3mDPXgjMghTYDjsxaDLceiSqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd0lHYCdKEgF4ahd2KtwDPO1eUnJtmjAfqb181Bz2fX7tYthB6OWIii2VIdeO8GM6vgGUHeLCnhgf413QyIl9qEQcbHoqOkWfTDQ8C8vc8XocEh61gGzqe1b%2FM2REE0%2FS%2BhIqU%2B7Vqbeg60MBOhCrgVc9OFSmP2fKykTqQ1ShapFmBE9zPfaLI5%2BxrK5cOotKB%2FS37bD30BYAG3CwTr1Mj%2Ffhp97Q1fNKkLM7B8v6ZWv%2BWf08hAVh4u0PI01icAm5b7J26ELUtgHCd0VQYziAMCF01VhvoDaXVvg1H8vNpSAf2M%2BlqznmRik8BrTVLFvPcLyXxRaM8PSozxKiShc8ZbEVj1t6bh3du6%2F91eQZamnqeFYuMKpoOaBZzy2WZlxI4HYxj7NYDNhho%2Buch%2B14my4chdwc6%2BPF706MZCT2c2WY26tXyenj0ZuUz0hA6GBatWxBRSmWqjiXS9lQh%2FSFUf61pfbz8HllYjR4Gvhht94wWKCkQIDaSp6VCHVzw9XT1Y2xicorXy5yk%2Fufn99On%2BbkqO4jsc1L13k8wr2OvdvX0dwZBnMUz9LMWYqV%2BmMLzJIE9W78jSu2pJ%2Fb4EC13Abc0DHGjkOzUDZ2mMILsNJNQDL7rrPe9SrkVNS5o6YZxVG8uOdf%2FCB9umUwvbOj0AY6pgHd%2FbLR9DpdfWmODs7BhsfYckIv3U%2FpsQqVvKKhYIYM8twmZJ%2BXFZ7HEITelcg3%2FZwkIAQlHAPMp8TsXR4EiDSt1zEde2UXE5NVKl59hapmERXw5J3b12cHlHHZCKE5G%2BIkzKa6CskUa3ucz5nzvJgX%2Bi6evqhgJT8Mb1oLneSmWQajSru9f%2FD8n7r%2BCijEITRcSQrTOMv6dwA2yeEBpN6aTDvkoxBA&X-Amz-Signature=79b4e79eae328befd48fbe1d511f6695df36ca8fd1b12d132dcb69bbcd1da63a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
