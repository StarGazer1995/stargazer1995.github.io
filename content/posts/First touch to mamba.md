---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V35TCZSH%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T164353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIFx7jbPm%2BXvg4rEDTJLIy%2F7nf5BDNHMlOsavWotOR7YfAiBKwxb3P4Qn%2Fjdu6tFZamiJlyxURi2Dv97DbFNKCIlhhyr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIM0iy0qIr%2B8m5s9vX%2BKtwDb3iiV5buash8FyMENBXyjOUDWQJI%2Fj3CSrP3TH34mCMX03AudfAAl%2FkzXn3lWvsxyaLAlo%2Fd5HX9b2TMh9DSrXbt0TaG00BZ54yaKgqJyPrXrOOq0IOcG0uJ8wsrREObJk7UO4XKpUfk6Niv7QshH4AKd8mVROVSLebkUg4iX8wAN%2FFcuMb51Zgw3JST8zuSCKM2GJVYw5Lzb9ScGD6Mgmli%2FJCKcm3WD4A8xsqfegrDjDt1H1T0613esDzJdJ%2F%2BJGXNdtS75kDhxQWKUfw7yNQkn54h1EZBPvR3xsKrzH90YYrCPR5q6wTITuLig82NANnHBdzB9xY4E%2Fuo3fE%2FiPqZ2ahw9zUM4d%2FDzXE0VfnppjxLs7Qoc%2BcLXC5L2I5ENUVX5MKdQJzBnLtGsBkB7KSBVn%2BTOYehwCYUOb6%2FU08lFvAL2BB7qzd%2BxVDU0IRAXy84m7hiUCdCU6nqY8QNE2OqiktK6oPBr10Qfp2Gk1UysM2EFxVrJsEQMlRwojG2T07MsId9URu49sJnzFkYPYa1Ux%2BKestcq6gbNz7W5W068LgOPdvqjDE0x%2FLCj1EP1AIW9bAByoMZO2aQ6Fx9yrPRIkzy2oiPdogUUwqf7GAkkGrIlWXrTwTuZmEwzqOT0wY6pgE%2BwiRy8cGCYOjx955JNyTpwfwjdAI4bzVDqbGrSf7UxsrQl4IlCr56y7r%2BCiubZrTCx7LdFJsHxMq1oRWwVoqnemONoRC3ltkm41Lr6%2BX8vIvUcReT6AF9zTnvDxrzgOut0LvwjkzwXEWt%2BPotIC1yDKKvTeudZmXguaq59lVDrhpmWT9YO9YklpAEZOErwSLujpjgI0OSGjHvrxpvr0dGZHnM5PkH&X-Amz-Signature=ddb5f3a0061e12b4af59ef51234c0f91f301f298e5dda727c0fad04f3193c1e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
