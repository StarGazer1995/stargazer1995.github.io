---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667F6M4SQM%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T211549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIGXblXh4Hf0LUa0FknkOI1qFTbP2LwXWpIFELL2FUSiWAiBSM55WbVE3%2FJcH2O5Gvp9oBEMNu4UDEH5P65e1R7xIRyr%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMqjzBzcYJdieuRrwSKtwDe%2Bj%2FmKUvc5lRIypmBjrI1zkIggvX%2BXZk5QZuhwQOlXwCPSOoOvIAfdWGLPog5rKsLi649tS5WVsdxDSlxC98TtwjnfBymUC9l5HVRpN%2FMUgPQQhXAzYC%2Bn0NJmPHH7fm7Nlb13bGZz1WphEOtuRWc0IjVfwvefmq7B%2F0S9fAM1lmUvEwAGVDhE9RG53hthS6s4z1DMRO7EjkiDLL0aJRxxLW%2B%2Fyj9yx3mI5%2F8s0aYc0HBsuM6HoWNEBiH5y8nFFvdMj%2B0k6VREFmivFX3j9TKry7mSPcPHMoHzwv0XnWeMNhtwFTlkjXrQVgWTUXPuckTnTzu%2Bno%2B9lSmqcjB8kwI%2FucJuxD5XBASP6WIIPjbbolRHqFcz1S0G9JiNMh3k0tBK6hBd1zSfszjr7JTb4FfrD5BFhUCzAJc1%2Buu5YuJeHB462eQnm6jfw7gl%2F3OzglWzbOaS7mEzesNwAHSoomjbg8TJRseiP4f%2BsI5f%2B%2B8paSod665t7OObAfjQSuln2o%2FG3lyS94VxToysiRSRFh6LHAhU47t4cir3pCh2iG9M6nn%2BDSxBsRI7Kfocj%2BissZtH8kLG%2FNJr1aZHXoJxWVTin9y3SWEU7GhaCeePqUp0k%2Bx5b5cMGKbNq600Ywrtaa1gY6pgFNGrmNclRn8BTe%2F7DHAqcKJ6q8xfWEO2TEGHh7LPzMnY%2FLm8ZRABzc3qmCxZ875pF%2BlSziTV2pOlCJsNe%2FN5vbDOTpxGJ%2B4cnWFtyDHi7rhuZsQcezznKfFsPxWZYu3MPMdUKJiGtiCK53QtZYdEx9PyUHt41uBpZN9Q30MmtWp8G9WreyhdluQDMKAcinxEZwoogYjNG4Sth%2FIkpALR%2FjRpruEFLc&X-Amz-Signature=23a506e275feb91eaadfefd1d8d2bad43cbe136e82430a0093ed85fd2543fe32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
