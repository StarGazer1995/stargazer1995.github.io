---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YO3URMJ7%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T051359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIDzUIw1iPlfWtTMzLXl2HoeumBPYxfJzdjciVkpnDvVFAiAc4Axxtw2%2BEbD%2B%2BLIpXzFChwnk7Jb0hZrd6xBVVk%2FfsyqIBAjm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7c0GOzMdXhmUE0dRKtwD9yq4o70Uxzq8F85VfN2gvjXMfrYfOg7i2vH8rBUkRwBv1sgJ4HV4kSrAYwOaya6DOHxGmSg%2BLiLZYm%2FIlvSMu9tWmzeMil0hInqMadGvuRpCH%2FsUCzhbnS8vc3gTVHTGNL%2FOEhMNt3FuUd2cxW9mdSOW3qqY8Ki7LdXejdVsFc4D9gQIr00UilN53Mb2L2Pap6yrnq2hflARE%2BDAkgl6xnlZBpKuL%2BQMH5y9Ue9g5yJAeCnqPbxuygCxSu3cfXvnJbQBHS3KKSCuuu8EdvFWaINMgeKphMoMZML1e%2FcDWcYLOB8DScNoqfNNqfGc6uKJ7LubczUKwDEnlLw8zKgJManeqz3rN1wd4oWBARX5fNp6jDCX39atwaD0R3j3qI580hX7M7PHoANgFHCdCFThxF8iYLC2Gi0%2BMcfWsjVgFzqqXXCb%2BCwU1KzqmWyMFdoq4yfXFR0NxIdHAl6ellwNdXJ2wuXXL2DlhouqPfoftudBT7YLeiv0Rc%2BU%2Ft8%2BtOtUArDqMS%2BmniI7UO8CsP8sYre%2BR%2BQsfkdma24PdPRiaZFtMz39BR5bHoebxyrtr7FC1LCkO9Q7AND3R%2FwaPkXIexgf6f7pP0mXfdxsLnahPwVVt4bQMZR3z3Y4GDUwwb2G0wY6pgGTKwksb8CD4%2FiWazQujtUzP4QlHY3Es1k6O%2Bid1GBD8WuSpsCfHHy9zZN%2FcNlpQCsamy6VU9dHGQWkOmWxEiMHa4%2FSdb644Irzin%2FSZiAo9FFx2F8c2gCDQGMcTPWxL%2FKQpmK3ct2OhJ5HS%2B3%2B%2B6p%2F8qrtrTMkY0kPBQYtNnZVrg2b8mBSJ1HMvQ2O%2FasNQfaH3d7PmEGQW7Sc0eUBY3au6sTPD8b8&X-Amz-Signature=a8c3f52842529776cffa17e2ab8f7345aaae9a68c71ee175cb7228af35684b34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
