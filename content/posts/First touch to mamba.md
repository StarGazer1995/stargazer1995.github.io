---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCJFJJ2A%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T064030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFmouYHdtgE%2BFqNfdrsLCLK%2FTVkqlPY1WWuhoff9hWKcAiEA186OEx9BHR%2B9V2xGytQYAwhuP4EOzpqGoKJkE%2FfxdHUq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDDZ7IboNMl2ZPXq6oyrcA7qj4sVvvJRAKvKxcny%2BVteZcPrqrp75F9T6BA%2F1aAq2EgesZXXDixvRaAXd4UyR6ftilmxN%2FQjPXodYqAkFXLjgTl3MoYaJ8faq9b4NhY%2FbJvsWMfE7aiELkGUYGwgn4%2B%2BXeACStRlDtXR5dz9e9igvywD05kJGD32jdRY6n%2FLloZXmmaG5XkY85uYGM97NNrDiFL6bCm0D0T530gfpvt%2BYXHgpsQr8BmkNlmzofv8D7bRdVorzYdZFrcmOzpDKLOEuQrO1n8Wz%2FLOI0niCgd4LN6L%2FEa4VW3nMD8t8x1wwL1rgaVRF7TFqUXG5lK%2BlUFpSVt2rqjJ%2FYxd4vn3TihL3T8GBuFyjvFPVekgrIKpmOfrVbS2om54qRPVhHqHBbvO6SjExaNVnskhtrDmXBG5Js9IHl9YbxvyafxcnJuwN1Jg1dXKhRe%2F%2Bya54pwFlX7YuS08iBKVm3uWzHeDBizMJiJr63DBDLMuKEzPU8RHs8Sc55Oq9pG1hLtuTQOOJcGgyP8qPdZEAMUGOVyh%2BZUt%2BlpRBu9UgQD42hL1uwrZvEWmO4FjGaKQ8qIltc7pz0SzYlGqqp5zrTiKN8R9UTR5HX9XHH6kAgzRaeuO4jkRLmWLYW6%2BK6%2FZmNV2SMKTR%2FtQGOqUBgB0quEjzn1ddPgUDCAi2Qhsb84oWG9x6vMhAaHZfzl4%2BrvXZDUdbZDzZ0cDQlqqGdRSTb8w8vHHoLbI92dMVdBQZxxhLpoaXg%2Bc9BXViMrADSpOUu81VCHR3SesPOOFJDMfNAwbk%2Brh%2B2zb09cncEOBHqmC8xtxkdYRtXit6mNYUcA4F7sf0baQmpG%2BlfVu%2BS%2F6QndLhfpy4fHsDdzchVVanJkiF&X-Amz-Signature=84da616ea8162cd1d5d043c8fb690089c37b2efab19b17d63389189d5272d316&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
