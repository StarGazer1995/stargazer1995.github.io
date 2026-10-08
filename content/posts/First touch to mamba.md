---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RAC2JOU%2F20261008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261008T223542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGUaCXVzLXdlc3QtMiJHMEUCIHL%2BUeCo%2Bo0XE%2FrswrxLimz0OGuFn5MJIu1gdWPiBajPAiEA3cJjWeisaxFNRitDrtmARTmP3HgDVdNz8R89lGF5XU8q%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDE272aS7QlMVOgrNjyrcA2Iyti9d7KSRJUepLdDQTxDvXHg4MO%2B5bWt5YWNXgx%2FZj8%2BRidjQzxIfNwwlxPkNFdepKmwuL%2BALqzrTApm%2BTeXoe%2BQk2hv5BzUWcULeDrHLPK4C8bT0exVG1TQC2nKwIs6D4LQdz59fQqRW1WXsVv2KS%2FQ%2B7mke1IACZjJXRaLD9sLWHq4N2bWtTL11Sgn7JPf9ufogiK1aHcPA7HXaLCSGRnQVrtG6q3RRdHSs3OnVWLYjXvRwvDl%2FXbWDnqQ2yIkaELzIIUtqokxk6Cvd1%2FqkgFIqzN1Gg5ZJM1JNEUicjYmc78X8zcM5h6pXQ07e4sn844xl0EH9gBQrrRtFSLJGPVYubCWc%2FNxfJhBHeO2c3eloFUxPYUgxSgKIDj5YKh8C4IY23x3ffdtHqswdz%2FxuHbxxEm7OgIrDzDK5i0mZ%2BVK9bhTzGZK1ekuqonze%2BrhmNjXMf4Vmn4daR%2F%2B6zLRd82R7gW5TW3sjoS73J%2BoBF%2BIw0hlp8JYPH2sHbyTqTbxrL5OTmtwR05%2BKjs9i%2BubpRQUfNUjEOHcxBD5SdGEg5u9azbEHcSZpSgH0bQjixo5NzozTr0YN2e9euDDlp23n2mVW9rXDi%2BwPzNk5lb5dCj%2BvMUhzYaeQvuulMPj%2Bn9YGOqUBdQRDQBYac%2Fuw1lTnoE1pPaqkva5bj6%2BfSwUjYk2hQquDNPtKqLE5Gjl3V4k7xH40kCQF6GzgjyR3cdfaGRGkzEEvgIuuVDo0hdtYX0Cv2X1jMTLZvEYdZTc997V2hjYm70Mgns0o8cqG8LdGlENJoeT0ys3PvLibuYlIwMWqsoniaXRa7A8Q89%2B5a3JTA0V%2BcYaWcGm%2B7u9UCpYw0l13oVcqhiMl&X-Amz-Signature=2514901a299520bf644531c23fb880257270be367c77751f83630a1e696ca606&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
