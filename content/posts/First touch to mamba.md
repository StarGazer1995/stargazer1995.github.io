---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPB3WWVZ%2F20260905%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260905T193958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIB1fYRkpGKzQkrUgfI%2BygWVHbeDZB6LHqCl7EfSITWPsAiBGsSqs%2BwUgNF05o%2Bl5TSoWqyURPHsSlJh6GCscM6KJKyr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMoY5nu6OOxb4YFYW9KtwDOCKOIH2mhQDR6foSg%2BKFxDUc7RAT6oVX7QvsnKQzAk%2FiBWsirIpYnAPxSgW7Qw93mGNU8P74WM%2BtLV2JZlU54oLsQo9yjP1oK53YPakfx6dj7VZmTOSOZq2DxSx06mmkLp6fV9DOPbwFP%2BUD%2FRAgwavrSqKtup2jzq8PY2d6DE6LwclW2XP5G4VX7Cb5ytf418ubhl5kw4ZWQwlhcgY0GamfxR9WX4P00drhnBZRbGA5QJoXOS1m%2FE3Iyz79F4w3zebBJCO6w0gKiKc44y6DnDQbul0kR8pNtvPH7ZC5biCtOCNFdFRz06HsxBAK2MUoCKAepqQWz4Nn5Lfi3osWpDB3stpTB8JEM1FidupyUI6oRRsq%2F7GJngJKVp2oThezvjXtAOsNZGMQ02Y0VIG5NoOd%2B2uG5qluh5z9bt0axN9EtonR%2FCaslnamz88FOdtVao6fmZZWmWGuW7AnAtTNNdAR1%2FXry24nsVrSgJGlR5mKxsZ%2BuePdFX7pC3vqwQqQAQ7SSlE6fS5g1C0lIf0D3hEzGeV%2FIKR%2FX9ROg7szSdArDSius5WM5GN18PNb8rWUuaSsjmxWxt0XHcNrcTDa8eTFCyCM%2FQaWd6xwleCK8WoEfnbgauJKayMmPEEwsLTx1AY6pgFYkVJtAT4CctVrQxprzZ1LKIS58Sb44RLXyENto9lyYg8vpYGBOH4vWT07lnv%2BFmtKdUrvTCD76U5rmbafRafG7ESEjjYkVa1lHiR9LycqpdzZadR%2F1hpLemJnhrSDW0mFuMUB%2BwvIcKH0Tu4OTjUdG%2Bd%2Fq4%2BNpF%2BBToUtUhYZpFrvbVIszUHlR2NPCfw6SSNS65HTQo9wYpM96%2F7waH0t%2FJLGzePU&X-Amz-Signature=c73ad9ddecf7650bd33c59c3720537638d0181d35c5496165fb69ed0a973e5a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
