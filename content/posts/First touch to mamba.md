---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXNK3XQZ%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T074159Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDZsnpX29pi71LuMbQVH%2BVZoUhEEYqWdhu5oXlgIUkloAIgagt2oE5WWQ5w1DcwUBZXKMstXlBN1hF3i5VHjLQ3pgYqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA6h2qwX055S8Da4lSrcAycvQAoNhmHRle5rpGaIRQjSksrTq%2Bo0TI86Gn4jyamVfzLDtO%2BYGfZciIyk0t%2BgvmQKzMOwMWxgkdhQkTE35qRp5A6OkikZPS9YtIVVC9EojnwpUFgD823eM7djCKXC8qiAO2W9XLWr5ddSKJehiFssGEOJ5OgifobeJsU1v2%2BHJ%2B5%2FUiE4s8nNzw6z8XU8Zs8MHFd2qotP22Xwk%2B81Dcdbym1To%2FRAkMuGv3FHZE8NkH754zvqMkDPiDMNywwdlB7LTBwl%2FDSuU452kqK%2FsRkwYeZWljEHSoN32S5sj6SjWZzV6kiHXbdQtxAR%2FiBfx48ddVufRqnBm2ivNfEak46Bb%2FFoqIbcAc9Bph%2FK08sr8r%2F3LAXoQN3gTodoawd5ngOVh9ESPBi2CSYHk4xI5IKy6nynzRJ0EH2k1vWBxXcPgKVSPn2wKCWkJW0wyZt6dlxG2O28LcWttdkCDsN8uD0TGhtSCqT8S95wICS2vww5tOORZww0jh4w6HNzvz0JJqoQ0ZwQ7MAEYOOB9oYWtEo2nf%2B6ja8q8da9yhI2LoYe7N5g9GKZMiQX5XEoEG%2BRlH6xEazPG3Au5bdJOpREh9VufP6g%2B459Hgv1GKXwB16rjE92Ei9vm9gqbhoNMN7v2NEGOqUBgarvR%2Bep7ezpFUzaXiXU9oF3uTM6R3i38bIfjzeGcek7yVASNVmLegk04UDtQBxwBRkxqalcbq0o%2FHhnEyF8gHufg2JHs41GXF5T8SWHWA5WA3PJf4DC5jGATWvyRmUovraU90h0q9irbL3oh8wm4Z2m4m4Gz9xYkVXExtRtMhmA0bZnP1cASOKk7ED5sAEtWWzwQ8ZFy7wwF%2FBFu4eVB1ykxAl2&X-Amz-Signature=6aa4ec943c2906bfa40a9c0e569b989138d264d426d513afb9d13f73845a43dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
