---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLKL2335%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T144432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDYaCXVzLXdlc3QtMiJHMEUCIQC2ZMbyRR3xUtdFVzX4WcieAQuxAH2Ap1UFJuDUwMXFEgIgQBJnA0ntz3PngY5Oana%2FlLhXQxXXnaRlb3Tq0qCyXeAqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJbamzdOcK2OTNDE7yrcAwXoM88qKeeIUwu8WuOTUMxXMSCi0iedXL6J%2FvzmjWK22387G2AtJbJ5yZLdljE5XMdAWhdArNyRFS%2BvR0A03l9XWF39ZsmbYarfuJQI20REDi5reLb5ON7vQTFnM2k2H2a%2FwmHNvxxCTM2dRZjIUsD0NWwfhmHFw1GY3amug6gud%2FhRm4CnfzZexcfxukiZ1JsEYnyfEnizAOtFIFrmEmqGFf1I%2B4bj7EJYcLphb4qmgcHcNlp%2BNuDxnv8%2BwV1dUfAB5GtNsNCI9sMCRmtBckW0EnU80nvftqw7YlDZxXuqu7NG8JhE%2FRX14e6sJy3ndqYHj1qxXMZhZK8dl5w%2F9A5NoIp3nxJyVIu5Fw0Qn14A%2BCYhiE9KBR9jQdgyqYGRRLLnre5td4i7%2FdkZ8%2FAmhVeAO9JF8dKxOqzAB%2BG3u4Gr7TT4eDiZeIecYDAr%2Bi8y0BxBVbg0Be3jmwkZK5yS2THcefJ3%2FOtt%2FNZquXKX%2FXw2LsKUiWW7CGcgBRbBX%2F7FGWO3OCS5FxOICzg04SyG%2FBrnnZq6jv09wbqYhAUAwhzr0pMFuJ5XMkJHSOzzPl6R3xoKroRruwMrG384LWfVifmsnB2weby6K0FNaf2MXFrWVHtQVyEaOIAANqFpMJjB%2FNMGOqUBG0ENz72ooPuYm2hpFesGfD5%2Fxeaij5i5xGmdfkrN2RoWXpbwTc1v4rnN%2BFia1sP5dA4UuyLTnrenl7Ul%2FaVB%2B3IrdBO7I5h8f7vs0sQkQQiyWNrYC0BrmK4d8SXeABr5d%2FTYbWGDaN4mBmFzIMhtOZ%2FdYK2AqA4bpa481WTTVRdqAfgLHBRiOMtXwvzVMxQteZv%2FML9d462A855AZ77Reqf7YWV%2F&X-Amz-Signature=be0cba80e4b089d02c05432a4922f0c89ad6c93f59e68a4babb8859708f4cbfe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
