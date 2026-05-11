---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUYCBKHV%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T123453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJHMEUCIF%2F%2BPok%2FlpJ6ygMoj3YApEVv5Zrzu5uWwpE5Oh8x0uZaAiEA0wr032orCQsLvbC3DiijEJRic%2B%2FIRC7hwiKLO6LAfjIq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDJFfT2Z%2FMxt0c8KbSircA932WR2ecYo6oU3vy73S8GOYpzhNFMQ1Zcash0xd%2B%2FvZAzvTyS0W6BY%2B6JqBPIhXxNO1tgd8cPONWm%2BdFe4NYMe2TE1Q6NACMBle5InMKQXBLR5DN39zeqY3QLlVJuC9HLi4PdPlBQzGgdy0We2wDTRnvGJqu4kILBPgDX2RC6%2FFdiN6cbDRndvvnxFr1tw7M1MtXSAz%2F3lWSZ0fcvRXfH8j1tUTY2%2Fd6VbN1FNGmgcilv6bpcTCvczWlesn8qBYoSNHVoOEo4od%2BO0e9VwnatQ8nTYaonfae05EJilPc5N9sySmYWDJWtCgAcqii%2FrbqhZ1gKv3ThAcLVabLobXPW1fLrpbYhD8at6LkeUyDvKDrN%2FH3upku30t2Av1Kjend7fyyu%2FKVzuHJxNxSc26AdcYbbrY1gOW%2BdjVzfQeayY10mxCRGOk2Dond%2FPCFvbSzD2pY3pAKElSx6AEXgm3TprqikQO9gTyCotKnugYMcusT0Hg3xpBYjO5b2dUTzR3WSjTeH2NYARSPZvHOM7PNER0aA7mYZpSDmYOsbsvtT%2B%2FkhXCQ0VVZvN4xb6AQmmMXBTiGSxcr6R5Qrh9pHQYL0axXfqBvUlQ0N%2BM5pjjE%2Bg0JrjDyVj8y6zb1DkhMJWIh9AGOqUBUAERlAaa6CIAqEi43U6U4JKbEfW%2FZyCnu2GoxgGOhURxv3ZOdxwrOJ8BIZSfOJGaRfYkNrAK75z022%2FKVWzkc6Aktyw6N3HvqYML6N6feJ7AAl4hbbhb7Ve%2B869Yze2HaN0GqYRo8D0m5qDTABEkHpTqEDWhHAty%2FggAhnjnF30DFFlsZfzE8uQjZWc%2Bs6ALkSUBly3zET8EeFEczjiQvVoIQHsI&X-Amz-Signature=d6556843b11e0f5b348537ece05f01b76fcff01576e7a73a4c034fafbb065260&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
