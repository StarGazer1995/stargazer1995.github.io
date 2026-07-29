---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAXFTH3P%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T115324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCX981dnH0pFmDUn3urc3wwIJdCvDkLkiMFvryFKGj3tgIgSYNcV2NpWwY3Iv1XLJMsAQB3mZL%2B%2BdbCA%2FPfegA2yUEq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDA9pWDvWhUl3%2B7Y5qSrcAzoHdoGOKQ%2B7zPMF0%2FBNmuOIlkvBxiO3i1Qi5ADHuxeaIvga4V9EdvhiAjyislscZGumGL3KAP8scEYiVHJiVvtNIPLRcs%2BGdsUan0jfCh6Pc2J%2Fd4Z0BP2eUnnQxDi4fxbuJrXBtPC1UpDHbALSUE%2F3o8aPX7%2B1YJbUatHpaElL9Gxjd%2FgW%2Bc%2F%2FJ3beOyXTf6%2FzjuewLD5%2BGkdN90SZWCNlTr6LtnYaGsUTRZCH3%2BifeleFEF4ER%2FgVzaJ5BzNhvaPcwADWMJQeulpvoJ8nfOhJXoIk%2FuoymORMWSakfKEEllznJp4CN9oLSk22pdynxqgR3MevWMNKfVRMIdFKkU%2BCVasyGCVIiKB5Z0uVzgVKh%2BK7CpKnRec%2Fso18815EGUoCB%2Fc8pUXzGaZ2dE08E04VnZk4P%2F%2B78hPVvs%2BM3FW2a4z%2FQJEEzvJY2orZAuslqqv1dHSts9aV9n3AAY1NRGqrrDJyI0t4h1IJ0e2QfX1FiJigmaOMZMuOGWX5v83EPxQX3dSGR4YpDMY5Qy3uOvyil7I0BEhMUzGaQGWXTRF%2BkjvRTZnXR%2BqDQpsnoVupo2kjBVFeruJH41KxCRbUFqllhqV4f6knD16xlAD2sRC0wRdB6zvM7Jm4%2FRJAMI%2B5p9MGOqUB956Dv%2FhytkVhzZvOJCPZS14N9VUtQ1weNzAcdLa9zD5DoKJce%2Bjb0FVSrrA7E9IORT7JEpH3s2lXBrqH4it9x2emvVNyXAUfPUoOaH43UCQ9zz%2Bgn060D0EF%2Fq4RTI0sImO5UL9Hawb2Rj2OKNHdtxbmCO7a8vTCq4pFNXvIvTt0%2Bnw3hUkZmecRx9C1jj%2FEe%2BeHfK%2BqrB4bDtx0KrjVA%2BRAljAF&X-Amz-Signature=221bcce39eb76d720527578addb8b9d8c0662c2881901427c8475e8d6a7946f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
