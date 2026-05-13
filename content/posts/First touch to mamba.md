---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666A5YU5TI%2F20260513%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260513T225630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCebVcAgFUmyjBMI6FEIAUGmYDwOLk5ntca%2FVyZOzVyEgIhAKuGIRy9xlFc92dG9KjOArHD%2Fr8GdhABX6VPswvqEQOpKv8DCE8QABoMNjM3NDIzMTgzODA1IgxpWwyC6bAFIHjcAicq3APro3lZTB4Oz69Hyq%2FyO5tDFVsQBMPbmNjU0pzZbHqUPvJCLENmvDfdTMj526KyeEr0zSM5LJzu9hb2AGXN%2B3p5GrZ3KyDc%2BufNUzNahoPa%2FkT0uzrEoer%2BvqU6KKZNgHY3KpixrPxqmzrUdiCQIfH7kRqgjYhg9j%2F30Ke%2Btlr%2FdlatlpovMDAfGRqJcmaJncklhgZ9iGowl1DR2aVTYDGZ6QqEZWyKhOXkXG5GePTT9ptg0i5afiSaY3iRkskBPxR7IAdnzQUfOFIIW%2BHFLCkxv1%2BpayOvM7DW7BWzULnJ1htKwY2QtNU%2FGb8wIlshgzKVXpE6KJkCDaHnUr%2B0v1zVkGAnPeje2YciV6kxc0WfvxCzV9PtNiiatLbafmPqnRXEjpIqbwGJpNqqVct7prebBjLHdLF49FAnmML0sLYPsVFNaFW%2BstxHLCLWX7xQH3RlJTGAnmfk0SX%2F94JrZ3KCEdpDm%2FAVPuJbyea0h%2F2ubQTuV7iyLi1zeY5p0leILPRagOAWq5FCQKHGlkdwhRUDxko7EenGcL6P0TepgB2WCIAEonLZvUbFJvunSsgkArCkZPla2yDqgS4cg1p13730vHMqyzJhUDaSRa%2BzyS6dpV5a0nX4Wk1%2FhJGugzDl7ZPQBjqkAfpQFL9A4ZI7sy99Kag808RXket5HsHdcuJ%2BvYUQ5YFtV7WxgCYeCVgZ0iCtwsPia8nJ5JZArFHVjJMKZ76F%2F7MxkdXilTGqza743r1x%2BruUtiH9et8rEE6Y7KCa%2FZ2DlWnI3L8OBH%2BYQZFIjH8ZQa%2By%2B5OlHVTPQdwQCxvl0TJ17Mz%2BaDvxMFKL57YVnP2mMyY0J8Gq%2B2%2FOfIYoGvPHMJYsh2Wd&X-Amz-Signature=3175250757691e248b278cf000949c53faac80a0a3ebb40a074ba0d990ce288f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
