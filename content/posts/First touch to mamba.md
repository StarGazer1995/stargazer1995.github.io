---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5MAK3EH%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T224926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClAqw6cCpmaU4VxqoRo%2F3KqVEgDoxq%2BqBcHsdggPwxDQIgF7j4%2BCbjUSc%2BvzEgrs58Q5ZgPTDneYwfbuImmunLeNIqiAQIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFIEvkrgIyEOQcSUJyrcA%2FoUUVYLc119KOHje7sKG0n8vDFxndx6DUdseI9Auo1OSd5sBA7O%2BYtvLdpkeyc3wHWs%2Fw7Pb%2FAqLnIE1Y%2BbHPcHsAaoq%2FQcqaFIdUgKAfTq0oqyb%2BNwE60llrOHaCENwjMiAgHKM2MQa%2FHcZiXbp1BpZoPNeYn9zvhNq1ufFu2kzBdu0PgJCetXXM7NvaJ%2FARFK4DgRrxnPLDeBRnxjZ1b1dYIz8BidB%2FopzbtzevJJ153yenxjlbk4de%2BCzU3juIeuN8GxaaPUM0PNoY9%2FUfB2oKvXiu4W6Ws2pPMiijE8bVJhyjh5Hnn%2FwKOZAHqfJ3vaZS5nw05YO1zj6g63PTnyMFqBC8%2BEGVhu%2FPz%2FzwotXzaz0kZ4gVLoLsH2ljh8on9f8g8lnkPaCSWAnK7fVEY7WZ8UXoHxMAimJrpne7%2BHv83tN0fJjIpqsnf5ieqQ7iiMYWJ7p8dCjFsX6eA2O3tGG7cXDdS%2FUp%2FSdapnAPJlEkMSCnAJWzogepS3u9b0q7LGUli2ZOpq9iuoH1XAUDr%2Fzrgn3hURyN2W1lhQ7akYEBMI6Hr1csPqdnwbtt0SplzbxdT5iMmEGadoCAU7F2eHHhqJvlekT5RseXxH%2Fq3Oq7mlZ2EDZYeRbsTMMKO8tNMGOqUB164kp2HgkRVWNZNhJvmiMSH1Ovk2rl8hylehoP%2FYbDoJOMG2bZ4XPM14e%2FK6USFD3PVlIeiHhkg%2Fo%2FcyiAVEH1154ai92yIajwUz38%2B4oYqnLgfxdyDhybvCjs8Uj64k06ivGrKsUKy7pVLysSQY3uQrArxz3XehRm398hhRuYIgj8hmASth8HyjYnQNDwNUXouuo6PsGhuSg3h1dFgCPRqMN3j%2B&X-Amz-Signature=81f5c9a192caacca72488a2e101cbf990ec2b0c756de797fcb1a9e379c501368&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
