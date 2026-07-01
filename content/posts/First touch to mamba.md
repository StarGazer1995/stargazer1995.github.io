---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVO2RPVP%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T122737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQD0sKxv1jMdABvABaNiaJyw5i%2BvaMxHINlrA8CWXkSCkgIgHnMhmaMkipYE%2FW0qc3ejH5ueW%2FxvUjP2m%2F63DxtD38oqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDKRsrE9xY3zQG7pcCrcA9qkBFVjz9rdjjTTJAAnsXn4wY8ys4qd9b7XFyP8j53WJcBEh9U42%2F%2BIqzkyRfSstQDCmOW4dGebYoE8JA8MEDS6JIqsI3mWPBjaOwrj3LhEwCzBS%2BMl9n2nm9DCSl0WvWvvelVYV5xBZGZspIZR98il2gMV%2FPjS3k%2FzGTVGvBbSgBaKOFtqpxba6Tu6c8jr2gcIqvWmggRx601zuHqCPNK76mkbNb40VWtf5llQxRJJTOSBKKD4psor2vlsZ7LsgKcsdbPWG54gnb3aKLOyY87mN05xeojrZMdLQpnWlPXcsXhwnGGLbJewFIkBPI1nPgHs27arPQ2Y3%2B%2FhO95eZbxH5t%2BikcQCEG3Dd86N7w1HDG5DfqjqQp7ogfAeOBbag1Ow1isjWnUd5QD2IEbIeH4SprjYBXjoGfUcsNmJaRwETziSUn2NRh8MS6eGqGgfToWbTapm5ACke2YZRpbLJE5QhyC%2Bczn1dmtGap5k%2F%2BOMCYeONolqQfJT2jIyBQpyIPy68%2Fv7PEVzbJS2dTruskbOg1JSXYg2K2SoSEBqXOA8O5foILkDax3ZB26ZDjD5WjODO%2FPt%2Ff4deqmYvSGsgfmhxbRdrmVh%2FQ5fgyQ%2FnGN9stKCmP6NOi9sU8%2B6MLusk9IGOqUBNYhoLvwcc0Uwyty%2Bdo5gDMs96r33IoGim0jOC69vJ%2B3uWfqP8crmwZWFL35pTPd2PRtA8e8RpGKswK9qFhJGUR%2B7IAjGDbG2vL%2FXuC5gvQ1hsvgq9%2F4N2j0Fzah0lFrpku8nqoKav9rMh58WYq87rQBh2yOaR4PDPMqt3onhIxeOSUrZTtujaVVUJ8ErLePQyO9I6xNRr7lB2VwnMWRvvuDCQcT9&X-Amz-Signature=90b83928348f6c3545e112273b7e40d28b154a083a1c3a92fca7ee1eb1c655e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
