---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CB3QLJP%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T183739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDKCswuryf02TGUtmE0Dsb17kLSFqIplw1vj4nDXlbHbwIhAMY0kfKVnoycbkyjcNhNvD9o8RzKZwDvx6KY2IQynjBSKv8DCFoQABoMNjM3NDIzMTgzODA1IgxsFx2cfEt9TIPAY6Aq3AOc%2F%2FT7hStcjWLSiMjkk4k5hHxpJOpmN9jZG%2BsSvaElhCg9sK0%2Bw1ChWXPH742S%2BYbfbGgl0nyMEcLjkakcNyPJ6OVoo6EXzU09UEV0LztJrziX7jhL9ojWSng8B2goWlAkQkoevyLFa0TtO5s3WUfDwHhkAYfRthZN46%2Bv7ecKt16RJja1YO66ByE2eLBZflwxigxqCxRciPtLbmsADC7Gr1i4IkpoA5JfOC6%2BhFXi9k%2FJsQjtmc4cWYmSTxCaCIbV5O20ONiCtQ4e9rhoj3GNU0JNxp%2Bj9wdRKshGLgdJ2d17RNVOHPRfVRiV8LBhO0vpcTWFJEjAI91bTDaKNbhj%2B%2FMZSXIFW4t1PelaidgWfgXROp3yauSrItjNf0moSel85EullZEX%2B1JoQzByoOjUFYzK6i2IHIrb1h3gcUoPG84%2FbQc10IGQ9nJPcwFb3mqBDXrd52UWmjNV95f3y31ibk7lHIMhKr31HNg805gDxpRoQ6%2BL5tPVJqRZDgrtxAuLrqJHOdnyAWsEr%2BDP6JsXWhmaiMmO8AKHidVIQFvMwEsIrpTLa%2FNFlVPEZ7qeGwTHZL11V7L88gNurhz%2FYHz%2BEHX8T0PxmTZPKd%2BN11xbKiVb9EflMSIJS8yP3DD7ltjTBjqkAc6%2FiHedkQFX1T48anPSe%2B8j6lxpIpy%2BdWmwmvzU%2F6g84gG6gQpfUE7ymwgJWXUP3g51AIr3oYMHrnWU9S3aEtxlTwpGtN2Sshdj0w36cdNUuwl%2FzGW2QTQqQGCoIYPZn4TGzuOmnsTETgZyGuRjWtqetZ4WMzb3mCws39NRIfRc6bjUGYv1fQSEpPcNg%2BnF1WJshDPWTgRf23ntj5u811pttn%2FA&X-Amz-Signature=635db615c43e156ac25fef18220b2bcc61d16c1d8b2bf7ced738bd777c733375&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
