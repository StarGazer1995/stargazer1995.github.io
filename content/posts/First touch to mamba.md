---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNUHROWC%2F20260917%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260917T192226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCID%2B3mcxR%2BH5GcOYBAZqZ%2FjqYbU%2FcPwfaBDZxs7PCaVa0AiEA8SHKscF%2BIJ3evjRZxl0AX8t7nCzAlasVLlYw2ySSWsIq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDHUb3AIhJsoXQuPYOSrcA896ygaahk8H6OL0FOF4YfU%2FeN7QWcLetZW3sKGAEXQacSdM0l4t98Ca7lXBj6T0MmfhJVMDiYeW6OArlx9Id7ehK35QfmbyROFRFtw0T3eGzlKreTWwJN7%2FEjCIo4hGv9jYOBK52%2BnUBrlxenSo2H2Kx2X9oX9kjd80sTuP6XJGIQFcVlrmy5PlsOWPSFmzD1P8YH8QdDHLoel2PK6iYEP9AK5HHUAE2Vna1wTKMynlVkfGJ9Rno4fqyKcvB4qOY8WdaO0spV%2Fx7MtegaF5ZHSkA0h%2BFo2TBiD3AEv%2FxgeyxdpItlmJC%2BLtTl9xJ3R3fqJIZ3s4vNEC9KxJ0mW4o%2F5w2QIpjNvIE5%2Fg7a4ncCaWzi9lYZTA6XnKUiZ3YjNtEgDY%2BR%2B03IaLmGGOM2TsdKY9SS7ysAn1N9R4BxJFWw0Q4kUXvRijxTCX7k2WsGEnUpkjr9Z2r7gcpB15NK6wJLYQHGrwdVeJw4F8d8OA%2FFP7K%2FKyxrRHE%2BzQaaQ5gwEZXkjvRexDMXlprXzWBbdOVDVwMCAoBur9yOe19%2BsW827q2WDpYp%2BbBZbxRgcE5tNBiRGLwkU9P2FJwxKck06ZfgGRWb2THE4gQ5oXpbYNL38boiRWfzjBOD%2BvV7WCMPSOsNUGOqUBDlSXG7kgsysz%2B6lWCqo%2Bt71LqGKBk1YbPJ7RMaaWC2liLRHOuWgikdrRy81WGiCf7Fm8VAVvxn2S%2Fg5qi4QrZfV6DMa1uWtGN0st58ma0OFL4eANCumvMtEAq0SET0DxVI48T0OAgZKKDBAG%2BHuUAyKwDUBT%2Bge9Kif4djwr1JU7lRvFWXmRo0o%2BJhfadGdhndLIqObBhVZDVB6s4klvST9XnsNU&X-Amz-Signature=5a7c7122801f39e4274bafc65dbee37148b8ea537a60920b9be498867fa8a25e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
