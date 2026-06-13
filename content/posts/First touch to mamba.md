---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TDKLRY4%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T190553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQDsnrmlzgkgEyIAzmSL%2FWDUreDvGJUMJGTBJRICcYGupQIgKPutAxtUthfOOFdiW8GFfNn4cxh9wTPQdhK2yU5Zwkoq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDLTBmtIjdJyA%2FAE2KyrcA5km5K%2FCPqrEfdedJEv0%2FnSb8DcG%2B6p35J%2Fckf6iQx6TD375xPyCbN1PT4jZ%2Bhuj15R8hpLH4lmHi5cD5yJf32MsRIR91Xl1OZzd6uSmw1WSp8nArlsH4Zvc3p2UZhpEFuXTAcTLd%2BSeHqVDuWTtrsuul29jK7k8%2FAklZoG0%2BoG4nMvWrvWc%2By8we1FXeShBUQXV7EC1gSE63QvJnvkMtCJv8x8iLOK%2FJexuxjfQq3sLYPpraHu75kWY9l%2FU40t98tmGU14OfhWfg4EvfH2cpgW5hLEkym%2BlhfwvhYj8h55FHLC6hIKB5BzG9mnOgphY7uxvoqVx6ZCPSTw5VeD2DcQS5zzaQbCR5C8vTI8gFwVh2yVPhFOpgba0OzLY%2B4tuRj9okk7nVZMpHo%2Fl5aVO5tRuf6TM%2B1P2GuwjB3hCNxFk770LsC7DGv9M11Hn5kite%2BURGv7rxoC6ZKgQAVnClqWh0KEfk8H2omPgPz4L26Xam56z%2F%2FgqHAhYKkel0oovTWMc056OMsJnjw00a339DNKf38IuA9MKoE0lNORLUARxSMONsYeBbEVcLXTlFm95o2KWdGbFh54rNP51gliB%2BeichhHPp02ALLwTBFSRqvqEkxejmUzVR6zhuWknMPXIttEGOqUBbB2lr1cXi1urZ3GloxhE60%2BIKhyow7metsDU1TgiK3B4CmxoxBWZkbrVBIAU56cOl7PiDq2svgzZ1YIp0aFoGThAL1Mo3O5hYB7Doeao7rMPPWmENZSKoNggfUEnvtcqwyNacSXT8q%2Btev%2BhihgF7NMMUeLsEXMDcb9v5AZBn8n8DXIWOlcA8E9wCl5POjtkyBrBjAKXYlPGe3%2FEq2YSeD2RSI3K&X-Amz-Signature=7644e904e0d6470ec4ead68f1e298217df29cde6e63586d7beb199c48de8afa4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
