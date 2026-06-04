---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UINXDR7Q%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T164332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBM0sfKRO1rVFc4PWqHPCqK%2F%2F4wRB998CTyd2udnzJydAiEAmrn2zbbssWTTdEga3RNWrXMBLRqI2Zz5JK0YMIFmKbIq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDKMfdArnR3PgM6B1tyrcA1vHns1HLVlMHUBnPq40GGZUFLelN9Uog%2F9vtEb0MB9WOvOWECfsmR2GmIYOZrvk5apghOoNM0aekqdGYiAk9KwZ5azwOapJ0%2B07Pj0Ir3N%2FfW%2BvlFUYWbInQzW1xw4zs4DE1UwKWNGnropKJBRv4e%2B4KEcPfbErn9rPB3zdEbJ1PXo%2Fadu7k7H6mnouoEQlbA0ltwaENfdAup331qv6ddS%2F6DjDaE5y0DYhffebMHY5YqX%2BblvVK9q7i%2BumhewazaG9UzJ8VSH5hR3AmUJkYP2aSwTGEmzlL9KPOIALMj8R8th7n6XNO4wgU7X%2FaPqGTZtMsIQDJy2HJ78YD6SPKoSH6UN%2FiQXbIiYZAVgXci%2BiqBpmEIO93RCsLc5l7FHo7nZq2f6A0H6ssL9wpkC26ZxPC3Gu%2BBHw7hFt0x%2BsYmSCxS%2BjGTGIxaVU8qCtQHBk%2BevpCevjO39rE11c6N%2BiqMqLXKzeiGB%2BuBie1L3TPvJTke%2F4rzKjiMSRwINyKkAbkXpzYsrJRS6byaeeDnJgoglgA%2FvU6Mowr7MPqC9La7yc0THtJt%2BmQ2jG7FtGD7m9Tl%2BPKjo4iTbFu6YHORwxHRCdTKZnkqzDgk0d%2FkSZ1o4Sr3K8V2EVD0XXG3pwMMeohtEGOqUBqqZSOaE%2FggB8BiixCBXgSt47WsfWY7GdMoq5nYKTtAELFCVX0EUWvWGOo%2F6TPSVaGjZLMGvvLOBk%2BmljTMqToA4fj076gKBBFOOgBk940GUmL3fO6Aakr7rFSgFIh3q%2FRnJR6qPlabnrry5BDcAUGEmmvMyb6iBevpVKTatIpTtqY7KblyN3cvWbqVHQV4GDNFjgOyFwGUCFJfoKS3O9zBMKnKRS&X-Amz-Signature=bc7db03303588cef962384953dcd0bbb1237dc7e2eea76d2adbccdf163491ddb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
