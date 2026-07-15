---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W43ANTCQ%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T112021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQCc0MizUPD881xK%2FfndWVgj5UXrNJqafC5ljVJJRS%2BXsAIhAK1B%2BeazV9auTWZgKHxpKD9a0eJBok1NMwDghYGmkooPKv8DCCsQABoMNjM3NDIzMTgzODA1IgxFtlh3ZPoY6LwGtRkq3APzjwobRC244nnxOQHrKqy1rZdzg7zObpcMJJHe8beLK3ChtmiJxreOBfINnZ2JY356amnCj5T6HYMfP1vveCXgU6f25TUbUtI%2BC3ETmOB3GkFS35EtlDcQti%2FTop5AnyBpLiXky%2F2A%2BBPj4KO34s1N75fg7O4QJnnUxtDjLfVFRCvB3HYzTlKc%2BOVTLzUb0Qy08yNedR%2FtKeigLsmKsY2EU%2B9Lz31dF0QJKZpGHyIwTDDwNXco1X9vn5gGgw7JVhY3%2B5I3SW3coEejo2I7UDwqzjWpxIRnmnTOX6Rq9j6z1iZVUJ6a9m2AkfH4fvaSHkLy6ockf5Heso0Qtu26ytN8JawkOlNHHnONfPAQFx1xwuJMxpkZ2avIZY6wUvThYDmFG%2BSYajn2HNJVhUjpGkl3nNeY9MpxwGlxwp%2FKndl5TLQXGykqRzGgQYPKbxXv3lT1cTtmKwuat48EUt820ruaZpVwePlxzyqNJi%2FCB%2Fgc3Rftfq2jYxKFYgpcO3fW4icBwYDS2qgqKFudhnNhJsMP7ufjMsa0IfpAd9n63cBxGYTw1cb6pSzWj%2FjA0xeUYohy%2F4uIYbZ66KWuf6rntoIHKiAz6jfp2fZnYmPffabwWK1mQTaFJ2OxrwQQDzD6wt3SBjqkAYHOh6F9dvm9Vbn75%2FOMSVoIlj00djhWAshTdwVmuemvix6L3Wf1ybjPXkaaThn4DcXB%2BJh2AH5%2BnYEhm%2Fp2sIe7TImNeqJspJjaDd%2FKoau97ViY3wn%2B%2B60MMX9VKW%2FyKeFToRpjSS2R0w3tGlF9ktN9nZZrlQtxl5N8wqx41uDYxQN9LeXrw1F8pi3CPZw%2FTaQp37T4osVHuBKeXUbRzHRq23Mv&X-Amz-Signature=59351a57e053d2d7adb3f3ec34ad1b94cfb007239429e62de3391c640777423a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
