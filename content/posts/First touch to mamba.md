---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZDAKFMR%2F20260913%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260913T065437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDzPACBA1f483yKvFK3Zl8reAdlfcM1OPYmUtNcYGF%2FAIhAOxIJsq%2FN6mjlvu8TD0s2qe1T4%2FOIDIhMxzwUZQwqwYDKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybdTR7BJKaK%2BwzM98q3ANarvWJBRVKu4Bah4eKnJeXtrcHVsq2uMh%2Bhw31aCVykSnRl%2Fy6%2BJ2Naig0O8Uwvan%2FPwr2sg8ZtM5DtUhkSVabr186kFOHDaHKcQpupysYN8WYEQLZ2JUL2mXfF6kazBe8oAaiZlNp2BNMNJN5%2FRuy7UsQEvgLLEg0z4qGVuutjqhiIBUVHQ%2FymHZ5V6OY5sPrprWVyfaj81te%2FCFpEJ7x4uIwpA3%2BFSDuOZpegLg7On8cHlg1%2F0L2Uswq4kDrcO%2Borp6c%2FMls2pLdHSyqNYFR2eaV934V%2B2Oz6D6dwshAsX4GU7UY9W7OwXhAqpfwtXbACu%2BzBoiaxWDPYmP5dKA6VfvzMhSbawJ80RdqjqadQwe7vuK32aHcUmx3%2Bf5ZZMchLlO%2F1n%2F5cY09zINn6sCWzHlU70x68n6%2FK4SJo6Q1ggL6pkgcSYgUYmpAneXjpgvkRdEuNDgx2RrJGJcmgDUdUXBqLz%2Fbt2Pf9bt4Q3v5wSEGdne8fMryaIh7EIzQK06FkzzmE88dy0q7gqsdSbziKEva%2BUk0zoYR0LTJuitNK1mfDqu5d%2Fc7RX6iVEAaGmql56mu55%2FUPFgzmVG3i5dzH003PJz%2FsMp6gnm%2F3O%2FIZWzxtRKKNseGdeDzoTCF0ZjVBjqkAfg9lC65p5X8%2BrNT0e6IdH291G4tPGkxuyhviXwPuyuHTEwj3YDtQ%2FpANH2rjKqHC%2FizQk13P4kEYg%2BeDJ7%2FPT89eV%2BwIdeL61wzY3QNlaeaRAVdVHpmn2PofUT1VsiDkNvM%2BijkQTLJhyLEaQqPIOik%2BNQ8UdJD6dR0hD3n24brCkPVpPsViCUXGtCVxyjfftaFkGrrgzQfo8KTUMLY9Aqcp%2BEp&X-Amz-Signature=627132e4ad8507410a8eacff1558ed6800e1cc51d7ea41d5d5056b2d526b787d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
