---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KYXRUMR%2F20260505%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260505T235253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGF6UcxFuQ37QAFCc0A5z%2BXj%2FckG5O58M13%2F8ub8W49DAiEA91dia4Ucsf96d5oIZBYkWCRd8Z7MoPy9CU7pihju%2BwoqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNEa4MBaqjdtTdj6kircAxWZtZ7OgSa2HBLF9ARhhbE5WYwQIAfKqNr%2FrFshZ1m8CjdqRjhmlQTJ%2B2kML2KQeOKZ0yf3riAnKxRu1bHMbz17WjNRZwaCmk5NQYwjSnsmUCf9y8nEWnjxgsOZyXszukwMNF2KZeLOplc51T7fxBnKaFnJfDDs6V4B2UnVud1BfgcTHaDvYLD1QGHcNtar%2BlRD%2FVBQOzNKuL%2BNh%2FPBKMwOc4UiJfj5SjyTrM3hrhMgkOb4UAsh7DvKrDq%2BYA2H1Fm5jOA7daJ4ExaIE4WD0NLbCsfYpYk8zL%2FULjXfCv6IRnQ43B%2Be8q3PqwNOkLmW3g1WbuIwoRAWBBIcpJm4%2FpVIEcLKvIZbjUadmYHSXeqczdD5QRSYsjyLjRjMt4%2FxKpkWGPdlXgcQ5dnvxDB80QirJuVJy7RhfPLHbxJhTFTMlxC3eY7mVBgxir%2BCsqm1l2h8qnkvDGvQSTvZZWjtEBt0izMspc116b4SswfGimnXqqsVJCX8iqYTjuwxYQfsvDDgomNFq4sn0OrXHyehjOqUoDhuYvnt%2Bs2x%2B8AX920RiRkgQb02HgaTdSDy%2BmX7nQPinebcjKOLmA08JTE7PQgPyRuK9p3XmeYs62%2B%2FUnIoI3zgdI%2FTJfxi8PJLMKfz6M8GOqUBWAzlYlXz7LR5HA4ziHbgTHThojljrDhH%2F6kc6EKkmL3itAXrpwwc27yd5g15tg1xcy3DUWmgCLv5ONLYvTxwB%2Bc0oDWtMbsepNisDnHJPdX2YNWNjyNLmp70xXVpSBN30Eo5gFfRO2cDWBQ3C6biJWdloxCMkCCBuyDOsgnaxwIaJe%2B%2BJ%2BG1qJC4YVzx9%2FeT1nO%2BsOXZIv3VLkRf3%2FN0OhdrO8p%2B&X-Amz-Signature=6814aeba47c3b7f8fe3f56f7d3d9df60b314513bdcf4ecdd6e99ac28344fdca7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
