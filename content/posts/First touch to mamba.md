---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QN74MA5V%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T164440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIE66a%2Bt2Tir%2BRkwnxyEXjC96XNebCnAJpJrY9uvLaljvAiAoSm7jn5BFnfdzOFi7DB420V8zusdGXBqBr9dOZreHwyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMn01nT6bYkoTuZPf0KtwDqSn%2Bs1%2BmMenuVN3Z8VqWA2Z19EBd3ynlcBBe6ia0p5UR7GyAFIRVjZMQZu35Up3r4juplHWqOxlClQqo%2BdNnpky9tdvvGl4mwZRzJy%2BMByRzca9KEtA8%2BBy8mSkZj%2BcTBQLU9x0u96UaIDYoNcIDVehvF3lh1jAdkxiaK1Wtfcv5enUWPApEm6lcnh52wTJIUchmvMtYHHPw7ZbKvlSsHywrgUYbKsJBWrm5j3MG7cmjPqa%2Bbic1MVFXfXzaB6qeAQbWetMxeTavhJfKeEuQoENnK7Y7vnj%2Fqy7GBggA0PMn4RU8S6RSsoikYys21XmKfWNL7ZmiUHfOA5DOd8hEes0cWvuClT6X1Kom3dpC5uqOasiIzo2gHbTrV%2B8T1jGk%2B1s417okmG9MNJ1ov0DXjdOeQ%2FJhXNhD0UcbUMuNNa6pStgWts2ouC0iY3hk1dHGIndrzy9W1nYgC5slZxmLHy00ucPlccvD7aD%2FdacXoi2zmtY%2B3b6hKe%2B3oIkniv6aFA4DI2H%2B810ujWeHOjvXRYLRFscdb%2FXuoP4gKnbqOay3mSY9QN0W5JaX%2FLvu6JVWhBBHCXAj7anjc4TpvaVs2xNtX3x1DAqczwhn7dUAP41IbZHFvQ7%2BDzHJTvYw4LTy0wY6pgEpc1p1RQOnJW6GqV3VSBqQcEuLSjle9T6Db2Pq8gnffZvtGHROzFy98oOSXgoOUeXmk9xAVNsCeiabksTyfjh8cJyqtfGhwTsvmjWcCb%2BeC7W0Rk6d0yWZMmPq8InNx6bVcU20vpOMV3snAWdxmSA16cLqYe8iVpZPWjtDDS%2F7afNwIHN%2BUncqhXAx9MpxQGgHkp%2FY64I0%2BjiSlr6NyX%2BZuAvYwS9d&X-Amz-Signature=abe28caaf775937f1b75ff174189ecf9bfbb3f626b5354b72378e8f9515b84bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
