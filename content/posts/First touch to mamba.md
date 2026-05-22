---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MQQ5XCB%2F20260522%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260522T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQDhwi6TIwDfZEunXRlWQ4OjrI%2BgopocsTFHCK8dDFSetwIgddHVKGjgP%2B4dfHUcpTarRsJHWQD9uUBOux5wlLipVhkq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDLQ25lfVlqNZ5WLZ4CrcAxroDFTnZ55VmOhIc5xC6uaiKJnOmsnOmLQATp23tB5r1wwue%2Bz1bbBLmQzLf3MvhNhqDn%2B568GRBqXvcRxiNl31Hpwj%2FATpS6p%2FCIuLbcKSPGSk94pUaVoRrx8xV%2BFedeqXgwYHQLCIe0NyO98ShiQz%2BMvNkP4louUEDZa5AWwxvAavzSediEZaHy6r1nozQKg%2Fi0tylqrOX%2FCABaZMJdSVaIijA%2FRIyjUxr3VLM3KDqPNsyf65QQzex7P4bFO4oy62hB9SnXWHBN2XyUuo8RB%2BXy9EwfhhTBtafP2g8q19UUNqRdwqhUcIQxBdahkH7T5VD5uxGPhWUgDzW5BjrzSZpxzdlb%2FFI6CihuNHgfgOpx2%2FAFYgrzTzBLB7uPYD%2FVsp9mqGdjd2vHermyoVbm7ppdXmlu20JWZuo0QNSTnYtSlgxjeIKqitW5cv1voNMWPYWAodrsFi6ngFyjkFtvXrwYGLQyDAJmy0g1V3duDBxmVGG8KGrYH1xyfh03Mme4VtaYSxfxLHYcbfJb4VoV9xZ8ljVwnqV6rF8Y1O%2F8UVFzAuKxCpC9l%2BfZdWS5Zqp76G2rmP0Z9i7AhIDlIT6gGgJsL0Ep8Vr%2BMMyqRQpfTgOTWMHjrGAgfk5JB%2BMJ67wdAGOqUBvYlAMXUKhsPOq1bfetgEDAHrDdvzBwcZEwAw18v%2BXvNoBD9z5Z6odYO87o%2BWKEvUWX8ln0gQ7%2BmACRGQuHyvAvFVv0yE7n1m8mi29B4R3nbzt3ofkwwka%2FePs2d6mToxKYqm7YI0yEMoFpCaGwN0xZMmjntZ7PnERl1mS2pK%2FxKBYCAu44NZrILgdDHpW1RQoiKlWXTVLBoOYEWNFTOW284jlunG&X-Amz-Signature=5d42c51fbabcf0406991486a3a86130475b0c113f2ea91ab3ebe87391d4c01a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
