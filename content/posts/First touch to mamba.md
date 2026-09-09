---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LS6QRSY%2F20260909%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260909T200924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FQo2RJ9DOgn0Q38dqg0NRNB2kzyuGiVz6U1yW0SopNQIgTOIs1fS8KDAOWAlILkSHwe4J7D376p0M1HPIiKQ8Ljkq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDDwiSbWFMQptTwtKoCrcA%2FhKsbQNxcPoGwRnf4dOrrGLXSfPEiB1sEhwLFGYNFMRZFs%2BXCIGNKtCOmfxmK3emEX8SGTqaWsPHOi8Mooscd94clXopt5Y7g%2FdYz9AeK2SmsR2uHOqh%2BtiNvkkfN4mLDHEG1eiMh9yVdDClltjrl9aNn7lPXwi3w%2Ff3xWqPgGfg7MCBfawxfFlPETvlZJwFkd5f4jADC0PpIz0%2F4%2FawomB6WUhdGVl%2FlOo%2F%2BihI57kqO1R7jLaLKvfNxRSHq1DyDecgEPpAhlliBrLu%2By%2Fcd8AfjvP0sClyTo8dui9JD%2BfICchWAvR98BTD4LZ%2FjVQr9y%2Bij1pxzTJ374YnxiZBk5yVQFlnoW3wfYLHAuoKIg1%2BEpYjw2BkyNSgPaGFaqeHhqEn29hrBOpw7iwser40RHHCEY9Ar0OV0NJHfI9L0GoQUrW8rvvMDTD%2FzJRpP%2FdzltnSRaCw1ducLMnFvWpo7GtqCk5wuI2z1IrN7SZYRTFzbAcLN2asmX0T2YBfYdrhQKWNPtYKkPiX5DAvlV7ZNun3ScWMsvm4Udk9Tdou0L3lZT%2FZh17GAG%2Bqj%2FL75p2mYnXdZ8X7A91JA9pzFaHKSscyuUTUCzHR2WEH5yetGBv%2F%2F2D82%2B6fbCNp7pYMMXghtUGOqUBjY7slpeV5kGm6vZTwSo0DuxjtDn6qTx8XOcsR2dP8VvdPSvYZ0iUb0fV7pX7EbxWK8gBd7Bl%2BUkwQWz1PADiSsJ3xKfiSShoLPJ12xrXeIN7YIyuvM19RF3ZhTKd%2Fjd2Zlg7X2C7KoKbkVCMikcCwp3ivU91RRp6JmLSFL%2FFi7XEKsyMK6f5zbjkZNTh0f2x6yz6klIRqos5cugpf662gTORn3dr&X-Amz-Signature=9e44055798c7d9e7b7d3d40a869a4c9e9356b37e94b02b04285fd5f110a486a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
