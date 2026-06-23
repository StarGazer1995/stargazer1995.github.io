---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622ZXHVEU%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T141804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQDDdESZVx8f3NP6Y%2B9i6HyNjgNqR6inY1rG989Zv0AZ7AIhAIExVrp%2By6dx4f%2BWVPDNCTwhbUcN08uD9FsRR28BJHIiKv8DCB4QABoMNjM3NDIzMTgzODA1IgzZZT0bwtZDxZFpJwEq3ANRiZe1ILkl97yiS8rKA72RRm9AyEF0idPErFq6I2tDkZ49ahcxKUWJKNiWsn0n77Qb%2Ba%2BHsgGMLhW%2BUmf1%2FTms8yqc2fTsrgzu0vQDQWvgl0osXw%2Beo5SkwB7Xw3PxZUy0cxhZWDdH53ujM3gUFJcozHWV%2FFJrS4XdHhCwzI%2BkiXpRoIT80InX8F1v%2B%2BuvkdUO3lWE4lMSnxEKUulzw8qd1OMJHyzLgw7T7kPYXdmon05pOKzClohj2taJHpaa4wWuqIIV3wzsoOxVefPgRY1ixBPKASq%2BpXaURFXPJ21bJ%2BN5IswrI4tranU09xKHgreu4px2PuBP8kNlQpQ9Y%2BZxmr4ivEXYkG4RSR0xsZlEVa%2ByLZVOO04dSMMCX7lDEzOxtx4GHW%2BZ%2FNE3sUs2Wkxr6PVu%2BKncgXV60XBMzEtUK3U7qFHQUamOA%2BUNL%2Fgy1VaLdDEv2FvKXG8MSEzWJQkWj5Kg60Me7iyYQTh9tetAM9KaXaqI0eXl8mw8LFDt17lCjGM5Am6colsGnyt37ZMiNhvmfDF%2BXGEUpWV%2F9eHtW94KxY0OagHCev5Y0GGCuAqsVWHTcsAPobGl%2FZaxbwMSqgthQS5ZuWYK6bZulxCrjcbHOT9qkNxE4IUIhTDyhurRBjqkAS91GRANBS3IotGahR51Q9bdOZV%2BcTaNtN7T0IETfyyH4MgjSGA4d5oq%2BcRsamxdU0hkgAXP5%2FPIrEkWC6AvwWSFYVgCz5qLKanT0xmla7VvnSejKT6qou8MZKXPcI8L76SNMSBWo5XgDxxe8xADgSVgZ9OYXLj4jShDzOXCeMAVRqTWjy0v6Y67k3kmvIEz7TdRnOAUJp0t1Mw8aH6Kg1rNjsqM&X-Amz-Signature=5693a9ae05cadef7167317d042da0cf0d76d5761c7f0db468b01e83cade0ee6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
