---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUJ6UERK%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T110434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSMuD3XZfn8dK9CQZOhEU8IWyiksUdfm4BzG2p1NWc8QIhAIU%2BYVNGjwp7dC7MJgjmDxzTLe0PM0Njmo1%2BT%2F07dAkfKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzs87qFgJ2vLD%2BowBwq3AN57%2FRWUCUX7TqpkJ2l8ms8ZoOhXIvOzn%2BBCC%2BxBkLoRKRXkzJpgBpXM3f7KbaLcgF5qBnxTZ9uDlSQEg0V6TGyTDHzoHwAhEFMblVhv4IgntTR9oCiRVdp38ouyHqzXnk0YpltPRwZQDHN60DC6QZ%2FighdjDcI8sULVgqUkFQY%2BVMSE9Gy%2B4U4FDnNJp1AsR1EuWhQQmDOXMNQfEzGastK%2B3kpZFM1q2Z9WB5dwtA%2F3tY3ytrykGdanVZDubmmXiZoVks8HXsy%2BnpYktd3HOinjIFnDq1I99ejnpV8702HJqxwP2K1zkftyYxNc2tMUouM2M%2Fa%2FT3zGtvC%2FsMnh2QWUIrgB916B2PXzwDPLWbp2aZzuF5QMmyUOPq3yGgjRxN7EKM4jVKonfRa99HB6rUXlD0UhWew1xtdrBvyUQqLqAMsxxDI5W6JXFU4WPBzZP1AprLDYgIuwwao%2B5zoDwN%2FfwOen8qgrF3WPjGgSu9yvLwnh384P%2BC0pRiTWrxu5rdMiKpl1TanIEfrmVvl4Kjss1ZXzOsblvJJDli6VA0SX%2FKfrT8wH1r%2BXBjBJKYr%2F8gmTKjwsvDVLvBTMFUrQA5nn3TMRduQ3VR3rOXGXUqtXewGVt32vZ6q0baDPTDQqfLSBjqkAQQYa6nPG779rV9hciLAEt2A27GpEuNX32yZNDpavsICuWzQI8%2BuLp8CIKO8FUwSTxlILUNWAP9aW31wpvJS1%2Bi4dhkp1jUQQazt8JoAUatU%2Bw4BzXhof%2FYcdNz8Wx4tVmL%2Bah8UAtQjcqFWLfKLFQ8r5twZXwXeKjgc4GeOxFkP0V%2F15UKoeGy4PtXa3EFw87OQslc8Wb7JRtMlbmPaaKu%2Fzu3Q&X-Amz-Signature=7a9ef5f6e53a8a6a3f94a86553cabdb8eb959b15be3506cc0fe4d812b443446d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
