---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XYGBGHI%2F20260915%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260915T175135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCICOCrr5l90%2BmRNhKTN8AlO4zCW8vjeFlQ1JqQbeVO9MuAiBDpoymCsMhlY2zeYqloH364ytjXEyukUnpzpYEsOdRlSr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMU0g5BZXhakI7fHyzKtwD5YvR8%2BVlj1Jtc%2BbHvVShpVFCMFGo8UjJ1%2FfUMaCFYNq6qe0VtBiDUSgV3vMZTZa9g3bizA3zAHn5jyly%2FWMTVDR%2BBVM1MsN24dvOsyhZxQfN1%2BR7GQxnNRqJU3YDLde5TVHvZLLSnudLiZSg0wZCl2p%2BFwsNv%2FEVA3VZ1kLYX1lSEnrP2%2FCaYmlMg2u9RicHsiVDpLu8mCxEF%2BOvsCVN1%2F4OVw1j78oxPiI9wf459xBwYFgMH7o97bmvtQiRX8UEzZQj7N0s%2BB%2Bmde0j5VmpclrpSzyRyt3chnwnHHt9xjdR9litEktgDBt%2BhTCLLb9N5ZyP3DlhcDUmoSmJLbX7%2BIRbY5qAhk9OTR63x4J0U%2FMq3qPlGNkA%2F5583I%2FnU3FYNmzWV%2FS0paU6LXBAKaZiR%2FeADLj3R%2FTzBlq0Nr1aevEhReu%2BHN3ekxj3yJRwFcg34vwvVSA0VWpwNk5YMbO5V31Lh05S3uI6invE7b%2FTtv2NrsrY7nPv%2BU4dcczepHhaQzh93bYp1vHnl5kwJrwEci5JinccnOHPm%2FI3bJGTrKpX0UK0Zu7M7%2B%2BaBMzaZ82vQHvpqc7RG6jxv6h8WRLhElKb2wDDES2K1f5KW%2Bij3str%2BO6r8QzuWkvlSo0w14im1QY6pgGeQyRDgyiJ6zkWymQr1pjf1K%2FfTxc9OazY1%2FkSh0wcc9%2FsCetPe4gHOS9nTZYf3lWzA6EgQwo9HDpqyu%2BiFzYnl7MyeR3P1RALXqxEoGYmlRcSyz99M3B1iXHEjkvJd0fiJL8y7hJM844spXaWWh4%2FVBsvMCa7tjUrh2HXmLFV5xlkQs5sFIi1k5Z0wNIXdUgqsOYRLSRx0c33Dq72kPGWG5p3jwyF&X-Amz-Signature=8a34de76f3ce609c6ad74d3c94f93e8b280a5fbf36fcf06537fffb24548a2c38&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
