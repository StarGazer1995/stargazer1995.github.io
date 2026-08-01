---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNUCHE2F%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T080000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEfiVxNkT%2Bh1fgywMDd0z09yq45Mq8bDyu0PHYM1zj6KAiEA8XMlnTMZpjXSJPJD8mGlme1VYkAX4ZPyvnurH4PG%2BiYqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFrW8UbRVhOm1vZGLCrcA%2FwQgCecLqcx6QewxO%2B5ybPWb4tNWjfw3SP2PvnP4jyXJvWF3wCsh%2FU3kcSu2AOx4h%2Fq0%2FRRSUS5ltyzcrLA7vstd6TQ3AvDEAqQpnDP4dXjZOPxMOrSqQyaJ0kMYLNfP8rY06cWNt9YFOR34cUmWi03C%2Bleq8xdHf8RcD%2BDLfr%2BJg70gQXglBn9CX06rCfdUh5xewwCubeCUthaNjf%2BYKRhszjw%2Fw3%2B8SS12o1dUrMgiICenOR9PnZceBFxChXdBLerNR9ijwM63Be8VirRsHekKpn7%2Bc0FDQxYTUgP5In9jJOgn6lbHsuJ%2FHa6UthdTxs9Eae8SjX7Zpj5pgUEAVuSUvM6eYzfkhkaa7J7wnJaMjxRqSVGT7oOMQNENLe3zlJx%2BzxwgSR%2F3c7xmgmF5D4omMGQ7VThyFYrLGXh5jn9Jv9VBNvpyQkvDkMCie7FR40kr%2FCWc5YapCcyKgPP%2BYk2PEAUcsAi4Q6sMbXmxV%2BnRQIwOseHzDx4sm7B3lR4%2BOvFXMWTsYo4bzYOQUHqOEoUvYasB0Z9PTT2diCOZovRsZTknPpPBuxIAWEpC2pHgsSsPLV1kJp2kjQ7J%2B92o9y0tP4KMoXaSn046PjpMJHykF9pp5GNmVrIeDmnMPuxttMGOqUBaIYbeWYILzkndJbKGTg3Zm6K1%2F%2BnJyhk7UioW7tZpoRk2mtvVi9o8mqRZcXfmKnXteC72ZTxFx17E2uOD1eHHqlVFn9tixABl0QjteDLxZTDTyUMdyAcdFqWAkDYTK3TCZwGuBoa6Y1JFtpQQt9o657PttJxeEMpOdK0U4NLoVFltIREvWPRedaRWwYAx6vAPCJ0v0a9TmA0mWrti9MoafHTe0nb&X-Amz-Signature=ea88dd4bea8c7a468c468446eb2d788f8c0b9bd5dc0a19c3d67369be07cdbb71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
