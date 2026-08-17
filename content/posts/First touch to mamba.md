---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XC5Y4DAQ%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T221245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLBzwuZ%2F0481t3FzE5ZRFLIVzaD156eOoFo9LuIymVSgIhAOMSt565i2C%2BunjDR2mt7ws9aryyrPIKY9DK8jZnYETJKv8DCE4QABoMNjM3NDIzMTgzODA1IgzZIaSxvxzFTeHuIksq3AM13KtJCXsKU%2BFd3QjNviZo%2F74zmcfCPo48ds4LqNdskzM3MXN05Oa329q5neycQBTIhLhRIimhezruyHggfrl7%2BG5OP7l%2BqM6hCY4DGrlfqqcBn60fmQuE1S%2FS0U%2B1lPCDv%2BOdg5BlF6biY2nilNRYTAKK%2BzeY%2Fmz7iW%2BfXM8STJcjulZgwyBoUNlCTGprYzuZ35FiuEviwan6n8%2FnejjRT34NOgxplVk7rvW5hnDDz%2FrW5Xc3qu3iyMykwrIIYr6bJcdGnAiIrcPv8QsGnZlM5aqtNh7cqTbKazxVxI%2Fxy9q9TgOhG5nfYiKOZ4iKAw0TAvzUqlfrXjcHoXMDMR0vzXUXNu8qSo81pSgjEDUmEGBnnXJYrx7j%2FC09udYz%2Fi4ORXyqL4FQHRuByYBBJ94CQZMPb0KbrMbagvUhg4EGbgIzoFz5pjZ%2Bs2aCM2kH6IYHW3%2BS4q3NNh%2FdxFVk%2BBXNDk62OhFVkhtvHqTvxoVTOUjSFnhpORZ%2BNyhnbNV%2BbxTmZE6S%2BzNLgsNq%2F37OTH%2FqjdQ5Dsf3bajRlB%2FS7P4Qxv8wvSocZRn%2F2L7KrKOmowVgxKSZFbEKdHjGY2JWYT8EuUdKS7xLps39RcmZpbeIh7x8eOGrh5fpKAOBzzDe7o3UBjqkAf%2Fr2Km0vrP5erx%2BNsLtl0CUe0GAI2oozgmKRCWzeSikfv2F%2BpQ671PYX7s%2FETBdi6W2aW2QBbmP%2F%2Bgxu2YoyscheFN%2FrUQfrHAfy6eg1Y3eWWahJCX4%2B3FGsVCxhEsl6mCxNVZZXDVtcxhejZfl2S%2BZUViAomGkXl6pLk0%2BggFSSDUddzmT5kJr3U7PbBS1C6wsvz7wY8zsAclrsUDjH35tOZfy&X-Amz-Signature=6d0c194accc69f09995adfba81773dc570152333351b992a12155b2ac91de861&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
