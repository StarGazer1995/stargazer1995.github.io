---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7Y4DOVC%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T203035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAnVLVpdzjaexNFSdzR9ep%2BzOZNzCBjbgPi97lML8c%2FnAiA8HIaFUdvaNBv%2FYf2BeFfbi9dMbmmmj6yv%2F0yM50vs%2BCqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6By9UJwX7ri2vRT2KtwDi2doqNsLnzDhiZf6fsIKDDxzD7TIQBqhzCoArWTDY9O2uOKKv7nSpomspdkGZ6niLyinpdms2rrZM%2FzSMereK4hcR2VXp1u6vv1hhcmQaD85M7TcDHbAhmmSCbp90YBatfYheIHCWl6Ol%2FBaJTtk6ShaQ8JdFv3zrm7iufzwVOtajG88tXXY4bnAWxGUJnXsvJr8nbrmgJ1YdkQoWXHvtNjdFRa7362W4qjVKVFCLlPzA2QjzjWoKkRLYCYklQL%2Bp9Eq83Hlhdn0mUxwsiODBEqvr3JuScBO6PL1w15V0AtFKsWKv8lVKuiH5q7cZ9gz2TqdqwayvIL4HRTgMOx0o2Tl74sXdtzgVjNqhvef423bTVN1X4wAOpLW9MpgnwepOKbHoATsVRCJ6W8VBmJPQzR8J6SXSYK1FXdz0RdK2hR5l50meHXYp8DKj0KSlGCmGp4RkzWJ1gv7rMna0eiaeVVFid4TAHJCoJON%2BY%2BUN%2F65ZkACLSYwl%2BE4enwYVcfJe4aYpnwfLJFyU7p6crO2OiJ4ELnFhUm%2FcTRNMBCZMFrUQZV0RZDxg0YLzxk4Snbc062dgQla%2FO5cCfKuvuzlvzSvO9YWfwZ149jOqwogKhUlrBrFomabROLeBesw67jo0wY6pgFdwCA%2BkQecl0g92RLtT2rcPnqbc7TgNLIsMHY3ghRTuTQtGpjWpNyQ4Jydw9zpRHaD5Q3vmhYbw5fPhD2IGcjktde9omp6WA0AkXECVN1tw4Wg1L%2FETFPY5cE1K7dj0BSobXYSw0lpZf7DK1F%2FUB636GaEvPUdWdoNxuMRcN%2FlA6TEBW%2FuSTZaSAAFo4eas8a8ZtCoWqN6mRTEl%2BxM9rPV3G8tL%2F4e&X-Amz-Signature=29de81a59a4a44c030d233e5553d293eddb6b8514a8d94c6c66afc0e6edb2a11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
