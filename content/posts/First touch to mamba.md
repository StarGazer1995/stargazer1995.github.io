---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSAXTTSA%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T225235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJIMEYCIQDcShTXRIuouYLXpQ7sXAC3fPEShndgByO8FhBz7WAAaQIhAK7gxwcB%2BBPPf2xRZvkJhRO9mXMMqQxV86neSLZ1yvU0Kv8DCBcQABoMNjM3NDIzMTgzODA1IgzR1WDuOUGnrndmd0Mq3APgXEa2sqo6XtJO4LrOnIW%2FxBpPw1ypAJgGClgWzSFImORCIZC197FSgeERKwZT3mnEgF0BfjmUT9enPNhaymcG2819Koq4YYfS0slw0kplaWqnEULYEFsPLoyaFAC1p%2FXETQU5zuSrO%2FKyImpgKWUpL64ZVhl%2Fu8kYnnskg5J1Mclvnz4ubT1uqPjVfiTtBcHSV%2FzQmvvMQBM%2BAFxYuU8yOVQLvCHiuBVUo668bMKWaz9kyBy1MSYu%2BYura0eaJzRyOX1Bi7wNm7F5m0SvG5aBBE%2BKlDZeHoatna%2FhVGFjiwAsj4XDpdTYbmKQ3pMdsktTIZCJLUTUlqvG7rlSVEep9PWvrwIwKfkuKguTRk2HYjiDDyCIJ0lygEc2kHccc8NH5pzOfEQHUoaBYk%2FYAwl0J060nlVj7LKBqFSqS0De2YcvEgaHINmRvopSk4fIA10LQWfVrR%2FHTIAUe9FbXuwt6Gi7957GOLZzSnCJMQp7BDITBdCGHbMS0nHAUPtqXC73GBBYO9X7Nr3C4%2FZLIAd5EzzjnHkUR%2FpxPWOFf0Zy%2FKMcTJBV5ntQxkftHMU7LtdcKsKMEfmn1eEBBszZ59J6b1RhtOZsLQPtBBRTrpbgcQ6g8O3f9ehppA2FXDDNusnTBjqkAcC5uecaRt2eTYtQUsyvIbJZy3D%2F8vXGS3ZGFs6Kyt0pclQs0yGrK41OLQLLKZI7K9NIoC9TWks0OmM%2BRMqaleQlUddpLWhhFJ49XmK6SStjCZu%2BLMDw6%2ByAmNowgrQra6XVV%2F%2B64Ukoti4vwRYQa0mM%2Bz1TJdSe9wnjL7cp90RTniDCBSnbF2W24ILMjCJOcxsA75OXNKXecWfwsUAcV9u%2Bos77&X-Amz-Signature=aedb12dda01c5b5c0898a61cfb8d898de63153c038212599ca071299b1988d71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
