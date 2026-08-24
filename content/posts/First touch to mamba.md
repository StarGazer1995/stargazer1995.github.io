---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3UTZV2E%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T182555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIH5w6QQty7HoB0k2%2FETls9RcQrWFDOry3%2Bd0Gik5LQWzAiEA%2F%2Fzs%2Fwsw297%2BVdl8Bz2UBgpDyHLzXmL3k8X5RrzrL2YqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzb%2Bb90vb7prwpqXircAyrV69B8pOYDxUmgrJ0MSnR9S3bF4zE2il46yZ8wrA8CFFJq1mRP11AwXAkAh4Wakcx8bmq2g5ukW28L6E1NKhjd%2BtcYFmKtxgGqNXFCa4pOBZdnmCj4Kiae5QDgj7D7QNxoUG4ICCEONJ%2FuZqxEsyyvdaNzndUwseNfDwuLl5eDvwLjSqE8rTvRMjCSKnnJRRwxthjVt%2BmSydOoHLBEH3SVELWGjLOHjsrXIJnD8LVA9L0zFBgqa9xRDuC8mBtlASOI27979mUYw%2FFICYMhjuT7jT%2B63j8Z24iCYr%2BxP1htCjRMlgEfxBpk8W3zCNbyYbQtAqqwVCRos4s8XzIqXnwHPWzIFPMqqD9hNdXy0RryYPA3DAZMQjR5XUYDLWr6RdXtfQ4sjwolFnODSD9Npz2t80zC2yE1Xh4wTz7QcbddygN4HV0nCwras18jRA5KKp6hHM2yZRRbU3rLjz0k3shr7nF0FyD2CHtV2IXguxMN7cS6%2B2ge5MgZISZqVPrUdtJ8VYOMXhDoQSbeZHIgoNac8xa0zjUkKNJdYYRtEdXKHn%2FQ1Aqwj%2BHHceg%2FesPnptzUeHuXnD2b%2BLE5Hor8Tdoo8d4Jtlz41jS%2FSIMYOgoXou0FDuu4%2BwcxuiLCMIOCstQGOqUBXNL0flBeWT5mg2SDM9V3PznVCDASI8J9fg4hF99nLT%2BSFtKgUbKgC8%2BYtxK%2BTQRCth%2Bh%2BLnjIXSefiep0iJnA7GwXAkR9HYyK4feDDK6jh%2B5YCMU9l7nRNMW4HN3VdhxulNV%2FwKz6GuMF7jS7ZDd%2F1bkfNTzpCsEEvFCAhzXfbiZtrRgN951j%2BuCPH1j3BF4nleZlkOiUVnlBK9nY%2Bll%2FjMjriQV&X-Amz-Signature=f5ddda0d36bbbb4e7bc16c50da6062803de7bfb4d1978cb17d72b78310845842&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
