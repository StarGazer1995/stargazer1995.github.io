---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FWKYECG%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T202203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDu8Y3z8V1irGeZaxZXfi4ccBrOyh4mK2d%2BrQVPOBPc1wIgLrastB%2BW%2FgF1eX80NNiq5thDzpjkOSj0YBuh%2FJ%2B2ckIqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA38xZXnUPLWpLohiCrcAwUAXrRWZvlqGLXczwaC%2F3F4k%2B%2FpUKnE0PTjs%2FAL4YWq8Tdb%2Bu1F%2FkYa5oJ9Bgyi92aUwQafKWam2rZGnhxqD%2Bxa3pGm9etcH7BedGy6Q%2FmwqgLHwht9XHwOpz3jlhEIkQCePDoL9XUNf7b%2FDlhMsZROc8cWiLKgI%2FS0FUofO2Qp07K3yk%2BhEMPwSbNUXNj0zAMjuCJ035wzx18SGDK6fzTeJBPsTcn9U8FqMxvkZtXRPQCHFsBuv%2B%2BIggmMEEDOL4zUFYWsW2W0ma7skkano14WTzMQGJY686JNturtXtOshsL6lw5CzzuQLpY8vtkLFUsenaQfR489eYv5zZrxlZXkB0%2FqQEz6yV9n%2BSjLeoPGMGIpaSdfn%2B%2BX%2B851uppISkjurOEu7vv%2BE7B9QHbgSyI6OUYTw61KcNKJesxpTdHyA1xOnJGn1SjR6S03MEVRlPfOKMzhY4R%2Bhx%2FncttjFDn4hVpTZqXNBWWfLqOLSPNHTemn1nFRTQA38Kly8BgvMNDcAG7pKpOuJo5aGVSeUVDY0Y7ccBJmfEtjHAbYwPgrv6QgluZhiTB%2BPn6geA0rseQrj%2FkdJgcNoRjwygaAyeblDkkEUpFJC0uOI%2FrxnMWqCoTaC81VUdHqCyqcMN%2FJotQGOqUBVtUsOX1A9rOYd7jm6uej%2Fj34I1hVO8%2B7v9qNqX5eVYjPuTYdUBWpCUCUPVUty8LUh46E%2B8IUZqLljfyKcjm8kT44jz0LX1GArYC9krHcjoI%2FLb0xWZI63aZT7Zf%2F9bAeJHxuCafOwb6ZViciPFXJewnsMEF04aXga01Iem45xZji3p1X1ZOw8%2BbzeOvHciJE%2Fj88xvwZQsxh4CMvoqsZtzo5KaTZ&X-Amz-Signature=d0a7781c4d34ebe5ce88a18200ed9730b8ffdc2b8665f539962eecde887b2b2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
