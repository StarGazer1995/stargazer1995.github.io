---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VJNEWWW%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T020429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHysy5Ym6h%2FIrPYGsxwPO4Zv5SPNVs4gsrOM4HtH%2BqL1AiEAg382rYk%2F%2BLvNRdEWWSbLkXc7fwa%2FjI6FiKojK27JG0QqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGUMFzVn4MOj%2B4T1dyrcAyucVYzMZZhF%2FDTkVnnh6oXBrTIxMLa42DeUXoY3Ux040xkKaE6keLdo69pu8gVHFdDjfuzMrG1aAZ%2BJItV8jyFwtOSm1VGBAAVEiPYpo3e9%2BSh1L2T69Hdh15JqZ8zJlBayGJf7z4PHyMQ7Aeh9tUDITwnSS4sW3u%2FccG9dVk%2B0Wf3qSY0iWYjKDoaCCCqKPVhzXqHnFlRlm5Wx%2Fi7Y4DUvPtW15LSF40tNQKzlKVtDqRevHQpjKYw4qgrzOFHJo3kYCF3psC4Q%2BeeszvXdb0oc6eXDge6%2Fv5TUeRQCVW2ii4zb9oYTtMDrp2QUHfC9q6q4u%2BOsZxaR7lPuxWuDLDmVxGCVKiM%2Bw3FFU9BD0PRFV%2BkWM9xLNMj4OkDzyM8DxZGfBLM5D0h6B2aEvrib3cM0ySX2RlhXDJumHCa1U3Ica9lYFRAij%2BEimUcuohIF%2F0PZiYVI5BSKHySO%2BMe%2BrIsqIOWHXD5Pbzi3QXICktfeIaaKW3NAd72FdsflAbrliVL%2FjA4CpoTkGFt6z5ZQw5VsklthUrg0RMzNxVdhqbp%2BBUi9qiebphS06MAN5VQUfzTydidYAhxXg01N3RubtV%2Buw%2B4Cv7Mf%2B6MeMc4QsTvBvsFUWEAGdSkC1ydvMJe5jNIGOqUB6XCUhFD13q3GekgKxuXBMVEwCK%2Fk8MzrHHnPR6eGeM1UxvF7vnVgYIYvpxKbqzwbA4A0V7mmooV%2BBdVrTZFoucv0IKDCpsgxp1iTu4U8mMpJVOWy4jFsyLkgPCXbJFM2Me2oiFDu%2BzHo02porp6fzOJgKtvGRcGL6a1EfntV5%2FMPbonPutR0Gqp%2BtZd3zZbwYqpURyyREJLK9OVSMY4PYo4JpXY6&X-Amz-Signature=64671abf795b38c2accaa6a3deece3a8b234744a7d541ef7d48879486f1afc04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
