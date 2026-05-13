---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKI2FM7V%2F20260513%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260513T015535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJGMEQCIGvtj5b%2BftVpNj1VKQeRt651f1k0PntkDUPj8VXej832AiBaFe0o08iakcfa6diDpOoEw2mKGndhlno9yNcRpky3Fir%2FAwg7EAAaDDYzNzQyMzE4MzgwNSIM%2FaNn2iQUium2rfx3KtwDJP1X%2BNJnZBUBSzZbQtbQoRAMLHKoNWs4gzaFGXaypyCB2U3D6oVU2ZyjQv2NPSuJAcwhRap2HEIySTffNBI5p%2FWRRKh9shTWuIoMPyYhrISC4wZP%2BOIoXrQLm9%2BDcs5f5BVCVwuYNqrXJDYT30SJft85js0NyJ8jjmzD6H8NdTE9DZaB3Nay7dEcSl107IvC2lxrmIn7grooFW7cl51WgTy8DSZiRUdj14fgok2ElDfr0jP%2BUbXZTV2Br4Wb1x4532mtjMJoFrPsXcoPrb%2F2tA7%2F%2F5ZQa1wL9GGS%2F%2FpnF5T8hy6Hv305zA84MahqylSNqXEyMKPQUARvDuszzaBGlbB0aAoMZX0TSyUTO5IJznwMeiOJcx6yOL0jbgNP5FRiYlNcbHFMqfx3kvMTPMB24ggE91sFRU782Uq6ddvLAE4EMvMXpoxwOn2U%2FVJ0EnMF6MEF9xdY9MXcF50hHHyEDxP0I8XNd%2Bb0NokbO3bV9VNoDMM8qA10MeQkL3EV6YQl70zxONr2TOG%2FSCw%2BCspr3la7nJN5Tj97DSCbjdVq3QZ0E%2F84DJUs742eWITFv1hf2zrEfb1t2cpJ%2F0Nw91Pi1qMT1GNBloBw2oRqvkx7myQthHYd8uLsVngQGewwrauP0AY6pgEE1VBvUqv8JifM1rzJkV9NyHTDC4r%2BLQ4tkGLLjhJihHnUFjPUc6H0m4gpDlhIvZQpxrKZraLFG3qEenwXoCIOrjCJe%2FuP51%2BlwS3Ymz3JKGmC6Nmju6cD%2BJsLDNqDgPmilTqKdeb1dliKD80yi8BLs6YCxMDmZ9hDJgNrqSpAY9rHali1zYhY4Vptc66aEOFxB1Wh7Ihr0wfoEUiVpGgyWeboBTQk&X-Amz-Signature=22a994494ee1bdc269d0b40e7be19134d9d38f907e294525e62afd8d8a77d4d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
