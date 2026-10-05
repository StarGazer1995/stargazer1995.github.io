---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBB6LF5L%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T232551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCwqbM%2FpE%2FGdfyYb5pVj9EAnp2ui0Uey128wBpDyu6L%2BwIhALiJvDpGjlQnXfd9m3D57kBcRA1Wa3ukAeYCYqP3mcpkKogECOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJso%2Bj%2FdOAN1D4psoq3ANUAehJumgHJYdyggAk1RvxJugL%2FsNb7ctQxV61PxKjkevW3DCs%2B4zapuE3n9AAn3UCnkpU6YPD0xM%2Fad9RAMlLUmbCiJbcoQCLJYi1WwVZ0Nqlwl7BduKkn8cMcsDfD8lRzszlAnOaaN1TqxZHAQxJmUaBhqtPK2OUOMMOC3S635jPVY0mflkJqMrYyW0Oj%2F%2FbCcFB%2FxXHYorldE4AtmNnrefhBRKssi0jHzwx3De51tQLzSpN9y5qkGD8Q3CvDK0t%2FHVP91Lc7SQAfBV9D7e07wMCWESxWR3z%2BJAEJn0O5FfMKPcDCu0Qy10C7ydMumohJ6mA44w6N65%2FH%2B04FP2zlPmwvMLMRl1rQug6LNY20ksJGTwqa7Ltg6%2BXliBgNLM0AlcUw0%2B05IP%2B2obpdHJz0tKdeKwJxNTh6tAWkAKnCR7g2NTvl9%2BduRCOPb2ap8jXNRRY%2FW1tVkEh7E%2BlVlnsYMN%2F4iXkyG4Rr86Wiemf2l9vdCkwIKenbxhObR8GqNp9rLWj17QID7HP22Zg80F%2BN5hHHvR9q%2B8qdYSTTuVARFYNi5McA8qwbJm%2FyKFzZ0fQ%2BkhQqm50WCT1K1X%2B6WDrjsrJo2%2Fy6Z41KB%2FBPivIEwwiWNLPX8Zc6JndZDChmpDWBjqkAYk38PqJ4%2BQzk2BJXbTGXZK0PSKq2%2BlAYyh%2FM6W3j3xXLdbxdZP6qaxK7S9TIxf49p8vW4u2E3sESsq7coozojkmkGSisqfxDUPkipLts1EztZB8ymocEKu15WXr%2FOEIeUmlJKNX8TU8BiMPIBSAStJvFYcsip9b%2F01lLGWYG3ivNOWYyQMQVO%2Fa3lC9oHPgm8ZSYWUcSnyCZ14tniL44A0gLnqf&X-Amz-Signature=f3fee772fc348576355f4a3212aa559e5259300abcdc812fce4596c67443610b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
