---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7W4OLRM%2F20260612%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260612T081557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQDw0ggWtdV4MFwR1b6thRN2C88aLR%2Fni0gZyV0ITkEdPQIgbZ40dyWZVSQTv6V458%2BoBeyNrLrpzxib4iRzM2OYDt0q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDC4fS2%2Bg0n5TxCQkbircAykmtgKXkhX%2FU6jQ%2BVaYXBKzNbCELnm%2B3ai3WLau6aEh%2BFqcx4aihA7jEM62taivdA1Elkoslu8Ub7EeZBZ8LJ7Gw%2Bh2X1tdflxPrKnJ5UUULK5MervNTRjDyyeJTOiSdmtTF7%2Flov1HU7YthRyrx2HrZfUKLEva4mH%2FJaT1Au6N5fkY6XxmHItY%2Fxhbv9oxpZp08uYgPuZBZ8rt8hGcy1beJ0wydDXVDbO7PPV6Wt3vGRyATnLz8fopDG92EcClrn%2BxkahukQP1%2ByrVNzb619VvgUyUCeZ1GZmUizC0X0RtCL2yavC9%2B0Xfsow%2BfFEwkGTgOSBHAzE3khhP%2FNKh6NU8Q3Kv5hzZ5CTaVFu0yN9A%2BXiV2FMuo3g2bAVP9ns0EOMWaxwVSuVzYP8z3vzDuExgc4QitNoyM2voFpbJBklsludEFeXu8YkD0sECUyd7BOsiTL1%2Bo0jIjv3w%2BRCjMHgBrsworQm5CByoDmNOA5MC919y0n0cWArMR4TqIVKBcyVxo2AA%2B9NMK2xcI%2BxLnK99nurvKev6dMfxyQhvC5%2Ffnm6QrOGQdEwHps2NrtQjJrPN%2FZo5R964DI1TR%2BUzvQfL0tdLm2sT6HHVNBcIybaXih10cpyPxV49Io6xMOTyrtEGOqUB%2FcLDb%2BSWo9B2J6MW20Bt16G4cLRzdAqTEEVynv%2FDUs1LrBamncc3ENT%2BT5tpm7Z%2F%2BBlwvDvegkdwE8T%2FYphmp4DSlW%2BwhjUnjLoeUzBGcDTQ7lWj6%2Fgq9k029MZZ%2FRrH3YwvWUFvCLWKL9zmdLkkmOiZXUS0Re3YP1Jo5pzW6KMORQNfujYhXQ8dfDaGDpFldC9d0C4jvBlRRqdC0lV83oikPiat&X-Amz-Signature=c41b998efa794e206eeff067c36ca581ba9a0052ff2659843d68846fdc444036&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
