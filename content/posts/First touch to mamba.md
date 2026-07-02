---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2VAZSG2%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T020229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIG6qaZzIqBQPPhER7CqzqqU7UslQ1CaMXyXGoX7V%2BjWvAiEA3QsHiChqVDKC8JPEByUc%2BJ8V4TFAswNDjAsMEHGweoIqiAQI6f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOWYTaqzVtA%2BYk0enSrcA3l0BIytqXUntXv71oQtcD%2BO5lzXiCy%2BnkRKqQ8cVTKyO7wIeCMXN0ewZBHr%2FgO7LpiXRInzYUvco0dFNn8C96wzuRaaxDCmL%2FMoQQ6ur3EHuwxewSgzFNEI4hZs1VRVoJJOBgTCbpBQ%2B14m2KvShKXh9hS8zMKOH6OfprGduGQAW7%2FfLR6%2FQt2NDVS7tKVFKlWCirOfZ9qicCprwbq7brKVgujmTduHcpzbT840j5sb8lWt9alnVrnesnKBOpXsVg3waTduGKJR1wcOo9BM8ppp3wYTHXg4omOvlDGrXv%2BRsa0GmGYGajO4T6RFC6OzG5CvSedJ%2F3VQ9%2Ftkp%2BEqy%2BSj1l7r%2Fn5Rf%2FzhMWo8K2Ggs3i9TVupMHZfH1mx%2FfczR%2FNVh%2BE2WnIQ3iDLRM6yj5EycdSjkUDPAAvbNf64uBACZK2c2eQ1L5GiRr2R2%2FRdkBBCMyJ3ulWGYGSDxIU4RqqJXIQ95hjHOSK8jpSNC5eqbgB1vX4guoI7TSVl6IArlK0k6Ls49UuWwr4bqQgCogoDiWYmNlbLvI31FAtyIBlRxfvY9LanMNAZvci5Bn73Xw3xFUTma0R6xGmFTETGME3dwAJ6Hbai9AVy7h7GqI%2BCxt3%2Fw299p8Tbwqp1MInHltIGOqUBiTg74o3WLR%2BWrTIja26HRsg8fcqHlcNKw6jPtKKyUESgZ%2BR78rIGfs51KijIVBzfwEL1Kkr%2FVN3fstLkkoi9QbBuoTjzPAW5Le4FCWU%2FwUvU6JEPWspHdilclIFXaVBwV4PJde8C25vk5C5%2Fu5I%2FH1Iq7PFKNzuwXC%2FThz7WBkXeBBmXAS4wgDI8IgiVjutzUs6r0FaEmPsSQB2DANWRy0BTjXda&X-Amz-Signature=720e056d63c4bbb442cf767c674abcc8477b2a81976d17012f0d9b273049abc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
