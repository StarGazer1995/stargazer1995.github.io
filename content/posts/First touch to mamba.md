---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWXCPWGM%2F20260831%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260831T155041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDV7jw%2BkqkLlp1QSfKTpqk1oCZ%2F19aYJfPGO5c4eWm1nAIgR7aAG2goHagadk3e3%2BRJtNK4VjqwZlPGBHFIwRf66vIqiAQImP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdJNlEnz1p6wWoMYCrcA7mzdC9ZIt25PVaaDv5Lo23GrVGrn9CtE4WPNkq1lTglZawdz5aGLBLkDUf5ZUaBjxB3WvMBABjUBRKL3znD7sPQrKLkcIKVyjIGd7YGgQwHM9kpmOHuhSnMcMsKFfFyJRFebRjpAn7FwyMpSXACxI45mBryPCo9tyfQzgacA0xEz6N1C0NuWEuB7r58KULyWVKG3yYM86CCtSr4vHpE9Z7q62%2B4hfhQTm1trznZeulEnTmbZ3ZFwYGEWpVCHsAbORCx474GUcWdgYxFeo%2F43ofW5GpKcqotWR3FWoBRYLVcGFNGtUhb%2FUVIySgMptQqbJiD50yYsC0fkMXR4nHmY3lRk0Hg0tGOgi%2FvbY82Q5BJjDpEMo%2Buceuo%2F%2FVW0gUjs2Lra0xQY%2BBaF%2BV3P2v3zYRKLB8IMthjLwBEQZjz1E5d%2F%2F33wO%2FJgZ%2FMOxRBdE4xmD32WJqnI6PI6vRP0uXNvIh7slEGES7KPICBatOUbeTn2DAXYJqKg81PiJnoyjxKYlh5vQHQa1mbPs2B6l6LC171RXm9gpSZB8CUZRlWa3LpA7E5%2BQJ2bMjVToGcg5%2F7CUpRBRDPEBWtxsjBBJkw9LpWbeZfdC7K9rXFKubu78vlsZgs5wp5TLmYoBbRMNCq1tQGOqUBSlDTMuJehuQOdm4238RGJJNhjzc0pRUrX1hPMD1A4C7gu5bcEuEO5cSeKTq6I58IymcorNLtjrJGE4sDTf%2Fd6A0N2TWPVg0vp6e6YB83yFed66PJIHMS7pRfNWKy0Bbfyw6mEwp3%2FO%2FXYjQiFG8NnkwqOweQhyYMP0rmpQRulQyPFjvCB%2Bj6o8E58%2B3ej1pmMYJWxnIyGYyxXedxzn2r4Bpc7%2F0B&X-Amz-Signature=8b4031e16b3567e66c0acdba42d809eb357be4cf9bbed31720e289b80d128e08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
