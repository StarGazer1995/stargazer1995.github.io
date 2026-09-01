---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2YTVHAV%2F20260901%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260901T005225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICq2al5cNOhFK%2F5IUgSJr5%2BWHzRIh9uFBgQmw0CCJRW7AiEAx8DvCUpcx3S7IMzCAkzuN5uktNUZmaWbWPjnmw9fF1EqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO1KpGSNlxFP34PIKCrcA5628Ok9CsTsj0RoHcWDB6HqmqMv74rrwnzSg0fbyuiwmmyELTY%2BA8kwB2ArxW4aW%2BzStMSRNNZg2CtZrbNkWeudxBKCwkg8wWTyed7xKg4DppAOtnGw%2BtC9Eb81Az1r%2BXBi3xSW7Mc20IWFUy%2FYHbHCkhXuCwoC5wwGU3uORhug6dGIFu79Wsk%2F4ZI10UfCkxqKEwD53pvjOXcqQ0CEoAhQ7YtGmORWueWlAWanUNYlSUct32QCiQi49%2FpJvb9nJzRk7J1FZvM%2FTTck51w8%2Fi505dZlEXdnGYFWSa0iL3vx4NeT8dBOfydsXoLzu7qErNzEcL%2BPqYcMoeakqCR7qLxUfxukN5Alwo0dNRtCpmb1UHbiIVxZoQ0t5SDB4yP9tzb%2Bh%2FewCElx8hjEa7ISfw2X%2Bzx0054dAHIQRNh3ypUS5RqSc262VEULZtVcbC8n%2FGYfAyJ8NAUltZ62TzTyGZbs6vebT88Gb2HbEWJl8DZZjjdlEWfrlVmcjg6cEXLKwGzxdE8ba2TDKt2l3K%2FKzMRrQdcoX%2B1DPsBTBB0DxHIjzfqGDQSAbzfZJrOB1mdQv9T9qd%2BMe001xfwRsDF03ZmUH%2BhHuEHyl3Sf4uf2VjqKwRjQmUXbdESEh6BDMMOJ2NQGOqUB4fHHV1%2Fsn3rxPzMvLrypVncownuuokzVB%2FVdXCpFylj75GBjK%2FjNm5PUY3c4PIf%2BU19c1e6yICba9eVBWnhBQ29fkmmZ9Y%2BGrZP2g9S2b8bgHnDV7sgKncopkHHwo1jZDO7ChRHBYaezoGlglQ9l1%2FRFe9nq80P02xOHnH0iUO0Vpm6OcfPJDVArc0cPnVGZ%2BQTuiNsBYLYV4UhDx0VVg2qYAXz%2F&X-Amz-Signature=595cadf76eb43c5b7c651beacac8a210bbabc736029a600ee439162fa0caf268&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
