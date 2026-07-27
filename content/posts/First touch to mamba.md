---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZOTO4JA%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T190837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUM738VRkCTLkpbmjcpaAvNEfNx011LyRj2w1cmRc2GAiAmKoMS7ppRZRZs5pKvLjdPAWwbG5p1yJu9SRm9vyDmlir%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMhnTspPjsujjtojIEKtwDqHXLblsRS4olgR88a8RyFoGUiLtw8wOK0bdw6IaefPaOsz1rrIUmCpCLuF96H66B%2BjERu9lhI0FJ407U66S7zsQScrEK9uzzl2Ulw1ACXvy9hHPmp%2FPriNFqnI%2FK7c2Ny4bJ87r9wKp5CyYzc1CrTN0ew49QJ41ADuOBoKkW37DhDkEE6%2BITyvzaAeICJZTwhdPzWXndoqD6PHIhbv7nM4kNFPVDhasgaeKzAn1o78UJbdfSZaZ9D2Hrc7Bhyqf%2FnIb1DqBwLYTZz2uoVT%2FFqxHouYrn009jbI0CPqGNluWGXpeqLRfGVA5ClOatE4WxKrQ36bpiGVJc%2Bfsk7Tr7nxusysLe3tW35lMJli0kyauw07Ct2%2BKIyOng3%2Fl%2FLrYdMRv9hCT9ODOr88V4TGhTJtZsZzUAZJW4qSDREURZJ%2FTSDi1R8gI3jFcGJItA%2F4lO%2FP6UNzeShLZ2ob2C8nOGbQYtlGasjdxynH%2FemeLhssvsZJ%2BIFKTK4xhLCs8PfYtwG%2FuHimB8kVASDn4uDX53%2F14GtkyVQ6WKXNVP7M5lLE1NMvk%2BDflUsels0sSlVnkCQshWoGPGn9w3%2FTJL3D68T6fAImnhn3WHHm79x6mbzWsL8lahp6embj0ib2owzsee0wY6pgFTaOTgsIsr1Ft4ZJw00Kqrz7xWLqaKynZgClYG5wLnr0%2BQcbUfSFUVnkkn%2F2tl%2BB%2B16O%2Bo%2FNTnmNudHWv870RJJkpoOA54nVgDcC%2B0L%2BgqfpNUaJW9QrfMJmNgspZ2toOy0bEmJhop6Yg1DkZVw9xL7kGY7Qz0fG8oRZ4Bv8FvciAIHFTqs%2FLh7y8e%2B5DaaF854HsOcYmmTXzyQVuS2J6R%2Bp7NAv55&X-Amz-Signature=7535e190ec899c1db6279ed95827c63ce10bbdbdadc97e0cb78eda8bf613e1e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
