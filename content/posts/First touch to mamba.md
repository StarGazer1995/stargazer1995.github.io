---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QQJXXFZ%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T185358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIQDDI74ay%2FHFnMzGCkhos8RAifpgu89JIbzq4uTxtCO6SAIgOb3sbnEGruUAcBqKGM%2FSozSteteur%2F8s%2FgbW7rTiaSgq%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDBHtPCbO8YFdBn4kXyrcA1hHKSgM9LLY%2BKQaZH%2BJdoAouDARYKzvo%2Fcg1uAsCS9DtF4YTfzxNbgMQd%2FOf4RepkeLXcmQlvMn8GTYOd6rBO22k3fQnY67k6%2FD%2F%2B0bpKYu%2FWiuCdcfZ6M0yK4VSnrvmGQnh%2BwjDQiDqK4y6BNByYXCLRQcFWrvPXSv%2Fb3ZASFDtLYTwFSaYjr7JTbPL6EN5hLj%2Bft5SNBEmWFl62EDlemuPRzCpGDUKDT%2BDy%2FqsTbOnTw%2BhnerPNsGmmOc1vXM0oqwqAJSHwofwKn%2F7nsjRq4PnoyeTvxTJ%2B%2FXFKtQFMhjNq0RZJcy300vRYJpiPJCBpzEY1DHAxqn89zJbgI6cBFoJSbGQbtydkJRTFjJnDCU6BpDcPDYwY%2BHsDeQWg5uaShHCwfyhGIGsAiu8rsisjF1p%2BQZoAgUTXtjxHnoNxeKmU1QAdCX7RS5sja%2FVJhVMkJ63w5mfVjYN0pb%2B5lcv2R0%2FLPqJVWk5lJCA8%2FTUJi5mYRLwm0kARZHWi7LkXvDtK9%2Fevwus2P6ZFr5%2FWNnHVOv7AQjRs6FLDG128NwhwRJFLLTO0%2BnECwYYzS31TuoYF2AzodwJsGNvY4QPaNS%2F7K8OnSn4JtCtrgww0%2FbR8ep9gDxim0HcwKOvE4%2FMPLA49IGOqUBmSB2acFQCBS86cnok1MQQGgICRBIl6ULpQe8gvU6iXjj8FT2hRp1VlASp3VhDlpwbCU9eHrDrw%2FExOmE%2FVwpSRV5lW3zBqpREeIXlgNhdUL6UTVYxo2fHWc7yjISFtE6j5Nxto4m%2BqdI%2BiNLL%2B1naoCI9tb5Zt3e0zx9XaNHfvVH9FpGjkTydLZGIEFbcZ4KUjTtxUlORNnnqcCRihR4cOaJlOgh&X-Amz-Signature=bb1b938d6d0aa9c5a25f23cf44f5987fb3bcb9bf7740334d6e831d56a33f88d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
