---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEXCDB5L%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T194825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIGb4Zxt6seLf89R5qaSRGT1n1h2CfVJohqxmN8kiz3l6AiEA2eNwA%2F4ZMO1NJqQwFCu2IFDcbklJNCqMH0nOhOYJDwEq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDE5VW2mNDCNIjY2TbyrcAwsHZDA98uDuewC9PfGKRYLHqwO5VB4uNCnen3UenmcE5XvKemGZOtUnLG6v6uS8e8jRSwj%2BLcPD27qb%2BjHUl1f2b2X4CZTHG4gzYmtaM%2BIIzhjYHgQQh5zmF3yuc73o1%2B3ETuuSFL4q%2FK5bVVlEsfjCh3Rms%2BR4MNHO9ngez3xYNzHAflP%2FpL%2Fw9EV9pX6FVsNOZ%2Bd5zSYpdXCHwa5lLgeyF950hsHqfTUe5SM5NKhRgNpHAv6jmbV6zQ%2FFT9WVmggI9IZml3YecXbjMcv3zE9xGUEig2QWp8FCeIGRUGAHrxaAiK%2Fnlgn70r3yMrbEP41KarKUG8AHTgLZp1lJU%2BkDjDvHmiRV5pjnI92NDV%2F%2Bm5mC3k8U6KZ8IljqSJt2LDW5roR9eyPpu3NoKB6bnmJZLkm5YIRb929m2R02WigKz9Vh3osYnRjjTcimnGHg0o5%2FzFYVCZGw8DGrOkFIZa2m9TTHIWH5mgtNZE13%2BqIASOU6l%2BWmWW4AuiL3OjeLL8N0X9vuObaZa4qB0xVo6WnKbStj69a08rTbm3mGQMeAg9Jou8mKwcQ49vp8%2BkfwuIR8GQF4dQBeDjDnqN902obIvli1gDMjFU7g9EGTChXa6gBfx8S3ZuUJ6YfUMNC069EGOqUBxqpjBYjrF%2BbuUjqDZwMxlH2xwgzXUR1RBcXpFd7hqpUY5ctsHYmrvDaZNd1EpldTutjzRXOLf10TZ7v1mLsj7Oqd33vhoPGT3l1V%2FC5iHXrduv0D5t%2FCNuq11G3ErhIowBm%2FEm21TI49wf46byqpTZJ3f%2FUKZCKLHA6cEJ5z0cYfGAC6HLFjID%2BDB%2FZWvBOEJCk8KeZ%2FCYy3LzAS7KWZEOP8%2BuNO&X-Amz-Signature=73bb696531e91ab97fd0aeeed5ea17fd199d8ccea9c63ea2019005528828dfa8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
