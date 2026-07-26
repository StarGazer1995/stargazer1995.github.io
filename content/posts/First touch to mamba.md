---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667E2M4XT2%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T111317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQCW7l%2FLBl0ZgQbwIpmULcTZsRSIuwXQ7RDaAkYA%2FwgvBwIhANbO7IOx2hUcdmcKBVM%2BfJFkt9Fat2y%2BH1BwCqD95cp4Kv8DCDQQABoMNjM3NDIzMTgzODA1IgyHJRGhCkKLNX2NRD0q3AMBy5K6mXoLJo28UMctn6s8NHCRFa%2BgHQdBEUBZj3ltvy8Md%2FLqCpwczSP92tsdP39Xsr2Y0MBH4YkcWpUvp1PqRPDZ17hxQb6HWy%2BBxjZe19iELpE7Fl2VtuDGPodn6yespUyFfjHvdEjQiD5PYqcI0hGwZnLIUK%2BJrSwBBhtsmNlPDSQx8I2j0WEtvc1JezvlTpGT9cwUqKsxoPI34VqvUyU%2FCOXBnsY4Qck2dxGirKrMe5NOba4H%2B2G54V4Q0XCAtWRH0WGT0NiT8N%2BbZxenIpkG4dwSGV6ZnbDyx4iNz7yHok42h10qV06e9BzbiBq4laMrSiuNHwX2XpAabPYElQ0%2Fa7V63WwApvVXui2J8P%2BHx17NZvdCimF%2FqJPeHphBLDGNGAOjz9qC8rKEDmn6sG%2F7KtCLTeMjAObdKIq%2Fm%2F%2FoHwmvvXmhv3fOs%2FOTDtSd4tzFUbqqjahSLJiuvtpytnmeXdpYE50%2FF%2F3%2BXJ0FeBEzQ8agbLviGd5aBiLWUBIddymH4Y5MagzQCbqUvftW7Hyxi4eGfNpxGdiY7aocMaJwBNS9IsUG8clXkcc8CqiMTUS7mrhx0qV8EVkqKo4uYhzNWz30pzNHjip0EheaXAWdK9zA4RYmnEMGiTCWypfTBjqkAcLfFrsyxHm9KlGyxk1CA5SsGcKgNpIO1Mbg63wtYdEsWEXi45nSzaGaLt3w2BgG3sNW7U1i%2BEyuok%2Fgd0jnleAxtG%2BBqIbZ03FjLjLJWlv%2BvOPXmmxJIvB9KRgFj3zX7VEok0it0a%2BFvwZIKjkuJPRQFPEygRQAlVs1PQDL1pjqh601tGvyBTWj%2FSAgdgZyh%2BIWu%2FHvOGeER%2FtD2HbwyaHw7%2Fu%2B&X-Amz-Signature=dc5f2f5e6a7a2306c9b5d64b11e8452a183e8e3c8e785eab2f8275811ed5c8ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
