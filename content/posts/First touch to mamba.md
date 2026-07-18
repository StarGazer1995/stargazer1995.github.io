---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VERCKDFE%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T091507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDQoxAYojExFdlh0o8u2jWEAdGrPZpBC3a8r5QIF80DoAiEAgbZO5WnN9dncrnorE%2B2YerD9RfQD%2FQS9CDi0HI63Os8q%2FwMIchAAGgw2Mzc0MjMxODM4MDUiDOsA67VMBas98OnIwircA57ix9ps%2B6RPIEqfA7b838EjerQMpeM29UU%2FIU4m6sLU8fvYRbEbPm6h8L1FconFCIc%2BBeyiAN8dJXvpkF4h%2FueM6wZh%2F9ijzfHQzAQbYYLiTkdaOfdu316dW33hjNWXoQj1KPpSTgN5za%2B%2F7D9xTVFh%2BwgPM1o0n7%2FbdJt6JDAoa8%2BCB470rLUud%2Bs47YYFVtCVdATpjpIbK7Dn7bdrVS4MLopQ8hdFWDselIxLy7SXH0g3YYEVyLNTBqxEzU4Lty7Jolg3qaYqBWj6qpDrmabIcXw0uV5HaDPJ44MGfx0%2FMIKJxiOOY5fxZbBMbLtvziEEqmbCxTpZElvbTQ2lnhL6KtcKIDazwc0BcSalAe5ouLV%2FaB2NP6skP0prmQ7bWym111dOhDz933tHjyiEb0zQAqZxWLUfcCPWTJ%2FhVPnna2JtixSF0ZSAUHa2qfJBe8Wady8tPqvv%2BXr%2FpjYccix6NpHaHI6VYlJCUjYep7Sxnop6rBE9bc972pT6tVm7Vw7nzkZhnEocMchgU9fiu03xE2jvJccsYpt2%2FSqG62zyYtivB8cyMiQ9k4rLvBQtAAsvAtAmIt%2B5x5DYpnMT6WkE9dsbdrl2OvTcGQItFggj0Twja%2Btyu1acJ7hUMMbz7NIGOqUBlWgDTXrlMFvDiIaYHZiKXAGvOnMKpOivlHj%2FR5aT9xzi%2FZEKrq78bJjLiG9%2Fz7sCZPU3PTVd7mGof7LEF7vqb3AmgR%2B0Dk1vF0OxkuUvBi0TZkZngXcAcAMpnJwO2IUdP62HUlc3GcU3Pt1EFgEWTv%2BZuj0mcUgJflQKGnSO67Bm5SBXJbVDylaUjouNuoBkkuBfa%2Be%2Fg%2BTk%2BRBU8u7upJv%2BCZz7&X-Amz-Signature=91a2dce89464cced427093c59936c8f0a7746538b893ecc8bf38b6939789b2d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
