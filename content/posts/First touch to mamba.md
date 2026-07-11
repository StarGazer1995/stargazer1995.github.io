---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OJ6CVZ5%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T091527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJGMEQCIF8UlBm1H1%2BI5tXDI6MfnE%2FhXYJKrnp6Qbh06KWiV37%2FAiAgG2gEzO3sq7R3H1L0JILL59l2HCn%2FGuX6ryFNYArC6CqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMb7HSHR16t%2Fi9Jwo7KtwDrBJv7M221cg6yI0v683sYc4i63m0sWxe8Y6FEFraMdOYnIklJje9XH%2FNBCxpFLFh%2F4a9ienGURUZwc3eLZuBTLhxGlS6xgrD%2FYhMKJCFJXQIyxc9vtxwzhmmr1d95gUMKZ0HsmkqHjcx2QqM3Q%2FJNJUjyk86QUQpx3wP%2F1lwx695rUEcEMUcZbM%2Fqg0f9NCH3qxiSgd%2BA22zCZnOz%2FXr1CcQe6wSMNLOGaIvTl0%2BD1jP%2Fati230gouDUXseksOvn6uCk18i1CIBc45HYrPpCIdCKq%2FDGyCFQfB9T6mxx1vzbn4ViDOW%2BBFPRIl%2BoNuDAe4pYn4ihY4gVoAAPbewPkiibshjJo56TlBpxjtLkwKLwUK%2BIZRUC4bLZ%2B23b01JicaYKngDSdEuZJeGQClKhtQ2jddFq%2FnmtKPisiNxm8OXlLPpM6BaGIrFxYJ5E7jUOcKo76zpveP9mNldq05%2BrXXZpCFHWFqDCiUKWH8qj6HT7nebNiF0J4cEUD6%2FJbQftHaDiUzgryt5aj2RY309gSVA0drPBkrzsl7T9UTISPfdGIoV%2FrOF327S0iMuUbWm8t9rrD9FqQmkoCosnHvTy6B6EG37sJ8RoEtkQ3VfWYr1Pj7Q9KJUOJaQhYvIwgf7H0gY6pgG8dSzdMstf1KmnfSLN4j4IjbrclQ2i11DN7iCXyUHgVOZjlfXvbY107JGMO4uswZNTsvlcPS97uqdN6PJo8u4HJFFcKco0jnNrdCplUQNqindkqniAf%2FgDrtkhllugeTMOf7IKgoB5ZOFmj8SwltVGjxL4TWrRIz4zoIJ73cg9Ek7%2BG2wuWzGqZp7QAlDJkfHccceVoO9CInKBgAThg19yc38t2YGv&X-Amz-Signature=21b3dc058e5a675136f9bca3d20a8327f748dc60f935d94503d46759b8e1c9c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
