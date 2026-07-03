---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQHLGDEQ%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T185928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQDD6o3WgHUjtWVn3U86eQjsKDeVHgUqcxWgba1DgbLfdwIhAN92HvlN3j0rGC6EkQewPlZgCyDvP7g6VFCE0TwgpBmlKv8DCBQQABoMNjM3NDIzMTgzODA1IgyV3QZ7I98i3X4xvikq3APfUuSbNX0Gzinl%2FBPAA923PIdGf6duYzW2vqdALlrMJAm44pvl5Frg8mRZqKISKDxogfG0WJyb8P869aAAaDwQRy21%2F6OccBEg%2BXAzTeQMHaapZGM%2FknlKBvJweQu23UK8zENCXzMP3rQ6z5tlUKi92r8keiMnW8qhvjen%2BwQ5UvaYmvnjRnHLXGZNSGMBnCTwAKrdLEXGDGyTVluxT%2BtsBhsWoi1Hn1LP7aNSIixAHQZakQjg3fuhBHrrrNdJDV2J88EsDMx7WSkmKA4dgse9EFSmXWCOvCpqpmytS1PUzdBSysbKc4uzBDFCfLnzHu9HnZN9UNlG4cUGStLjPs9w1l83VyDMp456cZYWJ454m4E0tT9QLrW5Hm%2FCLAkSQiFCSoKL8RZ3UDPv08kYqgBEyAizHCbxiEF5SBDNxBYA7L8S755eg2KGcCHFxJ5lTgBNFj23sS6ZQ1Edi71m%2BoR3pOG%2Fp9SsZtnoNEIzB%2F5wZmEMIEA8ZPuewDunCcjh1AqL3R6T9rVMh%2BLxHsHY5Eh1avNTopMj2yYK0%2BuDCT%2BFsXTXvbavqCeHMZUlkVfMzpoOw%2Fmolo7%2BQt86mCZeGsHz0tRCRIUBArXATUo8JeaLCyws%2BJTl7TkIr%2BsbXzCZi6DSBjqkATS2%2BOLA2R4C%2F5v1VC6%2BKaRO%2BEmtWE4HoALmrthzRsy9PXg%2F1yYjOScaSyfYUDhSNhl1VJfGZrqauZOFPOUoV6tAH97jC3WEurpUuOzJ3XWtfro5Zjq9cKe%2BKVCrs4RvtGB9gv%2FmNtzcvZR2JnkI9N%2BzPopHINEuxuLd7tvo7kgZ0hYElZ8Ur%2FWyaK1wl7Bd5NhFJvYEhbEy2ZkmBBOqSoUeVfHu&X-Amz-Signature=98f9a543dfbcb498654785ffe954b5281a5eb282bff37c4d80e81d859b90fab5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
