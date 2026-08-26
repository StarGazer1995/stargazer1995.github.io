---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JYXLTEN%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T062642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCFjRBUpBTRgILQFLxHcKxCPOXPFBnLzKPZ86Cv1WjE3gIgRZUhl7eVLzkq%2BPVJlGqn8Io7MX3Ou2OFVv1%2FMjVTFaIq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDOAavNQv7wR4RnIeQSrcA113zwUqyb5oihaTcxIdOdjGN0rHNRsqfxJ9QoPfTs4QCQNpMvw6kBgFeiYSQF7ub%2Bjpsl8BSp9Hor0bcv6Nt6P7E35YHqyYWE9MVcuPSaHGgBma7V%2BqT5sXOmXc4e2819ylFgCBFzam5LfmbI9IBOD3OFSd39E1AmKPBMU59J76A93KIXJ2otzpCdRKavp77fxa97nX8G0W4epjCdowXisJcsEULxHf9TmbbMym%2BxzV1h7ZytbJW%2BK4guTDO7qToccUKrQzOf4qIohFlRSYIIVoQXA%2B62ZpR0E2lJ385rg3evjc5Q2xgvlydCD8gxQ%2Bid2SUueKdd6lzqDTNUeftHvj0wRkeHJpWRJZWDnJ6PRQvBESOzH1E%2BwenzVo5Gya7Wa3hbdZ%2BkNVVLbYkq%2BMysRYhtZPSncyfqzISmVd%2Bo8E9b3K6ZgsNW92X5lsh%2BYIbukyunfdwxKuVmDJHYW94Mw2fERLnNo2ETZtOb0Gc44yB%2Fz1HRZfmlssP92nL9FZsWlQF3azlqeFkJmmFY4wW84rg78x%2BflkhEfDA8jh2pyVt4RumPp%2FFf%2BKEEUEzFe62REKNbph1OXkgTyo%2B7nq9Xg5TVyL1VkrAm2XciEYs0NGHHHzSlvH2rjkNVLEMNjYudQGOqUBh2iM1Kh4JoJWMm6UVKa5DaEcdt4rv4ilmCc%2B96lnRTpaOAECw1yiDA8HRE465xH0lA%2BV3wV7dJhllCUxUsjxKToIByAffbWxHOinDC5TIcHjX9tbS5RR3fwgbI1rwItkoGswQoi3dVP8VaszBwDcXIyMnFYcKXOZM%2Fv3JcECact8rYhOp28rj2UmJdN1qbsZ%2BekH6b5dZcAj8E6cQiMeCwqW62l3&X-Amz-Signature=ea4afba5077eafba7a4efa8e802c8ca15c4175eb534a0b98d2c397c3f210c20f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
