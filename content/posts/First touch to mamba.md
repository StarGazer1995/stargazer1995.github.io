---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MQO2DQC%2F20260525%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260525T191436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGAxXs%2FTu1eOTcJd2cW2guT%2FEcYB5JEMwtHS7gzd3CRwIgbiPf3r%2FPCrPOnTv03PngluZx%2BHBRkWGR%2Fi0j5ImAOwoq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDB7WVna8tCZ4ihqJYCrcAyBsDPHhKiw%2B9DSZY3ofB5BAI3pJIP%2BqyBmx4HEG%2FE9E12LCWPVUKAVhu65O46PnzjDPNzNXHVWtTwAJGfuYNK6OPWzFOwNyRdyJOnZMmtHeHbvuwZlAf2JLMwQC6Od%2BHHofjtDjSnXZriaqgJyqwOtBjAr0ibkU2dCnGlgUuPVZfx6vBtyeHMWC5PQ3CqKadzLwa%2F8MaMH0VGe0Ueo6GtmRg11z%2BdBU0C%2BFQqDDN6EnYxFUDt1HkZleK%2FGeH2QrX4LA0dlVuffU7KjZ5vdeebZ5%2BjvqIurXSbMLOc6FkgGvZ6zJNNXIHayNmo2%2BEe4BeCJv%2FcEoyRntPihVBNs15ecMXNoC3EKZcN%2FBAkm%2Bbj5qA19q6IDlXwTJOQ6G7hTYwmDOQsAId%2BP4T1p1Ea5QV4R5mpANI5KehRZon4uMza7dqtq1WN%2BLRTHwgsX7yO5y1KO0R%2FSMKCGUb2VjFE%2BOaTmj%2FnBIcp1UiGrJDT2AP5KOWbSOv0o%2Bg%2FGM6toydEtMGt4lgVP3iZvdMNYnEtvM3FQ5hR9OvYy9F%2BMne22sggYdjSerVIA7ypiCEkRStN7owSXAKXlZWsOxy5R9YzA%2FsBL9YVcrshD0MuEnWdIPEqH3g0hm5wEZ7rGxqjZkMIOo0tAGOqUB1kp9kX43JTymd8D86%2BY0xmqWeso%2FJ0t9LKSQxt54CoMP8Xm0HKvmZFE7Qjy8bNHHPP8nVbrmWXALK8gQYCa7S7sD5x4ftevwYqJd6Bu1aiez7vvkbSZ7RYHGE6E8kfkzSuo6AU7QbvjJ4Qpbow3RqLah%2FZD3OMC%2BibPquTCCI%2B2emylij58xuPdsLLrX2zDjirEkARCxPzM8VMALRDjNmC6AZErS&X-Amz-Signature=c2e2e7cae61d465960d466c87bc19e7d4b47e21e9342872caf594021403139b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
