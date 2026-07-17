---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDAIMWHT%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T094509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC0OQ2BWLYby0x%2Bs6esTrJQPr8SgXM5z0nKQPRh2nrg0QIgHH9QLjCGWUGHu8NBILVk3xD41ZrcsyWK5mDRSe%2BA%2Fksq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDGzqHF2kidGgTM0AQCrcA46J0xUgKqoO%2F354bWVP%2B7OTzoQsugtPN0vnzwIo56mT1wSf2grk1jkbIhRJ41V4o8HxdzvEQ6K%2FESw3p03j2k0JLQLiSDcG9azQH0qnaY%2Fn6JaNEjza125ABLe46DWwMJW7xwa67R3oF31fpPB2FX861Fa1npDP55fsfcHFV7UniRzJ7c4xi%2BUigKJT8UvDC2PjXP4D5aLomdp7KoiZ%2B1KvjvZncQ6poW9SAkXRmkmg8zf7w0hZConec6KjWRv83nhG%2FEa37CVuNY%2FTRvK3mZRfw8qn2hB%2FSQuSaIVZ8iUAAu5PAzHyOaPvjL0qjmwdFi5OhnfxN2Sa6YXydEvSjfkKHw90qlaOBbk6h9AaiSPVoTPzoGx3AeWOI%2BnoZoznxh9zhT4gZkvMlkUhG2P%2Bu%2BcXX7Qs%2FiybLl%2BvbIeyiev%2FPh%2FALkqsfx26SCT9lfnFdJudTGE9yC5P6hZvzdxoNlkiwUH8f5ZVsTRqNcmBp%2FcIJgGTqLJw4xcsxd9IDN1jSRydUyeGgwjTrCI015BXu9y6ZGv83i9fHexfGdbbgu%2FXROC5uTkKnOqWF62uwf%2BE1eQLEW%2BG7kZI9ARGh8wonNC6F%2BA0ZpCXW2uYEpe5DC2wze4o7OIz0mAzVYzOMKbd59IGOqUB6ttobqSQOtuszKoByI3pnzFtACUAvcXpkwa%2Bnm1ZyVYwi%2FhBBGw%2FovH6ziyJoujV4KMumuuDJMHlSg66i76mpGcJ%2FpTWI1eNky3V8dR4IjejFHJIVwGIkMHbdBUejowb05pXdnjiCuwggZ%2FbpcLfQ8aYspbx%2FyGXORlw7nlvaZxMrDygsCKlyfS6YRJABuGwzCl5mWMbkX%2BWMrtgSdCuNB8Mk03O&X-Amz-Signature=999bff3ee9f610978a9f88d2ad841c0bb61c41504fe708b2886811ef2d0a0cd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
