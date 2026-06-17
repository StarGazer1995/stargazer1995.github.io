---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XE4KIQY%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T085350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICdIbrBZ2EOnOhOnA7f79II1Nrb%2BBJkCq8yYwws2dcHTAiEAvsNvwRytDp%2BLHGHcC80S4hMZSqFq%2F1VS3zREucxcHqQqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI210y3LmdGENLd8OyrcA7Io80j05C2wYiI0aPQiMWPrT1LnJYK7JEg%2B0QntuHD7JWO4%2BhpCGGu3xbTqC62jm1b3zbj8yad5UXBLK2ebuHHIncXTdgm2hLurwMIi24i0aMiKWAYQg6DZQqCl%2FjoJZ5M8Bc%2BuAAkAgMM2QF48Gp4lGSACMxqGFcq0LDA32%2BxqmQpJvnUGeS%2F3YT3PJsJsI4My0OGv8WP%2BkNmnfS4FhV36FQ3%2BRrt2Wp4I%2F8HqPmY1t5vE1sDkxJwux3lokAyBZI0PN9Zb%2F1NR30qUUbbTE%2FjagYOtK8gLeY20%2BHfpzO3QhmqFgAZLqcgx6ezIzDV5oHQ4f%2BcS1yvdGXNWSBByWClM90JhXaJJzFlUYBEFEE9pUlCG9vYlugXjpg2PaZGpjgVNIaASOYiFZaU6TKfNnKAgo2wGQ0fNftUYhE%2BANLgWqqEBZHbeRwEp16z2S17v7DNUflyzozydC09voXo0uFOtqKQ30vwWcJttfiQQaPF8sknEaYNTpekzo%2FjOyh8f4fFb4ivhfGdqlTpA2AzqzSQ7nVsT%2FOslED44ybfY44IYa%2B3ugg1Ztxqg1RRB6VQ%2BtZzL8ixz22VacJeloO8u5lZ8VKg4nJwZik0DfOCzJvRAuf2qWwIPFdmFAvdUMJmzydEGOqUBezdczndgy5K99ZnWL04q3Iazlr7FeBW9WGdve4TalmOEYUt45mA3aPKPGXPNlhAGK6Bo75pQXgI40BcJT45%2F0FK2aJoJxSGrCElzyWfzzH9sES6vDplA3wZKqADDxAGB3C%2FRd0aIjoKLdvMgARChwCpFvsqlV8JgFTaIEudsArD0vzqZ3DoLlpJBg8XbPn%2FxAvPObUf7r2ZTpElr5KDFu7vadmu4&X-Amz-Signature=9b24be530636781487ea83ac79c7554fdadfe5d1519bcda074e58005c98c55ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
