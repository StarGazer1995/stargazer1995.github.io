---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPRGV7DI%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T161850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIk9vBVra4f5LsrL%2FPtVGsO2aO0oE3YOfXGjn3x%2FQycwIgD93I%2BiW4pQ%2BKiDL1ObbUOz2tL0Ia%2FesSa3k%2F8DnUkHAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDC9Hv04ql2TXMsbooCrcA5gSM3KhMfYLKCgM7oswxuOlNURPenwC88ytW8uW9UoXHO9x2PgRm8jj3iOgRTXegOXonuMwQ2anqsrvZ0DPklhF0UHbN5G9ve6HPzYTNpS16pd9mDpo8o9mavgFOirNPUUnkanfr14pVvPRTPEevXeZdTARS76aKOzaLmIjPg4U0EA72AQ%2FRUmFYw7dDI0qQwtzgOV1ZCwDp4V56ioGX%2BQtZ6FfqDYEIYnpu6Cz4TCk40U72gXalJFkIA39%2FCMCd69u58QV6wQSxhv7bhjHnNPOu4eEin9RWcWLGAfOlo13SqwEXmb17kc354dFjRUmCQRwb7eqYQBMuldP43FvgXkMsE0GIz4ScQBYsWH7APZf%2B%2BODw7BUBuGSctUXEriOE1c%2FsnBSn07AcsxXJ8QjaaJIy9x%2BBDGy414Dm4MQdRMWiOZ%2B%2FUtg303FAFQ%2BIbUNs%2BYsAXKwPSMpl79hXI4MqUwR%2F7Wu3COEWS2l1hUtauoWvweLirOe3l43FlX1WTrcMrTjwjgkmI0ymzcMzpuw3Fl9Je07GadpdfyhYDC%2BrgqJnq5VzG%2F6l1JZeVzIHAWOdctNwHVm5fitvAQAG4iZfucD6KdXGKpvtvGLacIey9yjxwnll9eXpnl2QV4MMO6g3dMGOqUB8BaWDJuovkshJAd53Y%2F70RnTlWsOu84Et5O5RwkmvfL3mEa25TEkqKl2hh0%2Fj%2Fgv16zXWx32qCra4BwQGMro0%2BD1uahDZD%2BB8AhiYEzfksfum%2FIH9gLwVZW7gQRTJb%2Fk8NXsI1d9yoZMtplCDuis8WuH3dtIKgUKXRUSYbV%2FA1nLyv4r4VI1aiUDck7glwFau4JYLT1FLhQHVzIkoUpQ4MgNVJOw&X-Amz-Signature=ea505b74a51b51ffc943e65da433c19733ca8a557c665d6860970e32ef4e3848&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
