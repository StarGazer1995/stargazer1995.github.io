---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7HARK63%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T105328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIC004jCrST5KfdQyoOForLStHJb8DIPvz8wAYJK%2Fr0%2B6AiBLFvgpkaPISNy38iI%2FGFoj70M1VGkRIcwbHwpzt7aCOCqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnS04nfjSwc42ha5LKtwD1bxb6LXaSRWrVFSKNO5QpAz%2F7GiJ6uCBrecvS2oUo%2Fz3I7FLD5PABnSjoudwsJZNH0nHkDHP%2BitIavzG1Hk%2BRylm3lTvBJQ8KZl3WFsYngaGi%2B0GBhdQgXZVwDtIhXMkFzmw3aCujmmFInlkJHR5rw8BBAmhvl9yy7Qzb3575lB41lmG3rm5onE7bJfaz%2FpLUAQfSiePMGbl95mkVczCH4KDaEv9ENAmpW00%2FbmY41Hibb5PzaREX%2Bvd79jJhelvI2hstRxr1k%2FbqAN4b2ESJWvSwYTV1mU0%2B1B%2BOj62P%2BHtoVjA4ng294hSOZO4KNPpIzhEpppSRQXj1LACMfi5PdUHvLlCRRUsYIF4NAaAMgC8hUsIl9KOHHXXm6eCk%2B4yIukLPhTmS0Q%2BWKnLIGltjtEC93TefcMo7KlZ85DACTvcFlxnMCogVOKPCPM%2BeYn5kwwD6nRzAElT5r4JqOPfjMBjDXjnlzYziI1%2BZbyryGf6LyAVVuL2vEqzJxMXv7ECj9A%2FsbkYbOzL9181QZzlsb7Q2SgblzwjCSUnD39wzR%2F%2FmdWV4Qi04vjPd6VA7MVLo5He5G6cmGHv11fIya4LF3E%2FjPjIb7MzgfhcZEBqN7q16U0sFBYDSc8B6Pww2eqw0AY6pgETdgMyiZINo9uMBswge3gZJ9hf%2FC05oCN%2By44EgGaf1UNOG%2FBLV6h%2BkbRvPqGnO%2BFM%2FcAMQgk8nX1pZNIWvVbsIm37XdYxPfJjbN8nWWsgFDFdNAz2AH8m%2Bs2TYeaFYdmZnhOaT1EuqPboB80DCKwF%2FSig4cqFDAEfdDZgrLPshXspTFng80LDS6Ft6YhrJZhpsW7HMZNsnS619A5KMXQwPcw%2BZH9d&X-Amz-Signature=7a2754813a81d28b741d9f8ae70d6c9b888b1861bd27fed148dde83ffd4d70ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
