---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GEU6ANU%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T074038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVqMp1I%2FZKABLEX5vTF8I%2FC%2FX1BPJyvmFjFnOZDVSA2QIgMICOjRVEzNjSvNQgV4bT3xyFlVky2wmLX9df3cIB23YqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOvLtukTwZ14t6nEaircAxl9eHwyF14Vky%2FaPdAOdvw7ik6GuryfT6RwEE8qecg1GKQobzS6ejiGcKWxChuTqZHdGlTI1iPjj8Sn6b042twcLCQUAXGqkScD4vew80lu0h4DY7XVr1z1CU8mr3VyfqDZejDwGO0jnkC1FVG9ZNgBE8FwbyazFwn3qxSoJ7M0xdvQ69TIhXn%2FwtAzTibrr%2BMKLmvrxH%2BpzAJhva5CXgoZ3abwKkplHL1LkUX7t0ve7GF%2FXpQ1GrsveDuZovkFiG21NiG7qqqknsB3h6HrY8xbu3U%2B8HoI3PL3NOgRJyKbkrYs%2BjivMChHBzqydhlKLbFZXu0axtbwssUurlCs%2Be1OYPUZoivVnV8Y4lmw9iKUImxLc3bhmROwYvSy2hPA10Ep8eJWNy9evoKOTPoYTn%2FuTNeJhUnlchWUY0rRTRYbDaW15lA8xYl2wCies6pTA0OkoBfuAHptHAtws3Zl5DF0xBKLS6ul%2BhFmvLHNN3CPkEp01OqRSNkILae53xWVz%2BbkLhZU6Qwh0uHpxY1uW7THg6LQ9BnpcihUZ%2BSLr%2BuGU%2BeGHOfWQNsirtkWb7SJUa2r%2BZnRphc31x6dpMgVoScPKuCsTRStuXQZLpRSvHgE2fxKDUKEq%2FAWetIgMM%2F0%2FNUGOqUB0fdYWGQ%2B2jo6kjj%2Fqpx8CapWt%2FGnZt%2BVW9mO5kybSgqQ0i1dzTdoD83V0Y9GgCyE1%2BTfmmJOaF6GtYd39AJYtEE74LUQCKDEh%2BdP%2FfxkvaazUC0X2OcQVQfOgMlkbn8gmzVR3tyfJwreLk58M6OkkGm5NokM1CMDPeTF9Mbq96raiXAxoUpD4rAvFOMKiWynh3b20LwpFG8Tcj7xkfRXYEr65o9U&X-Amz-Signature=6594467fdde7c0c027039d26af3c2813c31eca1dd41f833b9e308b4798e8f40e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
