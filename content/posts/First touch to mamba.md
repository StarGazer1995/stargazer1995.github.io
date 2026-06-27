---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663242I6K3%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T082500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyor5UN%2BTVaczbE4px7bKs2ZpvLD7FW42qSrKGJ7SOzQIgRh3TV0iuNabObEkV2LqgbapbZ9gDjdtp5JvX5G0TNE4q%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDPlNR3mHTFJ%2BiTKMSircA%2FP0pauAdvhsAaYIHjqn8ZFhc5qCqsdYYXjrCaVaSs28HiGbEQqjUo2pIAJf%2FoIjZvMdGuFEhr6wgJKc5K3n%2BT5jgbVDJaEjsxvz%2FW5iv%2F7gcFK4DdUJt3KkLmlHrHWSznVKpdNS%2FinU%2FxGxE4ThIPdRM9HdSkdaq8%2BG9hxw8kJans6SFavPLKSPGKOf0Eq%2F6kSirXA7k0SArbaGqHGbghqaGrBX9x21O%2F2yFMFcX87IlR%2FSIg1gxI0bdDmDTosUW0MeqI6SCuM0FsznZpFjfK65F8Rj8zFGIj3MYmFP7mZxZw5eB4gvsfR7hUpWWTF4gB4Xu%2FXRr30yacr4R9vEIy5Z4tOQA%2Ft7QhZjCwzqO06HSZapDxJPNQZwd1gWhpv0gwkaVpTx8Gtjo3%2FWXwC2WiJLOPfcWshZmMG%2F5RHFVp4GAuPwdYQi5lqaVX7itqV0tfcxmW2CYNpMNcs%2FSYw0GFbSj4wftJl%2BB0oalGMxqH%2Fyq67%2FvgytcbjTg9Ne71pNb6pJ9mxbqRCF3SwIf7GQKVSaeXi0c4QUSNWiqyrLmmEs3S7hjPA1Xga%2B5PVZo%2F1TfMAjRNdn9hL%2FoPGCQQkAcrrz1B8Fq%2B8lmU4dDriHCUNksd15iKqs5vGx3ydPMPb8%2FdEGOqUBNBYmkxkjE1jmxQfKLeNKiQfX8ISzwJFtbjJl2KG%2FWnpxtj6wHIq4UU1ejERhZ8wT9YTR7HqI8TQf5W4miamG1%2BlIIkKJOFFRfKufr6BFev3UCiAc%2B%2FEarsslydv7RYACnxKvX%2BmHM%2BP%2BBG%2F%2FyNQzx%2BOzMI8yjU0ZGBNO8zX3cPY3KozBdUEXjts4ToHdrayeq3%2B0bEU9eEEAUjK1ZE9DaS8vW0cW&X-Amz-Signature=bcabe47298245b613d62dbbd52f6dafad8ee3a3824999537c254b7f7c12ef28f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
