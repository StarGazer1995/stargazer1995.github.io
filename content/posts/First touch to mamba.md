---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RZTGVZE%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T200914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCMO6zXJOJnxcKS35NWsUi5jKo0UmpdNQE7lFjr98T6hwIgV3kLjq8HRGIO%2B7P%2Bg1Ez%2FhvFoRLikOQn0gnuF3u%2BP8Mq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDPWrag2tBDhIPJN29SrcA4ZhyUzcrzGOZjAROv%2F2Fxn2U2AS7aBcv9%2FHw5f8T3sTuaI2weSv4c5YSMjH5KdG4FiV%2BAhsTXUHpbvyMb9dDduBbS56aBupZwOmR6Oj1f7Z2tLOmIrfQCGvoyISp%2BP7pifIaxD8%2BlGFZ1tLM%2FjRVnb36vhSmtIlO53jW5OxrXMQgsRCm9W4VtwrvaOCnnk%2BXNHBecm4%2Fj6FJQvwO3dwiS20mNxb%2FlD8NC1cHBRBvAzYKAc6FyCaclXeFTw6vQtB%2FMAL6gX8nJcO%2FRAPUw9DnD02Jq7%2BFXWHBq9%2F16ZRHHjxkP3aZ1WrkPrUyhBs7smyunm%2BBqrSZSaY1B5lr5V%2Bb4WxUMsiWc1t2G19MFYdvIxdAhsdjJC4oQSJTQCtX%2FeizJFzy59463Eh0o%2FWwj3ihjejmmugoZ%2FyUR8j7zvjDeKj8BZPI0ItSzVpSA%2BdMCn7HwMpoW31Um55HrrOnwgvtnlqEQXbECOf%2BYHMBNVEFNKKeuZv0boSATtYgNHYV5sJ4GIeKNOSMg%2F2xzEnNpOWRJ%2F8vwH70xp3KP9jVHD173O21gNSk2d2UDrFb%2FA%2FXqvkjAkOGNCv2atMsZ%2FIlqNYd9bOS0btV62EUA5xR5zIA63BRaM94%2FfMIm%2BKYJBnMOyDiNQGOqUBgICNJqpcuhhNBoPu7rgphNlIuIRixmxbrCYf%2B1MhpjwSX4zZfKVPkkmL%2Bs45t937dlEMkE8Fk9RU1I8dN1hZGG%2FOVQveBO7lhHhQfLBP%2FDE7pSueleraclxUmWj3WyREdPJRddYM2XSOKZxDvL62IziL9BsfxLHNUS6dXl3ZvdQOqU5tFUv8L0MWgnikwaUTtmXQU7yZgsEv0YVh0OpDOwYhaFJ7&X-Amz-Signature=e248de70db18c7c5a95d03b401f745e94e25c7136276f60c08740addbd21fd4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
