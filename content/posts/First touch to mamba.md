---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WPKWDO6%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T182304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBdWhDUFH2pAA5eT9oVVAoJbc0orROZNZZcW2nffOp9CAiEAk85uqsjUmqmNQunBrUlGBNT93iTMWzv5NfhyQBvSoUwq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDDg2%2B42W3%2F0p3CRHtircA%2FduXdGj6kn%2BwJv8BTkXhVeGl3SYvkXU%2FkB%2FDeHPqBBZ56S6mXIGK7f4YLAcX6%2FPSFuOMRqINnZm9tsSnltecIdHLgMWY%2BRVKF4vFOk0mpQ1Vdh2ZRdSgnwzvXEy34p6Q8BQYOBbSAAfYRqheeZ%2FiuO0xOxIG8LsAC0RDi1cWtwJv5IxNopszoyoy5X2U4GdxnLrc90W6qUDSmOOnnVB2YCz5aUqHtVxe3S9guFIdq%2Fa%2FeG%2Bzd2NaQvfwJvgcFYuSO5IfbcXOPqn7Xm9OdgFY2HVmAyNAMAwlYdCsO0pDwuRLlKiPlYlxu9Zarduaa5HAzCGBHVxSjQL2g8LuUWs6gx50vzWtFUpwxvfMEe89U2MMjcXmxtNcZtKKsRp6rGNqSBmgac1GvBACv2aq7ru2Zs%2BDLz7Tit6t3MfDq9RSFbjTqU%2FGUWmIgIOCqozjxri0RcZveR%2FtVFewFmbZ%2B57EcFiipr1wAI7hwDhAsNU0%2B0yF1wwDAwZzfn%2B2JPDPQTbFRMJPg%2FxhIi1fPXztIlGdkvC96JPfeceFdnFJgUQh2Zu%2FcBcAQHy6W2VhpRJODsQcEEcEKszsC6DKQwzCZIrDbgsoPEJ7iUcviK0O1WPY7mTRH9VMTYQua3ZMm6yMJHUl9QGOqUB6iNoQzxSqDoRfiTRm893qsjRc%2BEZbbr5TzETcSRkRnMuVbCHpVPpUEqULyHkOKdayalWgr4kb9AdGjnDEyBWPYDk39tiahQKoC6KYfYcAePJi%2FI1dlyONbzQwNiDSTVoCl33Jn9hVito7SYLVWHeXjscm4tdqNOE5jzsH5cUk1vmctM43VfYXOIQUm3RqBzsHlCdEmYj1oGorTGKVd63gFcmva6Q&X-Amz-Signature=4ecdd5b7d6a6d05267f18e63b339fc911f907dcbfc87f81508bc4cca7f9c30d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
