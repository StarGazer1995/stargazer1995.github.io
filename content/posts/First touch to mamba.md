---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622FEC5UE%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T213224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIBMbeuhXCC5%2Bti5LBFo8eha7T2lxs%2FyDA0WV99vR3OgmAiB18VezVxJB5XkZPOnn0LFDTUl1esDm17t3buXvl7pcBiqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMy4ciHXLldRA84LYYKtwDiOhARBdI9nF0sW9BgVFvUZPuPDKelbKah2xiCvF2w9NZiqSa%2BRv92%2FAyR7Zm1T6OeRG8vUCdtDxrsVXjVQf%2Bf9f48Aq1pzFM2fD%2F3eTzm9rF2xsD2p%2F2KmldFStURyx7Gs8QvfZkef3VI7BP%2FsF8GPBgaszzZ8crDtiD1D41IxH6moRoBgPFT%2F5ii%2F2UNE64yZ3iazK8O%2FQ%2FN8NZc3K%2BQpJIjYob7UqrsFyZYOtm%2FhDmAx9oYGB%2FHYVV0rsuDKABGpeA4dx1h6ZVccrHMc%2FPCTOrYL5Oyh%2BievQriQnd2lm1yCxnxI9mQaxPz4k1%2FlHw%2FoJmwmLXg%2F3CzHWZGCCY1jUU%2BCyPzT8z9fOlVNnclcnzqWe4Vo674hQ%2BbELFCuwcZkDIOUGUFg5mUKw4UwhFbcFl2KD6uDlVuVtcBZfyc8rU5rPogxTaJzBk7sPJ8vWD4fjvq%2FbR%2BpCK0tPdSPJC1t4JEh1pbUZynnrrgbEFWxhh3JZ5M9Y8ScanEpKBqNaW77%2B5RY%2F4BFmo%2BEixJpFlCpGUoh%2Bo0DCj75%2BEJ6kYxiMKhnelRUGbCQNEIRSyfT6NjoE%2Bo4C89gHHRk47LRCgdY46gdjucBAPoSTOk12O0LRadwHBD7RR4eQJcj0wpN7n0AY6pgHVWMAQWLGhtMzTTaKhqVHo%2F5wmeCNp%2Fu5LCPK7Ak2nfn%2F1p1wlsjC8AWUSCI8jEnF%2FxLmYFnMfpWFoys1z%2BkT6A78ECija2vg6zDp7iAGTowSWejusEWr5%2FClyQJlItL475kFwPTn5g52J9FKUVe0twrh2KaU4elUkuNVBShC%2BBoKczWwuCDAVbOqUlu2LBJa6PZngpwk3EhP7E7gcPlNhavf1iTUB&X-Amz-Signature=4d01146e84d9492f243eb4e474996269cca9a326190e0d7a0be6323736eb4846&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
