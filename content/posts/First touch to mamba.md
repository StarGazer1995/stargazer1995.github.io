---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPWXK3A2%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T082647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC11CrFqIXkZG5WC84Fnbu0OkA62X2OxEyHPeqzj%2FMH3AiB%2FqIrwrjkIZ1D2Z8TW4hF3PCrhrIxTMGZs37JMNrsuhCr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMg4jjcqRzzMu3e3%2BsKtwDSZSiJjI4FcINfF3iqKi8JwEE1uSUAm05JiTvguoi%2B2M%2FRUvaM1O4yEsHfVVqpRvVMHkhnKcNYJwxCykWe8eLMo6GAAqO0XOIx7xJdJ3VSWDRO8kMbkRnfDBYU3C%2BpuvWxccpnehujbSBa3UhlI7qRUXQuPZPtz3cYHCLRLZlyfBnB5qmAYiXzQ6fkx4ok8MraGxK2L5%2FpNdyOx3%2ByGInY1Qh6wXV4XYqWDMkZcnoawDK8lGETPDcDn%2BctWQdc7P0mZPG4A1JP6XQSHSTr2fJiqmSnbfDdhebj4xgLXLh60r27P5uh5eV4urzaVHQ0Ey9SW4QywavcHxMs%2FP9bXAcQ%2FsZDxEgZrIuZVpXhOsUgCDsab%2ByGTni8s%2B1od9CAOqKCVxlzl%2FLYqIui0IrYyA1vce%2F1lJHlDif99mQDrleL8iloQbBH8RP9vbNfipVLpSWkKbWKt%2Bnf%2FwqiuGqfK36n65uGsdCdPZ50f65CFhMITshNkTNmZfQZelwl%2BAcFheItFTGpNLd8P5k3h8UeBgcpAEE5sWVCcZfMUqiEIlRf7azwZgjRNWaZfQNCbD%2F21Lv30uo5x11QIbw8wGaIZmK4vzioQaFoCdghBiF%2BDfKFbSqtfj97igdE9n95lsw0qPb0wY6pgES5PsLC6rbCNsl%2FgQ5MXKw8PV2hkv8ErZPqJSzrNgMsAhi0%2F1UpRTvQwBmKuLDFeJYElS%2BEHhCy0bHq6t5xEeiXD8xCNdrTaQDy1lANADSVHJg1a6N7ANRbSddOhy85eLmjVRz5UuUWr9dSWCrEXp%2FQvPwt%2FVdgolLj%2FQ4IhE24Xg1AqrUA4ADhE4zRpRwfwuwcabaZR9sAzPrZpMm5vU6Dr47EBGa&X-Amz-Signature=dc63864a7a204e9af38a387241420b3ca63ec826f29a79dfcff2d3973fd0f700&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
