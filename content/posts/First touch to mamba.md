---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOSA3UPX%2F20260930%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260930T005042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBXd4RvM3nmw6OAqDhULfIgumkDlKpn%2BH2N0vCHgIZlMAiEA3RV%2FgCsduTPl3EJyXppDuySaKxOcA69o3EsgRSdfK3oq%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDOAIcOqhUb8INgwFZCrcA%2B3BxeiJ6fpmfrofJl2n4U%2BGQg5GTccdhzRfdx4zvOLMDuQdeeypRmJfbps8KKFqaPcGdqDJINF7lICJeWw34%2BShmNyAs0CHW7imgBDUv2M5RVgGb%2FnZUB85kzl23ehLG97OZisPk8Kw%2FYFa8bG3%2Fnwt%2BpKUwLEbq6YD4VKgypIaRZXUNEWPjPW71Pmn%2Bzk3XmER17FbyDeiOn4AOTZvtdQC7Tj04XALwViej8%2FG8PqOsujYaVYPmoalSP6Mo4ydT5XUxXFI42%2BDeigwltXcYhP%2Fg%2FmxjOn4%2BglDb0x4kcn6v1iTaq2jnT3NkFlrlIoMilxEOMO40ShUvBWveKek8NXC8S5cSP%2Bhel%2FF8420U%2FQA%2Bq6LBR%2FubrhZVqP8%2F2R8bNzb81ES9j0nhNv5X9j6V%2BL93wf%2FtfMzajGqIJm2rxySVM1GJjucwMC0VTcgntyxk0BSk3mwQzKjr3wVyrPwb2JriU5FZc1sXikWDIDq9WLHWdyegT%2F3y86fhJP9S0agVwPupi9bmG7XSKNkQxnJCZ7C21K17u7N0bxCzDVUJXGJ47h6OawKvdOLbpJDjS4cBqTap06US8g5iH68HKpzHG1aQVGv9nRhNRK8m%2Bp1MNJWV2AxCczKNa4GhwREMJuu8dUGOqUBmCoXgM8YRh8MxybnG2egH4X4kpeMvsRQ6eO9uGFT6PGLmeXPb4%2FQB1E4vdZJYF6vubIcesCms4Y%2FQuPbermSvqZ5Oaehw8qf8uPkpOFk4DgOr1kNt3xPuVoPwzWOZB1Ch%2BeqiA4KBYkxJ7IGZfjE3Yb3ShO2n%2BWv%2BajCX%2B2xmAcTLVXJtNucvwa0E%2BcP5U5jBfw9LXElf%2FZinwU9Xf3Rcqkzwkf1&X-Amz-Signature=d83446c94e03d0376936da3bc2821a5a80f8004315736cff05d78f5c8919f9e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
