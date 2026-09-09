---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466245KZ5IT%2F20260909%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260909T065053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB6tbjL%2F%2B%2BhuZHj69fENhVx8ZXyi3EMYwWQxeH%2BrXH1JAiBG2DVZylc%2BR%2FtHPUsset6TDLO1JLbNrmkDNS7QKxwbsCr%2FAwhnEAAaDDYzNzQyMzE4MzgwNSIMAkVpXNVR98W1I9XkKtwDPnnpoegjD76sWOlvzCSfAJWy1pNAXjRD4CY0mtndi%2F2lkEzFyWFvF5hlDP6pZ4SepzWMrXaKoj%2BwxfOYDN2SayJOIskyyOulSN4cwH9gjUsa1JES98hF8IrHAE8sL6TMLeq%2FUNdMJruGJAQ9IEw5qhZMh39rlQAszEtHj%2BT6G6mR5N6XWxQeG22UulwbUMhYwc%2FekEyQ8cyZ%2BjmpJSbxXYTSt71cx6ONYEAfwfsluLjZKwUE95dhes5l24cxmgEeis1W314OFh5%2FX31%2F8HPDEpCqnmtLKTDLyAbasnj8FG9jLUKfn7ac6jyt97YCau6bJgmHsoGKBMwmlf5R88kyhWZZI9tdH9cILd29Y%2Bmrg0wdmLRVzCBwp2Ok%2FWjZVEU2pE7TN%2B1caiO0qmFzaa0NNtyMmnBq%2BuNOGNGk9k3c6Ss9chA1OvHriIHCJiNWOD9sA1lE0JA2i8FpJxUVyvdnOBqGYCT0lURBYOLFy2czdZ1h%2BYY1M4h02RtZyIESj9Bqv9Y2qS0hhtdpRvAUgdX2bRPxaYEILPPo%2FwwqYfBxcK%2BXOOofy8cHweXtUts2bAY%2FepqZC3Cmq3SXVG%2BYUt7fksYbrsMETFT5Wx4KqXerqZjAladhS04eH4KczpQwie%2BD1QY6pgF75hcNVGaex5gMzK2mBgMDYqsyvhF%2F89MH8NH3y%2F%2B2V9Wt0uxduHjooDdw2PoJ%2B8TZyDdJRyN0kdegIXsvP5mTtzsij9iUiDoWyGlfg1NtbEGXqmIHEFjYjqpRllSwPER0ojiT2AigAUCgr9hwQq8pjaa9MapmMe42PTggeC6Qvq7%2Fe15n3LJEC0vA9dTDRJrCglfJl7eMHMyES2d%2Fc71Dx%2BAscZsT&X-Amz-Signature=06fa502c8de4c63ca28981f5e99efdd8742a7df91eaf0f03843200e292e1639b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
