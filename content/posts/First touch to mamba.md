---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYUHUJOR%2F20260919%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260919T194306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDVhJoEIo6D3%2FytKXKq%2BUTStbyWmvfzzvdpZAjsE3PulwIhALJbMmBQqGM1G2keCZwU%2FK51%2F6b4NE3U9V6YaG23DUBWKv8DCGQQABoMNjM3NDIzMTgzODA1IgzNtjf%2ByT4MVnihYhAq3APvQtcacZ56hkLSoE2SoUl2SMs4cV1Xpd%2FmRL%2Bb5DJyhvaln0LAjTTbXnxskZjTJlZrFMLVnUrMRuf6RjJqHsAYz1D66Bu1PZDuzkYIysWqR9X15MnCp5pMcJyCNqQK9kDIv8Ib%2FTSoMWCbnyGMFe9ropGZkAxQJXmiZua1Hrd8NOL%2FYuJ%2Fyx2gwwbaLIweLXUK1rYHff2q55a6Ib5Nn3Hrx2%2BoVRBqce8pIiWcQsjArRY62QuSOsXn23Z%2FxAONnbqCH4o8aqarTTFl9DW4xaH5JJ0OCz1CM80GIMKPRGS05E4KwIXBLjRUdkSvPqQMW1104v0AZQYB5CNWrKSPPaWiyaRS7Cnu2rQKCunbt6RboXGJAtdKZZ1xEe9IL5b1%2F3xMM%2F7eNSewvsU4tXY7NHYRCpjWp8AstCMBTphvK5U0cXi6Y8YtYt10Q6%2FaN%2FTV%2FmnbG79MaGRVcHomTTdxuAvnkiY2hiB6iAivXG5K%2FekVxIRExYC%2FuIuPdEUUYGeGAufEoF%2FonN1JVZ9uJhhEk7A2oszg3BoV0GUx8P9n9HJSCd7d0S3SVq15s2dVcuYGZsdVeKOr9DLS24JhymrPcFrSHZU4yvx9Fu6OV5Qwk21nMRkV12Qym2vH%2FRXF3TD%2FsbvVBjqkAVnz9Zr7fqOt45HQCqiD8WPgwaCh%2BeTl1to5ryZONJg2Rva3gdyStlbyRFYnQ%2BRfXl095TlUcRHSVLPvkYMZ%2BT5y3JhlWbwH7YFVA2wv9cTtVd%2BF3o%2Bhk%2BoRFEguuwqVn4yXvE7ZOj0mKgv5QQPTGBIxyTPah%2BLO13ngdM%2FV%2FS%2FL8WYGUX9rPDjBcEoE6G%2F4d3jOSTk8izzolpMdgu%2FrFC86BqFm&X-Amz-Signature=cf7bb301281288aa6b6474c49902c00d728ee35581dc6824c613a61e6670f6c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
