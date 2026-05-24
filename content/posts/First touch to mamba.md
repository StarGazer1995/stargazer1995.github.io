---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PBVFT6N%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T224607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHI5Fe6FKmJYW4CJ2ytAPVMKT%2F5p9HxXXwRdjZwa%2Fo0OAiBSOsnAlaEzOq%2B3HQ46%2FEc3Cb6rlc%2FsGsqi3Gsq5j2tTCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMh%2BKyMVPAf76J0wQ7KtwDfqkxa8FS6CgXncNrG%2Fa%2FqY6%2FZP81WNLYQaoy6PwuNmko0cvjS%2FPzbBcitVatCUcR2kMKP89jaO4Mk8n0zFNQeQavNNyUSu87gn4xknDtR2XP2I2dJup%2BME9BOGCrBe%2F4%2F8Y32mYn58v8Wb3tVKNRRRV8p3RyluNbsVYhaovD8WL1JqL9OUchQ4vzgxIqjIR78RMjsdOgqj3NcUV2fwbrwPV0qAMZlh3jtjoo2swL8%2B%2FaEyy%2BkC%2BaMfL9rJYuWbuIAWybfoueK7WJcefPDzS70Pdfm%2F8A7mcf6qKT0jy55ORWWDd%2FskxRgwPHx2F7vkug5H%2BTzgAGtE3Vc6yb7rHmw1Y9Kf0kBcvffQFkrv7vkNoGwkCejPNUP4xIJ%2B0bNwxYsFad%2BU6mzX5xrzPq9Qg8XluZ8wwpm4k9VQP2FOky%2FhbUe8yOrM0MlhXAl90sazetE55g4RmUgH70q9%2BF1v0NcV2g1ZPhmGvF27t85wji1FC0a7EcoUqqWWQkz340hoPYTLr4hy55X3kk%2FDH1mKvkGRRcs6H%2BZIQVi2R49%2FjTylZJqOfUqqj9UUPVJJRrzugLdKqeFIPVOyNbs7gXof1cxTtuHjKn%2BCY9hqx%2BYQk%2FWgdPWXl3uUeTXCHjCNow0KbN0AY6pgHT6vJ%2BdGVVUAO6Qa5lFUb3TvovuSMeW7IaaJ%2B0gA6aMa6y7XURnjX3x4dEoHE1T%2FwfxOyBDkeRH8X6da82cPd4VD2XYSSgDC1Rie8TyiH2Bj3qPp7TEHP%2B6zKQY9setJKQy%2Feinq1tjwaICkxj1r6%2B64zapHDObf55dXGF6k0rKIuHWRzjuJbY8OvNOUBTYwxwZyNn5SPRw156livoyJRZicSSmZil&X-Amz-Signature=f5094b7df508c1d94e3d275e60d75d24bfc7662c95e77fb311f3c24a8ddc1831&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
