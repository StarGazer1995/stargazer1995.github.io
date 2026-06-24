---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPFDCKQN%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T192513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJHMEUCIQD7BMoOGo2tOJmFu%2BZy8nsgy7eg%2FIEh%2BXVInJl6gUKL8QIgO4ZoTz2R%2F%2FW6OSNN%2B0XAeeHBM%2BEzEFZH2Wfdx0tvXwUq%2FwMIOhAAGgw2Mzc0MjMxODM4MDUiDFLmmoal24P3vzynXyrcA6scRmTT10qvCFeJoHqFwoEQnqLQ8fudeL2YHisRrbPzqxC7L%2BjbfIDtjQG%2FqzkuCshf1zZvMK%2B8%2Fc96d1%2FhsJnCCwyJ21y7VVDzj4hGE7aWK0857O3OT%2B4yTPmXLlvo080995ghK6QGaW3BngSfjGfNVRnK54mdhJz0ulwhiikuY1wu0w78GnkTeyOHA5LMnANVhMrNwXUA5j4ToDJgf4MScs2V%2Fy9aBwcNHI4mLD4KrHmxN3nxQfkWyR2wIDJ50g0SaYKNNpNkBrNWwSRdYsrkWPdrnWqapDJre1%2BKqSB9WespOF8%2BlxwQDRcm9ZDvKWvJArrLsC2Oe0Cjg2cwi5YaLP5XD3n%2Fxo7uChVnhBhTy%2B7HDhj7PE8uIcNEryHHeSFNr2SXK7RI91gAWg1vVI4W651PP7hKTYUtlWgg1ZuMR8xML%2FuTNGUbuvuT4ay8hbsViYSFg2VqFiR8pB2xf%2BncmYMae5LldIVE0COWxC1VxTWPjCdHB%2BDnRTG57UHQGDa28%2FdKW4rZdWHyY8Cr7iHKZF0WPeq1fob3ty3hunlNgjip1ZSjKUxvUW7l43VyHguiNRn%2F43z9nwAW%2FYh%2Fix%2FVzUZV1gJTyHfozC9GMxKg730j5Lcj6TI1t6sdMPmT8NEGOqUBPuqRJjfEBLkNjCEYM83LFq1deQH3NXCdGlzo0q2%2BcPywbAAPP32tAXiGdwaHjePp81AOhGo91umvMbI%2B3BVhPgjx1z%2BBV0iLQ3vs%2BYyXx97m5o1LbII9%2FRRQVNAMRRFHtYE8kWNCS3%2B80%2FqGTqutTHv4fauh9E0bZk3BhBd3TBn57REslCyJU11Y1XBhYGS0ubZyL8GsZ6RFbVrBDgpKF3tGR4nS&X-Amz-Signature=f980750fc0294913b208d64ff09f2c27a001636d3d1087847f5e0a7dc7fa8537&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
