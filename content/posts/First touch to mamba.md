---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZZVZBBP%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T060103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6cdcEHkzY6vQ3%2FgOnNT5poJxMDCvE5YBzUDZgbK%2BNnAIhAKSgC5Oxi2AleqGIQ6rivfxuDprUNdiocJnfzqpECUzJKogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxTpgnDEgBReo05%2Ba0q3AOpbwWqkVZWYv6e%2BSjg0rMP%2F6TBwzIzx71txlD2hsvVanVhoS8wDoGiZio0wqttCEQd%2BT7UIZXVwyefY7Ol%2BZM4BsqHYZoobxP%2F%2Fy%2BOZI78sEQ6dL8TazjXTRt%2FAM0oHibncwtyIkwGxMYZtJbQS9d11CToxd8fRKhati2tMBvv4oAGGv%2F9Vt06H%2BqBSxbg%2BNOQ6SDXEtow3XlPhGWWlHL2iYTffzJAVXWKT6MPzjIvCci2FckqKcTu8kJoysTZmbcrVUYcYegc7Tl9OX7eQprdiE%2FiLSvPpqOQKLZqAEPaihYq6DmgzS%2BRATtiA%2FsIzBpZOMVDF8a%2FQns3sTkzfArPwiSt%2F77hu3zDC9x5lGL%2FyKKaq5a1B0tuUwZWpYP4w55du8rYUbA13BeamkBQaGi3%2BrxUCddelrPIgisGUMnjls3SF73humxTCmoYAa1FViJwEGSFcJbaZOnzv5h2DiJp4TayO6eYuTLDEMI4TQstoSwNJrNQmsHvMcyixljY4Rcbi0YXfDztJ5l1MtOitlATETb%2FZVnCGl3tQ2i5ZSjINSAp6w6to3B5ntptpUWjzwAxdNfrxTIuNh92IT4Qy0Miz6zYbEct%2F%2BPj%2FGHMLlBmQgiPaYhFGAB6DEgBFDDrrd%2FQBjqkAWJ7harHiYG0hLALJyYH7tYD9vTEztjSlqGKe6nvbgdXPf0R7dflBYQxRus5pWhIu9L6m%2FMGd6BeMGg%2B5WPLC3pYFr%2Fnj%2BmrRTPX9aE%2B5u5rICLHXAb85vcBATQTqtvlnMVg9Q5mWbNPy3GWl%2FS8IyqjO7Q5PqWZez10UNfBlrcccn0R71harc2pwg7AHNL3goretCvJeky16H9AceDJQooj6RTC&X-Amz-Signature=3cd32c217ad46b51eaa1b2f5461f435f8caad0a7a21bd0b3079f80155c48e72b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
