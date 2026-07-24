---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664C6546YA%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T080452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIAKaidGQ49poUwcXFJ8zpjUcFiYpqvHaQc6fi0ryHgwWAiEA2jLXTzhGn5aQtycujX51ExmNGyEccOIIeYqLxK9WMrQq%2FwMIARAAGgw2Mzc0MjMxODM4MDUiDLa%2FLiqdicdw3NfUMircA%2BsKB33Jwt9gUxk%2FWvie6BQIh%2Fox7UnJ%2BUBHvnA8i%2BQdUxIEutw%2Fp8N40XDho2pZksb%2BBEtRcu9V7Rl7cnj8EuCkAKi1NvuYgCrmVFpAFp5Ki0rboXjWJT96dmWgGriLqk%2F4H0P70n6mTkAViCb28kCowI6n11WHCxNqzHl3pMLQY8dINV8iAgnrYcc5yczm%2F5oItjynZ2iHHwlPF9SDKa9%2BMbnaWlOFaEnw9ny%2ByB1azWKYf9HDPDYa1R%2FLkBgj3Xg4CGj6rVjIt%2B%2F9lGmzMLaAKnRbxsw7KDhHSu3tFPhIbW4FanOMBhEu7nN2GwNpobXmI9RP32hiTszn4dtq80bTN9lfnXaZJ%2Fzn%2BviJmP5sxjGl6VwRFaMUylR0H7h8j0cOR1SHILuhcAtsIJSC8hN%2BLn3%2Fkuaam2y4yXLrNXb%2F1mIIGyhWMS5wCUcxgUUOOkcUW%2FXNvC5bG4jjfPaUlKB9g9%2FJXZ8y4bI5jCbU%2BitRTHhqbiWIA%2Bk82pjXBx6Z3S1kG3HofTKu1h%2B3%2FzpSU69lsKFT0KyX4PpKNl6nJcYfpS1Bg028w5wu83EyQyEOYOUA4QXrs46xD48QcYEUJv0eRWMNGq%2FjsTJ9hqOjefHGa%2BDAblL9uZduRKCPMLatjNMGOqUB5ay%2FsIZu%2F7k83%2BsjI8PDq6KyGA8hbBlq4rgi3HZcRbG5xfa%2BTMhqKtlJUMLlJtJHCiEJJeCDSPo3APzlYDkpkXs0TMXMirhkrPI%2BP3milQ%2FEer9dyzzl2umX07oVp7AtJesLioVkxPQCSRJ5G68iZPZmFunANtXbL8%2BkPn8UromvXoMNjUBiwnK0YttYEum%2BvVFxNjVhZwV3tD6%2BQB8iQOJFiYer&X-Amz-Signature=905c36cdd805b3038fa1ae1658188e27c02aeac8fb693a5912db81701722b152&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
