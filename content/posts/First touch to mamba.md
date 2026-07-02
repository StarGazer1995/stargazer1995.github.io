---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MM7ZABC%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T132649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJHMEUCIBxtcZ3Wt7YEn%2BBWsorOgPY9i0W6v2syGZROtW0Hck4aAiEAp0h4Uk6GkO0gskzFRzCwPymMp%2BmbvAlJGCW6fv0EBXkqiAQI9v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2FfIYx57659MR8IRircAw6W3agUZXrSvfvVovER99rs0ladOUfSrx%2FObkKCYlxS9CAf8JJv%2Bvt%2ByntBaP8fnj8oHN99mP1UqJRFGpi%2BY7QE5Zd328XlYBIcTTXJ4QOdWGe%2BoJPic2MpifUmOrZhSKp5Ux734yj45OYK03fGQcc%2FVenRrxDP5rqcF5bHpHoo0jGtC%2F2T4F5AOdj1N%2F4dINeKA55l%2BDz0fo%2FgVQjmEYyWOIiX4mD28tG6sXM1suR%2F7URIn76lmMJpRgV4Mp4Y6EcyWNTW4RqiYyaQ0tKDf4UWN4Di0WA6NPmjnKunCX2LqQYnzt8u2gaKFEwrBX2sjMHk5d9cB1UaRSEtmeZix8EDPs4nXcbwfoKerOKnkh2eFz86P2Ii9OEJU31S60arE9jTowrzns19uiVZtP31DkVYxnMoqEvST881NquhTE9c9BJmOeSpUifL%2FmeZwxCvKN5aDEXoYPx0D9yci%2FQmW8Ij8wRHYnK8P7hs37hnwXsDykPrB9Gfjq8bkZaGpWvJeVQPYlpevLQu194nG%2FBtMpuJq0g2RIzDuu1LOeQNiZovaI%2B1oo%2Bf9jKR9DIxL1SCHjfoK8i%2FyoCk8tcvqK%2BZzkQTR3auXKxmTxByMkSIY1Tflrsul3hzRa9svfwkMKXFmdIGOqUBs8uOKCv9afSbSKX9gG1H07titXpS47rMikpezalemLIsQ9Y%2FZEFmzXTWLyzGeE6FO6VNGhfdG3pOQvf3Pop9vltTK9QZ4wPR1Vi%2F9e4tmW5jwIseQkK2nreDe%2B5fYZLvYV0BDXB3UuYS%2FigPBB8MPqsaKhxLo74XcKa3RK4r1yPVk8qwUj7f6STnvoVqJpiyA2x2ubQD5rTrEv8pLhZmZ3wET8Ud&X-Amz-Signature=2ded13efd57f04c3450e7e5f898bf569281e14dfa594a8a8e9a52319c3e99680&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
