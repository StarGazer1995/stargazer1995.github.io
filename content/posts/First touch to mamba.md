---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSVBO25U%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T230054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIQCNV3g2i%2B7eyWbAjvkeTofdlHzoT4ZgmP51zQrz%2B4ayjwIgc%2B12EWANLAIe7DyXWcR1zI6OGG%2BXsgcJ50wfFJTbheAqiAQI5v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHpvMCQStRIPpjPusyrcA3vaNK9vpUKygzgjfc79etIphCJ9X9pE%2BycJg1Zc78HZCVLdbW0AZqbR8vhpS5cSSZZfyv7WbdMpq1JVgfaMp8YHqYs2KnjnfYKacjCcqcRrowfqgUtOaks71ucV1DGKqKEqiY4vUbv0Z1fLMgyPMVrWvk3JpAmxw%2B6PuXS9tWUFCkBogepj6aq7NnDoPPdKiYVMDWGM9iR12vydDVa7Zc8JBrlmBE1Jo9W%2Fm3qhecVDBxg2CRhGWdmEJqjPLbIBa7FIxOLjacQMlIXDzG8ErPtt2ObyW5qyb%2BwsEEB31iYteU4oooJyU%2FykzwbSwB1RghsQPA29xwB7S%2BFl4QGPX4NcerPnyVRFhfEj9EAGCp8uSFegWnUzcbHuQVfJ52q%2BSMaB4Zbzjh4NCx5eiR8dnZX0T%2FtFRkrwZ4v0hZIAH%2BMWdvTWGzrwH%2FUGqs%2BmPeOv7iNM8wsxQDJFZqnBT9CGI30bjFsEZ31WnESre5sZxyHQc%2ByaMK1WFkVG8EWy%2FuuKWEmCc3i8EaXxSfPYj8MpT3HxOVXqxIvqSpwjmC5Op1nJ85O%2Fvi410cDUAFZKbDG%2FGbR2VVOhEGt05qUTc7Sf7NLNdQbNDO4exhLs%2BLRM%2F216ajEPOoeKkDza5d2VMI%2BDltIGOqUBa0ZDQVip5Iu9YPvh4WH8SL8JOf48F6iOCifKq1zKe7kxO4e1AydKYeL1zgTLWNZtoTIBz1Yq%2FaLSIPq93BPoET7lFLn7Fy4kO69u0ldj5c%2BKrGN8CRXrjEfwYTaTno%2FxqMDGy%2FjeIIcF1U%2BQzJkFjAcctvZcO2AZiNfvmPZV4SCDrgwoNaEjJ1ew4STQehnrXI%2FEk9n0ZX1JVBcM%2Fc2WPNCEmehj&X-Amz-Signature=c6570d442a1330fead99134b3e5c123abe4169158b65c043263e6ca1ee8621b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
