---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZV7SNGA%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T155337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCICdu8qokZkuhd79p2L6KwGQoSIip%2BFP68RWzsojLhRN%2FAiAEegfgVLPu5OWpBSKkpQeTYI32%2BLHsDpcvxS8aIgTCmir%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMfeo6KLtYkyHIgXUOKtwDb%2FAWN00QeIszpaYX%2BadXMM0A6PYPfHwDn3JZaRH3HeaF43uDWR2t3K1LAJx5tglMa8JnHm1T4prb1nlvRvNRzsXveqFYWnJs%2FT%2FGkEk50Y%2FJBetZbp2je0Hup13Bjf0AnWOOq4oazwds8Cdk7HnpR76WmVZElFALmxCippS%2FIGlGoOBNvCDZJaM873x9Yc7a7XG4QaVXg2viqfDqXA3CvwwuWnMAKUTFMNisR2suP9U6R7b7dl%2Bo1QRLUH3MV26kE10rcX%2BOy%2Bhl0H0YCnf8HTh8P2mZ9a%2FwmtrhUsW5DQUQ6K0%2FjNSax%2B%2FPesJ6%2BXLI6Wdm1Wy4RefJdK6UQLc8xjz5KTiYuw5VHAqIOHvy8819%2FMG8MuaHj1JZ%2B%2FG%2Bs1jWHjP3%2Fq8bqTFr1trt%2BAbI52zT5ju1g%2BDWhZGDaCf8zbczovUq42pf7uC6viGomvxbjUz8%2F5mtrS8dAK%2FMP3fEAIUT%2Bg0EREIXlAsgJcmV66DjNGtS7wrlufECfpMd%2FHAWnQop9%2FEa3RSKz5alyGyAhWtg1t0llMVJNusyxKnf1OPqkh8J9cxZ%2B5b6vdce%2FladQKVeEnP3wg73fziHhd3OWzm9ffO%2FDxzECnayfdNjtNNkgPSX0EH5ltWDvskwt7HN0wY6pgE%2BMWskZ4%2BJs%2Bc6cOTw98s08Vh4THlp28htDPpFS7VhKWROPngtAm2vtOVwY%2F4jXoa0GjHCxYbx7qLS0u%2B4PLS%2BXH%2BDj3DVaO9MTDZgOZ73qkXCheLpIlFvz%2FzhYGQ4jJBoMbioTRmcbvzRPbR5hyZ5UdP0Pr5WRi95kObA%2BG4OYL8%2FRWkdVjCDSpNGLMWCUd9ZNumsz6CHwlrppgKf18DQbAGxf5Ef&X-Amz-Signature=5e647cbc6086703a8c6d63de25f25f5542beb417835900fa1d264ca60ca00ee0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
