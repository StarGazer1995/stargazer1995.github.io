---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665W2UEXU3%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T201020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIEKGXaB0Pt3BcNANUt2qosTzUFVqwh81LsPrXEasyMKwAiEA8GhZryxB4kFT6J87NAVdZJrf78JxsyZqiF2bxlN96BAq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDFKjBgR488Tp3HpVJircA60sKOQvs3y6LclDG9%2BdcbJYhUoObNByYzidHNsJG7J%2FUnMOPIrDgUn15Pbm3EFtaQQQRPzu187p7x4KvgHxEzLhoA3pJTwl5P6mObYRxxnve8OIr3hXSAVVavPsqKy%2BFYQZUqX43pWL8nkteGnX0LZNHGxUPhXFvA5hNjRZjJ6cJqtIxlLsb0inzCV7ACWfNOH8tNfipSPYRm71rQ40PW6ifND2o4lcR5gKUW4ymJ9YEt4jpYV4O9SaeoWmyBnX3CUbGlqUph8ICBJjVL3k6IHAYQNjfjxdwQzRGaJUrFNCctZzMIXKUzfFtg0DDTA1Zrlej1kWFu1zPLMC9fykD%2F%2F%2FTI%2FyNJAeq%2Bz6k73g3N%2BXwmlK6L0ylzKbTc%2FJXtJWWvDqW9vj22LVyVKjJ3igcjNNeKmKm6Be10ct0z23Ng1iQh73KivC3tpqm3UFy3r5comj2NeI8IvkZzM7qpCTj80IFfU2jlObLXCUejCpY%2BAgyDSXlmjOMBy1NMvd%2FLs5JW3Ju6KDP6LpEpsc6hNMR1fRj6H8FgFeooEvV%2BGnoKCyzfHZfbPQPAfvPK%2B2UTLg5Ksh4upDxXzmCSKw84iRte%2FDSPLCofs1VVvd%2BxoOMhG%2B%2F%2Fcn4chhm2cIog3hMNGx99AGOqUBe%2BQgcMlJbe5mcotDl0mg3TMIEkIum8PHK5VxQu5RNQTuhiYVICert9DXiL05z6HJ%2FGcjVuwG8Q5yWovKAU5LV3hLoJv1gdI1FXWIXKC47JGNT0DqvBJ39n%2FS%2Be7wddTxbhk4EGyzIV5YC6ifnhR9msuyTKepEJnEf2IkZrvVihQitV5rZBzQSjUynJfxIU%2BH%2BPPnbcd181IsvXSuUZqjBtlUgMKY&X-Amz-Signature=2725eb9a47d2926e4de9755145f48dd7fe018db494c9cfcb5b607152697911f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
