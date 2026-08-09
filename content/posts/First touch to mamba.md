---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROWQ723K%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T201853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAnenbYi49W8omlxVCrvylVhfnWCkQ8QJwyq3hK%2F%2BWeHAiBxYCU%2BHlro%2Fqk%2Fa5Eu5wUASwuQgyfMZ4efZxT7snvM0iqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZ80TIpdJx28LL5gXKtwDVO7tpi0JG4Qgn0B53jl6EPuFyqkf2xc7kVkoOxLKk7nHZ1egEFsdJOMjKv3Ob74umvwDddBfiHcjszxUBNkCJf%2ByJZ6rTmg0EofRIh6Jz3X55j32a9aoHuE6Ry7BenWOleQ40mK%2BXb8v%2BYuTumYRX6s66hYYjcLOavGXEIBJxTncTEUVh1fCf7EsZtbVDgJ3XssXYcOb%2FQCpko%2BRZdvxhJxlh8MplOEyBD%2FgdpH%2FxOerXqaUnXaRhi2q1%2F7QaO6j%2FzJn6nq1MgRwOXWTyI%2Bif4zHXy7I4e%2Bs70zxxk4XUPlMSfHo2X0RPQlIFwNVGlkT7lrnAnwG0EYxhpcx9%2BDIYt2REZMzMezG5Be4KTbnBq%2BeH638nPjMWhXi3qu%2FHW5Rh8eFSUETEoT6jzGNOGcJm0gLW3A7AgEY9mcb7VjFv%2BjuctmIcMoWFW%2BDTs0ckN8ygRyddR3I32JkdXIMnG213qrlhnVRccAzisTcfKEjiMUOfAyd4lGMrfgofCzlAXG%2Bq5lphxg54fX9%2FA35%2BX41NAXwXRgN4jvQz3X2fv3BE3YC3%2BHNcx26nWAFGiTGp%2FMw%2BOfh1A5EYFl%2BtSOSjGGqKgJGD7eGRvhRtPiiX5Or%2BMe9PUnztVJDiwe8mjYw8pnj0wY6pgFo6EtLMAEfNOJUWEgBrcBri%2Fg2OHZcYur%2FW9qklfHFFvJLEhd%2F6eTufcT3zoJRzaOIJDx1woFQqly250vQ0VwSJweTkZoVVNwyxV7SO7ZWOmZ0DZ563bhSRm5vzD2iPdJhKkcPI73cJqdB%2Fil1vRaQwBi%2Bqr8U5SuwUD4uD65DzMyFtk6FSDKOOgdA%2B4LPk5mE1NLDCwBtOtoMBUmqCs24U2ezHdLk&X-Amz-Signature=f4f518eec87f86e3c237352b4b11abd0516ecca3be08287d2cc46e235d4c6386&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
