---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQ6QU2N2%2F20260903%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260903T233811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIQCXSSbT9woK6omyZqJFLuaF%2Fnk6uG35QkVl0guOXhv93AIgREsfBIGojrJaoMVx7i5otsB3pfNZ2KrWcrv%2FTql9XBYqiAQI5v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKDA2Mwdb%2FVYu05jVSrcAzai9BV3NCmwsgD9ecSsC3EW%2FdFe8VCnGMPqNYCDx%2FWdAopTkuri495uRN9mE73AmbqTky8oRoBt3HlwLOh%2BaEHiQY%2FSCAekh4QcL2ki1MTjh%2B3v7abJ9Cj00T%2FfS%2B0n7XnFjeBg%2FxmWcCuMTipQrn5T6mnkmmEP9wg%2FG4pDEYy6ZvIFL2XNDRhOKc5qPCsPq8kJxin29v7iXW%2FMJ5%2F20ef825PBAvLfG%2BJz0jr63JjlZH7NCjka0zVn%2FrQJOYccE1%2Bc%2FMvB9uTp4fJMWmjw1sWxwmK3vYz944RjRnxvr4rwt6rlQKCmb2XpPfrNyxaybNiYsCctpVXshQsY15NN5WXhO4lga%2BH%2Fp4uHMJHrGRhypgxkgqVOHy8rEfEzMygc%2Fmj6LdmFKL2L%2B%2B9AXtHZuo2va3tCYvt1tlP6ZbREQGKsLTS5LieIcayHQYmAJddi8l7tZF4MRV8F0xXHz9I5XzY2drSh23Gbjq0cXeLiOlpAZm37a9DGsMgj1SZZjudamJj35eQuBRIjzxzFqJ40cm5nJPnAz9JffIWgAd51ujjySxHEiKmDEP%2BeGJEBnNbk7nceoJ4aD%2BNVfgHaJvd2bBhRTB0urgelccR4HEHtdq7fZzsYwcZiPPYsP06NMJW959QGOqUBYc6DVFvo1CAMCbNIshENJlmlmE1CcHv9KcXrFdEH%2F1h9CwyHLagwNaKHKaToiw2TzxgsycKq1aNIxvCj2NCP28n7zBHQ1rgMSJQFmFSHfMMl4ZFy%2FevZdwN37doJVuXyiX1FBlcpacgw8JRP9kpX6W4wTnrB6d%2FUoTdC02GPGAfb%2FmTES002IOaihBFo88IfuGkXgZbrWUrvLgqmyI%2BWrcQJ5RMr&X-Amz-Signature=51f31e4d4040fce4f471e8925264cb122956bba6af849832f17d345f54407282&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
