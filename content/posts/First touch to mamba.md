---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZC4VJYD%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T224258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHnPpgFpBCu1ClWdpC9D0UMVI0%2F4qf3lrP2%2F4hfl%2FVrlAiBXZUCTQC5jkqjyyHGE%2BDm0LVNuuLzHWGMhpbFYM5e0pyqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FUzGoXzlrwBbNO7aKtwDKlVAxXqWI%2Fbfh%2FUrUeYQRtJ9DX5Irw6bH6%2BzWCUFm46jOj9rs%2B8KsZrvko09CsJjYBYc34bfEIBi5kfqbg1zDLIyWgR0LIWi2FdGYNGT7uucSsr7JcpXyiuALxTPqPvIYUSyx5E7gzjxEVoZOlTrfkdKGttqrHzTjRKZB0%2B5ZI%2BwZLHcsmgpFbUDl62dhTTTmXE6hlO%2FuLVNlK7DOsKq9Q4ff6sGixWkg8uFUT5wSuMkJdkbCnzFpSia8hGFMh6UnYQFve4ObEeE8Cyeg7cRrgaO%2BAkA%2BxdQ2edMjs9DnUj30y%2B8dT0F5smF8mFDY8Qj6L6d%2BZJ0%2BE5KszrrwVzjrxDGMFYo2vx40m46CBiDXfcMGmA%2BBNicXgnmAkYOSOnJmaIcrXQPpxEu3r7KmIrCT6fjZHSCmWYMFF9TsY%2B3xXpROSUjF2%2FqqHgdbpSgbinnyk1pTO9bkSOSnHWndMQxRQBzwAhPaTwJ482fq0rawROaWYV6G8sMZ9MqfWcVg4mFqp9T8knU6UnndQkRuj4VvhHxqxywcYLYZs54b2rb08D24TwMw%2BhYfRt6FBsAiVlt6yJDqsZhq9ddhba0nALBN0qlDFlmEzlrf2gg9J7pP6ZpkfBcw76mBBx%2BHL4wgO6o0AY6pgHkgB3Y63478Tjs1wpQWKMiKT3mi8SyO%2FrTyDyZy1vVvCyVjZGOSdaF38eKrMyEQ0R4oqlRrn0AZEoly3d3FLa1aNr9VvkFB7%2Fj%2BB93ah7xXg126ItzTmnPSdl0xmg5iqD03aD6JRwgyOFrPweuSr7BSO%2F8qilP03kl3qJFh%2Bp9n9h8ljhJsWptgrgcN33UGjzn1u1XaAvp3z75pxMaC4hi8J55%2BrlZ&X-Amz-Signature=659ccf1829c364553c5d2be809aa73d7e200cab53dc3b60380bda7603da233ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
