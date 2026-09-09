---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VE7CCYBU%2F20260909%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260909T123248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmYLNDOWzFxnUGex6Sp%2FutGToK%2FzMOPgN46wPxAlaNIwIganwByapreH7Y4qSZ5rESZ739%2BS9Xpr3bpq4rgDwj0eYq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDNtO%2FTyev5brqMbkaSrcA4gjzZ6xbUvKLtc9pdOTTmabjCYRMR%2Fx0KYo7oqJY8TzgGSKKoxak74gICM%2BmdvnJNC8ShfZGMOTSK1U2vrvoGWqIQbyK3TbSy1Au6G5CbELbOUBsozRMzXiJK%2BEymxo94T%2FUGaauxDgTQy0Xgx8tQngSyvG%2FzAVwJdAj19jeGQMvgm7W1Wrmox02WxlL1MLchqXaKUMB45mHYPmRZeGb3XvP0snriRqbAS1z8glTaKBmwdKCRPl1k8yAnsi6AtEkGjBpvvJf5LF28Lh3ICj5a1e4mpGgIYKabf9FvCptpCdesJnXekf5Lra1WKuvdKwIlEtW3B5lUCxsF5T%2Fbsgv744DDdd0pFlNZLou80PsI2PShVPgL50AJAC6jSOt5eHiUjqx31sc48NN1nyPnPmcqmAt1IWsgjTjBHxWJh5qO2IPeiFllXVMUezCQxUFkmKpZ%2BQtNG8ROIwuYh%2FVLLtPCEjayC%2B%2B02ZWswsaE0bYPs4XKFGMpfya6yKVCAO%2Bw3I0ckNffUI6Qe3l4bphyOvpmgqvPrQX2bk09pUT9d32IcIT23aPEIOuve0oeXGtmQi1%2FRWvvs8cIZP3T3KzpaObk%2FijugBZyZvh92NWv26Ylx31zo1d9msR52%2BxbWHMP31hNUGOqUB7f7kEvr0vrATvnp7RoZy89aiEZ3UUo4EP0wfAvoNagT7tfd0hRb4khzX%2BDaKrcsTJf4ElrqcGzOCj%2BPY%2F4VSXIMn0yfEetD80aJF8GWWYKsCZK6VHGuwqmgsIVz39Cj6NQK5RNBbyI42wUgiJv%2F9bE6j8H0gA9s%2FRMyDFytFswGmqDt5ugY8L%2FdrNP9o3OuaFjPv8YV31KHayvvsbg4zjjTIJrgg&X-Amz-Signature=9d593e550d04d441a3f74cfd27f532acf2ce5fb3ed5baf14f0d7f7f6278bb30d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
