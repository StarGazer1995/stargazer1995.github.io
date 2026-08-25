---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FWI7UVE%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T082816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIC%2BgipIAGsd%2FNAG1faD1%2BG6yPkHFSsO7tBSSpw32yr7iAiEA21frWl%2Bxr%2F8hzIeIR4pQLM2TMj3v4ubwC88OmRezyTIq%2FwMIARAAGgw2Mzc0MjMxODM4MDUiDFXWTEvZgLIEHZwJ9ircA0jH7Ecpk%2BiB2%2FBGu3%2Fxqvbf0V2qne2NxFcKIEvPI8rAyLslTbxtic0jPDus0i09UEp%2F6dP95RHicnYaJWSj0qcGR%2F0W21JLugIy2L3oi%2BXZ8dI9h1ehhWOTlMifZ%2FNApy3tzRqgaU%2BeiCHddt1%2FERreZulxYel%2Fxbg%2FwHRAAy%2Fe9vQVAoI%2FLu%2Bp3idTGrzPNsKQoaIwJj9bg%2BVVSE0Bl4bLOaNqm2FUWJ4gKK%2FZrzeihvs087VSR6%2BIBC5l0Yr1P%2F76O0SNDnHfPa0bc1gnkx1kq47jjnXCwiUHk%2FREudLPu4%2FU2tUFVxncMbTEIIHoy6Ul3HH2FHr8dKC9khSQc9WFm6dweXZTNkHCw9SFfdx0k0GUyMwfikJ6TLIMqiHjM4qf9qzxvXEKqnbIMfe8R93D1%2BDDNLj5YHBBpTzh%2BEy0t47QmFkHJsDKAX1HkZBIkPA1RLDDLFjIQOa9vRpEa8Ivfvikpfa3vuCsSwyxKZIEhclhsuNUtQUgfENZVCvDMRF%2B%2FaHkKQTtKw08WOczcRmt2ssWnq1%2FV3sUw5KfzQbPUhNwIoRI4YZctDzGP1lmXK30eoybn5LUdpEpKykrPv4mA2paoHRbaasNIJu71TAW%2BA9er6wymSI9gsQVMOidtdQGOqUBaO6dFw7G1HrCMHuZNy%2BgQFGGASSixxFB1rm%2Fz8%2B9WvMtOhxEKEoke5iINQK%2FwQ5IC8Fp6zGot8MtxGcbNAQDvxviqKVaHgTuSgRBKUowyP5m0BHJ7jyCY15zi1LRL2%2F6NWzR%2FRBk%2Bj%2BXN7U8T%2Fn2ogao9wnV1Ga0jWbFzOzdpw2M5zB0OfBhXKTkddmNevOf%2BOfNEfwDMyAgM7Qs3%2F4k1hjvDg8M&X-Amz-Signature=048e51c03239e1bcc992fd35795f154db2c09ca624b7c24ea34c4e5252db0b1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
