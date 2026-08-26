---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5C2AOX4%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T143340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIA7WeFwzM9i39M4sQ3ZjNSRYUGdxh7rofcl%2BtRPoG1ToAiAT1GA5RhC%2BDDzZhaBwOBeCXpi3K%2BztOfCW9zVHWfVlYCr%2FAwgfEAAaDDYzNzQyMzE4MzgwNSIMLl81kFB3RyLd6zCRKtwDT18LgknK6zCHbWJDPT%2FpO%2F49zXil75EUmRFTwAawukA6zhHIHMVrccYxTP2PcnsBvyAyoE8MKhXkJZiWEjKvJO%2FGYd6L4fZgtmQzk%2B5mSvddJIieAKfO3QriwrwozT0UsWb71gYmLw89bV0pFZVtHPdc1h9W%2FAF8jqJ4nIgkrii%2FKcn6SGw8psF4jNgyqyZhnaKvVc5i02qP%2FG%2FrZuFPbgcLO0bXOU2Y9h9M3k%2Bw8KTKIH44tivf4KytTbPvWa79b91frdr0MjylH5fgrrq7TEVwNdGvIlhWWDkQ1v%2BJxUBSq3pihKzeDTLsspEgsjvwI93qyy%2BPMZgU2KlkyKV1NUwsM2JWQAy5XkLbUhH6%2Fw0z%2BY5ZlFS71w6C2appEjPX0meQPkHGy%2BJVfAdNa62rKA716EDpeX6GB0pHgOCYGb3qgWkGCINlbdD3irB3kUHIO4CknkY85wXSU8ZnnqFc6SJGpEWDQUsfaXvkKqSkUAKAWePxthBmOlcJT7rpEQ7T2r95kl5i8%2FigLSzQg6lvtYBTLFK%2BYGYhbU7YAhDQRWWj4sPHVVoUzucZb88lotw%2FNWBwmXP82vvAozIhB0n8w%2FHdSV5f6Lt24Z2zoLxcksTmo9fXvcE7VSwAuUow3uG71AY6pgH4ssACtU4nnq1p2ATxFRCaTe6Sr%2Bep3YI4PsG563NMl%2B%2BmOtRvxNicOXZDo6JenkhoMr1vRGj78NUmIsQwlkZCe5Ewb3N7sNfQs%2B4u1TmCrKwAShauhJkfzlWUHgqU%2BuAyer3yC6qlfh7SAhtaRZqsSorCXkXF%2Be%2B5npmlSV2r%2BqnFsnjtFgKc5hYWnTDdnMGgEfqCaJQnukerbWD6tFvtI6vuaaYl&X-Amz-Signature=b1d8eec959a7169b35057eda20efd3f11f367ebcdf65e04dbbcbbf68ed5d0be2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
