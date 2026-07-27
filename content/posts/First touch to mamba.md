---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFOCNDCB%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T160707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCStLucUXRNGBej%2BWCO6OrC3hNKm38jU4Z1tRuZHeBUCgIgQcvUQZQfszigRBTJpeXs1TqRcLMi8CQwUdU9ZOckk60q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDGduBxXqK%2F%2BUS8R1vCrcA4XbQUDOEDZ4ApGDIAtNLLyKGW7O%2FSYV9Q7ZzBJB00Z28ZQZeuiFwX8pU9lE6eeULp6qse116k8wj3cMnv97Kamsw7kKyjxayRNajyY8H3u06oQuQvm0RaZpYqFEYsSuva5rI26gY0O92ZEQvDHJo4dXxxWvUrkcmdz94TZob2Pd%2FDACVPdNIHX%2F7ndiBmHSk%2FsS46yV57Itp01m%2FGJy%2BaUiQPgCz0VO2sGvXFt50SJHQaRmEMN0%2FDTYpv1FcOg0dH4Vwz3USBAc4ARIDT2f3W1p7n5mIOo1oXIo9akC7BpeNDuKlXOxxBeEWFOltbo2Hujolmt0KKtWqH%2BdkzE61Px%2FMLeVBTOfM2H53W3tY673UJCmVqS99kfrgVTUiM2T1kNYpHgIUZcooXwx7FYv%2Bi7egNjXsTgv5qj%2FObwQHOkkhIyFGsholMV4%2Fe6Bed9jqke%2FlZ5bmjdqxraszMdZcdXdp3YrXoKWQJnwEIbOdZ1ksmh4unay0iGjFnvarLcLj0jXIq2EHz1S2ZM8u0l%2F%2Bzs%2B%2F4zYZoNvbsVQzMSzTSzlJBkIBW6lBytJpviyC59f8Wv0%2Fi5069VwK%2FSdo6Pdd8xwjiRfz1kJHpohvpVHYYDdB5bTjUrPKsHs%2FcAFMKmCntMGOqUBzQT%2Fq1f2EdmeHfaSkvLhjFQ853iEiekgZ9X1Kl9vx5epsNpdRq7r0Jts7fuCslxONACPOknQkHVCN18mAP7T6FdKOmZFXDq6JROvwszuWA6zZ3ACjUaYwTxmxdtthwmbgS8cF%2B7GSYtLVb2KWWwLWMh90g1THAXHyZ1A7z5%2Fah8Yg02%2B%2FYW9hHvAlGrGANQkm%2FoPsUGZ7pdAcTLu5wxSk4Kqv1iG&X-Amz-Signature=cb52f15dc0bbd6e1eaa3287ed24d365a35750a6d276a1542c71942bace1172c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
