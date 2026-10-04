---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSPVLBZQ%2F20261004%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261004T203503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDFFMjoYL57djJANpQ4hsdLpe3J3stJaFJ66qj%2BWemOWgIgJO9K%2F7%2BFJkQlz7inhABVIgrznQfi27jE9IZO4nHaCKwqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBE4siHqwBvwN6Nl3CrcA61rQRSONaVfzPO3380%2B7hJi9e5mT3egwdKpbIyV3scGIAQ1ctRcvkyD5nHJ50f7eRhtWWf8%2B62%2BLlsehS2hwB6it3xJ684JUus3Q6Nf9bzpXBhgolMRAWxMgqc2DoamLStQaVhl1SuS41b%2FRPgrF1Sc87NGt6mYcRak3i7D3cX69q%2F3PwoNEotz%2FbIU%2F%2FFijbAQgDrH9VPgriwgvww168srIN4i2uaOd5xGnASPk8UIKmDnMX6%2FXUFlpaWrfWgKiCnn0hqt8AkZzcahZGnA4%2Bxx1XNxniWBcg%2FBUy6ylFfLZ4%2BK9KSSTDvcPjUFbrFpAWxFtda1HUTPtmIaoJXEbS2Sr%2FZeE2nDOHCvo0dWQf8vXqlWuY1It300BcMgIuxnMGMFF%2FOrijE6IxM5Xwp6BEMqssgM9ZXMHhNiabubTwS499XHb4%2FmkYpTolb3VJQbKzBq4nDC2SXlD%2FjJcpCbLOhN%2B%2F8s3bwIf5hZytYt8HNQIN%2FvjrsObFZLwVRpsk6Br3DgJCLHU1zuu9rnjEgdH51qfy7mUbVKLxlr%2FKzBz1tph4%2FCrQeNLL6ECfI8u7rsk6wvc5rpeF4Ru5Cx6Ej2S5Ja2DJ3IVaCekEbGnE47Sg1uJwwOZIoetlwzvmsMP3fitYGOqUBWHpswKLPrX%2BafH1xN95sdeqGfYISMjNRjLnI76sVI767%2Bxi2wk4Zf4SaeVf7NW0NGx8ThaaeKo6pjuPS%2BSxSjBnpQvrYtcfK67H58Wj7y6KtHe%2BlQjB4tuSoWIwuPHRbDd61lgOwzpupRNFgPPgNpqMBqj9UKaOw5UvZflFjNzPlQXOccqu2yVSWfuxGUnoJv9SKxJEhDWeAiLvxSJVUqm86SsuM&X-Amz-Signature=5b99d57eda8f06232c4e5b043b4f6bb7af12dcd88dfbd5cbca775f7e443b5b91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
