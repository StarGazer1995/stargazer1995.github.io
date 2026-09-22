---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ6XPAMY%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T203559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7zx4vNOVFQ4gXg7CmSoaEKRXO7kNtmU0M4ZvtRsh0mwIhAKiNX6vMtFiY2Xj4%2FM3JfAdxJV8JkB6nqEXpkD31J3aGKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxxRVlfY6RpBcw81Ccq3ANjTr4rFQXvdN%2BScK8jZySlBaulSiaACdHmNpTVI0WNlTJUUbjWJFQmL07zKZPJ3T1xC1QSeUsnZ4058D7kBzFPGFxBj5CKGpnKjqrPwn%2BPQXu8T0GH2XCcuC9K0Da%2FPPuvw5kMU9yM%2BRi1DzvjZE6JbPEnSOI6Jv5bFQYV1W3xh9OQRAn7CkTT8tgUbvH%2FOgiWzv3SO5uB7VjXYUzxFYYYe5VN%2F%2FkF9PVjQN2LO2QUf27hlGrSLiaR104FB4x%2B9b5onAEnJSVQ67Foq0NrPC3ziVpt0%2Bf9oZzQ8T2y1TV96sxUyEUnVK2oG5Si4inpMF7TFx0k1ZJlmZcXYIszsOSeaCmulxNIsXJir4ZoaRjVTizE0GxzovzfOorUlsnBuQhhaE6wQyLWbWCsmBlJF0WyJAp83L3nW7Xf6KcMWKR2%2FD3DQWIM1BOwX4mr823xR9b0QC1AUq0CmG%2Brjgj%2BkYhRllu10Up6oVVuedhQpq3u2Q1CbTSpMJCXqBJQqKgDBpSnqvW8hYUQNhCbVSTmyI4DYbRVcyVoLeLG84OqJbKf46dPtF1KoRzO6vkHJgDjQYdxA2zY8sJIBe8DiYVNtHezbITaVXIhMsd0ulttVQnz2qDS4PHo0VuMmtpc3jCYqsvVBjqkATK67IMUwWdupv8Yft82x0HwcQJMPA5uzbq%2BenOxrJCVYmykEMY3Mtd6cq3waerCc4oEVZN62T9HZMttf9aB1k4gy4OGvIVN54xEgfcU6gPOBGhZ4YZxw22bTJkeegv5juherK0wXgI5CxjfRPM6x2dJWL6QiyRQONcnRrSRP%2B2BVs%2BKV3UmhM9QLH%2FhczguAYZlDjbPxF8Y1cTMk10OSb4%2BhFpA&X-Amz-Signature=dbeb0c7be6b669969bdcd1440d3146991fc4188c917cfc2b06b0f26c115007eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
