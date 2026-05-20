---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFPT3TMM%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T230445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIDtNFBy1F7SzErzLJ7vtLgd5XKPg1PYuXqLN0%2BvQaBf7AiEAlu7Dbsccdf1%2Bkz8gur2ePYaSRbXObv5rgOytaRKozNwqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPXI6aQ%2BTtxNCltQuCrcAwzir%2B9WNEJvhbM2LBLhDRxBNhNIaA260mE1xOWiJQo5OflYKbj0CcwkU51Qqy0%2BqMstSswi%2F9gIyw%2FE%2F2UbWpblSoA1KZwg9GAFP24LiOoODTAEwqaJZRCeP%2FFWNwNUZcCtaaN3OWG26C6FvycLBsGeFxywrqjFEN2JI4MB9Hx5LWuRCoxfhHn%2BbnosAF464PMqPeAr2jE8rsGXLylmO4II0t8qyo5Cr8C87SKx4RrHgJ2CPREP1ApzCsjl0vzYIvcxFg9sck7Q8DeaMIUzA9zBfcmvlnwpfmsN%2Bcd6sFruEnfMURYoE%2F3ET6Y5u5JCtTBqf%2BNNCZGJ9HTDYyqyprS5nmIuwOJ5uIOEItEajbAkZx%2BlBAUSrZ9LDC38OZzOpwyWoFMZogbHLO0gWqi7X3HF%2FV8MUwbXOzCEgkPaaNs%2FhxqvqkO4l%2BZsmsaRFtPMqBo0fAyHVzCgss%2F5SrUHyaUjyDWFNf254VcAK8I1xXLPyNUez3NnX4hdzx8HUTLWRotLf1HYTXV%2BTaNO0mfvRYBCN%2B8mXtga03XUDM6x7hEClXwW0xeRHLZfG2XSEbsWjiiAKrZsItEEOBgMydjcI5M9BzEx2EHYtZAJd0RswIErnTWMISvNKVln1rPKMMf3uNAGOqUBJAw1CGONUJCiFYNJqKS82r2vZqYhvrIflgMU7OxlrSTt%2Fsy8KFUAFnW8fAvsDIfR1PG9%2B0BQEmtFs10%2BxzDuCLSl7hk9NZZDWDZyWloWGRX3nEbzycO3JwABzFVsSwnG6MJgZRN%2FM1HIwcBkA%2FAUX8gM8c3Fj%2FJO6gl7MWdarBNczNTNM2hjPuB4eZ3l8WeIgkZkbSmfzSgjvmoVOgl8ftjFNMfX&X-Amz-Signature=d06b574f443d495370d8be565553421c61b6903a3b52a1103b87fd63db7ead9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
