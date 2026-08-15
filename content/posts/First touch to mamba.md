---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUKB5JZB%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T081428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJIMEYCIQDQwNNKoRp8pp%2FtybsIh4fMoR8wnoCt%2FGJxUKhhlq%2FvngIhAKAwM3xLakoGeAclzSp%2BIlr%2FP%2BtCHWdXxOKqy3gHywQxKv8DCBEQABoMNjM3NDIzMTgzODA1IgyHqi3KCY4KFo4bPQ8q3AP547beqw3TJa0V45v7A4XRhd96WKJTeEs9sl7tA3YG6ImxM0nGRQLxOEJ0EHL6TE76AdBU3Q8v8rMc9Ov25q3aNBCPWwfCKIWBcB9RW9xVn89FkFMLGLVFnH%2Beo0%2BbbT%2BlgLwDKf%2Bf5tF99hyO0cm8eImETaIw%2Fyt7PV8qtrkJ1IKGy3xG8vMxnqtOnWaijTnnU%2FJ9JM3z%2F3yKFxu5%2BmaPD%2Bp6SVltM%2BaIYp3GYgns6XJVNL24U%2FUT58fB%2F5mwSF6d58iL7sUmiNh8qxnnMzVXYQi9uHt8zhOQtTM9zCLOw5TGyKHT3FYuzdI4UTmJ%2FxHGKksUhZ4TTgQDoxtgyKJyMS6JfU122AfIYRulKrmpTuFJmrfxPJkoJlRtJctILH%2F1ozEVmdhnxinrypLn1ILYutXcWVJj6nahiylmdQL7svzVfg%2BjxDkoK%2Bw8AZNbn%2FFBZ8ST32p7KY%2Fi6txxhO0lirbcsLj6MuZLiZE4Ff1mFspKKKAkfGBgfBkQI7PvCzbPi6sobI%2B3C0CvpmTl9UAJ865svfwsgHEOT4Ezd4aUL6m4N%2Ba3G7SXjajTzt22ZkkzDQTbdCO%2Fvxa%2F26%2B4hY6qcJPMU78ZgftgZaolm2ed%2BT1TuLHY6fKhgYOAdjDptYDUBjqkAdRPgY16UZjVlEWtM8uusTb6VVopn%2BKa5IDk1plqlVbU6jPhikci%2F7Uo3y4cY85FbD02LUkcir8pEmghF41GAjQu5%2BRejhi%2FB0v0%2FH9LSY0jsWGH9xy%2FXW7FDH2Zfy52s%2BBp1eIcVUv8vbv4TCSQsUZ2QHPZW%2BZS3G1%2BdyiI1mKSe7W5QvdSKzr%2BAw6QC4t5ntYEU7p59mV%2FlQywpaJoH6u5Tb6q&X-Amz-Signature=ca8e53199a2f5839c88341d37218117381bb81ddc362ac5b04d71968987f1362&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
