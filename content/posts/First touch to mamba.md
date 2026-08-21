---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDXUXXK7%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T025356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6gzypmoPn8PdujOBeICA%2BSo60tasZZZ7z3HR180OnnAIhAJt%2FpF%2FEPDQYa9nt0easnWkpShyia%2BxeuwzIB8eg2MSKKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzpsGPoETW5sJPaGM0q3ANs%2BJskyZcvDoEP3XSuKQYLaMizd60dgvYxv01fCTYY2YrFwD78ezCHYBhi7TKqyAJHUgBIcuqL5vZajFzoHKhkHQef4NcsNXnoSbQ9vkohqwkVNXG1xFN847b2UzlIBsCg4wMXBPqA8U73dvgGCydYjJxfnst4n10cNdvUB89c7LV3fFQFa8w6nx7xvbg33hHIMMm3q%2FRlWH%2F3VLGseeH8TEa%2BhGOIXYL%2Ff0afBlid6mU7kG8fUDQ5Hk%2FwWUa%2BC5B5TXTVe1HAITKCW%2BpOJKi2SUZaNOCugL0o5nMbqwSqgBnRR%2F2GtDyMbJX0R3u0eB1K05X120mJkL%2F%2BkqEYTCeEoxmDHerHHV9Et9wyo33jhc4IPHeasheCfV8nJTarpSGe9BYz9pd5Ppq4cmo79%2F6P8R8NRTxM8%2BBW2iUR5lS%2BLO54Cy4WrObtmJ6urd0sgZLiomHf3uFAbINI1KXbv7D6VcsIpbc5ie054YXjv7d639q8fctRHv7U2ccdl%2B4nwh6HWs9OuvPIhaLwSISqbPTxm0GnUEwHt5aSfzcB9FhIyu8TFVhkxS%2FiRu2%2B%2B5npmzbo3eqL5Easeso%2FdIjt4w6UO%2F%2B0Q%2FOI6%2FiRgR9EWedyAypm6iyKqV1rjZurKjDU7Z7UBjqkAfzyCk4JzHOJU68Y4rf%2FquxHIijOxYmJgocsUhRqZuwbC0VS1nGIeEgzPCHNJJv6TRfQb5vCNt0zTkWxL4inrOjfTdeZNcytniXbwE8RUhvvceciAL4ttxZKv%2FwI1%2FHmYJfCasU7kQfg33EnvO5q91A449kNFDj2%2Byypvj3Kymc3VgZfEJ9hpoKFJpM53SkBNteYuci%2FP88QbeMZWBa1OpttK6Nz&X-Amz-Signature=7df0543311eb1f93b838aa128c1efa7d649496ac7f84790c66df6497afa5a7bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
