---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMAMDFRO%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T062109Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIGJ82kMaFAY6IJyX9DaxuuWh8C3zdFPFDe%2FpBlpoklaTAiEAlNmx%2FjiepVLpq0sD9NMytxQCk4bvFvKxYCCoxoqZnI8qiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH7PLzZAP8TBgglUAircA7lvYBT7WiehuRZ9qnnMsNbufXF7WwVyR2R93hhwjPNXBPahx2ucjO3NseyTk%2FR%2Bd3osNHGqE8mD%2BLZlwdyLxwdvuhFQDl9%2BZGFyjriCrDUFi8pUGLUfM0AiBmMN7cjqUXtOK9G628dsMxaE621TtnY3kDeAPRUhWVEXZGtGhh%2FoLym56%2BL%2BLUMICpYbFNEvN7aVtnAjtX1FEascTirankAcl%2BBpBCNVIixQMWqH3ol3tevNx%2BWb7EPumhdA%2Bfgfw5j1%2F1H0NufhGMvzxAmNnzZN5ulRMrGaSXHZCBSC9FIBpFqui8CAj5az5393EnMMqvAl0%2BqC9VOd1RLWuFNvV2HnG1ekOcUPAv0gRNqgEVbxaGkmt4cBTM4J2SQi2K9MXAwyI5eb2XwaigiE658%2BEz5Na0rfTsY3vEG%2BoaL%2BW5IzuBLYUc%2F1Fy%2F%2F4g4N7SWnfB9VB6FWiubZUGdsUU%2By1duGgy1TdUSnjb2BuEpIOT%2FyG9Dr5yNcmd9Ps13BbL%2FkaKrEHB5HCC5W5xtaFgGDOcIrXFcr6%2BVQcRjgxli9YvooK0oOheziGuFToUCkXpUYJuxPc5QPRlVGWIcGeEhqoDL4flFF5%2BwUMYNYkflQWsHhs4TbU%2B106gM8lj%2B7MIi3qdQGOqUBY3M2A%2BGkHtSIhN%2F0FulQb4nBRbdqAVU3mpHElAvqzvYTOe3RKx2Oi7zDO0RAP3zg60OFbZK8TgBHnSDXadq0RQ2pDp7rOlzwU4wh%2Fl1JFFfasGjyD5z%2BUtdxSpsbElFT31zIIFHEGendWi1C0%2FNVtjkF9xi7uOkL8rMCgI5x0zCyUpCCYBxtrwmoIzPq29cCzPiOyR%2FBfq9joOdZ0so9dZNCOyw%2B&X-Amz-Signature=9ffa8c68c21e068367be0ba59579e2d81189a6976546b2ffdf87da8eb02905c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
