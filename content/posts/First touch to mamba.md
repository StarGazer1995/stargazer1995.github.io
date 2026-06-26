---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBMS7M5B%2F20260626%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260626T160846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICSoyW2Xem5X%2FlWAyYj6XBS6qNSo6OnZE3jrzlLEwK0NAiAR8CWp7t2LemNrtoCn%2FPIAwK07G1x0Fb8X1HaXIeOsryr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMNcZLCazP7XlaeCU2KtwDmoFbb9I8nMNeSJnRy5mKjPSvrTndeku4JLwVlOwiig8%2BaQzt51e825nr%2BBegH6mgoONYbG7LXDhDgzUqISwcDsj8qHFI%2F4cU3HBH3vbsWDBABUuu285JPtNzJEps6vf1FuS7AdpxtDtmtzao3pAwGpZChsyJb%2F1YT3EnG%2FMcwmUujtdwLHNA%2BRg77lQFfw9OM%2BdsYLVVao93FP56S79UA1qcGxb9AlTVs303KNNnxZWSS%2Bgi3%2BP0PJXP%2BD5E2Qeiw1c7hLn53smaiRKk%2B7gO5BSsYrniSDMLaWpZWVQ1OwwWpy4AnO5Ww8SKaPMnSt6X2JMO9UW0TqaoievLsuhK94CJlLHnBJLDqbkKOgrKnXUMRYi%2BhxuFEefkFoPRnxaBAchHx0F3EFiDvn2rPYsvsZZHLUsTbYXCgjk%2BqbThi6QNHfBvn7OqisoW2Z4FEGgNBhbiOj2aSbu46ZD%2FfL8ukQvtqdqbcdh1ptVvqmqAycwISg3SfFuT7d9aoWolkxtZiX4A%2FblJ9BdKhYARIKYYUOkKqVsZpBnPzTuAT0%2FTRXPoRGbtJzYHoCw%2Fgx5lfXUa5RTuIg99H3M4hX6Fn9uMealoTm0yIMVSJPVaNSZf8ay9gOya3yT9WI1Hz9cw9LD60QY6pgEcatSdAj8Xev8xBdREhvegRsDh9NODo8bYMT4RX8uw9sfhRkmePjAzxO%2BKtYzxh4%2BhDevXwueXzO3uE1pDPjQlEQIK2nr2wacDnknHWwyHQPxpFBzrKZrrYlJxX9PemYapGr%2BdCqKOwr5gGL8j8p5O6Rou0BeixH0MehiFolgs%2FipFxpaFFvHiJeJnT2mQJ8nZKn%2FauwlC8yuZvQimtw6KO%2FONTPKO&X-Amz-Signature=ffa546172280389c88e589ad0f567c7eb0ceddbdb344c8066d0d4663feba239f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
