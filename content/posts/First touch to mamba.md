---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSND5EK2%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T221432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQC8PPAaOgj%2B0EiQGDzETA57l62qu6BqimbUfautZTgRwQIgMVWd9DcbksCNyvK5HhKGsHQ07ea6JOJ7IuDoe3jst2sq%2FwMIDxAAGgw2Mzc0MjMxODM4MDUiDNjpq0pnaFUdOs5NKCrcA6Zsv3S7ufelzV7lxaAtr5F1wcXDkhA6PZ%2FtaG0u4oDhAtBBaFPR4jZQn5NrNk%2Fj856s6zElAdRmJE0%2BCk3wTuiTXGbfcJReqagwElQBRcUBJSW7VQLriOrmVnuuxaq6bPa5lVSraMlVshW7woJWX%2FDf2LdMY%2BOttr88rpZ7HKRQ7nKsAlkNG56S%2FKMeNkkIeB1vypxYNhwRZA7kpl8rFu18oX%2BJOTauyYY2g2yCgTqp2MVU9NI24FuT5GgiBZzl8p6ZZruRmQBfTSILQiMp0VcKDBBrYE5AL1DlIumF%2FOG0lyQsc%2Fwzm0ow5a31%2FBPmTCNZnvvlSiSWEN4Fiuf%2Bk4%2FaAUXV1TU%2FhcR6ABRuHjw1BKnIptG6zVQORmWgcSQGBLnT9JnU0vCI75MaYIjUaiPy9lpLmDe9PoovsvAjqpMlpf%2BSGvW00furKaC09F0GUlT2DcWOt5YWkSYRGArHl3X81jrXzzP9S4WC7Y8BDgAgoX%2FmlAHBR6Yu81qtzS72YRGL2UAFNvcOR1Z12AXFCOGBAIbMcEG%2BQSsjY46eZmyJ1PpI2AIeBziw2VZ11YysdYwm7pQQeAwvMHRnPZc0AOyPbnpjgwVdPYQjyf56pHVz9Pl4hoX2FEoggB7YMOSVuNQGOqUBb8EeUlPR81IqoZxAdttHOHq2C68RbeuNgNaaxm9QvKKUJ1e4iDzINDtm0s2%2FTDEK2%2B5fBtR5RdrLz45RxiiQPMHQI%2Bzi16nxPDRrmGZyrcvPmJt0Z1QCpyl3SqgG3d0aShqs2huFHdAcPvIIUTeogoKb6AfjLERjIv1TY03zffvwvBCLWMvG8BIjvuXxzStI5YNbi42qydkR5b1nG0gPad%2B43juA&X-Amz-Signature=c124171225438b5d5b4d2cdb9bc1ae0e3451a6f7ea92a360991cfc392cd40be2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
