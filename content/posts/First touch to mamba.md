---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YE2JH5X%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T050033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQC1wMXtPJsJ5K04m24O9Lifww2yJD%2BgdT5JIUAoJu0spQIgLrWKeX11EwDwypUJn8LCfBQxvQRaHnbS3ubfWO5SbXoqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEjZdUaJwrfnGoPyuSrcA2E4o%2FGn%2FPbdn6yr3mm%2B4%2BV7xaIOISrXkl7eENEqlA3l1PByEJ2qf%2BD%2FF9UAYte1vtFJqtap9Ff2nxHP3mEIU8D3coin6zU8eVvqroj%2Fb3z%2BCXp%2FCd40K%2BW%2BGAj%2F8sJywe2xdDPACFX3MRhN%2F%2FkSEpply8hHXMSSSyzqZUGaT6MzMNp9n1OoyOOGbW5DyAKC609MwG69r8hjw0h3XLGzrv1%2F532XaBqlL1wU00oo2jXZBHAlcMnAHreuBpf2P3%2FvHN%2BhOYov3fD2lMMaNd%2B8NfYgO6NvV7SSlLEEPmfDUm72D5YjYDwxElJrrFZZP9WEEf7wM4LSf8GGfVjyPqOovZVHxc28xJCvMV%2FyktFG5pnLJlDcf8JPEC6P4EIzCYeyIXyRgeb7NKrN8wBH7M8fCOn1r6Bl5S1rlmvx3iOotZpRUdLSylmL34yUqfihsnN%2FTHQ6jDtDZblpp6G1FuuXqOGnEG%2F76mJ7vm2DE7UcLu9QUok0raMS%2BhDZufZN1atsYBkx%2Bs8C4Bmnz2X4UznXjpcBPka4dsWFUd0F%2Fb%2BwwR9%2FqVJDrHQURHcSLDeaoEU%2FrTGUnNaHaXm058iacVdNqCgLmZaFU91m%2FW6aoskF%2F%2BWGdNOWnVx23DNIBjtUMIb1%2Bs8GOqUBCz6IwsmBoTc3Msr7dyRMrOZ8iLdkslNZM7f1pQciWCiVp%2B1uHFr3%2FsZ3fsFc%2FX6dbp8tTPzg3QBocF729CjVZ8M4hUOubOL1jFksYKgs%2FY6KSwCX6M6nBaXC2BLhfxJlAVJHaTeuTRHaZU820O2oyorPf%2BrfEp0Q8B4jIMZCj4B6sAIwH28NWZoVLd6FOTvAb%2Fqb1PoJuCZuYHQtUyE%2Bb0pBUHSK&X-Amz-Signature=638b23c2978275ca713d1c0e7beb1e6ab8080d0e0d34907917375f1ac2072175&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
