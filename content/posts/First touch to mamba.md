---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKW6P42A%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T165500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIA7oqjaBcuUZ%2Fp%2BJr1IjbX8De7uAFzGr9aIXGlsuSfYWAiBBrh4dSmMK3lDXWKt5u1xW1RxIB0WxAte5ladlCquejyqIBAj5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4YflM0Jo5oX805UAKtwDq8gdzyjj8NDLLOBQB733yOMfcqcY%2F%2BtGJLvR55ResZKWXr3nvkyU8ReHxhKE%2FjZ0fQJ8nlT%2FmfW9Azoa2c4DZ6lKeG0F7C6Ytm6gpU0WAYy4AJrnRrjoBvwuQUZX08z8t2b6nCNd%2FlFajzIXMdRFJMPLCRtWgXrplLuXKqX36hlo22R2W8ZdCf7Z7t08oKsB%2BKH9T0Dor2lQBxZl91s9gR5DHKRIWwspwz0bwoHPxGDmUC40N0LrbxgS3byN6xC%2BreU6JU0fQ%2FWX8JiK0hiG0g4H7fCuicwfu4OUIx%2FpXPjTcs0PjQ%2BBGypBU%2FVbuQ9bMLrgvfe0Z%2FQN2Cu0KHeOu%2F0LnC96J9lX%2F6ha0dEfFMg0pMOT6P1R4KmuR946zhidhriLjmoUKUZ1e1gXGJdo9NOHahSkdrx6v1OHjfcVVl3w5rGmmVBZ7BmwUdyd6N80KhPKJ%2FEbEowCMvk9X4ycDUb0NXCOrSFKW%2FJziYUJOGY1cx3rsDn0MbDSmaozaadYdQmJ7dDeiOOE1MwC2Qi6P8bG6nxba9qUoA5KJl7fvxr6qJlk3pTE0yWlCgH%2FCz2Iaqgu9Tlum04OX2S1D2DPxeMrvqk1p9JgHtqtRvG6nYnuuUOZfnVTy%2BYOVbEwuK7x0AY6pgGKwZ0hcnzbYVE%2Br9xFXjLVEIJk%2BLJU4WWLythy8tF37KnSmH0ai0cLV8vBCcXbw%2ByB93Jz4rBfQaggaec%2F2nZ5y4E%2BTm2%2FFsMriXVRhhQpboYX0XKwb8%2BnRw4LR6OS5Rm9RP6XRjVsV%2BoDjIUwgsLFSR2O76oiWea0a0qOOGxEKXaS6NDSa0%2B1HqdJqMcddM67NoRsAWGCj4ZwUYXBPP8izDnGaNRK&X-Amz-Signature=7235de15fdf2ed8e0887d100e838218352b08865a8f85b8e8e2ab497fbea903e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
