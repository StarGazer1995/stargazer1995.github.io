---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VAGEOKL%2F20260902%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260902T201407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIC89LNugjHLbzK0pAZhNxqFhHo96hIz4S9DM6RXCUR9cAiB70fbgwNjdqsly4FybJyHt3L2x93o4CQ%2B2MFlbOl2OFSqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQcam%2Fj3PKqI0RHULKtwD%2FCGT5Hh0TI%2B7tEPDPJiWdrJS9A6QQSByRUy1yrrzi9j%2BI1oyvzORFSofkJa%2FsKpwl3Fjv%2F9BlWtfx5xI44XRrpvQ%2FqHePn7SLpjgKKOXobKlqBR%2BQEfJCsE2JAbOAUqWQR1St4x8oLJJ%2FyKqQkzduA73gfd65nRA2wSFuaxgCjZNfGsojR%2FSiyFuonTNDtrFUfjfJylQk32JooGtvoi9b5YNMJpyz%2F%2Biz5QNMHT25iIIEgG%2F53Stf4a1F%2F5nM6uNxZGTl2Jni4Q2ZEgQFJeC8Q2bF6cjtZF%2BrramLUQOvXRebc1HWVvo0PmE8RLKMZTk%2F%2BABeUj5x5k%2FxFjTNdiI0JiGDU7Xdb%2Fk2gCehR3XabOMsP4DjzZja%2BAVPKUGDyqAdO32nbh6SUWz7LYMRwi845mclmvJI7PXvlYfjblR%2FB5Pk1lBGdtZy%2FcZSIq%2FIcxSp0uVNPBJS78VRmKKItLjYZ03%2Fh7CX5mEGL4OJI%2FbcqBUCDNPz%2F79Ho0iD%2Fl1K7toieE15avD63utNfyEbJDk5cfKfeiuGimVCWc482YTO%2BABXboXukTmG1iIgiilhg34laWg40ghAUO8nT4BTYtK9ynnDGcUESUG71j5SMnXO0fNiQlDHW%2BsyCHyLdswrIXi1AY6pgGN%2Fz45LilTGqKA7piz8PeRM%2Fk5vxLfymQ7WZiZ2iUil7jcVW%2F6COIPXtrYRgnBwnSmXIM7TQFvI5waIk3u0WKASoDwUwPOV6%2BTkJGz9I8dfkF5T1t8VB%2BvaMS%2BQCnGUYXxQAgkqdhyG2tz839ZhBbUXmwT2bp89dR07O6P2Xw2nMRWlHO%2BwEj7vTF6ekZIc3KJyG0CFX8zEOWYZlf19JVD47CyShtm&X-Amz-Signature=d69148700ede146e5c3447f8a7a329c9211549dd6c20a15e584243a29abb6981&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
