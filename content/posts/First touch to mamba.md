---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNBE3OKG%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T063652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFCOg53lcWH3LhZKA7pFbMvDvURhQcZxRV2bTDQdMVbdAiEAi%2FekY5a%2F%2Byb9Sxaohj1sDjugc5iOkNf9eZoFaxy%2F6o8q%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDP6gi3b7U6g1Vu%2F4lCrcAykUTzmx1IrH%2FEHVWJIiAWWrhcFBU3ZqLM2TOUj%2Fge5kcan4RVIcp32nNIxHMrSklCDVztVicq26oqZNmSpQqgTOWO4E6LjHfAHBktTbF8%2B8q2%2FSESnFOPA7Z3ln93MQq%2FAkKZPsn1gCTzoaovWGGrqrk19T0juieKaemeZ6o4VxvZW0cuQxQwYTXhkNu3mmIGaloUvuxpOsetzcASzWUVqcMrYACcot4zLLVfwgJFptkjwrBRR4k637WEtgA4o2IyH9GouR%2FA5g5%2FW0%2BZJekToFF1ikJzqUk7lxckbOLPMt9dK9RZk30WFfVbgnKfZ5uOttVSDv5wrKKdm7%2Fs1w3gAhXD5p5LjtAnO6PkA242cq4ctvRVrvX5P6%2BWoWc5QPEMXvVq66NLN6CBCAsO3TRfHtwnPtG3LizAPqmimAvVJcV21UbpU78CaEkhYe53SFzT76j8hn4T3qm7jN2wZkr4scTg7ZAoS0AP1A7cotTno7LkwaxvEMXCHJ39tOckSDNEkoCXdE%2FR8nJfRp0B3glX1WjiiP%2FSGyZ5phR2PSkdRAPI38%2B%2BCWsT8jO6jwZL%2B4XR2BhiTwXLzSEvl%2F8heC2CQzBEllcW5KLwSYpzlDnBhmo1dFf1TPJEDfbZdSMKzttsAGOqUB4OUUWNC5yI9ckWdZO5iYUT86I8QNXiphCTpbGHMowc%2BYIUKa848dUkFzFQ4Fegx0d5zl1cPzsdQOEZRy%2BVpbwRrwY5OWTZZjxgv%2F6YJws7pnGCkNa1DDACY3HyCnCqixQ51NsGX%2Fje1d%2FDB8izOFlp6b2QZb3KCD2z27YVjr%2FHc3unjp4IlWqmxMz0Cs3%2BqvdiYBZPbrx0nu6F3TU0MPbLmRyGnF&X-Amz-Signature=962499a927056edf25a6c1e23cf76e8c0d7db69c43fb43b2f861658f2fd40e4d&X-Amz-SignedHeaders=host&x-id=GetObject)

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
