---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IWAPA6O%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T015758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCttnI7CdWCStw7JEzBUNl1lhWCyErZlps5XbDD25teMQIgCF9k%2BUzHIiSYmLcGfvIffRH8DYzTkkYJanifMRdK9r0q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDB5ZEE%2FrKchf3V5vrSrcA9MXP0fp%2BK3mfR2x3QztK1O9N4EYlLPJRRFcrAtB%2BhwTbP%2BQZlMpx5A6PjWUAuSJ2hFVu2GbMNAdkTVOH1VqVSCSoAzBGM9XiRojAGoexIITRZcAN6E0NlTS6HEe8q7dLSzr8ngo3zDJJRGur%2BwKhfYKn%2BjCLcckrBBBLMnnkbyPUZCGE0Mf5NbRO9S9tdXh8QOso0qY%2B7Pqu68Zn%2FJk9u8svXs8U%2FtbVqLXyBwt31J%2F6eEDiadzYXyF8EuWRid66U%2FhaB6LLUEVex6GoghEJpjzikIoYyjQL8PEgIyM9NbPWm4YuQC9orwamR068PSHhs%2F3qSv9AMs7Ol5yFADbAa4YbYSqyMpY52jM9zT0oydkb81nReVTRzH7MwuIhPfhU4UroDNTz0UofRBqwHbilLOFyayJgwDqELkRSUmwra9FZtne6yph92prhJ9HRX9%2BI6V9H7alJcn1jqkl%2BWo%2Bm8Kpd6HXwYj%2FCR7IlXqMj8zF0xwx7J1eipNEogKwpG5bDm%2FX1uOODUHkv4nnrBZZg%2BtokWJhxvGLxAKOAI%2BvjxIAO%2BtZKIp%2B7jogRNiVd3hxdnnad2zyKY5Ji3Gtkpfhc%2F4Bbp%2Fvu6g6kpLA6eQ5Nbu3UffuJWM07nMf0sJ4MKvrjdEGOqUBY%2BWyGTdmK2gEPwDxOnvoV4vV144ApgQnu%2BGVgS4clF4N3vW3yS7A8%2BmgOVE7PU8e%2B1AvhvRKtNlw0ElvG8X%2Fq7zFGGqvXkOvhyTUhIWywR%2Bezw2peS8qF%2FnFbDy55y%2FU5owUgpUSqRljtxgtev1cAI%2Fc9LdK5xZtev%2BU1uWJnMecShcXjrDcxZBndKvD86mCBSn%2FuSZGjEJXT0AGjyI4mxjQef%2B8&X-Amz-Signature=36872be6ece540ca486bc849acb83da6480eabf8a3a538e58150abaa604aae4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
