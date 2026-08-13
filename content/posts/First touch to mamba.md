---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KAILAC6%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T105117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCTkyOOYnTKEwjxAQJcRiJqCkHdT4Cgb9pWcDzDbttesgIgToFzHMiLeSMGgCd5sMTOUCCDD65DLC5PMG4ofAmANJ8qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHMJZkGOkJuwc%2Bm2gSrcA%2BLESmDIWNGivbNAD4GD8i4TcPlk7jh9iWI4QLPvYVyQThgWXiUJqyr1NhWbOLPGuzt29xEuR%2FI3klqk8mo8TL0wjNKcgvbxRn0ja4DefxcBfAPdu833psvJUnJ9hwnjuz4U8cbwvc8FV7fbgSMNHABjQ8K0Jvq4uS2pE3%2BI2dRCi4B%2FkqH%2Bvq%2BtVdPWWTfCMGGzMo7lY6UN1NpsTqF2l8cSkMziRrvaUgSb0EXkA6TvTTWjdfyXWI3rpZwZVmowbT%2BjnXzahea%2BOZAwxrxRJNbsamMrrkQXuxa123GLrjf%2FUBNrItqWUScAC5f6PDXJ5sYokFcHk0P7J78WP88nk8gZ0tj6VV1NpPWX2AygUYqI%2FBVGiLxMp9urz30%2BBh7hiVwhs6WXm%2FtecBNTD3jDd0WkzluCIftYGBUL0zkbiTA7kk%2FJssZfe5XkO1T1uulyPKHFU73uzmPn4ZYJFP2hId4swLtUMDDrJIn46ktvwqmImqsIwHQFENv87HZFD%2FyNOeb06VLEPvbiys62ZeUVAYuhKrdTaDu0pO1ihT2SEemPxONWokJwkU%2BnGAJX2lK%2BCyen73BqRc%2Bvgk7Vdv6OEwFLv9kg2POrjA7nR4Tax8lmgpYwE6HTr5iLgXLNMKWX9tMGOqUBkCDYIPkauZJEZwiHu4JtXCAXzWqi2139cRSmF2AJBGJ%2BY99bcSbYwOAd7w55T1zaTus%2FuARh6d%2BaFKbGk0N637EGBN8hSRHIh84iVas9mricULxdlbSW5iZ%2BJei0hT%2BGZrwYlB%2BDdsRY0pWbeE9f6gKIdgubmyRfSNLAfy6fxpFETPD9FHLFgVPcGhHHdwPdb1z4O90UMLXmoUQgjJDK2FNfDq3K&X-Amz-Signature=1a6d94d4f9434cfe48b82bb26a458c0b9b8988a0ea72b9182af10cb725d89697&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
