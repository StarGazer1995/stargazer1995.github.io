---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662X3B3OJW%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T161324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeW2XF5OjOYAjSebzKFrq5C0Cyb2SQR9ibI0A5Rp1HlgIgRBdbDDQuJ6AbpbXUFHgEOBxy4UPyQh4m5z93I4SnkRgqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFbqFA7PRZgaZjv7DircA0%2FxakSB1%2B3%2BQq%2BRIHhLi9jA9WIGb0AEDfKov9OkJVmYPHVqSGPcfeFlJLm3AHNPckfQeySkQzHEjxmsG1adkXqZVIjVJwHNhsmdVErvhE7%2BWyZ%2BRKddfmefjzX9ULZxax5k64cwH4eDhYAKyFIl3SM37b9uYyPb4%2FRk9wyIQz6eSJKG19n07xFVVRe%2FS7lfYgvxg01e8SQAgDjFJfzvIwUhSEqBH87Pth0Ecn4OgN2IJZruVMOeJr1gn1WFQ49BmpVGSQ6Z9x%2Bs%2BTL2UhEnsaVkkECvXZGvvSJ3MMKRnCSPpQmUFvKySijnxex5YqFoz5xylb5xtGfe2LHWRePgJ%2BUJKg6bw8SeD9ppmWWDScE0LOXvyomAzgtDtZaTG1knGeOVq75tM0us7x%2BphQALSLNf3jU17bmw9k%2F1VhbAMR6sAAirRsx%2Bm7JGj6BED6tuwXmylrIezpNOvgFbXSmS9tE7BmAqA7cWmIjrjAn6%2F0B6JjuAySZemcQrjfyDKLLKglTHQ1m2U1QAmktgzERCl3kq20aRS%2BI8QObMnCN%2BAStDpczlkQEvX%2FpgrA6yAAV3ulaqXhHzYMRUVCZ4oyiJoBJJAgFr7rnJKaGJxe7YRcOJiwYWl0lmjbVi8zQ6MOiKxNIGOqUBWUU5QwJAZNrZobiCErPOKD%2Frvnj9aKye1N4%2B3UKMY7GJ0V0n3YbN6pML9beT6zwjJhsO5HtBKtkllgHCW5H1Ybzg%2Bom1wb1RrIyRAi1aCEz1gC52XgfOgTeGhS9TPYDxqjW%2BQkjfIAF1JYiYSpCc63gERI%2FtGVKP6nUEt2dRo52GiQsNVi7qkt2FEOnMWjsUJhXWt4AyItqZpDlQLFkNNdcjN2hj&X-Amz-Signature=bbe7cfafb6a2c1bc67a106e153d4141954904ef375652af3a5627d439d0091c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
