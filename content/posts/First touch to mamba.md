---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HDQO7L4%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T171707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeX01cSIiecYx2G7UEliTq10IV5Bt1QeE3wdOTSGduOgIgU3RfnBx1LXGkUsZ1x0Dq2cw6VQ2X1XQ%2FUvE%2FbxJxXLYqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDETMCjptSt1A5sBYbSrcA%2Bgs5HdOOVYmZd6VMDLn4%2F0BMRDc3bnWcb8C36rzABGz%2BELP6MkaounWuE2XEdbibjK%2BEbURk9N6jZnvZbVWpa72LIgofRMcjmLEJSu4XBhzAvrsuoHf%2FEDYrQXUf2Wx5H0wFBTEducDcR%2BXChtFa%2B39rwE846bhKfjrZWRQiKJXN3jxbdf8OSr2eGY%2B3w0kkr642yWO2V74OKpwO4NSGOd5bUFitf0RMhldF%2BM9eALOp2%2BJwKEq1aHUtYmfhj8E7X%2BZlR1ib8eJnUujmJZq1yAQsYj%2FXSn810OoEXhPJPLFJbi5cubf2d2%2Fkaz0HiMY2PWf4KJ9HHQGdjDJzNN%2FfJ2VTq%2BUugKO2m7NBvTgXMVNOaymucwRta6cK90TxjLldlGZjduUoi3oeBNAToxE2cUIMIkxzKGtFwaxQMQS6hD%2FUJ2kIsSWBYeSr50iTXwEyYR98ngUc%2BrN7mfRzCcXVUVTj8wxLmIevZcsbWUSoVknP3cWyQ4OVxyYll0gzKcbSJxVU8qxJo08mAUrfdPYZDiGqyXkjkn%2FN%2FMxcTro86VYwPPHrzEPMUayfyFZ1XyvcflauHZBs8Dh8n8eoG%2BIeYuhJ5TYDqqAxjm7YjE3tkBmNis8XEPbB9XS%2FFZOMJmZ%2BdIGOqUBxIsVual95rKtqS0xaXxBu1HFREU6G1AiYw%2FiMIOhhu6xYK%2B%2FnC%2F%2FESXxhrfJiuwP%2FHZMgDnjXM8i%2Frh53tvPuzQ25zLk5Nyp%2FKnQacxg9zZfswbbzTvqjEi2SDQjE4XGR1dk8wtIp87LG0aeFx1d93tKa9Rzs0RPEyNRGYSd%2BS5M%2FSbhMSQkI53TZMA7WYlsKI6MpyBj3eCNmh76vSakjY%2FYWhRN&X-Amz-Signature=9e85fd5cd7d11524e8f92d147f758a2da4e011d0c05352da5de10ec4ca93ee89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
