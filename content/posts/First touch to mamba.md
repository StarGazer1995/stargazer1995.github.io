---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XR5MPMBU%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T211642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICTJ6zfarx0oaP1Mk4%2FegR4Z2R422hOeKRT9fC6nB8axAiEA07%2F2XbcjncHpxKvn9xQ03pLmEEvxm3wBwah3nnmwtP4q%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDNMz9NV4Wd0HYxUAhircA5%2F4jEhPBvjTjotN1UWSZEaosfCCW3ujCl4dr3PLdjn%2BwwJf9xhKAtWu6%2BP4oNDdLD7FqzXyKfmBoNp4OJU1LG0t%2BZu1X5ZPA01lznU9ZFR4%2BJKNgY%2B40RCF%2BoNK5rkflmLvQXYES4K7l%2Fu2rIbrOLWkVqEYt2rkYSWFlMXIszY%2FW8IjEMFYz3II4gE%2BqHTS9wjU4VVD1TCxIDY6q%2BggQxuO6jlLk0f8Crmf27RHEpaERYmD9hU5yZrnjGWn6pAh2kd6%2FmMBhM8qQ%2FRf2xg9HzyRmTLpPoEOhBriKAZ2uE%2BBji1ww%2BRnttrOF4GebFAilbYZ0QWQfsbDPQIvSX%2BKD3fA6Ly73Csvz2pOAayZKxq%2BupZ69egcCCH%2F5IifCGlePCkDWZ9wouoNUN63%2FG%2BraSW960%2B%2B96xw4noXFfasPheeYDpimjQyp%2FeOWDrDcXuxZT3%2FSLE4sY4oMgZArDwDJiP4wqI71KLZi5WxVo6HGnY3qoXeCxbXQ2Sor4iYhvgiO1apyLb%2FZax4LLu%2BVGK6nIYG%2BQLq8hboW7NKwaA1ufZmKWNcYziqiO8ic6Xm3OUNZeDtilXS1c1X%2FZCrdF0dW%2FbdhwrUdP716kn7fFbcbmA%2FOp4x3R%2B%2BLBW2fkmEMPigjNEGOqUBDaXKVsieZf2F%2FOIWna75RwkUvVRTinr6Knn6JC8uCQ70Y58sKIwwe26S0TeQBJ%2FyOO%2BUxCs9oIZMOMG2VndLfXsKDNBFVGFudJA3290frfsTiBMj8%2FSr8r2cpMo22Wzi6ZpImdl%2B75R6fVwAlOPxJSMwsj2JYuMpY0ccXH4xZgKeQCwd0O0ZNZlte%2FQ%2BQpTMG4Rh2Od%2FrHzB9q0C8OcC%2BmidddAZ&X-Amz-Signature=d2c1a05483735a83d25505da9724875f412813d2447c663ad7ced1e57a8e3951&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
