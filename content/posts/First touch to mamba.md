---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UF3QWTAW%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T203749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQCGb05QTp5uja%2BdspAVjHy9y5aCmPTWBSg7trUSLTpMuwIgPOs8M%2Bvhct3FclVZc8DpEf1Qou%2BXEQrL%2FBy%2BylOJyVAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKejrchj4a5DdGSiuSrcA9h%2FsvrQ4bb95wlmHE09KpAuMiXNNWCscrJMNukqbdy8tKcnQFHbMjXkbRBdiyKLBIzCxztwM5s5uz%2F3h6M7pr6kZWsAorc10ts5vqdpr3cpgSBulHyCrhSR8N%2Fs5yn%2F4uNJsvbolFCbD%2Fl1z1WG%2B98hpcVBBLxOWIoclDDkYp73O1JDjSaOSgLmrY%2FeR3ohtev9j%2BWI9IHy06yrilqHPU5Mrb3qxPGYylX%2BltKwCN%2FEfcT2rI%2FpYnP%2FIP0GGjo5OyiBGkwGoXPr8YSEhcjocc0dc49%2FizP6CATDmht%2BT8zDwOseEb3f9FoeGQDtCHPzAlzVGury9KiLpSwuG2hUWN9Zv%2BoNxt4G3%2FSvTS69t3UPC7MO5ikjn6%2F1FrbFJF0%2F4p%2Fd%2BUV8VYu4Ay%2FJzWov7dXyjRHtieFOfIp4lTPGtPK%2BarwPaXeqZ%2ByQc%2BZ3q29KDK8O4atjA%2BhNO7eS27iKfIccz5DBPqUtLY1KkjL6FcRckGj%2F55jD%2FC4KfRsY6qDfXr86oo5IZvBFj%2FnfEhlaUpmyeC45oZOdvwITdzl%2BIehnpacquaiRYjLSD%2Bqakwjj7%2BTnVBo4R6LqFIrFSmp3NUfDcvrIfY5tIFh08Gqn06t5q%2BRGk9%2Bs3QA3Gj6eMLnFydIGOqUBWGTZf3RbON7H7yYjutmg7MCJC%2FVBuBKVK7%2FlK%2Fk38xlpx%2BtGxRsNdEDDwztctS9iCEbF15mY6a7igiRcGY2JPosgNgTY4VKc0sFTHrirqB0wsb3MgBnA5nAXPGJkFw4aAuDGfFJ9z6m0DGH4D0TReYRPeDv7tbe3mk4QkrEWZPUbM9QFN2Xmu%2BO9L85xerN6sDLd%2Bppt%2BUrO%2BylHd7KJz2dwnuFM&X-Amz-Signature=a679bec49031d20603fbc8bcc6e266937fb5bcc35f99047767a9e198b22acfee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
