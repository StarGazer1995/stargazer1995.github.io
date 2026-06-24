---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JFXMXAB%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T174723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJGMEQCIFkyApR%2F2jlh4%2Fa67k5j%2BQRuI17ALRXOqcO9ZgOSXcR0AiBvSzi7x4%2BP3gyrScJmouiLpnz%2Fs0A1hgGNXWnguFPSjir%2FAwg6EAAaDDYzNzQyMzE4MzgwNSIMF2d5%2B3b4qkbsZHbdKtwDJHHq05p8D96fir6A635b8Y7aiaDo1rhhqnUbuUHEFwXv5JneSy%2B2%2B8KV578yIfEgkWaH09WGo422qrGG67B20Fg9KP2ZEdnsOTlqC3pO68Im%2BfZ8aBlSCEhtjqLnwvOqccAYrLTBCedRNAfY6YEadNbiIOqlurFkp8NgevfnCUT26pTjtsX1T8QW%2BFV53mO0dByrIlB72XGjdX1EbyKxaU6IM9VYsaR6kmMmD6CRg6SyTtan38I%2FFVGULxZ2MEe3PkmuONNWE6gqZxKNh22cY7DJJgN8PHe4M4Za73ArUwjQVPMvnpV79Q5C66%2B%2FGmjBWhhoW6XKzVzveZ8Soaps2UAFyaW%2B%2BL%2FOLPzv3IGIZMCqfU4BLts3%2FvwciP5GE%2Bq6LUEru8CyCkhDIcHrxWXsTvUFZgfSCFevFtKZYixUMqv8w7g2nnegpJQ1%2FpQ%2Bdtd%2FDCO9oeTQyJqA%2FPn4ztMI4rH9LpV8kq0GlMBKWuFSUchfgKV4G%2BjqcdZK0M6Pi7a1jyGo23aiv458hsB2gRg2D9BAXB3vkSBe%2B6ZywZPAFAjVHg8CU19aMy%2BGFECZiZ5cMxhqlBiR6bk6ECaDvaw%2B8ez%2B0weZJGuJWCY5ZlmI%2FP8CvYe%2BvE7wRTMKO3YwiZPw0QY6pgGSwEqlLW%2Bg%2FH57KFotbL1bVd%2Ba%2Bw2POnyRfSv%2BeroK5PXtzuo6ENl7%2FabBwcCcvpxTdxk2oKsiEdZ0E%2FOCGelRraRXrG%2F%2FDAFjNQTtat5zidNUCNBTzdKYw5YWMgttF2lyI%2FrT9GBT6BenFgbC6KQHq3eYt4nxsU7IMDcVQVleZuOyZQ9IARwR1WL6XlbtUifLR7hF%2BbDPstIlD6v5PyLQQpvB8jTy&X-Amz-Signature=bf2be23b62db7b42048659ac7b3583de9fb3e445143a902e8d79124a71ffa231&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
