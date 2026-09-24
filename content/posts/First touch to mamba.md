---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLW3UTNB%2F20260924%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260924T065305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQDFGuqlajqtw49Kk5rxxvGcB6tUhCZC1GMh06nQH4OpZgIgZnQxg2b5kCIVOAuCeOJkIXmQJ3UaMj0N6avHAwSKL7IqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN55X0sDvJ8hcxTJTyrcAyEB17mZ4GebLAJHa7LkGhvQ760RE9RO17JEcb9o6sG6KrGkSRMQJp6OCBy2Yk8LVM4zTrQyDSb%2F%2F5zHwkc4vOZOVMukfndfETtQinvOF9jIQnsMKE0KIUoAlvcTEuOEoOxGf7SAaSvgOWgh86LyCUtMjOZ9HcePX7lY4Xxcps%2B6L7NaPyJgGXUwr7gJ9HJCucKrGmklBhRLvxENXqeoSqbFjT2xEavTzd9hjGoEU%2BA9HbdRX7YrHJh7DEsK6YNBKqgek0FBIdOQsYosLruHr6eTcvJLV0yYzX6VAqJKS4pS1ECYvpnI6w6VVdV8wtDbgwuIRGcTD6WCGpojk5NKtX3nD4OnmhTtXXk3Zbi4A%2BwejVsYkP86cxEhnogdG22Cit%2FsrHE7klfC5PPhHZDrGoWa%2BvOkJzSY%2Bj5KB86kkyUpzTqjmDzGXHOVbEl51MVHxxsgZ0G3eHxa7b64WU1Dryy%2FBKIPHbcvD2LvEeii%2FYNebBQA1HCwPuOFpCGSN7XycyuwB8frKVmFY0u1K4JOa9g77DtxbqEQ44Z0ZWNhnK%2FzTTVE4ZKRoH6OLAVkyUFQPL3XThhedbxXP8iVsCaHANgkhNk%2FLirhjHTVME2%2FvbvUkPIlcFO%2B9JaRFBrWMN3a0tUGOqUBcnmUhhlIAeY%2Bd1DeiJKsNtUKjbI6mWjHrp0WDdtTt34uEuj6YVrr0ESEQxRFZwKncjrsl99gbY3i46Pn4sEpJcnZjWJUbgDSOk2VCBAsH%2FZqeVv9Ia8PX05Lxx0jOOa%2FYLeKPa%2F6wEjnq%2BtWj0VejDzUaJpMl9RaiKfNI%2Fk41P7G3bTEjDu%2BeJAQWBlIX3lWDmXu2HNqfLIdRiIGY1xbf432vi%2F7&X-Amz-Signature=75b1e3ed03486e1a8b3c807df90591f261e59cc8561e79e6dfa56e817ebb3d94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
