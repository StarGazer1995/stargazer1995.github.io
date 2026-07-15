---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5T6LOGZ%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T074804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIAwSIB1s5OvkTl%2FoyvpSJnWNzzLexsxfLgo5wAMlp4HBAiBJBIXSSYtnVaKFZVJ5RHcc6KjgS2pakAfEObCcV%2BgZjir%2FAwgoEAAaDDYzNzQyMzE4MzgwNSIM7sNA5nT%2FHWAmVq4SKtwDZWZbCmRUDHxalKe4YiEN6Bj%2BIPjPbR8mkzTiBKFOVqBmuN8lEdLgY5UrCQU0gVdHaVnU4ldaq4M5vRhnT7m86gt6fFY8vHa1DV0O1e7QoOdOVzB6cd00FyY3vrRf4u%2F5nSwDL6asucOWj1430zBFtNc5aRHvaQc2kT6DxdTlwZxyqXifWMdP1%2FIA26rFZdui8sJwmZYwOcT5Px5Irm%2F9tm66q%2FHwSbeGHC%2BIFgKx35HVC2qty7RUMOnDwhD3CqXLL6keWqfBT0uVs9tVwKahFrly4i5GiYGRhLMwGNDNJR%2FpdMEcg5SItO3GmMndTgI4oKV0y2d9Xp7Lt54CX1XezENSGdb8iLhESJFIbRhaBHV0tNloYY6bvMOBBhsee6Reusn6kN5fJFQAL0n4TCkGD1jcq2Qp3FDhuP6IPZMMN%2F1jdR0yR7QHhy4Yo6LnNQVgB0nBOAAS3N%2FNfjUoYGce28%2B6FyQD5Yalzefc7lSfgpN1VfS1rtF1chrCKua6kbZX9GjX91Gv36PzxcE%2FQk2Amqn3%2BM8ETSXe43%2Bxi32fJoci%2FZsxaxBntkl6nsOqHHB935qZ4ZHEpa79piAdYfDb70rRmB%2FWAqbrvJjeE1Jzx2%2BbqC82K9NXy8CFRkswuuDc0gY6pgGeuF3i6iSR4k4YhgD1RgOd4g11V9hqEFI7yBH5K9doLM6mp%2FKpsZ681C0GGyIy7WHOuNcP%2Bsruf0JYicPbLaYvw5rKS9%2FM0LYU155y14e7tndmtD18Jfl%2FVZDzlc9FOKavFokCtsUfPxAEGGKfSD5LUPVL0%2B%2BswW4LihlMcfxaG1VexzyeqPxjCeVqNQyHhPno5mkGBR20Af6C4o1BdwkD6CDcq1GY&X-Amz-Signature=237ab0da1aaf92e0ef142ad82c999a5383f52dd11048f484acb81ae9ae7e3753&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
