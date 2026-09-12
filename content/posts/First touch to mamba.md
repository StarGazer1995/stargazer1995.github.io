---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IIFXZLN%2F20260912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260912T015236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGn9QpJSjIbB4c82q3X8luwNwdzOW7dZ0ajMeYzMCqPWAiEApngHMKgQ71ER3GZyfuFUTwGjVIGYs60osQMPoPotIiYqiAQIqf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIJ2q8fc91lNySzYIyrcA1LbxpECk6nc8opeTaLMfH35QkDwfjw91qero%2FVrMi6ROwrmuFXAZpMf1yXzx5dG9%2Fto7Yd0HBNwIE%2B57J%2B748nZiFPE99A%2Fl%2F8iGeJAh0SXiOr45VElHsj%2FwdY%2F%2F4vd%2BMU0ZiRk0OCKA%2Fl3OkVuxa8BrRzjcTcrYKbMYehcUC51Jk%2BjVDpF22LqCA7o0HVLsoaG7aUv3hl1cyKn9oVseunYM4Ia9tBKWuFEYNSA%2B4ZLjcF9X9f2%2BFeXZ6uP7E%2BxnAGOj%2B95MuGfq%2FA%2B59LFBzD3%2Fg384l8opTpLtl8ZXO%2BgN5bKL0%2BHnII3BaHj58EUEEpRjQeEMzNZ7aL3NZ9jejevIDzl%2BANagywkno79Fs7e8l6tWNBVdo18G5Qd%2B8AtUEKgMDO6iqwydsfn5H5GR8ImIXoTgplIq%2BALi4B4NvTZKFptEna9RLNljjmZwID4%2Ff4S%2BjlWn8oRq%2FsKuftH6h4mXbdmayDN6IDRqb763hKDOpUPJuJ2RrlmHRVWw5taz0p3VUPvUvj4YKMsY0NZGcHeUJBSq9H1GxjIZERGzjs3%2BMb7NYUOuuOWRnjnLHw9N0dDqYP1Vzg7app3%2FxHJQouLQ01fqiSubQu2d85wO%2FSVwMiFutmk7BUF1k63MJWtktUGOqUB%2F%2Bg9NKiNFCEP%2BiQwoq5eAQVHOr4GohxO53yQSwkaV0ChNzxOUgoXr0YyEZ%2BHKNm2Via1rpUZ3Nwq853pQlff7SiFF82yfC14IoVjSD58jBfHMLdxSzrruOQ8qXVBzP4XNUgoVcsY1nxxZR3am%2B4drhLF4iGxsH%2Bef0oFz0d209o8YuoW4ve1PKvSdSeBrd6zx2ly55IGROuAJF2T2GryJChLuK51&X-Amz-Signature=81b83fa05a4a94fffc83cb34117f5753d325d713bdab9e2f97e916834b6848df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
