---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMBPZCVV%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T210109Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDdP11iVXPnA2WWt1FdTcCymAhk7tzaHD0pOWTvdwXw5AIgQ33PZkoyUjj1NzebLuZVZsET%2BBdoaB8dd2Mt%2Bhd8f4oq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDGyNYBxll0LGwOknIyrcA2v%2FZLmFh5oxG7bFPB%2F1hNkAslI%2F18x8lIP0o1hJkzcBb5l1T9qQajiTv%2B%2BSgbUbrstv7MyWvpPfo5yjmeGKac5axH9t8oktGqP5ji8170SIvxEj41I0Fo8RRr5jUYxVGW0WyQ5YklQ4HHnbjbkIUZKZVFc3erKSO%2Fl68BwZbPCzcPA%2Fqqt7zULk44HaQXorap96TRTiLDY3DSmXlDtEeiGppfXOQcjU11F5ChbfDyU%2BTrumztEOkhkEFxJyW2CP0gURI3NHdKiYwW0b0aUh8MIuZ2%2BtA4AnW7VsCR%2BLEAKmNEonFr%2F6LDGRM3sX36Qma6oX1Dq8KEr%2FZVTLYQKf8AnMY425L4WRUuvyzJ9XgiVcLENM5Vhr7I%2FiWLQOuZBsN34frfHaQWc9O%2BS1rB39oePOB76OlbyIiANEZ5XDp2qnI9NeyYQfJUDPdtPpA6Z0WLJSLYznqecP9an8yZZ%2FcvfFo5xbKlF7I5O4HDxZk7SzR0m57u5m5qmvDC2UXmPR5w78%2BXRSYjg3TMUGmoSN9oPBjh9rEpKWqOopKRKHN5lBKNqaNqq0ItVCvK1VaTgmBk39Fwo6I2og%2Bu%2BeF9B3rHyHeGYG5c0x3FW2i%2F%2BmHSkJq%2BFynrk5r89IW3vqMObxttEGOqUB2MilWrDBrJOb0EgyGrBvdMmaQq%2FNUbi3Bd%2FpMwaKAFha1DN%2BLL2WWyavwcXT9lnACSEJrBMkSCtKlfpSEDFCW3JoaAEa6YipY1YzDvkwL6Cw0KTlu7CJNLLv5bnJTOIsP7zCVyIGQcf%2FgWlI6qIYLwf0E%2FN9GFNlxnnM00yhlR0JEA6MghfbW9m2FDBSea5Da2Lvqwz7%2BRA19FvYloUvJKEZXTGy&X-Amz-Signature=259183787596a45a08593efa742e153cc8024a81e6ad73e866b72b291d6f4d0c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
