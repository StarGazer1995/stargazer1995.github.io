---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI44JF6U%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T162228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHwLGPE4EWUu%2Bnay%2B2puT5WQx4ClGo8QvQmW2l5zQ1o0AiAdZJxYUh9F%2FXleE0OIcoq5E8FXIJf%2Fe0H4HlIec3kvWCr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMpMPrF5bth8h8sg1jKtwDouYhc1eaQTKNQV01fsNpgXXmrCE5mpsuyf6HfkO9tsr7WX5mA56pNKaz8B%2B16p8Sc%2BCYlChHr%2Fn59QI%2F7YMpClWpLS27FamfRmPBec5ETkxh1%2FzBiwiC1x%2Bf6E%2Blc5xA1Sfi4CRjligA9VCWi9uVekjUXkA%2B9IiQA%2B%2BcNyXdRxWoYR80yCQZUxdKmsEgtpLkJfKtGvBLRp0yKU4rBujTRUrtQVl7QONSrcqGzU3hDtWzXaxWDSeJ9x%2F75FEjruVmXct7kOBZxmoi%2FADMJruhx8zGC0Y%2B9rUSUHpvJSPmsAg0HeBxUaSesNN8PJ9sUU18W3n5Ur%2FyEQ3DFwNb8H3UlW013%2Fuok99fVJDH1ht4F49fHDIB%2B7MNtxHjKHbWMji6c9NxeEeOk1GbCvwDD8SvQwzQP2fHgTEJSRgfXK4j8kRU3%2BMFH7HUFJdSs76YABRzWn8AXpJvmgg3GmWlpG69uMqUdwKRtu0vDi3ECkVi0rDBvxHASM%2FSf3b7fjRRxDSA2G45exc4EGfMRZFx7T4rMZcgYBgdruE63h0E2C%2BPOoQQ2%2FbujJwZFjdnvapHF6MHp%2F%2FH2VusyuiDqI5l97sWm6md7%2Fsu9mS1fMLFS1UERtQ6443nWaJkwj8bNkowgIv10QY6pgF7Vx3Fz0jYrSCsA36z8iWYU56XzWT4vgoUGDGjuFBvDMtFZApq2bC6EzQPzB6zZ1VkxCwboszvJ3yzYbpvIHzMjzD4j7B7UWksTc1gdyORmfwAruyxSnJxG7nqSl50z%2BSoQODxdxPTsT%2F8oPYJm2L5od9Kh9AU4zRn7uzVCuPUVr%2FHjqQxHiL7yzNPuPRcdd51BZjiq4rr3OKAOSAJ8ULIZd7aJmec&X-Amz-Signature=0cd453567d20a2657c53be853727a8d12700a20b9955dcac5ae703302fb593cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
