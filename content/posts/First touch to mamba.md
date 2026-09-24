---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQI43ZV4%2F20260924%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260924T224833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIHzP6Of9rsTErCXTLwK1vBmLZ1fH1yYjYE5%2FGbzSGWHNAiBOQf2%2FFbGACDtWSNEhqq8sBnFYesvOqcaP7OG0U38GHyqIBAjc%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjvzg5xH3bbLCOQmbKtwDBzDryNri528heViyqrGGo5j0BmQo6tSOws1kABD0SEm%2B75JDR7D83AjbKOpGOxWYD1jMA%2ByCbG5qS%2BXjV40Ufop0%2F%2Bz6hcKvNBXOlpFVjYnOvp55tXUdn4Mzzw8fqpdP2fO9Lm%2FZu81A0MoZI2S2WK1STfJ336oBT0Re9YGjjTe0jNLnt2fMc7N76Rg7%2BQu0bWRoZOxM%2F5OnBQ5IIrumApV1GBkI1YXusvxpPXIfMjv21N7LkqoRjp%2BIGhqsdoAZfq6m3ERLMiLKDYtpQL1eWz%2FfUD%2BBPW3t5wlpJI0RwfIA1n7sOJKtMqOq6b3V3WVRAUrl49neuKtR8QlJHFh%2BCIFsUE75GW%2F8nI8G7J1UG0BVz5ASCt7pIlCdseFxydbEagun5ZNVfOIDJHwnlAdd9CZnD9la91HPJ9I5Orr%2B770Rog8wsy661UF4WDNtmNHUrO6LZ0e2EqucfRAhFTmKn%2B%2BJyhA4SCrpJxt4CjjlX6YjOXhWuG3nuuRWrEDlLUNQxEZBVl9u5s%2F9s1OJQwqmzlTJR%2B2lo9V6iY7EQ%2FzxRKpxO3RTUFFoHcYe0Y5eeJFI5aS46ZihIkM%2B19c58tZICpZ%2BksQauEQZqfSTanLC2nVGpfd4WqR3FR%2FHTs8w7e%2FV1QY6pgHsiVxufoEp78JQ2RNbyS7BcRzYq0WlRDoWDVEnGzlAyW96OdhndYccCfW4cqQcSqb5hWM6upLzM1FpLHBkveadlzxEFP3OF%2BoMnDKyzlhoelS0umxMXHPU7vIuLfJUwHS1HrL74oP15%2Fuhsbl1erQg%2F2KQy97QLWi9OBmV3R9%2Bl9Az9f9t9KyxYGUkmaZQruHz7pAOgSfuDliNK6%2B0dFY1cRQE6jjV&X-Amz-Signature=720b2c3858695578cdd4ef6846ee8e9a9f2b22bdef1c5c413a95f97871ef3dd2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
