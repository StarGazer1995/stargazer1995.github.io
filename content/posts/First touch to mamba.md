---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SS4GDBYY%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFLa36Rd5MNhk4p1KWp4nlbS7I7%2Bqv0QO2nXKlRv4M5YAiEAg9VzzWhDxABHRFiZAvEHwvF8NJgDVORndUi%2BjdnzeSYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOgzTYKtjWupDcFqBSrcA1d4sbm9XYtke1GEikP4CC6%2FjZmzpDGacwkrRGn7b8BLNPknIyJVHhtuTTNBAOyhjxsy5JdpJkOHSvkVe17wa3%2BeCT1MBFmAOpP0CyTPc6dSGNoC0hddJjPHsePwZ0vZZpyq6AfHGSeUAY%2F2dsKtndJBfqrTrSa5MXs0yhFao7fuYBfG2AJrVcdsWZF%2FNR6LZNTb7ItlBhMqyiKsZmGBApy6b3C20ZMILveFT9Cqv0JG7YSnGH3nuGZdQoExIVnes5JVzEWb7gFFcmceV9L84lAMIz79mMXfhHaDktJBQ0%2BMU9%2BtZc9NLNK%2BYkyfuuiRPrCAYCV5TFeDFP9bx73fuDoVpp1cdt4GoThJz9nGsAFOSWMEV8fZ%2FlEuNP1VNiioFo2CHgCcPjkJHy%2FmxwsvjrXvL%2FHdznzW4ORVNCImcCTQtqERDJlzr2mC7tIiiTg85i5X%2BaRJMyEFHevNBWB9Hv58AxeRqL5W4T6hDjP7x1w19%2Fqb%2F80UtZQKClBDc5xHryidzv4WlgZRDjNlPLAw8qKpu63bpaYTbriwYYiTSdsCYJFoULtuMSVJXGL15vcH9qum%2FU6fOtLOwZYV4N5GKzLAYVFmEi913GzZD%2FegxnPaFweaEfWTgAVpKi7cMKa4%2F9IGOqUB4o1Sz3S810DaHDUY8k1AWMFGcCLuNaL2u2iYT6uvGIGI83hHR6sMKVxp60xM3r9OmPRQ4JIXKJ82%2Fz8Tl1w6Ft48%2FqtBTi23ddq8%2FKM4YPRkgF3N%2Fr%2B8bRH21ydjiSzY4dE4rgVxZu5bOKXSuUwIPcasYEgI%2BXcBZPOMSlBWYpNy73wBeJwCUWIH6a6yooal4wBhlekv%2FFXeMtnMQCr%2BTFqY%2BtlB&X-Amz-Signature=27eae46a146659b1bfab2f2a5a4524ef10323207733611e192351c7032ed97ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
