---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632DXXS4M%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T224257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQDxrmaUzcZkB18LY5lPY6EwbejsgUxJ0JWb7gi13eCn%2BgIhALfBkeOG%2FNiaolED%2B4gVhxYBSQQOlMmolh8C50WsBtXLKv8DCCQQABoMNjM3NDIzMTgzODA1IgwBPZY%2BRZ3t1EXNddIq3APeROqvXa3EdXaOBY9B2BfNdeCzucQx%2BgQYUF%2Fvk2TK%2FVxAXUAU2QhTY65Mwp%2B1zImWcD8FD%2FtNqol9xxs%2BiIYM6dNxpnl6xxSNNoCVYFv5tNUDsI7NzIrKx0pCs%2Ft0rX7mDGthLX3QBJV%2BUGy%2B3g8BYYE3ZdvlQMqEtjIc8YPPtHyumx3liR6jBw6SkGwfDsDn1NZJud%2FC%2B8WHzp4KxkugZtOTRP2CW4F%2FApnviGcyeH6dpTCfaqAeOi4TdiPv1CmLw05SLD96GS2IGEfupgeYGJdyA%2FNoD72j%2FmIjkXs9XCY57W8D8AscOSvjQw15VcbUR6Yxcw%2F9dfh7tpbjRwZCIpLxPqgtk82XjbAlKMvcH9gQzzVJ9vq3fLA9JpDgF87HpWh2mlPmwfIWCMq85GFnwIcwr0h6VNjTUbo4ouYOj8Y1JHDmKM3IhFqnsSYSB0LcrDp7nuJZnCiPT7ITwGfz11m%2BU9gPPZhkqOy8krgk8%2BYtO5Do%2Bx8KqRe%2FPKUcZuet5JJ%2F72r7QQ4aXEBeRL346LHNXMDGXQ5wHnJAkXGjdGDfciBBJVkKWFlYrqRTHbmEKvjlfwU7IxGKJywXZWMIUjXVR%2F2wgtH1Kp5f8WsuxyFJYqoLR1reeijnDDCukJTTBjqkAWnKt7mKAwqEvT4m5x2u2m6zEtOZyLZMTAEyKGDUWXhUfokIunEhzufas9HZM6uiY6tkAQWcNbzZYB7GdAItdRhBvDKboQNSimOLlfGNeDv2yVYmDr8HeERDJdWUxDR3FVUmEYh2vdNvUqnG%2B9sp1lj0z4fh33a%2BRE9CfyAC5iAWN3E8mx3kmM15eBtBivMzCKum%2Bw%2F5jIhZ78IU1%2Fp2CWrxo8m%2F&X-Amz-Signature=0bbe05156ce771e9a47c6d7e1c46da0e52c9edc3b556462af2f038bd02970364&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
