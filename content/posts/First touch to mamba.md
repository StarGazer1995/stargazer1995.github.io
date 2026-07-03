---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCRTC5RW%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T171103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJGMEQCIASPYqYWbC3sbmj1Ir7LFR3pOGEnxV25YsBZocE1s%2BlkAiBH6tb0kXNKSawAYM3wPLi1T7aTx7HmiuxPq078YZpgRyr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMJ44yIrNrcPc64ebnKtwDfqo9PuDSKUl5WLF4fuNgyFly8Au5gDovHri2cuE05uIa%2BRGw6bSxDkOQFLjrOhmfvrIgk3zswQt69vrNMUecGc3ECasgZvuoMaE%2B8ELu94VMw62lcvf40oE%2FybK%2B95YrcHVOBdxfeupFUH%2FOa1fjHJU7kzEBlyy8%2Fjvz0WHJbpgLcgA0IahSESUTUXIdygsiJ0S2e0uAvTD%2FmPNkl6IJxLE3JFAT2ASa6R8CvcaxRFbJnjaNNGVzbiDT5jY67DkqTWZAd3IqE4695cuEZhaHkefHjzAWo0KMH8kvSCPz1X%2FtmWgIgyqrNdlQGTdWbgLMNP7odyHQsp5Ke6rf7gvRjNucIP833KKY4CQ7SuB8DVf%2FRNEdYxCxPwieAM0%2F%2BVKwnHk6y8AepnqYvw2uWyV3TcYxmzK5B8qorYrkd0aKibYT%2BrWxu4lM3APFoaWjFT1dZQUSqMLgzgU6vNASp9v4e5XQ4NtM6Bl07zwAyp%2BPE3pcbnz8lT5dtG%2Bzso57wUJhgAKGq2ImRY6JIBjulKV5UGwLFVoic14u4hH8VeiZ%2BUQiZOavz%2FeXIIqr7r4H6eN6pR%2FfOXin6RnnZdUR%2FtzaJWsXTJ73ONhcCJJg4MAhEjR6J84jWylyTCd%2Bsdww46yf0gY6pgEuqOotFs00sapTR6bgR95Tn%2BvQd0C2H89IBRpSn4lPMv%2BfKshZXmyohHFLPl4U74S8%2Bw5UiBNL7%2B%2BVk6jovH7S2Am7erWuD5zUMoYkEEy4uCR9WWDl6vvVU3CwfUtv0U25phBhjYspU8NUTFaOd4Hc4Y9S3ixsgM5rAX%2FD%2Fbq5Q7TnMvb1wJBx02TmCZs0Fj6pQqUMzR%2FOrF5HBu91w0e4cUxAbU%2BV&X-Amz-Signature=b4b73a6b392e65662390a971331dfde1eb588975bf66276a64a984c6c1a629df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
