---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSQ7S2I7%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T210328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQDD6R1IqhrQbfsArtBKdTC9%2Bg6nBv%2FWwQG%2BxxDq8tIqKwIgSp6Q1Pw93Xmqm6QGotabyOVMadhG6zkMVIziOeCOh5sqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFUx83Z4jWG33XwR6CrcA9rmE2UjdyQKEFEegrHDIyrXKxenVdkdypJ2OFXQ1fswyEdfxideE5fvEEDxjcSKCSatzXppN6ihjzRrfTTrpuQFZbfbA%2Bz99N3qiSE%2FAwPIPlEzuqREydIl91Fvs2T%2BVbJuJv%2BZPMehBpYsXco1Qk%2F604YNkaHdEenFxk%2BFbWwXIjy7tYL5JcGtYh9XM4GVomGv51wSJlOuzFG4sJHEV6Fr0cV7OkbVzC8DcJVoxhxWUkQ%2FeufDmyZ%2Flf1cjykFDcW1NSUrH9e8lfxiKzgSCpQhxzDlu%2BzGB8nI%2BLEjkhsHGwiU4lS5AJTXMhI%2FkGQ%2Fy9zMIpSrfMAA60ZKytB5xAn%2FzM1hjUBpg8HabzSaYQ0lxOXZMCyHbAHxsgwuP65HjYerzedmXL42OFDAPx9c77O%2FylLAAKdjaZBiNYJNazHc2MjfOnQZgTQjhmST4gBV%2BNSE8rSrQcFzKt1MpJOyHzmpvobZ7%2BxPFxNoTxOE7HpJqQoH2uscCONjmAkM9EhCStUjUTKckFL5QY98Vg9tUaihqkijyvECsx%2BCHtybtHzCrqQk6mxFwDiIAba24QAJXwAoticHxmVyBRQlqvHTgsWUEpbAZaOzHS%2BQ17MA04SoE1Rf00%2BosOfC1gO1MNaB4dEGOqUBQrBZwQ7zs48QzMG5AMhgRPLMxj4ib3rHEdQoUJ8j63nq8kzA1FDEFYDeUUt%2BqGIjHDFOEJnqchb7G9wrKquWVGdfPi3IHlyPGA%2FhIRDT7MyxjYX6yv5gliXy6XThCRfVoVVpzLu8ma6vFyhTov7y5V8Rf%2F2TbKyg5MNU5as83EsWXkhccMEwYBAw8AA3EeN1MCtPoesnFGSK%2BSlxtLax2NV8C887&X-Amz-Signature=24cff86eb66ba272fcc8ec40d6c2eec4441107d1146e7657d9fefc25b54a7e59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
