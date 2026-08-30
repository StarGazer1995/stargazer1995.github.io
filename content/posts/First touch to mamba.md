---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647BJ5EPS%2F20260830%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260830T093234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC13S655eAAUZ59HNMNX3bTEGu9UOflEyWXgR7Bo%2BWpjQIhAN0aiKJRNC8oZgWZh7g4n1xI89Zg8wCYGCdr2qtwhx8jKv8DCHgQABoMNjM3NDIzMTgzODA1IgwzEnXrw79Wi9nbj8Mq3AMHBv2QRye%2BREUk%2By10zFrrzJD5jqvzFmUuql0%2Fxk7uHYjItKeABsejYgnjINdFyXTBmOoI4JqnAuzIMG2%2FxG383V50ZQ3H6X9dGKOlvQZ%2BiGTPb%2Ba7GGRhawroorDTGzTur83QaGKSRfftD4EUkaCcpH9yq0D9T3DqtGREDk%2FfX5aRTbyQb8TK%2Bbz1ybO8SFkypAm51TI9K%2BySAD2Vvt0U51EOJovHP0QFS6xyKPwD104imR7O4IisoO%2BWUXosa5RiZOJYvQUlixhPO0qFCVopyB%2BeIfECAuhYsxzCJ5m9c%2BzhAmpLOOUMUGHSWZqG1CmwsHo6uOKTARIhhlZv1ggGEV0RU%2BHhvgk7sFaZQ7wcFbpcU%2FRFc2KHtnyysiv0yZnwAZ3%2BfOgaq87p0E5oY%2B0NWqRfD0kroBGA6zteQsmNeCv8T0AfScSDDBC%2FVrJ%2FWM%2FNz8EYC8ba924PRFXIkrE0cGvBE3I4oklSh0%2BZUaJlwK%2BtUyHHeZrSFurQcHZOv4IfeIa1XawiTmkxA5N4%2BM5cB7w%2FOTHJGMPnRa7rj123VrEPiT4hw5j5fTwTFDXdbPSD4ibVenRN6Du%2FP7aWFiSfUwneU3VQUamhju8xNkuidTke72k9FSqOQYlwDDCnr8%2FUBjqkAQ0%2B1ffEpoYoPLCa7CxVtgz4IK3ZkShgHCzN1oUmMPRQPe6XTjG0zDSuVjJ4UtvnC%2Ftsod0e7mqsYLJLZpExBfb9zU6vDK1pIUO80d9xf4MRbGx4oYr75%2BG6BavC2RXWgVyhdVdhhvT7cAXIj09bnLfXl%2FLeUp6vTBRAGQg4dgCx6CDjDYfAh2gtg6JCmVFo9rCuLSQbYt1e04tOW14vpIeAZbqv&X-Amz-Signature=517d7b178e77eae3afd22d56f2967e7e50110c605af3f367c307cfed90190050&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
