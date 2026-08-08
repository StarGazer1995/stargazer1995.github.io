---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNTMMFH5%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T044528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCqbkJ%2FiauHLa6LjMmB%2FzFGH%2BAWh5KPZbC%2BaVUEsYi%2BFwIgHvBgATl5oEvUhWDCadV3MMaTPVIWM7AA%2FCL%2F4SqbH40q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDJVP0s59tEylrfsGHCrcA35gf9aldAVneu92LXDIuoJh5SWe%2BmHXyv%2BOnfCYg1HfFSXo6AvAK12BG2yt5XqrX22S93En7Xh1WOOXOHxjDqwWiJY3xgBkrDAMhTBaWvRRhnwcd5vTi%2FnPyS1c0VZ%2BEwzJgJlzD0ahAmo5dyUXREJi%2BWpSYBzhQSyHGtve%2Fvi%2Fzvqg%2BO6%2FGs%2BrCtsyvzEkcAyuRAELrEchN1PKvB%2FOjyP99vL7jKhnX5aeoyoF4xznvKAGAPI1AH23XUyAj45QHaG2ClPZw44H3zeqXISKqXh%2Bt2BQxODnr4xNXc7n%2BH4ufpYKNpxJGqDC8i9tWk5xETfzGG0dZguWdFNCL7Sb9uPVlGMTQJ6S%2BVXzONsC%2BK0yUWCvwrc%2BT5GDN4oeBvTlk5fBQA2XSU428yW17Pu2O%2FDFfme5c%2BaOVg8YZ5Zv8rodQl3ock8KxA2fG2zuESdzuHmQuj7WD4E2%2Fls6LldfrLSRFv1O51KyL0DbTI%2BNC%2F7Ui9JxwIg2OsgL6yF0FRUsXL6YHND2TewyXw0qvIkHOmB73b8Rxrm%2FogaJsBzXB2aKkoxRykD%2F5BTRW7mIdnaef5S3UclclAwIakoYs9f8GQK7%2FHjzbaVEGNFCoxysN5%2FG11JSzVgKRqfRDFvdMIqt2tMGOqUB3mzrpSD%2FD0%2BgXEbhHsfNC%2FJ6z0x5L1fdh6vJanwH%2FsGRCr0oVCgvlcM%2Bh6pdu6FDUWCqqrhwNY82ar2cb0NyX%2BqMZtgaTb5Rp4RmyMZN%2Fk382qioPLA%2B70NDKii1GRuXlK%2BiMMq0aIw18JDTta3YyDnK9GIc7Uue6qxuYD%2B3yKjvi3RfR7hhiq5jgjFIcntac1F%2BD7vAGBvyxVekFSLVMAGcOgxH&X-Amz-Signature=58d07ebec74e8f29c88e25c880164f7cf56d18b7e0f9d6dfa10750db27a145ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
