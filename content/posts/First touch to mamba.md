---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRTTA2AP%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T070902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIHHzyxpk3pe3%2Bpim9ofKlORn%2FV3tnYfOU4nf%2BY99GT5rAiEAiEmUj4zyEEhD5B1%2B3qYNt7HFeAPcObdv1tfelMTVP5IqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHI%2FOzS4UcYlUQ5lTircA%2FYeRQLa0%2FmZiL6ShzRpS5BsY%2FUFq69K3iz70ywmAkAPGhXtYvOnosGOeKABzkt2UpRIcoj2eSC2SOuoE2eZaVVk4Q9PzKGtZWpvO3Et7aTBXc4Or2N%2FLRGiFONhuFwjkwpK7OjR0LqwZPasacFDLh7WTbKglrqbkzzvmnWsdCDk%2BeLNnvqWUE9pogDKFSjEcA2Mz7hN%2Bzg4auM8bOFyCZCxymD%2BowPYViFgLfSp%2B9EnVpT%2FGsOrz0TbiNkewfFSK2pmpJtnFgmAO9MO0aekzEsO9o5m9B8tD%2FWUWgDse3JZPvmxQcDv2DCCbWuoPsU%2BG39f76%2B2Y%2FWghlRU97X7WwTQ32lnAWVwe4arIe7H6J9QnyM8pNpIlKgLrcTmUDv9M48qTOKXcMKXPnqyzbiPrBzFdEwlPsZ0R4DHVm6KM%2B2Wm5gqhFUvDrmNNzD1zYrDz6Gbm%2BQqozpbyVxEPYeltBoOS81R2OrkbswdllIf4ds%2BHAZDGL3QPpQ7YSBKZ1sIabZoCzC%2FOCnhO8UgNKN4w19uYjgS6HIbz5YJ2IgcrasszGHqNCBvJhhFc2kpV6KsXK5QnKzz%2FdfbZPQWEVuKr91ehoxdQXkHgpQrkP37SKpcGBZQn4REMkOmKSQIMKy79dMGOqUB7M%2BayQg9xYRzf37ofZOVROcxfcXk9JTdpbFWUOcOkSVudBajIx5OMXyPgW0YwKO7mDH6aUtGk%2FJ0%2FNBfDv86PMgpwdyiROHL3HHHasZVuSWfrHcW0eSGa5WEeqSqY1qT34rGPaZZgkdzb6sBVYxFTWsxgWyU4PU5usJHuaC3XF21SIcJDs0kqmSb3%2BgoLXnKtHqobPFGTTxTLHk62tcw85yn0L6S&X-Amz-Signature=35ed01e13548416e7b01ff931b8f5866ba100ab9f2a50a2e79947168fa40a69e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
