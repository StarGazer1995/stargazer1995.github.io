---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FKCMPWV%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T020625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIDl0hrUPSzMSDbl%2Fra%2B408h7dx9vSErtJmgkmFzmRY3gAiBjFStu6NF1%2FE72o1kt2mvL5AdFkDHkyvz0HOKaxYw4BSqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAgMU%2F8vCnL7ra6BdKtwDqxVmcMdiXE46vjSbfsZI2xnL%2B8KyZgaLSGsDUTf%2Bw1nQxQ8TRtEn3HLc5bQH2FRiSzbqzo72conx9Aikepkhhg%2BbkMHNeicmTlnUaRPb9t5K1qqjLyfA04t8UTJ%2B8IVnUZnIj6hI8teKIPLD%2FBK6%2F5oIyp%2Bb0n0rQh1ijPyyFw%2F0ud7YmFptHfpKrxzgviM6JI3Qr8WunDUX94cwhtsNOdrKuFzbbLhrDlbEjjElMXWzaUcCX%2FCyGBkmYRC5GBNqYGi4rYobEfPdN8Rc5ri7lpCjPunV%2Bo52tQocMiXjp4noaPpD0EqSFvEWRDrpX7S55SLTJ3DtSk0g1XbEchnc3%2Fq6dSc8hnJj5dpT64jrsJwlMPQUBEUPiWLX846f9ga%2FZsnVXERA5Y6ZFjpQU13%2BHfLYu750ktkx7NpsgkeYrrCACz7l%2B7ZAbZXhJwAvhrOzXdknvSjDPycD7NeH8JL56MX5Nqmt5kfvekc%2BIPdI5H7trS2URoealZuzf%2B%2BKUC9ZoY%2F7ozOl3Q%2F8oQIMdTn1rYO1uUe5w0G9BUWqpNY8BQgDH6sjZ9p7aWr7c0YFRL1U%2FW63djEH%2BcAOm%2FXJAjkN5Pw%2FXj5GiU4JnNK6FOotU0sZ7YahR%2BouNsF2n7gwnYqj0QY6pgFWx4mzCct9BVlDQmUAehns%2FZNLcTQIvCTIfHPwQWeC0CHFaH0rSuSxFIdBpS6uxlS1KkXGtEoxEBgFl94BZtNIO09IyhjHmpdHSjTv%2FpdyiqGIGjrd87uI0f432boMyYNadk%2FuUtZD5feHhru5G2ZVp9gaeh3v6yGfJgJaWEAUp9l%2F3Rl8Z7SIyQpNkXpkgCrbPGzRO8ncJzcdtNyPq%2FiGhTqO%2Fpb9&X-Amz-Signature=9d4f3dcd09b216cdafba5859d7e06594e9fa6e4b514c90bf30f4d740476e37a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
