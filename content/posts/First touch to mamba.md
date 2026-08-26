---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QH4SWHFA%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T042931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIAmaRiVa8aZGkYu2uuDDAyP%2BslhRujbnLPA7Up%2FXZkehAiEAv7ctrQT1Q6hQ5F7UJzddIv5iH7VbFnpLvyzUo9u2iEkq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDJjvWHLNs0eLO%2BSr3CrcA%2F4OqW8qdhO6sEvpOGkBpoq1MSqDPNlQtC7FoBFnL7GCmZNCgn4PKaAwwYQZIBYKrPYw2MiGFE668PdorUoAkJtToiHDd8KZoa3uWR3xqwciy%2BSwIJseMviaHWXiBVcoKEOx%2Bmazo6sO7QS5AycwjIC9ZXA3VuFW7ylhfFNQf%2BUOllpxs96%2FmkYQ9EGdItJZymVo8zRUMYYrjOdiXRWKfrvJ4PuGxBycc5tXza9oei%2BtJtvuMJ%2ByLUsiehLWPkBTRBNPryhQJBLiauQfYdZvvORlMgg8IxRmDy8AUjJNpvFCytOckR8Qq4kOEY%2F5Y4GL%2BxwbJ10odmifzSyTjud5wI3etKrTRAJ2GY0sNprNCMVyXNWA9%2BGFoL3Fbsh87YI4DhHKsapYUEkDE9lKcpYnJL%2FVhEzR2Qgi6FRxNLoLM0%2B2zeT9yxhK%2BGfMXGtbZWhZ3qZmjJhfvPGbUWrR8oDn%2BhznT75zHdJg3ec2IyO7pl%2BcVHBNwmQADWZVn5x1kvdvI7cq2F03Qx%2FNx6Ccl7NyZ4qTKIS6YJ6EIvNRmz05H4wLXjJEa%2FbsY1IuC5OgzRdCgzxYGZfriWl4%2Br9aATFEa7slxYovYvpf9FHydrESUvN%2BoqPZP1%2BOdCBbf6ppMI%2FTudQGOqUBc5wOGmIlA9HTNgV5We3wKNT3Md%2BqAUEnxW319vJcBvPrnk04%2BirM0ZJ%2BhRyrURDtUQrie%2B1QMLehVQHaNbasv%2FY6mgrILLuaYYJ7luAPBqUWL9VHzYG6Rh4Cl5hSe8rjT%2Brt4vkfAfY6fn%2Fd6x%2FLtt5t8Og6Qv%2Faa4G0HlM4xvRghBAqZ12zNn1hsdaULga29OED9gk3IDUJ22zCtoLMX5FxbpFz&X-Amz-Signature=e660af51b5d9f1d74f293e5e749c14ba56fab1944ebf9106fbfae73e0f201e6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
