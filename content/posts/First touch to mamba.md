---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LZNJXLI%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T203938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIA7TfrRdvGLGruZifBxctF7uDzbGdgOOkCBQ63FxwZKvAiBKR509qRZw4tc%2BqDp9hagErePr1vsvLXxNH1Um2MzeBSqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDYQV0Zr3y2ZjVtIYKtwDgY3o6mOkPCbEID5VkB0W5iO8DWl9tg0Pp1%2FHGvfJiiZIGU2q9g5EkVpPY0ZqD7g0kjI5Dkn3FXe%2BVE8dGDBa6iELfrRPIUUMJSS8I13OsnqpsKlanqvggqUIiv2LujeX8i0ejcFct3Imc4nknCuami5tbFBEHzjeL%2FBsthXiHRkUSUMm4LFwIxBGzXcgakmXRiGKpLDKHXr48u1MYa%2Foyu1j6SspBgVV3z%2FWYznvUvdg6t7T8nhTzOpr1%2B%2B4ozWJ14BmqbfKysXsLLaXekDcAlEcOjAaaVfcHpYX1WsDZ7YNIApUpHMmwOW0XEfTbng2UdBJfd7rwVTSZ6UpZ7XmFjKI52s0O9K1zvvaPBE4wiVdEOkdkI%2FCTZ2hVUPp0EKuRt7DYhons%2Fg4pAUn%2BSKXu7eSWmZCq92O4l%2BCa89ViQhF3rDB%2FNT3m%2BYHSw0%2FxK8li%2FWh25UmA0Qe8V%2Fyxymps1ngPf%2BGL86zlcVtZSGncasBJUWgQlcuKDWkJaWQMt2cWjnqwoEhl2bFBjMWPwsZ2kBKEAlNFc9MWM%2FDQIrxz1QgRxxFe4CKhiaFV4C3tTnjVB6MK8oy9cUsNpUqITTymUAg1hVr6oSZtBo%2BAzo0OCOY8gqP7ceDZKysS9Ewnpa50wY6pgE91r%2FRNiuWayLOivGat6yB%2BwuNjzoeWpUYN%2BDkjn8Wo3n9TSc9DlLO6ncmgsygaenKi5aLLKDEdX8MPfrCPDyGP9UPvOX8NCZUA4ZbvOO%2BZZq4wljeSlpJOppO2HwwVszFiNH2l5IaFRGxf%2BPTlaXXK8VxFpfGq0hUZStbXNLyDw9kz56gAVYyHBAhcIczUQ0uOxTbvENs3QpwG4yi8Jo2sO1dfL0o&X-Amz-Signature=4666e0212f74ab415db0f4d929cee8510aa8bf6eaafcecddea398460d0eb61d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
