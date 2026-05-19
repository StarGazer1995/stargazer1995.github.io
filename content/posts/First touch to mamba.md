---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HSJYSIV%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T073626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQCsMeJcCFFBrgdBDiL9TKVjMZP%2Bp7j5An%2BOku2YOPEFtAIhAMZO6mnWhM9O0EbJDBmezEI7aRifdPcl3kAFLBTCNce2KogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxEd0ZqsblDn8YARjkq3AMf%2BzIzHDHpl8KzoJNczk%2BzRvBlrbMuFS1c0K2liYfXFzHy293owhLvZ1dxMmAdNdpPe%2BkRUHtgKCFy7EdVQhFihSCLl9dYIYxOtfB64m8AuSW5QxQJdbfaf0rA2FX%2FA9U5kjmqdQL%2FwFbiIMWMoYxE2WlbMmU%2FLenSF2Ge6WnmCl6gT6FqVT8NUMalWU9dWsdmbq7Xg4OOn3b%2FLYm3%2FfpuqQLgu3%2FfLHxNmT0nxl%2FtVmMTHWcYL9b2O4w9QXlvyLm2vyyr6wrNQ3cLlnFC%2BWmHIMLNkix%2FSt3BlQ9AmVoQSfTOGNQtvLMw%2BMDqd0eMh0fopboLiIFXILXy%2FVRqDm8QOdJJXPcPlaAINwyWy4IU1okQHW2bvNO7zHYIrRUpmZdKLKQBN8mKUKGLSbpbq6a6GTFA7lTLs1NfWXFntEfZJokrJ8%2FWY%2BzUnG%2B4TUGxuIDt2O8%2BjHena1azRb9cW4q4jCn3%2FBk1AtVSLI28%2FiTyiW4K3Z3t6x8i%2BWZu9gXmV26MYzau7V5bWfYHv6JgwYYFU1KB2b38QFEAg9d6A%2F8h1xVP3FP%2FonpmM0rgjyBJIwtn9WnTrEjXwy0P%2FWETQ2pyn%2Ftk3gSlqXcy4uxgoOGGWJ8ZPim7Iz48T78frTCvnbDQBjqkAaiqLYmPYQFLh9hg54osUhbW4gdZonpUKH%2Fh0tagsy3gTEW%2FAdor%2BYxCECXMjxihik%2BMW%2FRWpb5paVN%2ByQguTLIKECCpmk3lmb%2FqLsIzLBdjlzmek5WEZ8RDhQSq8BV00hjRqFEefYCyIdZ1aVPhNpxLIpawZ4Is76k5JbT7U9zqxGXZNjNFmWJBDbLUON%2F%2FCqeumrJygXVIPT1eiHUdc%2FTw6pwT&X-Amz-Signature=a0ecff75b0af32934eef2d36d1a196f96f5ee9f6e2b20ffc0a7e4cabc26ca510&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
