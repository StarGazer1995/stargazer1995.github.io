---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SLYK26J%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T152035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJIMEYCIQCfxOwPb2FuOODNwVmp31cjpPub%2BpjlpFiO9aGRe9obkAIhAM13OzFfXDCArizcgMPRtnM%2Bj4enWRgfh6eNaBFCecmLKv8DCAgQABoMNjM3NDIzMTgzODA1Igxpd1K%2BBXAHqEqh8kYq3AMJ%2B%2Br18MQeixvuz2KBXBqiM2EWrms9EZbIHpe3XhHh3MgIXCtxdwBRwtgK9fWKTuVzcIC3j0qg71pgleMOI2qAoIWLcnN5MPBHo2W5v7fmxp8XBbQZcoo3pl1edMzyhcTtBlgCl3jOwSTAPUKrcc9vhPodnzNWG6eUn3%2FDjmI4vCSs9DySBmrDzJDwjKuQOxqBRUcD0jUwm4z16jBd2wRU22A64y7JzzrceyXpnZnPEDmhEiSipJEh9%2Bslyg9ivvsrU9c1wZLp7luJoIWkHQzvhHH2NLY5xT27yIHR7cDqRvbTiL5mnZ9xMflABWgHK96YevrOi1QkxzKhzDPDcvG%2F%2F9OJPQOXJl9zPdqcZjKw1Xozutu09EfoLsQKhy%2FbrgMx9Avk31M4dt9Qrk3jLGYz6cxOK3onOcMLJtcPQOCUJgtcZX73cKNNCG1RFb4PfYY%2Ff4Ed3mAncpmsJTzW8mRhly1wqdD8QxXzFpmY7uxkQ7a2zJ0BS8avyqAFCp9lM9GvzV%2FS8b311QpYN9aO6Ny9SYrcVtiFL8h9V4iVUOmz%2FD0139kFks5WO1KjTwIJiw6qJP4xjTDKNJu3sUCPixachDwA%2FQpkYgYqtIi1kXk9nMIKGPKhpRy%2FAEni1TCYgY7TBjqkAY5tJJ8IcNdNNJP4dEzdBDBSmAPULLhsct28sRD20C%2FakoWzXexR5fxwMUZFTQ5Uem%2B3RNceHdA0ceHasF0AarMRQPc6QpJFuPQWhcdKPpMDCFUSr3l7M3AxdboeY1rDc4LQV73B1O6pfdYgQk1ns%2BC4n1oIO6ITZfQAPv1E4aMc59BYv%2FsdtBARDwwugb%2B0EioWKow6IQqTtXUmr1WtfwrFvnDU&X-Amz-Signature=c1751f63ed80481d0a87e4b892408a35de81dde34f5d3951a28f028054f5bb18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
