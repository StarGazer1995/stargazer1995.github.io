---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJOD6XYQ%2F20260828%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260828T015147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQD49Mk%2BHqPSMTDNu%2Blp2iY%2BoI1YjB51bNRHA90d1EGjsQIgDOhTIeYF488hBPz0o71ugBUHGN%2FQykPqE55%2Bu4frha8q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDFEPo14wmMQyuSrXsCrcA7asNWUFp7zl3kBsGQo1MPHKJ%2BwjlemxbG8oZUkDdi88ikP1irw48%2FDTLj7eOEVpAt8kq%2FnpMq8yhyES%2F1SZOad9PlTnbAkvNdXdJKHTvTrtALX%2FFNDjNZESiyKfU7UbaZTywb07TcNf2R%2B7tFR3KnQfA0xSb59et7Mtby7VE8XRHt80NC05rYA1cWreyrQakyckEF8stNTiaJDzP29jhlNTLi604YIyaeyxOgbsEz6t0xyrs9P0swYkkLSi283akNhY6c2qHGVD5cifprlDCqqcsFsa23F6MvfT3KXDQSmTdz6rl42FMnnxPj0TJX6DjF%2FA00rZaA6s%2FDYAYlohsVddcUKMQEMSh%2Fq00KQ8WkE8m9L8Vz6xFq4jgkW5AWHReK1T%2BDVN5nLWbeSg6P%2FrGU1oMhCyTbmL6NQ5lHIYy6m0ykVCjfSIIr30bLDjDj9m7NwmAY3x%2FRKWSml8ILNsS4zTv9k%2FHEIUyitBtugzr6NPMW8mzWabDJJMuLhTK%2BkUUsd5YrSWW%2FzfrTR1W8Viznmmj15rEuZnLP9yYCh%2BTfQTgWDIlwWNEmOeQeQk8QJ6NeRH9%2FLoqxcaw2%2B6vfGF3odg7dV3%2Bk4iq7gmWdqG9c9kwzgbuD%2BElNirTxBLMMLYwtQGOqUBJJXSkCsM24Z5bCxECdcM%2FBfqjvON1AXhTA%2BhSRwEoeLTnc%2B14d%2Bbs1XLnpY0wHL95Prjyy3rUg8p7stJ1T0z5kX1E%2BmI5DGDZETOvE6HlCF891T0Un4Ef5Poz5TDPTdTRdTihU%2BWmrtKNCghfwHiQwin14SgG8qEJFhXH6kNdexNt9XmBNMHXWIlhO4TyhwmYfLPososn4ihXRsqqu%2B07FAN4Lcp&X-Amz-Signature=ca9aafb4c40d330f5b116eae4c74b403617b277f5e8a2f21d14ed550de37e166&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
