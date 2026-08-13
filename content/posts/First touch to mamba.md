---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ARSJUY3%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T035818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIEXElmviaNn1FsSQpYkIvSnIvXnPrWFVFhwJGuJrh9hGAiEAgElsmKfUOkOskJNwS6VteWFfu6JcRcTdGNLZ7t%2F%2FTQoqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEMIbucnIqZfGEbb1ircAy9nvbedZInh6sObTtKTZwICC%2FunaAjUhVSamX6e2uBYzMyB9ZatSR0qT1q85D2pQ10LQ07AIKIpyjgVB3b%2FjHo21CEqub5YKrcUW9h4K%2Frnll5uXj0skFtWseHsddvNcAfW3KscEhjSzSiCbL1HLOsK1h4%2F3gJc6WLd97ne8EkWLcSojmCL46O8O1va9taVAUUT98WqErO6vT29HJbCN63tMQ55OtGo3OmYH0uGpDawNVUWFpQrIGw3AMxFtVi7yApMzpiAi0a2QqWLRrhNvne%2BEhbvLh1m1%2Bd%2Bymf8vzvuvZEEkDMfTlTsjaQQhSu9VKvsiCTF%2F9ag7w2RtiVDxePkcEn8WO%2BPdcDj3W1RgwU6dZYW32qXOiYSvRIcJK%2BS3R%2FPNwDv47HcSAx17Mx3DYXZNGX2UeTGsF6Ce7aoUJ7Bix%2BXt%2FiHNET9%2F5N92K58N%2FB0OKpK3UCCEU%2BWr1ePEHsWz5n2uUcSYM6AzPPCIppcExNfjwzItnY5KH8p%2BrB%2BXANvui3xT2LnHP0bzwVoRdsMTEgUFxqq%2B4KCwKmlOmoqg%2FFMI9PmULk%2FY5cOkAmUBEg9ronXq0Cz0XUzlR3BD2xEuIszbX8%2BpQcpU59tjGHMYGWDvyVv4lnQUkVGMJ3E9NMGOqUBe171J%2FXLb2144XZY353CHQLXeKDpWgHwqWrDDCcNt7FAb4%2FEhgTvm148v5kX4Mma9qH6CwM2H8SoKFgM%2BmMRl6ZJgOgD5ckgsbxPD74dt0CJ4grhRNDTIDKD%2ByzIZlOA%2B%2BBLkuN%2FUtJRUvZf9RYVyfDzd1fi5mE81WMMxwFDfxpt%2F7Tml%2FnDR5Jkyi067bCjVNT9LsxNFZoYgXYndkxF5jHUxdAO&X-Amz-Signature=3d62ed3b819867f54ac1b76af59cc72db29051673cf2a18c449d5765c8762104&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
