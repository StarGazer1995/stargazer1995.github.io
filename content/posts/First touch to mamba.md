---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664INLETZY%2F20261004%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261004T175518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIQC4UMK6pATSIsJm0xkbZAA7gKxAH0bemEVukcGpyIunHgIgOqlc1x5JADQfAkqKuCTq89aTNIy%2FD7GoYXfmVfuzOpQqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPvPWH%2FAO%2FxLRXC1SircA9JPbjb7Rme7T9bxUMqYCoroY6LQY%2FnWQYMm2sLmAznfK8ZM0WYSpXDPnzwd8vxbWVtel57YXvn4iWh1MuOZVF6IlCW8KYqUUtDVlR87Ua44p11hhnIgXGxDzOx9svgR0R1qz0QLn5fWodupApsVqZgtfyXDYmltjhjNf79HrMM3Ke%2FaWHTVdeugJ65%2BcQYtd2aZ%2Fwe1hYfUJCXoRG8RH8YuKjQxd7%2FZX6G7KkpzvRRgZTQCgJ%2B6sPJ5gRwqCO1MSO%2FGw3Oae%2BFXHbJsF0gWmFyf5Q8E2Y86m0g4CevC5jNHGNn4mLtJlDt42EGVOZVs5WWUek5%2F5FLoTrf6OKAw6gJPSw9Arok2gIi0ETjZoC0A4n8r3mjXT8meVsno0ace%2FOwVRN0wjZXmxPYVoA2835Fxv4YaQaXtaLKdMFHqrcmLJrumgeu8elFDomGToPE%2FZcJAEWc94B2yDtCGTEhVaAa0j%2BXQepHxC3hAQ5b1S7URuyQDbmG6sLdQXaHGuGkYoqTgwtXAsTnZtfSqaVre92EuWMtzQfEOeX1qzx3xYu6Jz27SoiNNqj1k9HPZFyb%2FcyDNP3nvIzTm%2BT%2FNvLCjOEfAZcAx4AcsPRbKrhE%2BNQaMqbpG3p0XMp4XpAFJMOCGitYGOqUBZok2ZdY1%2BgwkX9BhSrtXSeFXj06fDN1Fy%2Bul6OrGA5oufrEj%2F6n8joL3qDPEOiR32ZSOl%2FNGv23XDd1Ro%2F9hFmlr8u2MV1FjO2TYZijRxBLyxCM%2B66daOriXwOjTsnkJQdf98vr2sTedqtkgguTYQk4dw7Ga8qi3Je6bXXW3fBSqPPkFDnUJzlvxeE9ZyS8N4G3OkNX9ob0nOna%2BdEeP1UNArLzY&X-Amz-Signature=c23b155e74e2781714f5cadf753ee773a30970bbcf747bf6f99825a670924552&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
