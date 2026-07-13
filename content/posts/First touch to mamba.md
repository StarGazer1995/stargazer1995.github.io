---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHK7XL27%2F20260713%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260713T122603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQCDqOjVJvPz%2BcuMtzAJtt4cfYEnMTNqMyeySj83TJBfgwIhANJuPpabZWLVckeqGsTlyJKbdx4y1fiW227g%2F%2F5XtrxmKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwlXROUbRdGMy6kWNYq3ANrzuRSd97KbKYP1UbaME1wnmJ8XqHu7myTHzKURKZ6fbWvXZTYhfBL0g3zAKAwNEFJegSmGWu6jQAmGKVs8Sh5EmGUyyfB9GxAw7tguloyj4yPOoh9Mbc6aCKW9wA6JUE3eWlrjJvhkMEVodKACMGcWgDH%2FJQ1Vzd47IqCEWTjKdAs9jJkIXnr%2FNs51rbTLUwcXjYxPrecfaCahLY0yOqCVeBDlj9IJNoxsLp8r7eghbhv6XE3q6lD1MY3aE6D3wNbt6EtSaib2W99F0U0gSeH%2BTiL%2BnUULPNQRg8%2BIrOhL9R6hXkjrDY6GjES0BPKcAZXg%2Fo8scHAePsWT8%2FlnTEmsumFBurOV0n4U1iLlNod39s3hhWpVu3w%2Bk8SMe2ZdEgjALrD1rxPH%2BJ678DLZ3yOczX7Fw1zJ7lHJdwEZknlO8nh3%2FILx1062yjMszW3ZG2BQPXts4s431bxgwoYMw4quXUpk73%2F5kAXXoiMgiqMt1qRmIKw5PrhK7LeXV95izbJkz2T03QK8y0XytNW8Y6WwfoL%2BzgDFsjWstqXNtjZ2dxaQXcfQU1pqW3w3xZtZaPVGKcqmhE1A4hUY%2FTXMl5QIfhBFT%2BlA4xlXyr5FGSc39ODsBrSKJnyg87%2FGDD5gdPSBjqkAe7DglTHsBixMWYKdqoZYAoLJoMYW%2BPpprqX4uVbbwzCVJAtNxEUoI3egaMXRiLGP6uNTFarvVQ%2FqLs5hEW3NqQKLWe6o5MMYqflYupVTZjHofVWyFilps2e04ZL44eGTeBxo747ci61M%2B8JBu5m7jlNLFrmWjTSKSo%2F8AVkQdq6DiajYlZhdNBTxH7%2F6ey3cMYaq%2BiGmJIPH%2B2xqqjExTEexWvY&X-Amz-Signature=613692f501329fa7a1ca9ff704785b78feb33cb21a01c03e33d9b9d7531615be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
