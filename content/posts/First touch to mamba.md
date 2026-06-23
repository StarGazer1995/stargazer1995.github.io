---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNXHYX7H%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T212259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCICGZ3SjRhy3o%2Fo7kPb5jPYoIZIRfGFtIvx2njZ0uzpHaAiBsfwzn2kAff2AwULHMKlgRhsLn2MS16PaKurxGJK6tcyr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMS8ZmhO55%2FLRglsyiKtwD1FrOS%2FIY6Rr5e6d%2FSUp%2Bk%2B1aw0epbvKI6GmgPyc44%2BjkZKYlvmrpuWZyouw7rHF%2B25ZOR9XWp9FdMabGHaPksfmTqDPv1ymnOQEaI6NDJ54giANgnvbFfgfLEOVmWcgi1rrQnRNH9ynFz1bLMmZBctOF84fXvsI7naBoZIbO7W8FYKea3yVAwTyoRl63%2FDVpdQ3ELZsVn5e84GSRUFs0n%2FBGw%2BSYb2s4m2fi2QJZ0lT4Ejl8vKQFmdKEYmkNi1U%2F8HI12Z5bEh1nEOdxOPyhE0SVhMiRkc%2BrpFBlPhxbQzuz3l5gFpyCx24j0J3jinLnZaAHHUfPdQJ25Vk1Mn5VD2cn8IEQhNGRDy7kn%2FlSqXkfY3GP3nnR8aOR12CRMg7PUGJc3pqEN3muHADck2XuFd8Wd96V%2FMYGvtB%2FnoSLCrFcz98Fjey4WI9d%2BJ56yVpQqz6AAQ9MiX1AIm16w3Ct8dvEYJJMNnyPUwImJfafVZ%2BIUplBYuirb0xKfP6qczui2zv8T2AfoSOXo5gR58VhozlpHlikoywbPmscdXnpJBezHHokVr5V3qMvBnTnW1612QwgBptMY7Db6KUrdNHKiQ4BR9ql%2F2lJpR3tPK%2Fpsxn4lTY4%2BnW8Dau9XP0w4LXr0QY6pgFAuHGPrikge%2FqCb02WPSBtIbBa%2FaLpb9i15cisd%2B9AE7FR5tIHiOY%2FMm8YKpChelzFotbX6fzwfyUx1cYJspaKTV1a15bEUqO6%2FfRJi%2FC%2BDXhp%2F3ePqqiHs0boZ3xUUaVN8tV6xg1E1wkAo56StJgzdzYk7qYInAeoMBs3TbEvNhU3W9fNbFeOw64aDo0OnSHSC6P%2BiSvVx%2BfrxG1zlLH8Hck77TW%2F&X-Amz-Signature=6ed71fda0408f0022f8e06924df15413f43a3822b9138e06d5a0b1028f610b2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
