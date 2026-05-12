---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U52QDPJR%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T114725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQCJis0z3e4VKUeJlqpDDwZMxrP%2FYrEz%2FWUQmASeeNfJBQIhANIi7ngAzxaQqs9%2FruSCquRWfcQ162NPaVJ1%2BdenbZH%2BKv8DCCwQABoMNjM3NDIzMTgzODA1IgyCABmNnztnaJkhFcsq3AP%2BBKIFVW8xuEgAvX6xgHC2NE8mG32Y%2FCXTVtQx9FFvGCgyRYpbI1j4T0vdp%2BTUumPPyl3wtbtQLcfrfTyLFlbfxv4Vaq1bdBBFWh4%2Fmfbou6aGEuMaVKp5wCqB%2FhZ4kant0kkR84HnYt9O3WQ%2Bp6uZmjpWIUTuRqzEVSxVobb2ihbdnIzCxDYOP309uzCeXyHVIxHFl9InGATlPftP0K9ZAOXBjCycmFaPyTBA0xV%2FGPNT2C9YZhA45D6ezHNPSLb0%2BugZF3Nah8zMdBlkVsIdjPEM5aQE%2FzR8nhJmEsSJZCXq8AREzDt7exDkLgSnD1rCLOMQCH%2FG4V9ztJILsBzI5arGvLzttIeVduY59864rPeFfz1FSHG0zvA0f9X6dscOTx87u5kkaRrRm45dpEe8WrLbaTM5s6zZxmvt8OR3WI%2FLgQ7TZddTdC5WCnf4TSCLVHhNp7k%2B2q0JlusYVyLoLj7tUgZyX7vMUfVX425j7iOg6qukh7toDtAnFvX%2FSSbRgMILZbzDZHg%2FQYpNnKDoLbxnHWrAZNQnsRqZCTTLzxYhd%2F1MNv4uI7zpGfQNFdUxw1xxbb%2FHa%2FHNe%2BnOShRybp5dztxMz5vGrNdsrZ7OLKdrq8Kz%2Fhr7TVOsRDCOnYzQBjqkAY0H9kCxiyJ5spO51eAgt%2BPt5px0K1l6DKac2UxV1qqd4JfCuInF5e16LiNe53RvQeE2gPgjkihzLsuIWlGoj71PDjWjJhpFWxOXRlliWvHY%2BqZWdIKPz9%2BoFfkE7tU5wLAiepND47m27bHiTN%2B0ai%2BeGhaWIoUEcV9m443TAfO6sHbVF1JgeDJ%2B9%2FQnIUnsQ9rgzFcUOjosoB0XEmJNNfOhw3ay&X-Amz-Signature=fcb95c6e224a5e8dada88bcc8acdf0e14ce14d26339cbd0ba315936771635f46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
