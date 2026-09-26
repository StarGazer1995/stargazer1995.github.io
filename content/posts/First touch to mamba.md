---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673LS5T74%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T085415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCICAuIHd2falfU%2BZt7yINyaV8vEZmTSkKzsdqhYsK9nMoAiBjjni3UWDfd63wQXolLrSGMZF7Y%2Bv7965r7DE6Ms%2FRyCr%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIMJOuF7VJgJXN1aQqYKtwDCkN%2BgWFl4RNansIonCn9xyYdqgEacmQLxnrL6k2eiTdcYYnS4UqIx43T2drSzH6NvE9XFw8zCdiNq%2BQl93I8d5sBx6%2F9xYihQp3WIJkovCxpqoVei0GD1b6ejPbEffRUoRiM6PNy0HUDi%2FSmZeTGXNqz9dLfhrP6fsySE04ViEv46JRNRS1I21Odoymx1KGdsElf9avfhjGBI8pT6VeshC7oqZ9dhXffxZkQZxBqJk%2Blb8V4PlCUyHSen4FtULbTh%2FnDxe%2FJANgO56VLNAllzuLgiM5xSJn8C%2B%2Bt%2BWtANzTjqAqxDT4l0szd3u2NqZ0NmurPYMw4vAL0UBnvaenxPC8Z%2BeILbhL3cb7g5yBANsgk%2BAs8wJlZuGrgNCYO3W4x7xq5lUa5TRcAnOdYryGV9TB5Jgp4NheBzk3TCyvHj%2BRiQbG0VyvRW9LY3DZn8Y8ntbXTuSpCJVI3kkebWKM%2BpaWlAXcwMsEsPwURqNebE9aX9Ibh9jmauKp59GEBizHyhzobhYQFMiv1P4vbhncKnYPE6DeALv0fDSAvK1YjA%2FZOAjH8e0no99JCDJ5cK9rO31DS4qPgoTEIUtPB36O8kSna8ZfYHAEGENAIU7wGc96MqsJ0epff6iyJjUYw74Pe1QY6pgE0RY4FFh1FTNSZW3o6X1%2FFnGE7wqZEeeYsYLS8mDVAmlw6iAV0CrwrIHnU3EiTqsKCiLHLUfSo0RQPfybhFqmxLDhqa0XVYAa%2F%2BWQUJ4sz15fthTEQpgzb2bETevCtRfLrF3tibupMU1a9kpKShwFzJflsgl%2BeZiw488QhwuBfmuSfxLKE7TgReVEZZdiLS59rw5nK5gQ79QJOQuaIjwkUjNXDQHqp&X-Amz-Signature=11fde1484dff6126082f97baefb3ed965d8333341d894c3c791fd0c123b4cfd4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
