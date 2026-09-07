---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627EOFZA2%2F20260907%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260907T064336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQDx3QAxNDySJUUB9tuz9RLzeMRasuaPz%2FAYc60sN4qAGQIhAOtTCGQ0XXu2c8x9q1DyCTSq9i9XOulq1XudwhmQu19QKv8DCDgQABoMNjM3NDIzMTgzODA1IgzJjw8wDSh0t6PRyggq3AOKjGWMWALiVqzsiksqit%2B8pFqfZyLM5hMyF18J5nvDrbpY%2BmxwBtbY9pvvW8MszvvopVLu02XUZDqU7XJinDp%2BkRK2sdcrCFqVbOqFteWx4yXWGbjIeZLx0akM4I%2FSuAXh%2FtYb1W8Fgh4pZBrypO3qAlviUGrrFYrD%2BWKlLGu0dddfpY41hQ5mxLdKLDykjWI4TAeRpjGMBz0WdZxtvuoPOIQ1Yb5oOLoKHBIqIngQEt47LNQIEePXwPqrCKMVa1GWnnuY5giqJRrJrd8IMZEwsCd144L4nUnZtWjy4bR3yca7bt8i9glBgocYEhAbsqG12C8FKL6kdZb9NzkTpxLgGUCVy2a%2F%2BZwolHnrd1xHJ5Ttb%2FFddz2moAp4JS4bHkiGUTEubGEGFH19yAnEiWiqWuychGVCU8ys%2BWnRWUrXkrlLfV%2Fg827Zzej6a%2BGczvc5jmAqGyC%2BT6PZ6pCYRgaJrT%2Frd%2F3MQ0OUkU3emGSTaesPb7RYitjR8ctRXOwgot%2FdBB7jgAZJhVO8TTOLLuGsVkkObFYGy48jHi4Pc3fdZ3UWrTdlY09%2BMXQpJ4IDwUKFMAhgKaCr0h%2B9kZTkuRIn%2F48AiOJDOAKGhjnlaZRGBa5ij9p%2BMC0ee7bwlTCvtPnUBjqkAZWT4r04dRn6paTA3L6zVkwhZN5CFCOq%2Bez7zxaLCHniNGU5Mr%2BasrawOoza%2BYMx%2BIpBXRaiewW6NFaLC0OgNPBZWpaCNTpf43qPEUudT06TuaRJeAdUpgVb00L3x1WpjGOC816dZcC6pneVP3D3r%2BkVwWV4e24pb4NMPOAvIEiOSpD%2Fu80mMu20hRCYLP%2BQpmo0pDogPjNLtJYsKSkLTicQFMqk&X-Amz-Signature=74884398d1f017e2c281c688bc7226085517563b364c05b393a194b1faa43f0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
