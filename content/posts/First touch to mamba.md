---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QCCMJ75%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T082245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEpc5d6yZj%2F0YfGHj7ils%2BoG1Sa3dFMTWl0uzLkWE3AVAiAfTcxJJ2%2BvomY3M1DqSuEohzFBLHbeW667ev1pGEyWdSqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FHglfvb4lxbKGZWbKtwDT79AKJyTNZGoNR%2BcBcYYgY0lJO3KtHpCMhBK0hdoMgeIdaIjDVV8pZe9iMCzTpgOcKytSzVlHxXCj1Cx5dmN%2B5qMYpUE8GE4qSQi2%2B13NfFbJGIL8wYcOOrYzCkl0zvI%2FRgSWH5ew6ztSdnArhi8l%2BZ1Uq2tgZnHt449t9M%2F5W4kn8F7rm7%2FRgUkT1fe0TPlkRnGFDBlX3HRnyL0oauq07gDwRbi5YyWM2V9oksJVsJyb%2BTCIi8KuxK4%2B0I%2BtzPyviQ%2BuzL7LUo%2BYqQu%2FxGn2EcBbUBAvu7X0YXajMdmbCi3xIY6TZOlNUUsjOgJavS7kNTYV%2BYMqS3M6gXOGOFagbvJ7KGIPI2oXind8l8yiThQ8qfiVyhAXfD97NB7peI3BACbKK2JfMr5DxAi4sZ27VQ5%2FccRnVYo28OI25rr0FY1Lu4gzSZ%2Bs85Cg69PdyYPtPF1tGBqIQbwTRVllT%2B%2B6UGbTJBQyr60pNrt8UjjFvUuct9BO882pQarRosDcVj9uu%2FQYCRZT%2FBs%2Fyld1h1oA5Q73llN63dvDc%2FTn8a2PJY9AAuJgeZpTuuHqNiH4ttGGnrSUqS%2BBemivWaAp%2By%2Fkz2COvvqVQAeONevInIbD7hZWqGZXzikBi0JQHsw1qyP0QY6pgHQX%2BQF78i5jVzz%2FK1lP89jTSzUtvlZT7HDwC94tWGljBvwjh%2BXje%2FhL0KvZyNSMX5msV%2FY1wl8aYWiyZ%2BUTWrd3GQnCpiOHHkdp1SwxY%2FnJgWDebRIJN0uo6b%2BYRh8UmVxIdgcETP0Uc5OC9VQtWVxCYc4z7wxjxmt%2B3WhzdjZa2w6U2QjwsdGdIWHsCtLmShbNtI87QezLbjBl4Jxa8uTOVLgFHxS&X-Amz-Signature=a921833308e9e98c23f79434317b8105d7264a3afdd5f900fa6c389a7572ee3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
