---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DB5ILHP%2F20260526%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260526T060206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEAh%2BsSiRQs1ushYrZd%2FbOQbmojzbN6tMMfmDtfVypszAiAX6MVOI9wNbGNW7VIU45iEIPNMiI6iRxahq2KUhJJ85Sr%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMPefF8Ab2PT21neoYKtwDtpezy9u6AQWihgqVXA6slyglGi3mzNBgB2tU3jFXYtJid8EfA56FgXfNjV9gy65yevGjwvJ%2BrYPS67NCnSrqhRjRe5Xctm%2BSqMtao3dQd3AMm2cn18%2Fq%2FErk%2FYEDisEcO2Iyctj2xY%2FiSYGfgQvzfzrz9Kb%2FL5DWqT0CdCqwsTLcwxfNvRETJPcnOB%2F6bOVf1m%2B06ENtz2snKahcrvoBsrqDEa3ld%2BmP58HQaIeQSzoe2eEhhdZZvvcrDXfzTXNXdsjzrT8H0cGUQ%2Fccb70TWQGW%2BbF%2B%2FRk5iopem6iheGHDmawC%2FpEp5Z5GEP0vwzXM3%2FiydD6zKTx5TD3xJe7r3rkQ6Nt3NXAStL4SzqyDXLjJXooYPSkqJwZDdIS5G759kNrPQJbFyW1P8q9qwPFRp4FI9PobPUOf5OffUuwZvvySIG7fOlpLq%2FO%2BNn%2BsgVLhziLGg3SNfwp%2BFM7o%2FyD2I8yqaJy%2Ftk3i0pb07xzCvStuQXLpE3P0v%2BEl3%2BWnNTdYAy24OKq8N0vIWdSb78jqoek35bqNVqm6%2BgDtwqK825724xtDoDbQlMd6f52IzYvLlojsG6WwDy%2FcPSs3kDQbG3zYiV6imVOrCMosAkMzupBLHfmQjmCh6avQF70wu%2FjT0AY6pgE8q2SMZW1zFtdtRbn7AI31ghc5RmYDYbzRlbjWdkgDA4iNHy%2BGopLVPN4ALyWQz%2B4WkIgYYP%2BEFNc9mM72TjY2Awg2UR6QnijskubLIDNmsJRxW2s%2BsrL3AbZgyQFw%2F0RPHGLX8zwWT3n%2FKsPs2lyqGScKdTJ4crYNbF2oTrSrFTm6kxNjZpvKfr1kzJm40Pp%2Fl2m6hvgk82Mi%2BxpE14AbH29JVYLs&X-Amz-Signature=7df302e0be47494bfc825ab1d28bf6c9dec69da11ad6513126cb143a7690a1ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
