---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XP65SLAJ%2F20260522%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260522T192142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJGMEQCIFbwAoiMNq%2B0tDkFaUjPT5pO1lqWchL%2F83vK6q91HwjoAiA8NAKNQy7IXVyMXv0kOEkNPDo%2FHUtpLaCATXpQojQndir%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMkV4AoERSlThpTSsFKtwDyAs22N4NXzz2U1BfFY8IOwMIkRvqDQTiwhTGJcaxT%2F7RNs9svxjZavnRl%2B0lsuelVbWBbGd0wwiTYVUu36KofcKWdFfZl90iYaKJcsbQ8j7i%2FoSQ0ooM%2BYI904EU3q3MILcfzEsezcJ88lm5UC1wB315RnwtECMlsQ6qGhSzPpIQFbIgBbFjCi3qtWCEyD0aOyPAsJYJQsXigiepJKrmzGrHxjTmVXryfcpXQ5FE6SPtPx8WMI1mWWWvk4Qd4e5LXkcwI6Bbff6nyDl3H3e7%2FPI6hq3iYjiYBL0fzxN6%2FTYn4gmbl33IFCsUIckD1dYf8fYjv20d46fLarmvIEGELwUWHWskNEkxOuAtzg%2Ffki%2FlhpqJdb16%2FTTj8saisvgDFvos21O2x9ZchCuQfR3cSals72VcpCeB%2FQVyxaFCbmGSvJMw6cn80rVapV7U9JvhHddHfuf3DRlhnKAdFQBu%2FAyJqJ8yqLcpnKQHbJrcBRHlf3yD0R4mLFPXj7aandyeakllSCIldxUesImENkKcQ6G87iLXqu%2Fxixrg%2FoQ%2FiE8N4tCIkM6d4yLmBNXcsDX1XUZ9curMidQ8efbNd%2B5U0YjlFSKD7WFemFUjmbGLkY5WQxTNFjwW9%2FoV%2FP8wpKHC0AY6pgGutAGaWpr5hR6S%2F2L6nZXx7w%2Bm%2Bcxxi55hiikHhrMG41PV8oXd8G0h1Hkyl0vQWDC024LUgMEgE4lgpgew%2Fmmf09D1hhteBB1NF3pgrvwEWZ0czPYzlpDx19eTHNS4GpE4BSK5PqNrXFZbSocVyi1DZO1sISSTn%2Fp9fUwpQvvC6Zxg85Wj1U4JIfubdo9ASgKhBjHz0xmWQCLTJLe%2BPyr4aHh0KrDe&X-Amz-Signature=2ce4d9295ae7fef539198c913480ace357b25aab14d98a9d65b7895884e718b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
