---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TRGSWS4%2F20261006%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261006T105315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIGX0tyYyOVL7iOPB1%2FlgBqGQ6Wr2x76dtHMbxTSzd2wMAiEA9ImI3mCGB43ZvuG%2BqZZdSBlB1QSIXRRyFJgYdeL69%2FIqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLL4lmmbo16GyXzR0ircA09XPhwaq%2BzZqKk7xKbzJ93NcjKv1HIHHMN8GpLqeUOV5DGC4rSdZN9vJFIX%2B2xgTLcpjU8hIEuS6o9MBVPNviPd%2FVPdm8OrBglNeSBX7b%2Bg5eiDr%2BlwLOKkQLZVKTGm259skQYISXbWXGJf3D467arOLlFSxmPXqp0Pcgbqezf0pC3DndEBXc9pBUfO3Wpai3ePEYxtr5NdElmrsrwULqm4UaSWbf9nIA9%2FUy9Yp9jzv8lIzSrbbtR%2BYrO8vJeW%2F3WEsVRgZq7%2F7PajLGILg92dXbcoFvobBxDP1X7fQA7YwKg4zhifLaEcN72ihknfuQc2Qcb8xjVaD%2FHoZ1DCIVK%2BKlmsvafo60%2F8TSCnmG4tjyukMtWS85aHkegFfkbLUXKc2U5UAQ3Ie3mNVpWCFY7FTtzcHmrlk1rlUSvQqcPNU9yEXKnuzu%2F75BTdQffeqaFXqkHq6u1MKPFx0yYfjDJi5o9xIYFEQWA%2BBZHcTR7qVlagTCJmSXiDDABak9Q4%2FFBwQNtlqeBruLcz1MfMY9mGrXwdF2MzkhIjM5U%2FT4Kl4rlr%2BrZxx9u3y3PKw7TxARJyyT8%2FLQB616hH07P%2FEn8GPXLdMqyBwrG44zRhXW%2FAEmqlNzAgIq5GONArMOCYk9YGOqUBjC4naXq%2BAdXQ43WiOErps5ZXQj88z8%2Bjsi2gXcpZAOorxFNyotBr0oCt7MZVrCuCHf%2Fya3HTbACi%2BGWE4RgqTKDNfvW7%2F%2B6OmYfWgp1%2FwPoTQLHZmPl5NtvEqqDCqdtoTQKCTdZNxAip3bpTNKDIvRq%2BRQ0g16S9Ue1PCuBUTCKRmrvoGv4qVyl%2FVCM489s5ir0fwzGbtOysciRJK4wxLm3XK3U8&X-Amz-Signature=82b6f946abdf843ca20766881dd218f9b17f6484601624635b627bde4e08aa76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
