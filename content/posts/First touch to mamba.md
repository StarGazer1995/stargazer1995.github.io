---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLVMCTBO%2F20260714%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260714T094458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJGMEQCIEehSIOCDEqTcI3Dz4gmD669u18GfJQyt1M4K6dUIIDXAiA8%2BQ79dSOqhpMQUbSau550JK918JThQgvqsPLbW88KFSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMLOUrO1PGT5jbFUFfKtwDdrdW5KhvUz5bkbnkf7qurVsrWpNMO7i52hcSHYS1YlTKtYG0Z8TVitsDHcWZAqpDIhnQBrpxayNewfQShhfTeoWYIiRfceZPJug3QctBBnZUXdxzJ841PHOy2K18CIYMrd1euOaH%2BbnH1RJbdnMgv3QdwyD8bQ1TZujU3eZbRkQIRY8MAjC0Icp6wrENgEC0086%2BU85jG%2BgEUQTycx1%2FH3WxY9YtedM9sW8FfP1mcTTsPQdmJE%2BtxW5KiqmqwXuyZUwwSBKLKM6Wk1oDgEyKqg3QMf%2BcDULANOuaLL0oXAa6rQ0Ts4aGI1tA99p2bDZ1l7VmxzhZUCjZGp1y8SUiYwWIcEt74MaVFP1B4fSM2jlZ2kU%2F79m0qEw8%2FaBNz5zllksrxAPYl9dNFm1KvSYYna9TZph1%2BWzfF%2BBr55l9zIVxTu7uRsCm%2FFggXBpVSZP%2BhWaN5Wb6rFV%2FhQ8roC42BhdZm%2Bluctl%2Fqdj5M38PiXvvHFV%2Bw2mHydJony3uPQyMpQM8yU1kr5R3JP1ObpqgSmBZmOZ0qI4H7qBDzYO%2Bz%2Fq8Yrt830S%2FXdzza%2FNdOfAGHLtYDtK%2FedWrotyGtYVx6IOTTcD246A55CSJOhrF6j0iByctFsiiPCnaDMYw5MnX0gY6pgH%2FWBynn%2FQVBe9tu0%2B5tupaiicZ%2FmHxvxlFLtRyaYaFsebAhGbvmCqvpQzJNNoOfyM4ahkTQ64mY0SytDkY15gjqBGYaqkY4gXMXRYrwc7JVneyvcloS48DIfDNXsBVxW24JQL%2BG4lN23fyBfLutwOiy4c%2Fu1wn1TwjKtHvLIjG9Qv4MBKTHw09RDBx1qZWEDAd%2FEFgm7O6RXy46bdgZdSQsJVS6gwb&X-Amz-Signature=67fd7c76ac7f88559630ebdbdc55f380af9690baa32845d8a1446c971ee45176&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
