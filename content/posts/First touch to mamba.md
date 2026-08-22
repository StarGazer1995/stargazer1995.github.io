---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645FXTNAT%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T181315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDS1dlY6IsQRbu8T%2FJHd0y%2FvZsePPkSHcnfjVbcegdhnAIgFUQhffMAWvzwXmum3kMxXtN73rTiJ3ZXKzAiuafIqqQqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAMYZrVLQ%2F%2BSNGqdKircA8VEdHKxVg5Jk4a3%2BIhYjIUCvXtesri%2B8jC03IiygY3u9Iloggh2BrYS1sKvjtldXi2v5Os%2BdJOny0UQQaDP%2Fem2JCt7pdTJ7AGiekpGFjqNWQqveAG6kpgW2C%2BwtWGHXrNCBmaZvfdWZF5y4yjgjHtUxFHa3plpVMyJkov9SnTTlBmEcErx50DIKi25vMWlzKGOHeX5V6UHiobN%2FJiC8BUPxEqo4I0F5kdVFYOQIK4yoNMng13NI9egWg%2BjFXR24nIsup3iIymmY086OnEbiq82nIIrDi47nfVd%2Fze5erqs0jqOef3atz%2FeO%2FFEXJ7rpTOQsEMHrGi3CIrRp1q5mq2%2Bo6bDDPs0bY2qDb58JorlI9KbLxdWoj0mBz%2Fhw1S0CCQrWLFNNwONSMTbdowS6lZGFn0PePQKtFb%2FDiGNdMyB6oi7%2BJkZfFLGxQABPIz0hMr7jRz146cUgw0MNUz9MI7XIXANwXfKgFJ5sSIxH6A6mmCkzAwIOFnrzTm2WLO8k8L4akMXTmTlKt%2BpER0K2%2BLCxmnpCynQyVF3hEcLJJLyMN9EXaQAslbIdKiCwrU2nsOKwce8zP3B0sZlY0DT961nem%2BECZbE6aRoyhGRZRcCjhzvKbNA2WhQU0VUMMqzp9QGOqUBM0oKPWxXccObJm4OHrdXLWbD9UDPEUdbOouEX7Ul36GCWiyqwKvK3JSQhKAjyd1r%2BSw5gaAUyVbSjHddSEmCvTA0ClOxLNBEgp%2F59fSj26v3N5VnFGDM%2Fhgrek%2F%2F3sM1d1%2Fh8GpT0%2FiwO5pBjOM2OOFd4%2Fn47%2FbZST0NYk9KXhg2ujD1tjnrN7xYcfM2Pd3fGDJVh1Dos7yREXbMg19%2BXtmBfIpY&X-Amz-Signature=03a7ef875ae53b886bc3ad03e8ef101ab31dc2c36937085250c42ab47148a3e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
