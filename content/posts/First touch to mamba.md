---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HLAT2ST%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T042553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDGuMd%2BS3eqmnIkDhrMCIe%2Fku%2FLv43NluvUZVoYNudREAiEA9F%2BI1Ukq%2BIo40P3hc4AF8kOND6wby2Ie2kr1a%2BBUhsUq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDB7CdQaj2hEUMvbKyircA1aLQ1%2FPyGUyCZU%2Bl1eykXz%2Bre9WfsDDb5YjLNB39mebA45AVGX3XaggIIrA9S9o3pcSLtz0amGnuF4ab4LbRtrtjoj5CoNslT1KWyhp%2FUkiMhOmLgrqHc1pXpJk6kVYiFDwGXlxW9CJTIRZWgypvb%2Bgi%2BkknvVfeWU9PZGdKcmo%2Bu6b8OLL1HNRn8tIXUJUSSaO0Tt4xrE15Gvpiu%2Fu7yP06Oey1db8FDxEMte3mKUm4v4BLCPx71bzvxkMwZJqNIW5tUvBxB1LNY54B0jmIndh67pxPwGfxM%2B5LMFjzZOhwUXjBST0TXcC0kkKC6kfpAPUkKIZbFh5H8d0a4YFTx3FSdSU11u1kuo7ZgayUwbqDRfPCHQF9dL0g2mPK0Xms9%2BTelwkb5dgKLbDtU7iNAOOL6PhYwU7Hpvw1lI5qY3dmuyHVFKsven8Y1poCEHZmGGFBZ7MczCsH%2Fbop%2Fy8Y58qOBjAaWGrtxpiuKEePG7cjiA8KSYm0TDaiA1GX%2Bpkbwtw5rOXr%2BQM5z9ohayJ8gWdK%2BeteXgqxdLq9CyWRE1U71%2Fcd3QNYXk5p0IwpLNDMt38HXMoemCbT0B0b7VSkcjYmSCSys0KquExU6pzDXV8lLRrN2dZdMlTQK0cMJaelNQGOqUBgGEcJAuScTkYo2RDbLotpbSKXmFFgCuOQffDDa6GiDLY2hDTUxXbxjE7IH%2BbNXv5qoXweYkBv1Ty9hoz3cOS%2FrSV%2FdpPsuWpxAN%2Bn6gXJAoNxqCVbot9oTfQDnKEEjqloaPZMxNKjOmfQX8tvRMNYwHps8nZvOT%2FTHl7TY4Y970d25q5gKmlvzI3DEMTHDSldCSZKS7lSNkh4%2FrHfebdCkDdiwWH&X-Amz-Signature=8ad25e70ed7a2b77a9c55d5508e5367dec894347a49db4c1cf3c8d5a66061680&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
