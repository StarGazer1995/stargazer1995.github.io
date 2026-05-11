---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZN6Z2G7A%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T162438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIHiSRSUi53hFU5Dt7HJFdtnlCkXOfqGkQwdHnDG3s87JAiAwAytyReD%2FA6XtDG7zV%2FRzyFZ9wmKtyBLf0680bx%2Fw%2FCr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIM%2F9zN8XyGNTh3WV9HKtwDIFSbSM%2BtMav5b4hdUA9kyampbUXHXD4VboZ8cXDlhVCn49v6DwaqMJvQEFOpkJnicSVPiYc35gHf%2Fxm28xQo0N07xoapxmHp%2BhAUU0OHmPhwhSbgSJBIsPgtyH%2FnP26pAraj251%2FhXB26K4yQSOfEj68CrGmPcgNqC%2FpjIxPMPULGMcjT7fgGSfvxmd4gDbwhYeXJKAloEWhm9KJY5e2QHqkYMgAnJ5l1R9cL2uye%2B3PDn8DvjH6qVoXytQN7xlaeDv8NAW1N4jF91LS5IS2xkQgSo6lwyE8THDCea0g831IFBPtPgIVrelhiaXWuBXBculpP%2FCyP%2FOzcNF0BcIDbT6tagGwz7wjOgOYw2RsnDvwZEFN72%2Bvkjm88qIhTIgxka8TzXSV7adVhMSucDstGHtawS3DaLDHXaOmIjZB8uCHqFgcGBXuRmKvhq%2BLltOWHyK1%2Fpf5I8E2R8YYhm6Dd%2FpTRZpa9537dPCgkaLFqZjJVrUxLSVYkAYXPO%2BhSlOCTzOjYFDgWkZYOY0hgbaBSyFbMdys%2B%2B60kLkAEN%2F8BKGoA8uqD%2BHXWimZfuUZOroQGPpOP7uZVfFdR8eI3rYhK40F%2FdD24zeIiE2ax53lFmdCf8k5h52QBwWjklQwoe2H0AY6pgGrcD3woucLgwC45RNcvnWmAxgihD9MIM1nq%2Fp7PF9%2BWdq4vEfIp2VVcgVxxJMZbAJiRGHoGRNO8iyvFrvsPCgtUeJk7BWT1NqrVkHrcKe%2BKAizTwxTDdKz2UyvR5S%2FpUG0KQQ5CGIwVLQozC9QXf0ESm3u1goK%2Be7LS3EVWGSPXfDd68l1EbmrpaitxIjSyyzPQ%2FKhH77LZUxCAcR7hvkwJC%2FIvdBV&X-Amz-Signature=18ea608a22374559fa5d308adcf4b943421a80a5c1b2ba6adaef1f54dc7d8428&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
