---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NPJO2C4%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T052401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQD6TG0UaTFpGxs6cE3y7VY4IeKKUdMgT5k2RjapM8bAzQIgL%2B786qWsMa5ZjqvSAPWjaoSQV4E9mSCOUTDvfZus63wqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMR1F4idQWt60R%2BZWSrcA%2BL5kekYDLw5K%2Fy071nEH2zmjM%2B3%2FO0nTRWBNZJwoi2KAAAzMN6o%2BGJIUDsUyyUqrzSL9p1xley5Favrv7qvCPQ7%2Fd4HDk3Uv37jRO0Wg2YarI98xPLKXHWOqBGdRuuhyNntuNcVSWobBgQXsgkVAbM4Amy4b7dRK618gOwJdfHXTMhhHJOCGmoNBZsSTakWeW7UukQv2fgG53X5XjqNd3n0JREuDcJbrj8UQOSrGbPZ1ADahfxnQaKEAho417HF5wZQy4h6vDGWBUDsWNxkxuJdwUPbBIW19LfwXWIjkzM1E55F%2FrVSzGaPAHhZ6JHvxH%2BMPYYcSuZn6Ej7X2s%2F4S05LczwYRoEVqZZSZqBFZBanKHfowflqjyOJUAKTaJ4pQJrWDne2QajagmtBr3RccOYZFOLGYVHFAO9CQtDdHgtc%2B3L2C3ZN%2F%2BN8ihmaRrLF7yZldO1D0NA5QWlzOE78Zl601zBf0jpEisajYnkMYxA7BhS4%2BP5nu7QIW%2BjzR9V5TPnnTcpE5yCN6jcU2loEOA%2BeVkWN3xBCu8H2QE3x0vjRbyOe%2Fva62YPdBoe2r49YjNDd9M0YuLc03bWDQJGAucroipaz2%2B5Yzc07Oazx4P%2F4bDPnd6PI78wrhncMM2f%2BtMGOqUBAtfdLTmC38pSVE7EBILzUv76XAt0ZunKXn9ccGvZPc4wRSX%2FxDB7uf0eoWQk0mHkbQa8HoSBmbFgDWhX3qO9dZTBPMA5BeQnVq1F0eWPrYkwmpyKPLSQjMgGqtVydiZTpjrxus18NYV95BlB3RyFryJaAQta7aqKO%2FqrHlBuR13V5Qq1vBTZWtLlVvzA3u2cB5kMeZ9%2BPHxZVWzj5rZZx5uIwZrj&X-Amz-Signature=643390b9b8fe1d2cef6e58e201399b72eece91b9be333d54117b9bbf62fa105b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
