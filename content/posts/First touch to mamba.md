---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDOKQLJF%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T191139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDwP7FUgxbz5srygLktDx5lF4A6Poh4D1TlT7JhV7PW3QIhANPJOyVyIynH%2BK%2FxclLi2j9mPYj%2Bvfs1wEkPFZA3PaByKogECPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxaTwEYiwUOmv4D2Ggq3APfoxITmwULDqqSvP3DngTvRk94fsDgtZsrlk1L9mxGaE53KHBVwbTmH0H7EGelxL9WpM0g7%2BzicHtnReKlZsETv34vTLRsbwRgv%2FoEso1LQf1MQ%2B%2FFFNQSQaEghD0jb4RqQdpc%2B5lbRB3IcdtR8c3pe7Uu7F8yRgEB17oZYzX8ayoFHxp2MirwlGqSQq2Acyw53FcMCMYTvl9crqST4BSeiSdw%2FanKtdnUYj0cr5%2BxQXB%2B%2BqbDlvy0%2FVLxg5%2FObIGxxJwAa3iGHb2jPyBqdy0oZCTVmbQ%2BSrIjy09zBbwbA2kYUOqJsRG%2Fqc1FD1cvYRF8OTz0n2wPm4V6WkCIN5IZ0CQN9z12VceiOhDNaB5KRQPwiZHoQuZexICSZx7LA3xWHB7DmaRlcfZnuLnV8KgxQMPGHDCo%2BFiEJ0bWB%2FKVLPzhsXLztjut8W1x%2FUjS5aFzXSNePHSj30tj7jbdv4aigAIlAqfqbi8DL%2FfS0h2xdtXUDlzMw%2FeRYzuPY4ZELFGOIkMa%2BjAB3p4cZ%2FDdlxbHLKLYPXkrMoSBg54SmXoHertTFwqD%2Bn97Lcw%2FTgq%2Bo%2BxdPJ8rH54upzIjELPul4Bl1hbwLBsHQS3%2FXnOndNpkHBvy7Lsrv4AQja2nqzCSpeDRBjqkASdIVrOanpYIazk8qg1u%2FZeqMSCXOpwZ7ErVrX4bcOqtXEzREEhyjL57e0pudEV4jFbHleoudtDAMCViIRa6nW7GVJfa253avMyZgQShL3oed8ALKATHpf%2FEYsZCL707rw9ZTpTsBm959n%2FrjOVjE%2F9c3Po7qXwsd0xF4CNDdtqf35LMuwQgSDFu9HRqWuaMXpyM3iQlRsvxcuWTgNR1wl22Ampe&X-Amz-Signature=8900547080be0cc2a7487f53c1d083e101bace22c5a9907d3649e859bbeb0707&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
