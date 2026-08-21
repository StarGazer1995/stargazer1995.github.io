---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IKDISAF%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T122344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHuezUHOLYM0nQLBCxRby9slhx29cITj4MrX%2BlTMmJSoAiEAjrFLgc0k%2BIN3sYUq%2B2RH0kXNJHvAbuo0DNdHxZsrPHEqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDYsfSPx6fAsRxiS7SrcA96EyM82Klv%2BqBold2SNfraujACtf3j8JwqRPU2bHD6Av9apZ7JeGMBAe3lzNxz%2Be2bZVWusOsniLJsUNGPlg9ENTxl8wQ9eOJIuQvoTyWq6n6MfidbggmVkYIV%2BZXJJ7sscbsd4i%2BedkNyP8jYYVuUzloAY0JvQ4w9fL5Lv9XvcKbU4JDQxq%2BaMSQQWwa3wqwKKz4e2te8haRi0BKJRjDvxv1VgMJDM7OH0a7Z2n7mLJBbpCE5KyqaIqwPFwpNQ2%2BdHOglU68f0XFjFrevqDmgttAlVW1w%2Fu7HlY3sRHt%2FZHLOoZ%2FB0pPqhOrhXGYUOf7fjqHoXyjG4Q9O%2B%2FebDgrNUqYHLlcSCUXsSVm1E2xJa9jqbsrf%2Fg0fdCXEsi3GYndSXOYkVt7MuVYzIO1USoBEn6l%2B%2FEPfpNbO6t0UsWeCrV4Yy9LhAkefeW5Qvyqs6SvklFy23UOvnkwba6eMr%2BnUXEvP8YxWYZDi7NYD9U9zCqXyc%2B5Ks01G99SEoZ%2F4ooTGMn5y%2B%2FnC4gAYyKkaeOD1VK59V33G7atYCXI7C2HnD2K2a4lvqZCVYWw3OHAH4KkURwN%2BNah2ouuA9WSJtILfq29bXTpENAquUScDawueMBMyw5n%2BPzvSQDYW1MO%2FWoNQGOqUBe2ptVi3qJHux%2FERWRVcAo6BAyTacEqaMytG5L05oynEGO5Db5%2FmkKatMD4tgaVfTFSdZyGagEb5Sl1fCZf9%2Fy2B%2BUIecTwxvIQXYMRScXdyBHzPxzDE2wVWTsRQ989O%2FLteFvoF0B9QOYfLBchEjC1jcwQe9mfUaZZsYqIlLttZw4E6hOXcQndElW8Fi8DHii4Ng6OrZWtOP8QoBYcBLB9sI4fkJ&X-Amz-Signature=6434d99164c76b5020ac84fe9e1b7aed4a1133a9b3d554c2b5712215aae9df1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
