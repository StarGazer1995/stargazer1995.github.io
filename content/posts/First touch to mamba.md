---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC25VLT7%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T192619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQDaV88C3ExUxNU7Q%2FMfjUZBsez%2BBIPsxkosuJxnD4geAgIhAMu0z4K7T9XW%2Bf2zWdDb092bLWyinIqMJ3um05A2IlEYKv8DCBwQABoMNjM3NDIzMTgzODA1Igy09nFzdTbX%2BsoC1EEq3AOYzbrfyf7ae2MwBtURAcr3GDKyBbHNNy8fk986Be0H%2BgG6jgdSppRURYm64ZVC5XyYGFtUYKF6NtOX2brzdYqDwavyu6GUHFIDFdbj17MQVUmpAZ6t2JLX6%2BBq5L0v%2F2ip0TaUE1cwPZzpEYpJrzWlO%2BwAXo4WtSuCq6iXqa39BmEQc53Ith2aheG8KxuY4JwLqoLPW7ENzqGYRF1qDeU%2FANWbHwbi6Jear2AHHsrfCK3OdrbPYMvuarcJZoqEE7JB2B85YkEWd%2Fcbhl3BJwKWvORNg9HFKhYNKLg%2BtvtmOwSZLSxX4Q%2FYB3QWl2Vu8MN4SVndFX311WWGfoTflRGM1aq30to7%2FASGlbgFj2KiL1bQQr2tT1jmv2Ugtd5ZCqe07OypsfVVQ07ehRaVrGHoXSRSyjJvgI8AXM0PtdGwsypiDyX%2Btb0RB4mKsjg4djatHNpNBd830F1jZj74AslxmYGvg3FEbqXTUUfczLHrTZSrdVhVUA21oj6xKvNjWSVCXmdpqR17YUraAgzqJ8VhTPMluOx6SegBvsArDQQ6I0baz7BfhdeQqwOSqi7psJUMQEWdlLsImP9hZ2%2F%2BxQtqHtnw1qFgQMKQIpgVAcDQcrQoY3f%2BanZmHNzkqTCSv4jQBjqkAbC%2Fl0FlG2CiqBEHNFjGGVpzpCx4n8eSnIdc9BlqeV5eHtIOzW8gk%2BL5ltoygMH4Ez%2BDlM65xqbM4xdnepAqmxk%2FYCZQocHDU%2ByhrI99CiDJm86w2QR%2Ft%2FP5g5dKqjixPTDiecyYsqZDjCQD1QLYibF2dn2JbZitk4%2Ftle2hXo2Mpq0y1%2FNWXgC1%2BP7ZxQIhdl1uHaRZmtslIHfwwhYhmALDx9xt&X-Amz-Signature=a875ba80abbd5d813f02a931d817e343c6e2db56e219845692d40534cea06d6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
