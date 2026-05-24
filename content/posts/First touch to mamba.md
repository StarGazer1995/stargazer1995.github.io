---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622JTLEQA%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T110654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXJ00UeY1sHhaZmOjMReH8l6aUCn4RhhR7cR1gk0v%2BPAiEA7cM%2FXDCXVBKn79NeosaUKDHQgxXj0nV6kl0wOpm8JCkq%2FwMITBAAGgw2Mzc0MjMxODM4MDUiDIEVd7ROEjMO8%2BlFHyrcA9TPwaJdvQCKWpSyGOnCipFS1JlXBsKuldHrl4oM9dZwbcOoXM7I%2FFcVAHh63lb8h%2F8QjtU9v6k%2BRqQjhi%2BL2VbkIGdK9z7X%2FCO2ip9ECuHzfpzJbgHmXIzjwnoAAKjdSFRdDWy%2BWLHuwwN0Ontc5DghSX9%2Fp%2BvgxhFEUk9WQMKZrQ7IL5o1KiiaKWea3sLQCVxKXZOwngKl2vd%2F%2BytdeI4nJcN4w59zaNKs8E4QDAOqL9EdqzJ0DuVYaHlcv6N1AYcI9tPcMo%2BTU2x16LKXVwFFl%2BbWanUr88yhrGrQNBhbGrJhz9F47c7jKEHLJg%2BKIxhzdKgjzHhUI4D%2FOajA17nyWg294ZF9UWMoV7s5eC%2BO2r6d9qJE27z3KM3alqyVYVLMSrZERWoPa2WryFVWO7dCwOFGBhiEPuuSwp74oNGBHm5YFDj6AFCI1Ih86zLlWDSYgNoP7Y3fln4Rngg8XBDNrtd7ce93LwMU3%2FmKN0fQ91dXH5WfSBtZnBnH1mW9NbU42B4kvwUFrAfc7j3fL3hjPJM%2Bywz7X%2B7nYO%2F5p7r699ouVRmv%2Bl7Da%2FYZ9w3pG3GD1Y%2Byf8iZqoesBuNqN9EUjtZwfauVU9JjuD6yQHCJTrU7%2FSPQrXvaCwpRMJizy9AGOqUBBPY0VhT7t2UL6JGvoAyTwH6eZeWLulO2OZZKOqP%2F7bm6%2BMkFJc3LTdVSZy8T%2B3nbn%2FH%2FW9ZqSE0FgknW1QY31e%2F5ZV7woZNNlfEYw7F39Dy6DTc8cMWydd0PkBuIvs5ox3p2rcRAUkVuN98X%2FHVz45dhgl9x7KtCW8VwUhFzb8hevrNAz9Ch6Gx8Gey0Q8%2FtGM9%2B6lbG26AgWgElOnkBnhsnBYni&X-Amz-Signature=77f00521feab3892168d7fd1622107da3fd744956d4210c159ed6ebad1d73568&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
