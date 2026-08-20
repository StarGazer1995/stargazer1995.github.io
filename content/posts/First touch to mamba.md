---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVSQZO7X%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T122233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDadVEC0yQJDG5ebAt1I5C44uMVO3NKof%2BiZqtr%2BRgE7QIgYisEAamlvTA6XORbA%2Fw6nkmw9wqentjKHAPys3D2InUqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAFCoU%2FsIJUaNQ9pBCrcAyA%2FMQawccNHmETwhHVzqS76W9EVripa6cqtMyVZpjeE%2B2dlH7BcSw3dpeT1N7Slj076t3KJf773aiSpsCwo%2BuRs3YIVNVO6XkBzmfAw%2BCwwvb59SQ3emLit6O%2BXfSGBYGu%2F%2B1YhtoCxwRBd5LJOMAcQu8jP2MPcOltEhiYR6zR3mpewhRy74qeFNaroOFYbyvZ8T1KC9TEaWBLtVc4yMf6S%2FcE9HbZIL%2F3l4XDF%2BvAOP%2BkH9WecMJhAlO40Z1IOhSG27IjVA5JLR%2FSaGRkA1iLWv5vvoAl7vBUeUZE1IYx815LfLKsOE2qpsOhENP7XTAWGpoI5lvT%2FISQX7s6%2F1SAhS2%2B9yxNp7OZknYQjffWds35Ul6GWKaoyQAE4uZObajPkR14h7tccqad9aKKZXrAwZM86jFdrK%2FpOSh%2F9CIVFPpJF0IsbHPnu%2F2RO2zYXjPYA8dCBaS56im9c4lRwP%2FHDRNSpQKPn5PFd%2BX6BF4J%2BET%2FYm32sX9%2FX5sZnjdEYWnWX6tF6kGOQ1uL92SpHSZv3iEFsqG0NkyYiyb%2Fdkhsa8VidYFcCgXVWQXcvXMhaFg%2FCW4onssZXz8uDT5p7BAlLV7ap17OxaGVC1%2BwaGQeHGOOxo7ZmxeVo4sGOMISwm9QGOqUB3an4T9oo6Dqci72J71SSN9XBBUMN%2BNKMJ5XIkqohY2JRDrXGE6HYpCy6obo6XMvSW1Dvsq0X%2FW%2BE74L2666ft%2FNXpLUfopBzWjZf%2BpEO%2B%2FTUwattQuW2Pg9Bsnhm1x6HSI147kiiV5FemNbgCQMLmBVqOAEY3lZROil10o%2BIBV5NX5d96R82t9omo7JqHq62m4EILyRumFOx0q%2BnVJBEMbzNuM6O&X-Amz-Signature=3bcebe4077d1c3d3634a3edd1d2d231083a6c817a1df5e4a60969180f741b248&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
