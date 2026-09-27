---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YDO4TT5%2F20260927%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260927T093723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJIMEYCIQDzDu9%2B2Ekx%2BEgWp4sIGMIhcTMznll88O6swpL6E%2BYR%2FQIhALAPXHWAdGM0%2BR%2BFq%2FJ5PCN92WLqcKxAl9cEBs%2Bn%2BoO7Kv8DCBoQABoMNjM3NDIzMTgzODA1IgzrRKR%2FtP6m%2F0BjqGMq3ANDblbuqYtZYqeqStk4iwaQZ2VVs0R7vfQp5uBMKfCoTcbmBlP7zPYB5fwg1irA6T8BrN0BqVwNT5AoPo9KeT%2FawCDRRGVY%2BZhZu5vVbQ9vVmMLBzBOiZUN8UHoJ9x8%2FwJMACAfiWB2x4njMWyp%2FbJkx8JILc3F2BZl4qnwMof2XFtNtj7AUMd7FSaMtNCElcyqT6Hnb0POX0qTGxoh0kjtPyAFgmbqCD%2BgqxVI4SyAuLFGonLQqblnO6XGySKXtKd%2FpgHlqmnsQcFfBGq87B%2BIa1MUUxHIdZ23eyOyTuqesKur0y8hM24BrTnNZ90m2gmjr%2B1OKtdcHgR0L8a5KQqb1QYRXh22oBRcSb1yH0m2IO7zJz8x9ON%2F8jDic4oyMEGPCl7KVm7TWApCrR4p1WLTvwwiNLrO832e%2BgBMvaLEf3VneSTPayQ4FlnNFCApn5LaY0VywzUIoXUeJXGyc8Q2p3P51Y76nuXgRpy0mP4zuykhEBnCrj%2FDCknzNMv%2FAVoxO7ymC6FaCiOL3hynpIkGX7fRFWlyGydZSxwJ6gEkKVeJFB2t954%2Br2UgoL2IoHFTXjekkewLKokLzuJciZXcglhiDbfjLbI6phy1HyEJakC7pyQz94mVYN7PgjCqrePVBjqkARht7hvs9ACjqER7KZqimBx4Itfv6Dmf8zTSzNwJg9WMN5JQsMqd7YWHISMzJA6IHDf3323qzjEcbCX%2FSn%2FLAiegbzn1lUDrQDbDhc1llpWmyzHJPPfgXE6FhrNBx1MOGNp%2FlKpDgEAoGZCuP83dFmXBFHb2AutQgKHt6Vd4RYQ5vE6apJfdH8X%2BcvjUAsURCkFdyjsBCDTRL8yIgUdnQsqWkJT1&X-Amz-Signature=1fff6f8eefabf7b5d5a68aca475a71e16d9c7e75df7116dd53215363bad04a5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
