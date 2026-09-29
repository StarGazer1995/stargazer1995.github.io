---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFBT6Y42%2F20260929%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260929T142529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnzObZa4BLQXKfY5iROmr%2B%2BpXjiaTTwU7Wuj4Z%2FyAg3AiEAmTtKGng1HU7yD%2FANnTaRg27iL%2FyA2u23%2Fvmw7zWsV4gq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDAqQk5fPdOTUrHgv2ircAxoPeXpp1vbA0g7M6IxnJkjLZecm5F6jNfirnw%2F0Kvyj7LElCxZV%2FHDtfchPOfriVISRK7aS%2FUcvP%2BRzP64R%2BGDGzc8EQRp0dL9PD15k4wsFu63XVPzkMN8Hsax3MHs%2Bqe6VPNBYIQbWNKJJtlmZigeQvIujQSkklL1rIVycXQtUW7ou0dOlRBTRBBLAMOxl9QBNbvg73iF9aBj4kJjQxn%2FTYpzKAhV5y%2BGo0Am2CjoDsESA%2BtkeJtfMLcD5RiHpHT17pDXnQiNKV8oJiZF36hwf2gKlf4owrYMgrAQI2MlPmzv5uyzxAaSN88hXSK4teBD7ng6lico4o5Xwlv1NVySWZF6OaqWVQyYRRUYLDBYlTDbfUTcQHxQ324kCx%2BPRl%2F6XG3rRLTeDQmtz2ByHteWEksN4MY6fPLBg%2FKRO73TdwF4T8vTKfa7WNM8%2BuyjbsUX5JeoleEUmIn%2FntOBwSPfQxJ5iqbIXF%2B0WbgmR4n1hstoGsWDuV6eYQqJtcfnbGkbOEcQn69TaDEbBwsxE3eOiPa66sxUvw4MWF9Wx2tlw%2FmAAJVyNtIbwJb16QYPy4xWZNI9qXydHVhYV50z8Y4lj49Ks2ylH2Q8bJ569pIZ%2B2RFGvEIIyQoy%2BprlMJmK79UGOqUBvVTnhNBqj9ovNTn7Hut89Ieu1QCcUtJNurgFKwxdqueimfpedpld0MrqWSx1VcpvN%2BojFxolXkGvxE8t9cCjXqDiAoWQ1SXcJPS1NsRhcMwwg6XAtAiuTD%2BhH%2BeUn13sTY0ofkFD5nuUCp7gIFAnvoDvw7TS%2B6cF2JEecsqRFi4jMWqDY1DrJkHMg5rEplowZUyWYB7avxwSHXrWwn5W7yjMdmMh&X-Amz-Signature=f57703a1f4bb8249abebbeb5acfc4e50979bab2e3a0e8c6176cf865ba8ffd024&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
