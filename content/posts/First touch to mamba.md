---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVA7UCLY%2F20260513%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260513T192956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2FxeIZ%2Bvu4wCp2aF3yzSTcNifYT2f7eX7u20LmERo0VAiAgPjruKys6UDjR657HvNYoJWYFvOIj%2BycfrPO0TTXDFir%2FAwhMEAAaDDYzNzQyMzE4MzgwNSIMgF%2B43ZW5wKUeay%2BiKtwD8OxhFpD0Vfg2zY5DQylwTiBqMI6r4f1vjj4sOWS3TClPVqotQEN4%2Fc9nnlZvckIf9aknn1ti9vacJhuXB9SpYqsLBf0kLOzTQPYvILAnGOJyJtq%2B1Dg2fsj5YJxXhWSRDuFp1%2FEmeQJUXx1P3M0pw7n1983dsH%2BIxte%2FUt1vgOd3uQKjYH0Y1I5%2FSvoOco%2FPpLRyKH53q%2FyX2rn4j8zRDo1JGzBeIycW%2F1TwhxQTwFCJDUmpj6W7XQkWiXpj8%2BMLseyfxcLeJ%2BlSCgzJPOVAWndvrpR4D2laRDS8E5bP09p8IbtTw6%2BMo1XpRNJcFfw6zERLmoEGMq7KlR7TDoL4gzWaH1zawjPoihT5FI3Lo8HJmhI5EP6acaRYLGGhLB%2BsY9d7TiOZBk1JWdjo7rc%2BhTsetMZ5tY2ht7JLoCbegwPVXcUoK11tCJExZyuMPnvzhO1X3n%2BGJj7u3DtQz9zZxhlmp1EyjxrmTW7THuOZ15rwJzWKtGNMPdIb7g8wV069stomyJJGT%2FnA%2FF3%2F%2B5xtGuESbzcJeGMex7x2VMB8ah4heQtlBbf10BD%2FSXgp7gy4KaqDYy4Io2YxqHppyT%2BatcieLCEjPSBt6jkTxn4hq6A98oJrRh1%2FLjPJTCUwi5iT0AY6pgGYQHvhtknCsZaOoAW5VWkx7xRwAqb9r4qeXV7lmVviM%2Faq%2FPQo6EvJnajiB4RBOp7dG1qOvGpzHL8or12MDRQ56oNYQjZrGqmKNr%2Bc8DeN0rptJcZFw23fo4sVQCIeR4kOOpRpuqHplLQltjkFM8dOy9KRP8g%2BJmlpzoOMJ7Q0L5Ki1R0%2FulOkpTtLkW8uTXeQGeb6fekbmxMKemF%2FYuOKhqC6zbG9&X-Amz-Signature=e97f4c008e9dbe88dc159760b164a288e64b2074aeb681b846bb152040f23b2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
