---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VITUBSGW%2F20260829%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260829T155155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDU0F98ZrKEDW2qpESFVXMBqiGDegb5DhA3LYMn1rcMBgIgMRJPnMFhalMbwn%2B0pK1NqFmhyAs3LDT3wf1TlU%2F%2BNaAq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDGc2IOtsLqVp5wsQdCrcA6hCK5cUCoy286%2BJLjXmthqvM7p7SskFyqcaCS8OQ8SpFR4VjmjDu%2FKjOyr1PDeQlIsKRGLUbsQif0I1UsHbyL6Z%2FDXZ8uazYzhJZo8U75D1XFD0wtYMitNcN1hceHMPCFpjgPbt9kFRij5l8DTWaCAYygRfjDSUbCHDlteaKb0zZnvQXRL2tnbuDxp0HrijZZxt0cgMrn4D6C%2Bzeteo8vQ1wRYWsmH%2B3OjoIJBopsS4PmrSZBdo9dorkTuKfblf6YReWABVTOGB6ZmtvZlZaRISEUnuNX8nK9c5WSw%2FK7raKaI2h7eBB7IFmAfZBcbXyEhwzYfeThw6aRD%2FGWhoD7Zw8FDuO6WwAyeJtKRGt8TLG9g8al8%2BtkbdJVOakWg646UGAowZKX%2Bbwz6eptqmrxz0JWJ5b1GIMWRkQD9yetFW7sbUJLbFj5yyx8FNVR8FtTgnbyMOaZbjNA1%2FZ9ZJYPA8eWUM%2FuWjWOZ9%2BpWh7GxnHvZdDE1qbXdJnAVmVjhyhCyehZKamm27SQBFf2tVwyDYB4cZx0kzr0FAcAkbDmHcJmX%2B73MluaH4Dkj7lPOnz6buouhZjJnDCKqK01hTWNyyUeJOUahrP6EjAyPB8Hvx7cdzr98Gz3U0spF2MKS6y9QGOqUBgAHnbEiBZdYcHdB8LUgvwCe6gc02BlAmy3JIOI5VflwdnAUJzklG4GVL%2FhIAlKZWQzBNJMSWNzHrqHdWTn7Um%2FnNMkXKs7Iz6Cv7LWduYw4OBfP77nLJZhKa2iPta2AGYOPftalj8jz7UAHnAd730VNzXclp4pLBEC5IWpRTUzzm5WQHbUcsCWtKUxsMfXKkyJFf8bRuMu01nsGeVEgC1JSPovaR&X-Amz-Signature=fe479e2853bf0515dd8d3ee95ca9a3d66b91d8c9cb15ccf5d4b2a4c9988b6eed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
