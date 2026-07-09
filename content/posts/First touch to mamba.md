---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUQFMC6T%2F20260709%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260709T090210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF6UcbqayjYOKQEaN1pjIx27Kju9CoV7eAHDPhE%2BtcO%2BAiEAqWYGDoD%2B14aRpcmeNOoTM57vQcTpgywKkXNLiB9%2FvnAqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLkg72UdfJqLODCBSSrcA9%2FxlmZFILmXASNmoBf0yxNPQQMJiSJFgMz5QabqinK7n%2B2My%2Bjx4m3eezgd7Q7VS1ZDzr6TErI8ieY9GnqL6nqSiNZGuDE1SWMXy49pSI5i9D8%2Fb%2Bo22Gkz6caA1DOFbAkcaf6rsuT4Oih%2FOW%2BVHnKj1DvTPf3i8Gim6c0z2WoPxUeeDnAhpWaBoe7qDIrFm%2BbbEYRPBux%2BCNCy4B6TdyRzjRmGSS%2FOjGQmXsfQOB9Js7HfPrtRIKfUl0htL38gjlVPNjHqpQu4iHqttTsoKJVFf1dlk05yajCmwdpDpaSRgKiQBk4qvP56A44Sy7Dv6cMjlAGnRkxC90bCN24p%2FbOd%2Bo0evcAuHPKcI0Yg5zg30tWkkKUAHTGoxWGSKrS9rD4g86kK%2BeMAUI2my3LlBQcpa%2F41R%2FrUKo9oQGIxtjfSXYpi7f0Mn3UkoNgCzxsG7YjIqRz1VXtJd8Mvg1SL%2BBL7%2FakfNuvoRxlpeMBRtrvmrzxo714S7UGoQefpsbw1oFwgFSrJtXPUEXviDLApI2%2FGGzc5EOlWb0anG%2BymYts9o0%2F%2BY84zJLtv68%2FV%2F8IFFS4X8a7PMjFdpsd9TWm%2BmHkS2VhT7H0GsOq4u6ZyGxaLoZmuNqwd0hU73zMhMNiivdIGOqUBZQsF0wf6rvdsPddTwX%2FHzb5E%2BMQxqY%2B5XnBSeyjGUcw10u3G4l6YuLupXJOxwGVMo4FKCv%2FlgXFW2bZcOziCZ4XCzcLCJt3xb3%2BqYRndmCzT5p1DQV%2F%2BjmK2J9cUyY4ZNNPxV7j7Cqjdxs61c62U12m2zvsgQbyR0hSoa8OaIdUIBc%2BmmmD3alFjT1GgcWv1bvbQ1nmiiNV8LS52XNBdQHFT1XLI&X-Amz-Signature=a5b0ce3114113dde7e96128a0c1ed803561604d51051b2411975ed8be05c85f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
