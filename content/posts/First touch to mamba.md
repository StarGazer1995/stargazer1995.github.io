---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSDWJTML%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T042746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIGEHGwc3PGe2cVR2e3w5C2k%2Fn5MF6PwUOfxsyAbuYSmGAiEAnXsz%2B9uTFHBTArdEBkFakceFpsYGVt6qLs5cRXahgzoqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2FUOhp0w9rd6BEoySrcA5743FjDZDDRUUV0464%2BmeTk6hJfOvjP2mHKYiexGHGj8cFUc%2BCbAd2R8a2wwdcWy49wSzJhrsnwFmQsnbT56hAP7myqUYpB4LMLtYDezU9Q92C9DPAN4Pogq60oRojP7S8ANKVCrEQ39ZAW70w9w0TrL7F6EiCme%2F7xyqZIgu6ln2WgV6fYrJG%2Baeg%2FzUXrtUU7R9bHtDERq95z8buFU0v5dN1kf2PxnErhEDytpnJDaSemGi%2F9XJkLu%2FVEy%2F4zUt%2BRzNjHoYowmSOr7MoIYIaKB9ECm1w0ErwJOskVu4MqPzGaTRB3kXTqsBhe8WLZ1ZqaGCsvl7gdXK%2FGGima7HzXOrT4AW%2BkEgkO4yAGgazElNZfR%2FEzuZ1lfhmGkB1gPj1csQTNdc2sZSHKRS44fL7Mjg%2FxzhpV5et5iuBvUaWxz9xEoKY2pgHlKjnDCpJXDFb1SuW5ky4L3xlAAIDKvCReQ5khiN1tVHOqMUKR8Muu0BCuRnHBEzG3QahAvD792qzLmL3vnfChdsh3MoPLqWiz7997U7718rsT0jFsAxUhW%2Fl%2BmNjl9WkeTjkN0PPsVSd9xs7YHj8dqfvD%2BfDoaqtHQ3cXA2j6DqHqWsydIKHCsQealPbc3n9J3mD%2FMJvVs9QGOqUBrmC5p7vz9A7GwvI%2Fw5jhk12dORzbHl4MAczBW4Mw6NcqvmlhGhGrH8MZk2S0JZAQbllgVvNesdX4w9a4IWYhcVGxL%2FmcKJ4S2XGHQB9zlmJp%2BdzGs3Dgf6mgBXfc0TL%2FZEW5n1FVNjWhein4zXjpLLaSzoXtj6s3gIfyVxOYL%2BftcJkKVSIweae%2BUqXammGTqOFYkjtZrYDQZ%2FBoNcF7pxhE%2FNQA&X-Amz-Signature=eef614ed0a6654998deccd765071ae3e90e08d918e78ffd881c313c8c80521cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
