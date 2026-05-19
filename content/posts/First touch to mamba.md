---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYJBONDH%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T143157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQC1st3ZIHR2pzrQBbMH1e1C9b%2F%2F42dfBhdAw0fm8A8KPgIhALT1DbPSJdzn6ULQ0H3vEpzkwg1qXL1Jx0aX08P6sMhkKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzDmPoJsvvvZy6BYH8q3AMEu%2Fe5wNTo7oNwVny3gvIOTHFTHw2q5gdXIur6JHh3108IsWVLCi30xhGTOpNW3vWPlkGrUcPBatKyD5euD4x4bNvlSKqaLf5eBlhqmIHceIPfPyY87xhqFrujNKbeTQBmA0p4glMuK1Ub%2FufPOhGu4IQy5UvPCzYZw7znI34SuTVek68gstTvjRXQ9FR9ulJfuZbQhpMjrje%2BbKQ%2BppfH6AkUyMyOgsPN3kPz6vBXNahTbxwTjjGbYtRUr0jO0NAz6RsH0Lf5fwxiMSYQuLZpzWjxUkiuQh6h8Hg9T%2FDnzw4CFVIxn9csoA2IC9v3K5SCJRNW6CnP2uc8MANZXWF6DGFn1M00vauCSZyhFuGvk2ISHGez6r8%2FgIeb99NorFbzZ8MNps99JfJSapLd6d%2Fdd3DkaQ8RPxcFGHaLEY%2F4MgxC9X4x2asBGEKYEiE4lDVy25lWKWYultv5GbGBQSw5Joxywo%2BShnP91HPKvjJzcg7QK9jU0zL2LWLFrkCWFMbNUVcgKVIqCz3LvGQhYLGyxzxQymUzid93ZHlSzpP0k8xDJORdxNn4CV2Xn%2Bd7cFFRSoBiiYDsBtvNVwMfLGdCeWY2VVgQDtCu1DHOiuQ%2FZ2PH7jDnOf0KwGDgaTDVzLHQBjqkAaI4n11Xo3NuZezZX5HurSIGwGYEtcD4%2BSQPDPacshsVBqeZZfCL2eUqvkzk89u1lxRc3QFru%2Bxl7OhUIzO7AM7Tw%2FzFfUSKUylWHIyXuXg0C7UicQONhFjqv0s5vLpONf8rlj2MlSeFYHHgviTZCR7ngOUV9dZR5h41oGDflR37z4oZcFxxfmoO48tF6DG0HSfdUWUxovnN8noX%2BMoJ4YMQQWoT&X-Amz-Signature=da310d7fa8541aa86358065d78ffc5689c074d753a713eae040685edd8da528d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
