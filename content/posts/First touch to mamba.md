---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIYSKCAW%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T143136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIBm1S5HK5MWJYBQUbkXd23nhWk3ypmUKyyvtFN6iq%2BOfAiBb3%2FsaKc%2FjV22E6Q9APkHr%2FUPBYf720lmLj8BlgvBxJSqIBAjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuo1XRecRoOarvJpjKtwDbCNpyrPocTtf2V959G4gk5YE%2BgarKN%2BZmCPuQk6omxRKOiPBHEXw5qHbp2tY%2BylUkswOSjEorGtcl7pgnFQeRggY0R2zDpXHtmxDwf67YZEgUMFcJ22%2F1DNljOjJFClAFSdPuDAaQEswfvLV%2FxKiRND72Lu52WSmvSDWWPeVzvDrleRuQs59oob6yTaWqZXXs%2F4sZU5V1QFFwamAvf5aVYTHt3i0TxjjlZhMODuuESlFC0saM%2FPOSJ2XEt9tY%2FBOVk0gbDyrYW4j2ZruMT8tTO1L3ZF1mPRksxQeT5mSVyjJH%2BBo07xh0BL5uhGAHPPkV%2B8KK1lbKwVxGkHLaUZVbmNhpHHjNvLEhDlRygm31lgK7r8l64vGvbSwBoGRtsBe1QlEtuPy1Z0QkkS2VroZ9Tlk8dre2VJpRQ4QTWzhrTGS2n0dsSH20fa8nmQF1BUJ42C6%2BwTSDpMSvqXtX6Z6yhtsNngYDBFa2EczmW9CmAdSEXGRel9BpTGnodFYl7VjO6pRLps3Gi3yTP3XQKoDhnnw46CiI1pFUdmlxw5qAUTXg25%2B3KCQMflLiiK1zG5JE4C9h%2Bcu9jiEJyvPBJCzc9mD7YVEG3YbW4n0JFlIzLGwksMW4JqJWMeFO%2FkwoYe30AY6pgEZ4FOZVPW3GcPmxhwdz%2F9ZroY%2Fc%2FBWl3S0hIwd8U2BsThyWLihQTPgr6xwodl5bawr%2BSgs9sAN0IsZ4KjXUg4ZccY52Eug%2F%2FVg0BPVajQjHXWuSbk7WCT30r09Fz74KOJuJJX7UqweftPJEowbccFivYyb8NZjkpP0C%2BveIwRl7lJQSKp40U1YL70WivQnC9jafCsw16JGD%2BtCjaj53GP%2BRmwWF8kx&X-Amz-Signature=0796baefa3ba151e087a876918ec41147944085f653193724811fbf44ab7f88d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
