---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBUINGGQ%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T142305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD7HfKpaUnrJRfss7F2JYSQtBMzbaoZx%2Fcs%2BH%2BXQLPuDwIhAJGzP%2B78KP69Q%2FOMkO2zzeSLzbepTL50zjatA%2F0zD9S3Kv8DCHcQABoMNjM3NDIzMTgzODA1IgxDe5MKOxum58UPQjgq3APRSEQPmuz1lU5k1Sd0bG6p5pHEYEIHwQHu5eLnhh1XUGA3HZxf34oxKxyrdxakLPL6mTWBR3kL3LdyPfOUurrHNaXjKaj8r3fRURpp9655GVyI9vNB9YhaIBCD%2B0y2sJMX82bAYYDn%2BSak2xpNBH8y6R4AwJ2ho%2BDNAwVp2g2lsqRAfcSnUbxYbXLQ8PsOnaVNRL7sIOXLg%2BNU05q2E0rSZlXVDrQ%2FdFsBy5rG2OyHJNwOblHi4xs81hdMmwGDTypw3airuvhnbIgwp6LVRZATB4wlXuwquUQjuV56BpljgJzBxg3rBReQEz6jq%2FiA4pzP4qi0eUuneTgOptYmLG1LrRcGeSUhBl%2F62up2%2BjToUYnSAa0HngSb9ErSuy0td2%2FjGTtDVgcPxJzxQc7v8m%2BstnXPyC5NWlsRo9IX6b1t3nAyoLnzktxLlzxzgbK2PC%2B4mzSNaXchgM0ZUIg%2BBjUrejDxh94sp6utwU0NHkfC%2FLQbQKGGTPwsMP7JZizB%2BKSXA4VPqyN3tia2%2BYObokHd%2BcR72knF0Qo3oawq9eL0THY5ALqkJNDxdGnga5m55ZUUJfAsVg%2Fe3XdByZkoRYfilxCkHJgC01YI760d8cgRXGO5KSeRRICAxn8R5jCy3pbUBjqkASt2FwUgp2kladF%2B%2FFL%2BAMd%2B%2B8uHsCWpL1Giw0gSaRPjgXDUbry4a0GGIBUN0eprb36GVAS%2FLx4qMM0mNkDBln8pF2OF9ErFS6QnZ08vbE7%2FMckIvDZNhw6yMqpWV9R%2BWX6l3jB2Fgde99%2FlGiCfxV0hXxt1PB5DGyPXVtarxrJm%2Fnstv2m%2F1hZtVD%2FmV7Yf8MAKNUOY3gqvp%2By0PqpN1UIO0SwT&X-Amz-Signature=c64444f43552a0eee0996fcea938461881974585cb44cd9d67c9bbefef10c554&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
