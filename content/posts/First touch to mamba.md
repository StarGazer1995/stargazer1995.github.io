---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQ44TXXM%2F20260615%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260615T193802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAL5EGinkPUETp11df58of0nsckTFfEZ%2BKNU2vPQ3HysAiEAnOKJRSs3i6%2FGBRa78zW8R856zmgKmoUT1CQgnInksyAq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDI11SPAZ48%2FX2Y8abyrcA7LKUt8E3YGCUdCrnILvK64GzYqLy8T50zDXXDNspBmtD7xF3Pf%2FtDLjiMecy1mzdwoys05r60BEioBQs9Zkjjp5VkTq6qWAWzptRoEwbKh9CSiDaKQiKgFh5K8feoFuIazRvDxjDxs8h4xP9uycglYF1iZyXyEoI1gAn5rjwlGr65l97hazqn9NQ%2FOoLWMBeOlFpzulH%2BQ7Zb7tI4q5SbKowSrz7U%2BzEVwAsToru%2BSqKwPkvXSRCclAlFgBvrwyBl7EGgR3DbL%2FdmMRX7qsoKI2eZjDEfeP0qTcyxi3s8xdUHkGvQKD77UbqWXTKzG6X9fYTySMfrCPg697ADd8xrNQcDuSrmfl08hP4l5nkipJGfz%2B3aCeQQ79Z71IO6FFsKr4y9pNHwiUhhKUMGmTEc3jyESKL8yxg3e%2FAwuX8CRxrHzgLxchykpdEsjG5sj6m0mW5bjkiBSMK7JG%2FmUIwNpy5kKzMBvdI0qta4IKz0Ss69GPSZ7nlbbSRQVk215AF4kw6mA4%2BGRpTIEWAzKz3YmEwbdCEqH9a%2B%2FWFSs28ObQpMcImgrGF8eiQxYD2b01xDGnroSlxiXFka5wvu21zapmkyQsrhZP%2BAdcdj5ZkJe%2Bts5LYHKFA6LQZeL9MKT1wNEGOqUBKdEy7W4I9tPNPUiJtG1gmrYmRFKcFCl9ApjTv4YzyCvykCwJQ%2B3Zxz%2F0FNYEV%2BeYArHg7p60wN3ibhuu42qkzJeZRauA0Rt6l63AgJqD5on%2BRJq0DAUXJtcxqen0zAu8zom%2F5gccdxdfA7MPZSKAwYTvgPXaLx728xbDoqYCoxVwIQ3QeEKhtt3fPAqJRXCiiasD3dXKMfTD8LjKW3eA4Nd7SB8Y&X-Amz-Signature=b70ae5f3b8babbdfacade7e40a88e13bc83faf44a97760b7ec675866ec7ae02d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
