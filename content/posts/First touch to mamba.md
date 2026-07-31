---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBGATWCT%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T132736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBhfx1M01b%2FiIotYAjmPfCa4%2B9tCePnBonQfHWywG9a1AiEAgqxDHV7QXPw%2BXLf1NWfhIRTK%2F%2FyZuT7QHPvpjc%2B6CUwqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKbw8KNr3O2%2Bx5TFqSrcA8R8RYHM7a%2F4yNalFZXY9JlvIef9IQsweZvU%2BA8mjrdTn1N45%2BGkA1zZr0L1RsA0FIobH2rf%2BaIt93N8UJsCY5c054vqPj2xuJaVl7aUbocjRZbEPP6ZkhG1g6TcITW3w%2BpMKOX8DZyIFekmDEb7SPBwiKybdRsXXeBOOADnncvcC0wdIIGlkqt%2BHtRcCjNDFnFhzIGcIiutl6wgjZG01f%2FBDPv9%2BSrr4GFta%2BKZin1V8Q30j1%2FHi4tZz5peH4i6GqYIAivOhDtEV6EFS6MkySFW5N658mdmGu0eyruv9mWA9R%2FvmKwP0LBT67NWJHqPvOcAZotI4Koc1t6gJiX4zsubLC%2B046Bcb09HtSUTGinwdeRKNMjLlpyizeUD7CColWv7hYrTZpO8X0p%2BbY4j%2F51GS0A5RK%2FDU5jO4g16faAGhn7lTdprZcWKlkjr9VOLx8GLWXEXXWVD11MmYKYzUGXEyPEw3Ch1ssE4n3bT0I4XwWbqbQHEbRDgwxTT9JPeCVSFrRk1x9RWhyV1FRwidbTYIxllhQI3WxDnobs328SiJB72%2B3CwJw%2FmXfZm%2F0H1uZzCtZIaWnedCakPO6PDbHLCaLrKjbY9SkytKULYehUxU%2FvgEWtv61dmCRUcMPyjstMGOqUBozXSnRhKuS9pHU9WyupYhVOJynlin15cQVAlgqBTzmrAork3rQwKKtcrqWFcKdMY08o9AwPiUyKVgvHI3Gvx339bX2Tqr1gSQj4c1%2FFyJlsUoVV3v3DYlIG0G%2BOhG0Ahaxs9AbzpmDR6slqQG%2BId5xlZ08mCM1QuCx%2B50mmBLVYkD8O%2F4eEQwNQjOorJNngZ3yv4zQYi3nsfNjJdnromY5pVzoui&X-Amz-Signature=c5c4569d46215f2a682c7df4c2103e2b627bc4c7b225c3069022a3bfce31f098&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
