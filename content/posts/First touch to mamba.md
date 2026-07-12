---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XN5FZNCI%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T203457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJHMEUCIElJBpyX7k0B4iJSv03SvAYGt2BXhcNASWp2PRcgaLtDAiEAwTTcGk1nvHx5F%2BUZa7F6cjpEwoEfzay0IB54A4VwmfUqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMHsJaR8aw4bDMlVKircA5f%2BVQYmLcVdS856AfDbKbwdMdP7AquM78CkoCXVU99yOSolTjOSE6iwllzWN%2FvGmeonrJiKtLFvgDN6%2BeUz7GzoBHpKb%2BwUOl2P%2FOuUZtAU%2ByU5Byjos211AeXJLE3EecVXM9TUjIlSyx6SerGTSVl9W%2Bhcs4912MRNjXqKzPIF%2FKi%2Fq%2B8xHRH6b%2FUNUgvSgDFnwnuiQniqULND5JuOF2h4hPehnCoggZgZ4maprqGyna48Rgrg1DPhsisk82PtSSJwaoEd%2FSgIhCIdH5sCsRA3j9JDNcylIdMMfdKYa8DBoz7KPu5i3wn0%2B4625hwpzniSnHnIsgvjGwhRgGT8oksaAmzMcqohe0%2BkhNsPi6nsyKulx043rHeeVcM9%2FNPh0nHLZY%2BLIIccWYcds0gn97neVmpWuXF234Uikoxujc9RMKi2sVaoK4HwoXkC0wUPLjqKTCZNtYjG3dokg6CDGodPZbtUAwWmP%2BbIh0VDb04G%2FEdmZt9XvdLev6RglZgGDUDUjFW4ORgyc8wsufDV8vCRIuFsZxNFmilvEF9%2FlVBtJpNiVNkdDni3STXqIwb6zCzxcTO8s4BnKFYHtHMqMspK1pgOHGLPng4Iu%2BM7WXB7LnqtlRUZnrk56xjAMPCMz9IGOqUBkLA3aha8tNtFM3GJ1s5jCUaeAN%2FExTaKDUFsjGiUBNwDspQQguHbkH2m8oXHbWhuyzU%2FRno7WS3kw9AKxAkrT1wl0%2Bh3Qy21qLcknjlUsre5O3WSbzc%2FyVchNL1W1kjFQV6WCoAYC6kEIBp5yrzb1we0nCmysZNwm7UPd3Ifwugso4%2BQFIS2DU6GtvrgQJrrhptgPdoHwgs%2BKIp7thz7w6NLiJdK&X-Amz-Signature=0dad9e1325a260fdf932e1e9bc042abb11a7a9d303e96ddec6f2bfa803863d25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
