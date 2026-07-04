---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU3O7H4B%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T145755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJHMEUCIQCu5MK77LoyfZy9rgu%2F1n%2Brvl2ueOJfCpuIDzuKZ9tDvQIgETx1HOsXbjZwF1SLXsr%2FgAkSiCcSXT%2FCuIC5UQ5nQxwq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDDHUUKh1FMyaGG6giCrcA8VwIPDpUb5pKCBc7k7oKHG%2FYGa1CYQoJok2smDM7ECI3wHfezIEO9dId6wpx0HdBbAKw1lYZDMvZXD2rPbs9p46k85XyW7jWPeblxEuKlugclmAA3edcWUe8a3U%2F108oe7M5I3ZIQLym1HeYB5LRlAAl1nskS2O99FuhznASFtVcXIJxaNeUUkjaet4p%2BxoASmRLb52T2ZI5yCDkjtn%2BrcWQtx3Hgryf946ymiglyxUfoAwaqiAI0Kgfj19%2FOB5ZKCYeTHGK6jsPuytcQDOV0ZrNWEM2jGS8crz7y72Z2WPU0aoiPvk6K1abiytUTayNZi11Yp2UCj4neF8aGSIThFV9nQ%2FeGDe%2B5%2FRtzdpDHTHkduwNb8PwDJ3DkYj6rtC1SDdRX%2FYlR5JdgRW%2BoTEdDrDgpIqPJwX0ltCtDWsrq56jlR9spukcHnwmBlxFtya%2FSVXCh4KzwNFFULblpkKTPUwkoRSvmomtT%2BtuCk0mhALKpNsx0WkTBROGlYrfE5a8RTGGnsE1jv0qkdzdgfGomzgGJMx%2BTJPwEs0PBw381prCBw%2BcyxtMKyiYeMTNAsw%2FS9SgJ%2F9uHJc3ILk1%2FmFBbN6aiR%2Fv7V3TL%2FYNqVwD0c3svQOHRyzBM3qpUN5MKCgo9IGOqUBM%2B8E3ufjS4SAO7qjICCfW9kNSp9FOlJpyRF8LShiS1yngfIEP9Rar7NQV5wwWwFr5IxyocEA0cnkau5Ri4BwM84q8hWNrGR612m9Yb7oz2Mm5VcBEei%2BpRg3jtmjzsczcqiFBYuRoZRl5BMK33kEag%2FEGFdHEoZVrVlJRg9AiL788feMVVxEY8gAYDwDSQHNc7oCQ6Qcyj%2B5lnSD3X2%2Fjb34vfWy&X-Amz-Signature=279e31ac88f6041ba13845e26f590a9f723aa3a2b645fe13a1c5bdc02de98da2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
