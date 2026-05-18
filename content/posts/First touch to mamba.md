---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKTTCCNH%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T175211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIES27E2VoQKOODY7BB1tDTi%2F%2FgGgLf7LWBQ8oZCVuCx1AiEAmbto349pXUWBttiWLVsIltVx%2FdYcSdgOIaoMh%2F5q1j4qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM4w4zE7nBbiNqwxLSrcA68I%2BRytx0cg5au%2FpWwaVTgFms9SDsaVHtf%2BYRuHFrWZ4oBju38uVhtmpFFthkyYbDj8Hdju84tlN9y44m3aMrnuwz4dbYUWNXwMv6Cdx0t2oGSRZJ8svsisSn%2Fpqkqcm4BY9cJy4RmfDkO6frXrOVe1G5tKNk%2B2xfx7YNJeCOBzyuggELZM4zhS9MAQ3uCFQD4sQnmgKuH6TbZjDkP1R8rGbUXKBB4piamvtyOGIJx6emW60YDoXsDe8M0Lh63M7W8Puukqr7ZvX13qv1EsyF3eQWZXzQScvblKCg%2BlbNLvZyew6sd0tqEfN0b%2F5xdha4nLQvGI%2Fu7gpBZK4i%2BplkQdVtLIcQdOXKFB%2B3X6KxlsjVi3i7kodRXucMtowljJ2fNwOX42ufdLkyk09El7dGH24kzyyXNFdCL%2FczhwTt9s%2B4NQNj0Wmw3Eib2YBUs8WHNXZQFRsVsUNzkdcQ9EARoD9H42uJe1OEjdxIRKRsWXGMuRwtg3zMH5c4FrkwsABJYFJbqjxehF3ZvC65Qp7LAlrbhWVcq9uczOFhjZuojKhwKyAn%2BiP8CXtXdcAYFmEJ0W0DCeSczJShWq8SSi7An9k9qHYqK4SN0qtxCsvs%2FBBQiJTXfWiTpQi5j7MNWardAGOqUBhJPQf58NajBndCqPxP9GMRo7E7AoHEHXV%2Ffa7kGdVEqlzoKUXg32LQXA2fs%2FPSrsTyUka8%2F4opsJXOti%2BesmE8UUNpWfTbeRrWYVGCN3%2FFdVsvYJcGvr3xTUYyTTDKt7h2lzrVm4SKCk%2FSsrCq0h5PupzvITsoVVIW3%2F7%2BbFp%2BHdXdR0DGeP8OjCOi9supPc0nQX31QuDFeFAI3uzMZgEw%2FSjlTA&X-Amz-Signature=49844dba27b06a072eaa495a1c241e4f175da9e849092e269dcf3951902a7bea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
