---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VU3HQVMS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T205746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICiNXdRfZI4m%2FR72b4l28QHShE9sxZa5s5iLbe4wdmyXAiEAz0zu%2F6ZzhLmM%2BitHLemyHZq5ZYnwl8wQix7itgHyxzYqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJYNhYbkGVxc8VKyTircAwHDQHdN7eEC%2FVzPn2zSAkjl7cDQ9O3w3F1wtdm%2B0Lim2K3kS5Mm8AUxk9kenrGi%2FehMu2TaLUr%2Bz4ocmPlXCp5fb7eT13lIEgqXpC%2F0%2BBAoYdMPh3tg740px2QA252FEBsYtm5%2FT6WiZd1hJ1D1bQjNPsd7E4UQsFQeefSv8b9DufI%2FNbZFcMVIvw6AlSGKiZCxkabO7MKT%2F9KdmjFqwPgQdrX1ixg770e711HKZUxThxf%2F4CZmGvGjU%2BmzoYwTkjuofmeBuo7AhbECqWXpC3v6tfb5pqNsiAGz7s3GwKzehjcD9dr%2BCgcndOBSiRSKsKAyBctBB0kQcWrncwKWx0SpAS9Zv2QZBTUbfVdaL7sYaQBFRrevEX8Xyfr9P7X0oj0ZdnUugvWz0pqTG5o0%2FzGNwX2%2F1IN6wkXr0BbWkKLWtvajYsTa0SpIC%2BNql89jbjpd%2BpT%2Fr33TOJfUHWQqBK49BsPeJXTWoX5T8B2tXJyX88hOV8FxIK4eoZBOQsQXbE1vArRcWDuDUqwBH8dqdIoqq9yiETcM92hWGoOeOSnN0wZDNgQZPwgL2avdjh%2BkAJDkSP3agV%2FCI9hUGk5%2BLtBKUNziUHEpigpOrLrhNRCe0yLfsqaIKfww3n9UMPep%2FtIGOqUBiXquzfjPTG2S4iyWpCAWw9AnAlpUg%2F5xAVmsw74t3vsiUlGSse7qRefMdROsmv1AhAA6YvjRs0D35aelqbqOQDg5fzgvCluvnE6jYsFAe6MavQxq79uY5BVScrtLXk4LYRmndniNrTE7T%2F8F8xws0b%2Fg5IZCccGKotJbo%2B%2FdS%2FIitvxhmqZOsc%2Bk6CB3DAoMgvCXI%2F%2F766pUJk4RwlXpDuCfN8VL&X-Amz-Signature=348b38fd76241940f239d470c7e952dc08cfd5816cf04d7b603b886408774d6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
