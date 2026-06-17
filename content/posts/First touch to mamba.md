---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R2KM6UT%2F20260617%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260617T195712Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGtjvbzmRqp9Z94YEWNLFwZPiE9wAWNY1okLcC690%2F8AiEAiPiRAFyHSC0fslGlxpQ5L4e8SISYqLiDFehMiTm2akIqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPkhTUF0yTStw%2BhQLircAx9r7O9OnkEh4iwGMpHhRBswiMftqQqPO87XS6G4jov0W1d860BDHv9eJx5dcV%2BROmmCdoyWp0Gpbn22XG9vSKCDzFNjregnkIYj3A5cOzUQowKkHhppl66FIN3J%2BErFiBMBqUgsO%2FtKzyxWrtJdtjlxNpT8lasbQVjUP7cmpXwX02pDgjySpnT7%2FLNgQgfxieuTr%2FClweOVlWzmF7Ez5iVn7SfEB%2FNndHsWvVL52G%2FLP9tlqpjHc617jCcQjb968%2FAMkoSTGfwDpuP1yfq3yvEI5QcZS%2BvICHzHks7uVoLI8eyxTM1QnzfF4EX3Mky2sPPjfH9JF2VabFy1fvD2Mh0VQIxDmCxYlZwouC7e4S973jdLxGgiWAS2ndfoE0S2kt2BsbFW4n4sNq0DnW9g%2B0HUGCAVMo4TyW%2BPX5aais0mivsnlefGfoGR2ZdWIpFlff9oGRGHbSVSoXgeFV4wNLNr2823r7qVXYjsE1lGg6zjRvU6e7qo7AZCsZogQuK%2FXw%2Fl%2B%2FX5ILYUMqt6vt1K5%2FFaKgGrHd1ML4LuADn%2BG4a9n9068d%2FBnQgHLhndXOotS0nZ7rWsocl73gFg53%2BorVJO2uD6IIXw9cnTvXj8ENRnhGBPMr9Qhz1X%2BtocMKLYy9EGOqUB3sZVeN9%2FmILT9irQL%2FvUlSEDsfSCFt6q%2Fvgy3bB74%2FBKWTQCscI2yOztI7usKJgHLzoF5PEdytTKjylfadSkepDnxOrHJ%2F7yIMpXpu5o7NrQcMm3h3zxeHfkh08sR2N6tqvqGm8KuFnZeenpLh4J%2Fs7s%2BNLUoG8No9PsE5W9f5%2FoZ9HIYC%2Fu%2B2TLgRO8Cu1EJQrrEATT8e%2FDhU0l58fS2y8LiON4&X-Amz-Signature=e2f30c8bd8b0029adb0c407ce945b296f179ca2d5db94ed55c986d0be2956a3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
