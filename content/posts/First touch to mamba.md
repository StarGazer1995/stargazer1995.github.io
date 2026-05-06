---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JF65GC2%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T191941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBsZsfp6k1UiUqRJs46CQgPIduEqQFV%2B35gvcuB6lbjtAiEAq%2BGrLDstQc%2FIzBKhMF3riVgeU1jVQyEXfnR4pHjT%2BZAqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJd%2BqzCWbwzpklNtNSrcA5HRMEvYezwFrgITqgpKkY4e%2B97tIMm4C5kl13vd3aA5pWii89rRbTYSe57ZU%2FWNduaaBebTbkNhwFVm6ebUqCj1gHIIqrdgClbKQe%2FLl9wCxWY7EjWi3DqS6NLx%2FNePnDbfSUngJZnX3ZWSYfcrfN5DR9OSGu9UKMWqBSKIosCZ2tYwX8rSYC5fiSMcnv%2FTabP7YrL3%2B0syLBpHtA3eWTXWFiP1Hf4DgNez8xEnZeT5jcXQbvKz9wwvROetX8aGT828iWRx74wEdaJgqz9T84WeJS0B8yjuUANTkcoY2zrJfnGWXPcxk0PI8c8riX515qtcbJ%2FEEBA2tq0zlburGNNcQPES5WbJE3%2FUSvbdnwJlAjq4qrV0Aeo%2FkAeO1Tvu3xiu7i5y2zKobePGoCxgOQHqZAm1UW7v3d6TcCerUOmkTNNiK%2BIRIX2cHrqvkWqtSymfUf82MNEo6wMcGjn3qwOu0GyFOr%2B38SK9DKrYtzMI5T2WWSyPLaUFA5QNI84BZHusSy5kOjoc7ugrdA1zBOaKGLVZMWBuibVEiyWWf60a9L7d3pN9JBDX5U38yslBNEXjUTvHmZUgcEgJIAC3ygG%2FZ5IaNfzQZr7PX8BMXQO%2BWGp6QNo6wFqHTfVjMO6c7s8GOqUBL%2Fy6WdDZYIJRJGUcCzoi3hL%2BjmUoSoRtceqI3BAYyK8UBQxqNGd3fxeBCr1%2BAgnV4sbhetNiTr1pNRQ2tgfm3nVF6SrCpbGzZIs0x3hUhl0eLuoMHbWiXpUOXG06rM9BtIa348jaWKPKoOZ5RIi2OPhjX0SNHI0cCRX0z6eEyoDhQuaR7NfB7q97xC7JBow2rlmRFuN4voqYnSUGpBoD1x%2B1sGt6&X-Amz-Signature=3a2a1d0e53cac3166e57ef0edd745d74e66671b7ffccca47f6c4a940f4920c3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
