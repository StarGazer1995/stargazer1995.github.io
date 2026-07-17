---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKOMYMHY%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T111358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGWoY8NonCTY%2FXwP%2FTsEpmM%2FvbPjFgCD0JcsKoiZ9q1zAiBV7Le%2Fw265EQ2lQO641H1Upav3miaup4gqmHPoH8F0MSr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMzNEocCc94RQNtPDjKtwDqUcJ8XI9nWueQbbvOOQKcTCp5r6yhDX7%2FTeh4taAqaMnAoXGy%2B5l1IXcMp68wtQt9ybFuhKyAsozePNtkGh5weN56R8aKOyqcs3Rtfoh23Eqsf6Qo0nNR%2BWfNVuqjdJVtxfrmtJdnWb3gwKcbcliRJeAjIFptqeuCft%2F1VQSBqEyEBfKXHkGy0vDrUdxBYE8JhvHZl93dJfc7pUE77h1PUbLSUmkWAF6kuagG8VZmAhoWYJrEkaRQRKLYCRQ7l4YqsUEXkGfnftP72HOR%2BjFukVfNeExdZQw3BvWgWbO8YOirFATsjemPQr%2BIIfDW2MaC9RNIyKErHUX92ciGiT7MZEXboDqGYTcTrV3aXhxvDB7UEN5YThzUVlPY1hBY%2FmQjLMvlbtulSCb9Ga3gz8YtOgo8XWo%2FAKp3JKgUdDFsT9wXr0v9jwryOT6tD5E1kgK4lNUXrQH7nIE%2B1lFBUjfqCGdOdaXQefA10pczaoBMTHJG6ZwVy7E5neUYUXrHgKGHxAboReUcG9hW%2BnNvSDeU8Qhgd22PrBGzsCRpx%2B%2FMXnNP28mRRjrOzlq7a7ZsBD%2Fa%2F%2BtC6EmwOKjc%2FsFm6owQVAbETmLx9S1jAvp5ANiSSYOMhh%2FdmOw3unFTvMw%2B4ro0gY6pgEwOST1Qsj%2Be9aFQq2qfhLi%2B3GfPmP%2F7KXtGUn9eltY1tkEq7yzW2z5G4KXrkD3lRoE9%2BO4p7LBV72X0wUSdWFD8Unuu6WjvqSxQ9k%2FVnz9qljhXxJ3%2FYFq5RTaaZ9aL52T8AFqFriej87hdKppASQsnGIC%2F3acyHLOeazGihONPVf5hw8hRTGwldEkJ%2B9F5pLlD0lrcs9bNqyxwfwVRpyW5dothAWZ&X-Amz-Signature=02d921db48a63dbcfb9d1e1260c368394c6ce32c65f7a427894a93168baf0b75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
