---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHOJUCNH%2F20260522%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260522T210332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIBHqwdeOcU1CJ9b4JVypInCjV4EULit7TmykvqoLQH8AAiEAtjzMATERPJyEFbOkGjnK1VLPshIwZdPwRhq7mn66akQq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDIB1H2ySx6QeYLUEtircA2KLg8rY5VUJ0ylKyH0G9IEW49sHT%2FSQJkWwk4KRT6NSygpBaocP1%2Bfy%2BnSdlTRR1VfPwhlxjYrdq%2FcOvyk9UboUW7jvX8iI0VbOPhHTFPrWMxaGZADajxcgqeFDHgQeGcrCAGgFW6NtBIJHbC09fZRmDsxNjUZIB2VBZk0BcFeP9z6iGaCc%2FDQZtOyIlCH4w9wwXH5AoBXNrJDeG7yyxuYxWKq8FiWTeXTosZdSW1qGK6%2Bly%2FTRfU011a0Q4IBzg0k0RwR2oIIbfKfuREFBIhRvdF%2BuIeUE%2BLxR8YlXUO%2Bmn0VCKx3irTt3VhY%2FuMozhW15a8TWylWVgFTmBaSikJWOV8NSz9AGvDDIwn%2BZMcUcc%2BcYDHHsxRXFjhCM8VERrUKWcJXxPjekK7nNfgGj8s3Lu1K78XZieracdAvUtv54uFdKjvvSQD1gYA3NCcHi6Zgu765TD8GemsXMLS%2BHop%2B0EKU1R%2BeAX8G1atM%2BlC7C2qv8bQGRf0EdAihnkQ%2BcfVSUqgRxubEaswYoRE0NOIZZ1pMlk9qofDuUvQIRlzJgpiGWfbjCBJU2y0S0wNT19lffBdF1SYGdP7n4kBB0hmb6pWka7kKSn3RG3JHIeCEhase94fIicqhgyZcxMOv5wtAGOqUBRlRR5tT0nhFPmSEY9R7hYVtlsTlloZp%2F1w5p%2B2kHTQ8Sah1zzxUetAxX1IhUwVnMHyDlRpY7496zqICokE0cqdL1wcZ0QGIfpRKg9h3uHSpXpurfSHt6mBRcYpbMTI%2Fq8j017pDGtnDr0%2B1HP%2Ba87qCaMnhCR9ACRoOi1HDGcwhSF3UMipYpDlub6Z7s4%2F%2Fov5Fz48MBz%2B59COuofO0Y53MSkR21&X-Amz-Signature=55f26da6b3d378585d3d8d5c2a34b85aaf8d169b20960a0224a7fa5264a1355d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
