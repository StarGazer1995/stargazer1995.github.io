---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYKRX42Q%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T221240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FA3Ej5gkYRZt2h9Ai%2FZ%2FRTGQ5nYdPuGC1ONHjLa2UPgIgVGNy%2BLVdltm6MhYfzo3EqUKkAVUnT6xVupNbyk957oUqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAi%2B50DT%2BlQSub0R9yrcA0Ormwhjap%2FyTNd82WPaDHVrfSk0OqCS77Xi9J%2Bf1drERKHyJzsECZ%2BTC2YLFtmsHgCZPBeFDvuDpV2rZRUruBqFfm4duY40kq7MN5FjQOFwChoRH7yvRouNyMNiox8tbwBrkco3j4377VNhDt8%2BJQbD3cT8O6d%2F68QIwUKlzC%2BhwvRvW%2BKUfoGQuZiZIGtUni%2FGvxT5lDwjb5ArJHTihHCYFyn6OB%2FLiBpowvGx0vOMdu7HACfiw8EvG8IvV2wXqweleaPIv6YnWlzrd9hR4Z0QepxE7GBUHCgtQIFCjRVUMh6swX5iim7sM734RF61qITU%2FAOxRYKEXwRjgbUC8QUyYqlJKR6rA3KL1HZoQksS60Hk63%2F5k3ondIlPvaJEVeu4mm6wgu6TYHTwA3Yu4q701zl2LpFW4cFR0kE2BXBAZr0iG7J8J2R%2Bk0m%2FN6bu0Uh4F8wAj5RTe9EQ9gNnRFflW0O8jxTOl7PUuooPUJQ1OE44WMEoyeZ%2BRnIdfCDyX3Ya8TlKL59BDqD%2BJTErxHkXKBhgImkBZcKivevCt7jIyQhY0NaeBO0iwFpmzuWpSKtI28GDlvn6J5AknU2296bPw3Gvo9y8FQvEiBv69sSI5qBK%2B3a7bCGCExS8MMODo9QGOqUBHAZviuIQnICYggSJ47zCSOlzfy0ARAoznE1x%2F7r30W3b4morHwohUBs7rhAt3BuD0so7wi5D%2FxcxyyxiP4LtO6JECEbFXF3rqSHR60UP%2BwT28bInPvCIyna4kX1aVpQGgIjL%2B31QeX1QgxrCEVdonQxKtCDIrrYUvvshNCv67h9ga7U682BxjvZwXsLVhaoRBy2i07BPJ8UprKDKKtL2gCClfd5m&X-Amz-Signature=c08aec768db5e4e2b1ba43d8f6ae005b03bc5f1546f2ca96f06ceb43d0f9259d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
