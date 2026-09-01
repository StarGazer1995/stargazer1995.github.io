---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663D4OWCXL%2F20260901%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260901T065515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG78AlxybMlqWWrGeWn4VDuNwpenMzcgr5hH5QKfNfLtAiA4%2F3eEjnZcJkctF7VQ16igVuRTe1ROEUTHemom85rNeCqIBAio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRvU%2BfFVpaz5Wv5sgKtwD%2FSWQntW38jxhq%2F7%2B37zOiclJe16qrTj5JBv%2FMME0UbPMr%2B7ge%2FfX%2B2GcQ8PYIuQznVrGkDUQMhpdOf9sRwhay3b2TsbPsuVSvFyoC9gOD3lTAkVvBdVieatsiAC6UPu72rSo0XAePAw2Lg16LpEO9HoRzN%2B7Va2i6zpAWJ0%2F2aEz2Fj%2B0J2VB32Cv%2BNdJD21KSRnh4M16ASPhFiodJCMDaC6sRGMo%2F%2BEaEdo2Fb2I%2Fy%2BBTO%2FX9W%2FB824Px6LNqcpI3NqBa60la4I2xtjZvvMiZfWEY7iH3saOM%2BViVyxLwxDaJiY6zSFQ%2B02BfkZ6eA1KI%2Fu1WZLTuMaQcSw16rg9BEz9ytsivcftE%2BMwXCQ8pWNJZMf4mjE%2FCPURFC3BmLtO7hK68uHBFTvlSSSj7JQF8pwt%2BRdWRsBRH5csZtE3aHX0fFOUlnkSqA4grvj7M3%2FB779XpfaiXw5m5KcbLJ3oTfcI0wxYHVSX0bdUP9EyMWms0lPWT1oKXBJcgehqV71clPUGjdzs6Dlg0iw0SxmXyvVHGhjZUoA3Oq586zDtq1BypahPUZRBpfSYqYd91oj6vL1KooWGiaa%2BB8Ivs66dNekeod603EuXPWKyJR897mZos%2BGxvedjPQBd4owtevZ1AY6pgFYXK5EjJ3PKpW44HzXb%2FG81ZZxW%2Bj6vRqYrAV5DHy%2FNOeJFWwQiWluasCRaBZUNCGtwBevARpS1rmKSYRz9cB53naXkh%2FaBZ7ERN8yDWv7ytahSDQYDe4yyYhtH0kYJghRhJv4RWqKGQY4VRHuIXwHUuhqCxeme%2FfMk1ufMOWf16%2F8FAZEVTCuoMLqR28yGVlf2S9RN%2F0pdsNQzgQPl6%2BeaLslFIEO&X-Amz-Signature=b14665d7a8fea8914fab97fd0b0b96b38f5ef063636b49eabb9b8b607bb3989b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
