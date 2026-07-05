---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ72ES5Y%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T185816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQDhNyxAuUFGm%2FOYiSlLwTtNs9h%2BFrp2h%2B8CaBAJWBHSrAIgYM5IUa%2FZ205FJy22yxNdQFNqFRcjygTGGxKnng5CT1Mq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDNo7dBpWIIP2Ngc4XircA2JTHCG%2FzvKqFyWqrkBHoTRODsYt52d1JOxsBafpOVT3puoy3JNq25vFaQeUTOd5%2BYjyVXZaoE9Hik1ya1p1XK4f4iiu1PC%2FFvdmS8zzsrWrst1R9T%2Bi5iTFjTmBOtLpY818EGTE9dn3KgIOYIEQHhuTsPM24Mju8F%2BT%2FUReZEaJX30nJ%2BT4acAwMvTbDtjchRLYs9oIHFL80Zy3RsoP8xwmAk%2BAcH3pp4%2FBqKHhdWfFxDW5rwgr%2B8bIwNRNEhU6rB4p9l6ssglh0FBrrZXjealrCxuVPJohpf2pOKW8%2BiUoITmIAPDR2RJnzquiGkoBgulcMG1j%2FV5hvxvvs1j6sQdd5vxR1TeKgGeV4CtZzPNPHrQeFYlSYLwnOHzy8xiJPCPPCEtuCh50r0DxqEzO0NDo5vSJ4ZXXeKbFaFX%2BXGte%2FuTngr6YSSAATqEg7DbtkDlQ7zt%2BCZC8CB9EdoB%2FMvmOa7SOVvt2%2Fszvi7KtHBPY5Fr4vRS1021g0IQpVnk9EJGKuYO5fbJOQ%2BeP3cNMFgUT3sLtZFYw3K9N4TpBAk8PDbtfpmZBYj2PWbg6hnBCX6gi5vzJWmR8%2FETcoUD3KcJPlT4nMRdtdS9ZIX1LDbT7DFJU0VpkHUav6wW2MMqeqtIGOqUBCZpLXeZvjFO8uk7wpttp4Du87Qx4JKPxZZzqCx6KhQMoXLUTRxwjSHJX%2BsyTK6XoOQ98YhM8RM7Minfs4ZcZtpVPw0wZsR81q%2BRaZPoxzRa%2FwwXXxNe038Fkk8%2BdgQikPfOCkFQiJqgRJSHf5Jaf6xBwvXaHPziH%2F2nJ4jRH%2FG5iJP9sw%2F0H7Vdo20Jaj5SqKvqc6bKYseY2g7mdaF48w%2B%2BLcTT8&X-Amz-Signature=56774ab469b8aa8e8a179dd393ceb96f15fc14cfac247e1601b436cbd8df6212&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
