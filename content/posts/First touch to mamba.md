---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VPPDOTY%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T224442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLXdlc3QtMiJIMEYCIQDvgmuI4GOKRzPZDaS3WnMgZUkfwjTlM01nu5rK0w2t4AIhAIBLpjjbuzu39n5Set4NAS80dSWDTvb%2FFZIB3nIw66usKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxijn4YaKhtvFvKf4oq3ANrTObVaphk6%2F3FrLWN5qs3p7A687Ot0dznZ%2F%2FV5gGLWQnNCSzuECaIj8sXkFCDWopjSb9i%2FF0E0WmoolUZj0JQkOqzo71vyCFg2crSx4IBOwnClrwiFtdyQgIcFloYZPB80Zy%2FD5DEqa4Haaz5x4hIeheyc3PoxH%2Fc8hWx%2FYjh4thv3ZaUluE0VSFacmWPtqzOM4%2B5lkKiWX2Dh8106dHaqOA3CTKOrPIpNsnUWsC3BpQxTcfY8XNcmzyNwX5UFa1%2Bu1J6J494Ul%2BPjprcrJnmrpgQJuQvHJrtmP8Dx8a%2F7dMn0Km%2BwcS%2BjikrbkA8bOhdcxR%2B0LNRsk3apR%2BevJWggcD2JYyL2PolxfgJRxs0ZCra0Mn%2BNyEpou2sZwd9qKx1XdhHQEsfkWjar8e6t68R9mLSqxLsI8SQOBGM79jQxoTcT2jLb9DegeOF%2BR%2FOojgQa8EuGHgdKZK5CPhP8mKRK7DeXbHloHElb%2F9bYrrMYmqRyG0WB3SavIgC8Wb5Uyro%2FPqbM3Obo7ZyW2vVgHVCHMGD7TmMYWVaq8oc9ekVMCpDmEDO6qnz8rG79tvjnTKiTwk6RbZYtmwCYff0Ecntc1dO2299I0DW8Enxy%2FFxBp9mgZyOft7Z6vPvyDCMxPnPBjqkAZE5FVfG31jxv2jJfObagVdsYzQwLC5vYZMoiTXpvTRJrlCv8qGL6qYdT%2FUtSLe9%2BbDBVajltjNDsO6OeS3xhCWMRw2UaD0KPGJ%2B4mHDtwJxh9RG4Cu7Q4JpOEnMyDpFy3V%2Bu63L%2B%2Fwn34VvXQD4sgeSjNvos44vjGgb7umN%2FTj0hzgylUnv25YcJ3O4%2BPlu6xYbC4m4jM69i0Cvhm%2Bk0tTb2Tg9&X-Amz-Signature=7ab49a59b9ff1f258bb09f2a4e29ac6852a9b78f3cc1858c4de3a46868473784&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
