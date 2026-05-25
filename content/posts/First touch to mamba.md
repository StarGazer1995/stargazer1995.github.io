---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRBBBUXV%2F20260525%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260525T225155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDVmTyiEOCjIXY8d5Bh2PYdatlh3tEOkDxrndXPs%2BSILgIhAOt1Q2ZNeCE8NjPXNrpgVbdBEPnQLjtT0YmM%2FRPY05liKv8DCG4QABoMNjM3NDIzMTgzODA1IgwjNwqCwGxRRhAIcp8q3AMtTC4Rnt%2FyqiWEA5ZzRsVpKn5x7unRUsAUsUOy%2Bb7sCTuxysmqenbPEquFbMX5ys6WA9ycrjjfrxg87MJydqNuvV0aD7NbbMbB%2BSMlETyBGo6Y4geWRe4%2FBwnnT4biXFa0AZ%2BNG1ad9CWDK2k0n%2FjzWpobQYnMsahUoe2zGvtfm0q5Pgh6YdnYUIkzwJNipjidDjSMMgGvc3rg2Mf%2BSTyLurhIvJ3RXDv6jqhZ52i3CG0s9R4zuPiTstd0Sa9jkfSjR1bK2HdLtpTLn1JYPGftVJyIlgDxG8Gycm9ohXL6ugYTRF%2FJKIMLCxIftWaFtvkyZBhUUNokEVQY31LhxOF8ZB%2F1k0p4t8fLmhd3QlhbS0ZpgE6bLhz14WkThkhjSFZzKilJzya%2FBN6%2BSu8Gd7h8zdSkZOPSMjcZGnNSl5fxy%2BceZGjtomu%2BSnS%2FTy7tHtkp1XPGoVZ9VeE11%2B2hnNspvycWb6MLLzo%2BDQTqNi5gvEXx29n5CeN3XyAUcOYQ0wfoPBAX9ftW0I9Z%2Bs2cq7Is7H4tH928o3skNVdUdQuH5hhJiExBG323f7o2l1ve2KOus3NjLiQsdCWm0nK2EBzWfQdrw1L%2BnvoLpOlBn6H8T55gSXJRUlf52ryqBTCh%2FNLQBjqkAYgeUeBXb9pgsVlTKRydSqmjTjI2BhpjK6zTEfIKYNVZDJCGtdQ0GF%2FeInpTZ3nvEC6l2HO43MrtjPExKuJOZm9XrLKnaQytrgX2h7ISFf2yK%2BrAAbKtRaTBNP2vIVyGdJRH8m3xVwJqeRFxPaxWEl4Svk%2F%2B7Uy6hGjiBUMxyuYCGDGjPPQSf8p27eN22rlIuBQsLiBsUmk6zQ6d1lPrs882LyKK&X-Amz-Signature=dd265086250df451273bfe8d525f03db40fa609fa7c51997f4d77152fd9f2bd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
