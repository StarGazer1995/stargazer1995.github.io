---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGZMH3AP%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T083211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIBkaC4IV24S60IeFIj1YiqsNq%2FmTPrmjyeztKd28QtarAiEAwRvYYHSI7iS9wC9x04HAmlzYskjdSMZvnLqMGl5IlU0q%2FwMIRxAAGgw2Mzc0MjMxODM4MDUiDHKiaz5wEIUi%2FdXjwSrcA%2BnZwEMy3VGS%2B2VYrLsZc9RWjRMOMq5hIko0xfqQuNuLm7KP0MkC%2FekTuo9NZiLkU1%2FBkWVoBBW3evkRkOYxVmCSRPFimoL5DLuQnmey%2F5zItceOJoLnRupHuYgpzelJP0DGJ5vVpnuU7U66Q498gussExcD7BqRMGtQBJp0uwwBAgMtDoQn%2BJlvJNUAhU%2BPn09g09dzTcBbRqI4QGJCpW1cR6ZZ6WdjxGcWHSDc%2Fm0OsTwH3GuGCQ%2FFcnqIBzDEHA6fMbTZ0I%2F1k9Im4sf2jzvEfdZmo8etwmUErCx6V%2Bj5eA6YM691XWtqtalKunexP3ptstyPhav2YSGn9V38EE7yVjK6hbObOvsbyxE5VtQvdOmoWi%2FReVatRJWSIDxb9d6ccHcRoJPDc3bWbXqJFzwF%2FOOYiSpqFYtOdziG6LXqzi8EF0MlF15DsE%2BHe3SESSD81H5%2BH3DM9DqmmJ2s8gK%2B4OqxuWzuU1nQBgBFTzdNJUQLMnSbs50jkMSmW%2BDeXospsZOaMbgDHs8%2F1ROgP8PEhnBZShUeXum6mh2KQ5A74PvG0PftTQ2OrGMlY7X9X9VQ7bQQlgQwWChk0ZXWZdfhGUwlCGq%2FrevqF7yBL%2BuJarq7TnY5bb2goSwQMPqvytAGOqUBytgSb0rEly3fjbM7xrVNbIIZiIhk%2BuVt49Vqn4rs1BCz%2FxrTbIYzQUY%2F7Se2l37kuFH4mLaV%2BjEhUy%2Brttpv%2BWuVW40fmXNV7VaEB26n3OzvnI2qaOBqqNKNH50iji80nJNOWqpo7SMjmi0RgRXuO%2F3HO0C9D9yn%2FJd%2BEY8P7%2BuHPM7EC5arCJ7MppsK7%2F%2FspW645dxAaL06WlX%2Fj4U05YEoC3M%2B&X-Amz-Signature=86d7c197954d03fd1db6c59f07f2c399727a1d33ec6e481f2757647c692af7eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
