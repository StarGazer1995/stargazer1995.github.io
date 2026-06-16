---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIVCIIGI%2F20260616%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260616T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBmZT1KQ4C2tYN0%2BybO6dcQZhyia%2FmtGQ3PYSfwHQu%2BgIhAOxvhOj26aE6s6K2dBvBFks5PDoSD0pdmdU4WCWNrtCNKv8DCHAQABoMNjM3NDIzMTgzODA1IgzLb3RBG5dLe9MrZAMq3AMnyPVGHE5EvhMRmSUlFjW2oE4NWdHS%2BKHpS1JE8cm24EIo5sNFvuZfMySchJ95XKfVcsBRKOvy%2BU5Iensu40acmebTKTF14l0vDEPhnqCy6eXMAs41Hi5JqhCv1bQyidtIDrjYKOA5GGJtpJTF3LZMtQKk0KKlUoalI70fQRwyfx0nVIPSt%2FgWCdjfVmfv2oI4SWEZ%2BwFU5eQBkCSt6TC4dh4WzYwiDBTf7beEhXl3uAufVvRrX4kCQJWX0WMyIOLWbKbTh1uUocGnPW4NBzgMcFu9rckIm3SgDsPZDuiQAcRL%2FxU9JYeXPDlrABsjAwc%2BSd7vbqK8%2FqpK%2BKSBiUNcWmVdXyYWlE6w8qVac1nwlbOFJlhNcVomBZjm7b34lw5fHq5sa%2FNxkFCQSgLXehBmJyqMuep5sqpuvlGUGKtvyS%2BzzhVhzY0uneEOMt8lJU3syI01hlA22xu0l7B5ovhPH8EjQAwhiBHlhf4rc%2By3VjcZL2b69rLKddbAFZjkufDormHj0FpCzAgkTcvBBJp3BtVZ6o9e4T4alh7vJ5%2B79wYbkUj4DsUoT5gbSvDBqqCpPHhhvIwlWX1MlnI5%2F6KhfWlJ4T4D7zF%2FO37N3z%2Fz2OAr0IUClKueVuHZvDCo28PRBjqkAd2WL%2F5WUwY63QJUD9GxyjprJ6DAsTirPu%2F5L5Y0fvPVH4rBIZiVbrDi2XnCrPDs3wvApVwgSkWIiqc2YpmWHZl95j9Wg6sUbzHCRgfWnMsyOdetubQyTcT5siLcJ2C1Dh7JenVaBFyhI5P17hDM8BGaPYBE3jppDuAkxcdH2pJ5PrVOaH3TcsU8Zle9qOc4eybNNz%2FPvXhRX9dPFlyeZp8MjgOR&X-Amz-Signature=9eb072c29d3e39097c750419119f3574ff25c07f32428aa3e63cd2d68fdcd10f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
