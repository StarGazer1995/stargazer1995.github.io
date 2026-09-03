---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677SFWVB6%2F20260903%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260903T172251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIBw%2BJC7AJl%2BFZhrCS1cdpGSqCFDKXeVpO6T4NJwFMkkIAiEAl7400hji0MdBCWOVKD3LqbunoqoHMza4eDIC3lyvIZwqiAQI4P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIf6aQw0xLDYM1cXvyrcA5aEueZPh%2BJB70Auq0f8OGn9516wqHitffMapYdkDhkpRThb22O%2Fx12dNCBY%2Fg13Kj%2F7Pk3mNEPC1BvjhCOAsBFmADqWSI7yd4t3xEA1a988%2BnZ9r7V%2BM%2B7spXzz0bn3P6oA0woYa61P4QXl4044GZ80z6H%2B4iNyRVg4IqJWCqklOMv%2BzvgCX%2BeszOPqNc4Lui8bHuN9IbM5Hj2q5eCYrbhXz2k7iUqFgiT3LUR9gVFU1okfpEvz8GCLcfnkbO3SkQy8JS4C1LeWTqtY%2FM1Rn53p67XrJbdNpl5T1%2Bk%2B7F%2Bnrc1KMmUMz7fBgdgxEy73lyvRe2ouPFd9pcH1VW0L%2BQWEoqw59VQ6PuhvGGq%2BIHnfVKdMrm0Gx7q3gwr%2FiocnrV9U6JEodTD38lyXMzwINdAfiyxjoXk%2BlIHe9lOfKxf4UWTM20wu5fuoxbEGQ94BQZSdwIhRnb%2FGkyg6B3oSUVpN2u5aViFzmofYCNYCEV%2Fd5bKuNKpeVPA2D34qDunFSqkRmihzLfkoxqpRdKlk4yxOPK1L2Hh4hKVzwmcnMnq9VVTB3wfpdghZNYSpFDitnpqNRCaA2yBISit9qz947UQ3ewykk8ncHjnPiNeFgaMtAB2ldgphQhMF0NCuMP2d5tQGOqUB3CWLYJqjrpzYfF6HEi7lT3BRyYR2lJSpq9cAhftopMOoRsCvmuk68qqPzEMonNJcEM82EiKQjq1JLSCSMLM79%2FzWy8rB03ziCvoMC0zCAFL46gvIV7%2BTqewqU0j9hf4cIWbUvV24yCBckMfQ%2Fme%2BTA1E9dUnuwi6%2BUiuK7u0F1dyRSTz0FVG5M4T4VVBFccaxtQQZNVAIw2Mttjlg9qM2fLlPsU6&X-Amz-Signature=7a984f062ef57ed5e0ef8962f838cad48aedc47d7113347d0f54b17cd2579b0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
