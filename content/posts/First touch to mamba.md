---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGMV3XGI%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T032405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHDf6xnBPcZtBRobMOuYUoP3u119F2dq53TxXiIbtN6oAiEA5HsYT3R6dg2IYDU47F1O0%2B2Tj9kgCWyW2PiaHgLOBuwq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDCjbVbzy3oy6uBUpmCrcA9rPpfuXjlVRDYIF%2FIhOrEkQirmX8%2FXz9qW2fTWWryTF1D1zulwjXZpTTCVKbNIGoDHhwJ7BjgK153Cnq4B5FHx%2BYGoBxkSAPmZeBivGYdynXri7sHMEQm8E6afnThpJP6n%2BS%2BUtMVBTd445RWKWHA%2FA4ZGRw9iUBbtcfYPn15SuCKw%2B6uZPsacTYZ3evs7h81AThZhEdFD%2BA27VWYZQbXZ2oRYWq5HetyQy0S%2F%2BTHy%2BwGAlCwv0YlBaJU%2BHHDE6hg1i7SsHg7%2FUTu93PRP5fgHPfLNIEkRt1Gh%2ByjdgKLjeigVK%2FzmEbB%2Bn%2FQ6H%2FSjMdI6wsWrq2Du4rnxq0uyjmmLYckmU9sxwawkDnFzVLEXcrIX4kxPpPKE%2B6BGBh5g16jFH9Hk9SkuR6aeqPjQM3QRFI%2FX6UAulKqfZablLJvgjrivlSUNvinLApbax%2B01uiWWor0432DKO82wVEOHJXWw98SeJjY6ZXD9uHdYe8IdC0zlWwcF0dY1LmrnrGBcRx42nlageh1lHlU1dQsVOZhdBXKjw3aS%2BtQ%2FUGbsjVCiRvrK%2FxmdqvQt4ANyRai%2FTzeuz%2FLt4p2Yknd8x%2F0kye1lshGCN%2FR6AIDedgaJDW58zgqpFA2gDuccxWiaoMO3T3tMGOqUBWuRChk6pZ%2FSRLd8MB7FoZH8%2FqgEflkME9BEcBYZ30UC29nsdvGG1AzzhY0XiJuGIAR4c5vQE32%2B%2B%2BybveOzYYvQ5%2B7JxlYnl2Oek%2FyHYfhyK0jIZM4i0I%2BXYIzOHm%2FnXseW2Ev7QAkyAWxxWUpVQX%2Bo1tk8eLYLa94e3JDrwnRASjmqv3XPJIXgUaZoGI8mmc55ZLL3mFY1aQnUCSueMIGi%2BCgIb&X-Amz-Signature=d02ecbceac4caa26ab18d203499f9373f684afa3306a387ab564debec3364f75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
