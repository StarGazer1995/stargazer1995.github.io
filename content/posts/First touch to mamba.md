---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6FAYKR5%2F20261010%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261010T140356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDU8dwpGZ7QoEFpbrwnfYlaqGxG8KWDzi6eWg%2B8MkEJAQIgVPTPkcdsGAp9QwFtMrGD5ufpCvSG8%2BURg8MqlUYHSREq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDIsjNJOoJDEQDsRwcCrcA1eWJBUT6LeujCV2ucAbCX9cbquxidaCoIGAsdO9NhKJ3M9DrZwJskHChN4ECEEofPuiD%2BUJldgXBNQst9Wm8floFKWwClPgeis4j%2FktCYsC13EIqxPkWBkU%2BSgX7dajiby1s5CnzdMpLhJj9XCxn%2F8nWP9GAPJADWkTAhKTpUUT9FJpUuq1gEMLPK3JLsF4%2FhgXJIIM%2BTEKHZ1iYfa5QnEv464c7KcKpmna3hl6B1VnE4Mm4VRUJ5Qr1DhLbGeGM5U8c8J%2BSO90jNig6OENEUWzWMp6ptUMwhdh%2FU6q3lOLh9Iv9HeCpMjf3%2B%2FvMssRLKR5hNhLOx7NKRWztFNMmqVE7nyr%2BGm1i2mCiS90nsdAK25k4EGrjCh8CDa%2Fqiw2MLXxm84IB%2FutO2WEPUbZgoivUKlgUo%2BopnrYZNjd3F8yVuu0tNNuc8bAdDgBpl%2Fk41R1OS0d%2F3OLbEKWkJX0isekGC1W8eXUyejwqbZJRKC6AM5YxSiE7n47xXLsztnn3ruSJ4glPZqIXMPQJLPePgQinaNhQLjasD1bW7Te90SbsUOPF3JrFheeEwFuBkRRvp56HRAyY4N%2FhRfdXR2HFCIcG6sm2ldvLpEGQj243nOpRqX24P53CjqgYeXWMKmFqdYGOqUBUMpRyGQZ6WGUR2XDROXVm5OnP0L24%2B2TFDPQ8VKiTiFjegiPg%2ByrEc1QVNHNWbr%2FmtQ%2BEGClpYESPJhuzzbu7AnkPQigwrROCLh1qSQmCPrjW4v8%2FwWlZiOz%2BbvUETMFrzPZXmcTqPTsgBnUoDUnyQC1aUXk4zlqxDhqgJcW5AEles6cnlv483dn%2BYH3j5YAF8nza9qlYT1BhWJBVbWjCGXswHL6&X-Amz-Signature=627092a556940fcc0cc6645da324958966a734d6eead8a18602e6925e555487c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
