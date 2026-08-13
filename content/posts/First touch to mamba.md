---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXQVBJDU%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T124119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIQDqwxDPpbnRH%2Bf9%2BcIGkIun3g3Owrjk77awsY7XCeEucAIgWMD4E7uRNIkoHg%2FuJkH8MJoF9MYjQi3r%2BhrcUnBofCkqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLtlYGH5XH0F4CpkMircA%2BjGBpqt9Sp50k4zm1G6TcgCrkJZxjy%2B27mxA379cq4SNxAcqknIt0%2BYxaN%2B4qAx4wUHtXTYVL4ktOgMxLw%2Fs0lQcBEzhjdI7Wy5zgaA5GiPFEGEM%2B3fIFPZ%2Bkfu6wQ5JVlxzXdSHg3z1eKccSqRPsTO0rZ1OfnFzMDH7dJufEmuLzPwbqBwfG71N0tp9g699OBjEsh%2FWROIuc%2F6P%2FPcgCzVG9B1%2FnejVLNMchRtuXOxgHMO3mBiGebcBVSVVjZ%2BCQghhxbd%2FQJ%2BaEr4kHnj0Q9CJ6dWC9JT45negqcOYTXU8%2BKCt%2FA8V7YEhJvqNJpUyDjt19%2BvJbtrYTp6lQHjnEUuC98TkI4wVypDG9GKHXSq845DvGUDzveosjr%2ByXXOSy9ZOpGfGoUFg69h%2BOSL%2BEVYDV1hDmY8qN%2Beqe4cVImHrM%2BdoFJBwPHejATaGRYHJDC3mGONCjLgUqLoX%2Bopw6C8LILY1Utt4%2FxluTS%2BFi%2BxgR4nCfPLVP7wbwmuQRhpHGOR6BPdv6wJpevED1J%2Fgt5vhwc6ZTls98v%2Fbfo2UG%2FTyGxlV7V45wglWq%2FuW2vJ3CFfrX57%2FToEC3Ojab0wPfsrh%2FiIDGlWydPGV2dKREcKUJw6rpOiwK3OIDANMOLW9tMGOqUBlnfFNaOYTNBVxYMRMgQeH7kgEfNHoLeCDRfPRbXRzWUd0liAM6nO%2Fih1cBxjIsMetqTYBXZau5%2FdVCzoAtH6ZKSqLaPF7tnuwGtR4lwpEAJVMD7bXU%2FS8WNwhndwzrjICYPdzg0BDJ6xF087jfLTHQbhyEzeyCKFvHPNhOJAQXcHhQZ6ENlecLcVYzvJ7xWlvRA0fc0BFQyLTknf7AFzg3fHWfwL&X-Amz-Signature=17b1e7675b78d7eb4c5d53f9a2cbda4cd9dcd4e88db43429e7c6d7c44c6837ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
