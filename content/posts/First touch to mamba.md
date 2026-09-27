---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHLOKEEJ%2F20260927%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260927T223914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIFaCLv0uB830IDVc%2Fc6MZW2gRLgevnJSwgwyn%2FeUJlv0AiAD2wCvCXZbcGYCBV1YzL7lnxT8OTXxzZM0gCtkakYkVSr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMlxqy3MBToMXD52yPKtwDq94T2uAJ0lZb%2BVejZqBwGIjC4dHkLiK2cEz37nbVnY03o0aG6Jh736ITS4kIVvCm3SS7zYc%2B608zhgU6gkoH5tSagZctUNPaB39byLqkz03bK3a3CE4HHj7H2ANLWekHiuZrzVBhUv1%2Bj5HCFm%2B48QZwkrs1Q0mDnWFIVq44QiQCAX0uF%2Bq0ZJA4TIdHrQlX58KDe05mKn%2FGPzWLFgrZiZnVx9UWTY9JoAqw4%2F4pEj9zQuPPy4gwt%2FOD0kOCGx2ICEel8cr4bMduJAt3iKOkyvpPjiMK0WBZAmd%2FZ0Y4kY2z0%2Bi2snH1%2FqMWrq8Ehou8TLqO%2FD%2FoUSgHmUhfzqsfU8O2chi0o1gKhS%2BxH5JotaLxRIMRx86eE5MpL9X691HMqXZSedWR4bk65fd7l7%2FgKk%2BjzIgG7zezf96jf23howD7StYjLRaxMTHPLpI3%2FNm7qrBf33kkyLFJ58B5SmLtgBJFLyWIFywkqUeeQMAr4l2EL1BpDuZfMC54VKPJ%2FVmO0fVx5qnEixVQQPNZa44qyj2RSX5%2BVweM1Yr9%2F02KQpbSfw2J91%2FDOYHFyHIV1qaaKFnBWgW%2BUIglwmu7ZIGrRjyx2SNlSxAFB%2BGolgzH0uhfFKs6s%2FDZBMS60Dswiorm1QY6pgHnojlt2d27vfr8xG0wC5toTyunEekOF2sil3yN6QIfcFvBUV3vjMtEemL1wbWyJTf%2FAfwqch%2FMjH29YbL08lnvzMXxPq96ohhxLkKrtCO2bsijc1YrmyNhKBAefBhl%2Bdp%2Fc09DBThXANnSCBz9WlmR3s73QCxQZADnXrm0bfgO9SmLljtA3cwH8aKlKoMsMcHyEcy1UkjjOT%2BhVBg%2BqHeqAYCtHEyQ&X-Amz-Signature=2e0262f0e7afb790711e0552eb260e6a8be9a22f3fa737c2735e68d13cb2c7d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
