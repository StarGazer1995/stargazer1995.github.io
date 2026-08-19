---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEEWNODM%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T122025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDLMj9AFfjyySNvmxJ0k4pD9MX1lVLlw%2BAGDWYKAvXkxAiAke8e5RTJSR1ZzJjpI0Oe4%2B%2BRNej3nQ2YVeCyZuslMOSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMTT5vruK6%2F85W%2F2jVKtwD8%2FguhzsKD8ddDAkc5GeJv9zMgz8mE%2FzbvPJQ15n5d4x0WkeeqFN1STgfl1WlHwiLUHvvwTIQvu9OrL94lYdmck24xg6q5YLktlRwAdZq1Y5NAIJm9fYjRBZMa%2BOISxG14I7ICqtNqc0DiqYo%2Bvs%2BnyJ7pr%2FOgzv7ILwYZIr0tB10c%2Fdu0amg%2BU6oIgbKabUjwaFqKpEkymfI6noEJF2TDyzqaPcBOyay%2BHgci8USgkl5eV2dGW%2BguPPm0QBfdQ89LggkAmZE7h5PaMw%2FEYWNGtZd304KdMbYL0PKFM0Edt1L5jdIIkXgl4FXdwO%2BKIqP7nqlo2Tzrave7ajue%2FWx2YO63BoAIOJ3kTfGNuCcnbqtcgQXRLbPyNZrYJtU7aL3ocHDgIuDn4sW2d7MjWwNu%2BF0n0JjhI5sdnaw%2F2I%2Bfp5kaTA7TA6gSfTFgD2bo56%2FGyO2mhAbngL6tUL%2FUi2pjSskp4JUcqOEjfwc6YlO04glRO%2B5Rv9JOUIfp4nWIOY%2FgNmQT%2Bz03vbvOsYCp6C%2FK0%2FAImOuj3EtakK6Ye5Xj3mJidUbHhAiIX5wWh2%2F%2BWSFTPId6fKPtYvjNlR%2BDKti0frWXrnOP1GYd4mQi%2BB1o8BRbjk%2Fri%2B6UYWucfYwlp%2BW1AY6pgGVScaLTmoidqCj5ysi%2FM4sNxjT6bzXeoM0ccnVQxUv5AYjB%2FdbrwiZVOxTpJrnZIIMCCL9jZ0ZqxLLQZmQSNBIH6vGKc0iDW%2By6hF2Arjsqlmv7EQ5kNSo3nBUuHe2OfkYvWgO%2F7HYK3lI4g8TkYZk%2F070W5aLhyKZ82XjzVdIcqbOZ7qK1Wq%2FalqcVuNwhKf7bY9Ijy3tmaU3t9Ll3tv85jaayjw9&X-Amz-Signature=dab04d3f8be474902b490be115968e804db2f39319c885c67c729a7950a09655&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
