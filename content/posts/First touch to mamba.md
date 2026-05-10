---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YG6R45L%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T144429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJIMEYCIQCfXpc49TBbPLAa1AAeJ1QaCdI5jYLZCF%2Fz8%2BdFRTZQEAIhAPoC17wurE5Nr1JDAU1BF%2Bbhmh6IfZwPCKL%2B0eIal9DUKogECP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwiLPZMxagTfHe%2FTA0q3AMwoeY70lSBK34r7iOQcEPr2DsK7d5qDLAYOh5IjxuNpmsod6jjXF7YHE2cCjH4rp%2B292rGU7jZ9ndBmOVXHnwMx2PjxuPsIt3a%2BEt%2B23BCvdO%2BhZUYrl8VsNQXcToCY9xBKbOo2WgYtUic7BraHTel4jF%2BfFwNlZqjuuTCMaQAhX6HGgsfdggaDTb3hnt%2BUmG7%2FqUWTDzHKN3Ax8QCLTQVsV%2BfH2Xm3AVa0Tsy3%2BYEXh5IPVkZ%2ByI6CZ2xfkgqtLC%2FQMeESAA2o1tDGJrs%2FwIwxq%2FhvvbgOuXzWu3K4KzxVfgyQkJiXvTmwoJRICVqPurewb3VZ%2BIfr7qBPfm%2BKoTdviM1WiStRntm5HkVAbxwSFm8BGolEjb8pKyDN%2BNYNr4R6Z61s9pXNKYwlZj%2Bo%2FzjVCLHHz0bjobaZ37SchCtGyyXWeXTikwj37UrBzXE%2BaOOu7k6oVizZIxag5%2BZFkO2FBe0v9QO7VB7e%2B%2BX99mRw1RLY1v73mFKgFDYrzFaRlPPkWHmLIPPax%2F8Bi112pNV%2B9kPc%2B9j%2FA3xG2o92BRzbpsVfkZ9wwcP3G9jL%2FbjG2BoMoyU0%2FVE%2ByhOw6EjPHptMA97YJpWOoilEz2Ey%2BpjOqyYB1jzJIvLVN2rMjDK6IHQBjqkAe0ag24i%2B1T6wdRT2N%2FTE9KNVoWNGsfax01zXsKI3pjALDwSGfhulMvjUJcsIIuTsH7lAau8KmbkhQijqKUcJHen8aIl4QtQy0sGhcP%2Fr0wOrvY%2F59UwdXRqJvbXr7JzcbT7QnwIJnIBS%2Bh33bRoDlSaGeybs8OIp11AOiagO3ruVTvmpXfjO4%2FPyUkAEV4c8VvQ3f272FuXuL5rJ5J1T%2BBoJFfB&X-Amz-Signature=9c7430d16bf86dc2320f731f9a8d6605d0057d431f8c6889bcf8bf3465334183&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
