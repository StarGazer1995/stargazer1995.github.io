---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3R7DDX4%2F20261009%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261009T173948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIC98DtzJBjcpW1clAmwzVzVEKTFe8G%2BQE7xmkaGza4pHAiEA7SLjYhAJjUoLRt%2B0l6Z1BG2F5P4OlRyJt%2BLI2ASfoBIq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDCS45nxhycxjUHd7ayrcA%2Fsn1gSQQz1nHecXT1b%2BOaz8Iw0rLFhcrbceCMm6MebIWsgqS0OLKAoDyDC7JHf0zTIPQ5aj%2BGH9t9YPCk8KRXFhvMWRXucOgwWw%2BegARXOBvgcBJQ3DYX0hmhWiqun21BJLfnR6MhROfGTRKl%2BmkXmTkzDppCnfkNsGjj2VKffboY5b3BFGsWjsNz0XsyoFuZ3lgow%2B4HWKeTrpg2CedYdL2LwbJmG7QOj6nplCqqz%2FRCShqdlqzb5UWaVadpYZHQgveYnfqpvNghtoMidSiAOcv283TxTsbsEc3zRj6Flv2GSX4ERkuMv59Z1V0e1stpOUVHvgHaLRIj%2B4YBLHb20pmoFcfbpuUU%2Fztej9kT2HtHxI2vq4ZYXcAVZrb8dZl2Bi0kU5kQkVlN2RkoTEN5poADXNOPRpWQANespsur8VOV2l2A1Ko0tBLvsQLTwT%2F8epce0RlM4GX8iUmUrI8CmA%2BCGglVJu8jsdLQrRIgabbCnYTYcDqpIYwfstOihRY0ItQQld359OeUe3fwF50xqKeA3nU84h%2B%2FviLP2GgmmPaEm43HKyXKSvYO7ScScNkT9k%2F6RFBTM9vCLIpC1Hp53%2BWHw3%2FUFh1ZVPtasZKDxdEvr5SHaaWnILCQVXMJWzpNYGOqUB7aBJOTMShpTam0x6F5J1koFvG%2BbuRbRiu5zQ2aICAybgqNJLEJmrtgfgQBKhNhkMpPPt%2BfvMOFXpbH2XxvLBS9UnYws3ryV%2BcW2CPCCdploNuWlR%2FsrViKCqL%2FUeH3%2FGwN%2FCZHa6GvneF%2BnL8Qm%2FPpB4VKUFG69%2Fmecc3WETo3OdEfVSsWP6ozzRsWe7NwC%2FVlBZQxi09d8EayF0V0IIskraNwd8&X-Amz-Signature=6904b00c623ebe6dc712c537ac422d33120af20330c267f37c58cca8b3cc46cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
