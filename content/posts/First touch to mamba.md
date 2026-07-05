---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Q45BATR%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T112242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIGw%2BHNLvIubIxZsz5p85KhMfBP5tMllVFctXMftPoOWHAiAvzhJjNA6hiCHVQeRKRtWRD2EzEaPlegpw%2BHhqpPuzfyr%2FAwg4EAAaDDYzNzQyMzE4MzgwNSIMIYodVHrC49CvUEwsKtwDizThPkuadgNRHZAGnSlNfluPOoaUQGL4s7AQh0pq2DndSG83MT8V83NYcarrAjMI%2BRauivN0yJRulj9sUpjhyTF9tqzo%2BVu2cFpwOzGLBBHjs6BMJ5reCX8t0oPlX2cCmcBnUi95rriykQ%2FYrXUvvPSYepXkLencvssEOnFgzDpuS%2FmTaLRXhHHDTh9qDdoPFa%2BR7YUuhKwjHe%2B0JzGLizDSozJn%2FdTkk91bXbU6kWGHqzcEUm%2FOyktKJjvtu1nTiWsEQ2q1v6KFgNXVfrFzIXP6IP2Tfk5vYjWZiwDoZvS3fGBkkh0XDiLIbh6S2TU5KNttUQlOnI1WMk%2BDIRjM6FYr61VnvN3pfAWTOG%2FTPcHJitrbYw0U5H8mcPZUWj2GgWGQLN8zCm7w7KNbeSgP23vxdQ4BpOJHQaegDnlcwuV23QgXg8x6cczooBM3cLWl%2FZ1lLcmN9NgVqP0sZTUfJhz1O5uospk1ydIDMusIptbQGRFH9d3iolVouC3MN%2BD96NxNJ7b4D7SLjLGqhnhPvqfosbSe4ukkXyQiFaD5%2Bkb%2FaZemyFyiuYgBJgaK5dQWiNiM3f09V0nGA3qvY4pQworo49lN2IjMbf%2BHs6nRgcgKYEjIuTAwqG3e%2FRUw8%2Fun0gY6pgGaLy7BNGZmRuq1%2FCj14zoigH12cPj03HanJg7TnsBn5zVMKAoUyPJl9t3ecVmBnpsy%2FheOI7ik6F6QcJk07DNhoZH8IhRquz59mHUC4lTPSJe83fDNzW4gv%2FLil78A4yr1Gilq%2F2zUgNRsYVfH6hvjAK9b%2BHwqKK5V5VpHYLhOg0sLoKfI%2B%2FTkZAyq6nDLgZQVUjGMA4vYETp1fPYQva2cKp3%2BQmPU&X-Amz-Signature=636fb10c074fb6258208ebb4640f5480d309f0d85700ca6fae804d210a5439d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
