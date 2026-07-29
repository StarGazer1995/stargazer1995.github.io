---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z43IJO5O%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T204256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE7aaaWJrBmP5kyEmgNPsPPstU%2FQ9GvmuVXLO4bcTgX3AiEAoEG4LcJF%2FbB%2B8gSY%2FZGNH9cJzWRi1MfM2cwNBeuMnycqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBYpP4px8YBHPIi%2BeSrcAzYLL3VquaQEGbasfaYZbzapec4l9is6PIOh92vhZ38laFih9A4iCm72%2F5t50IqzNHgNPtUDQYOgbiLlPyrSakEO%2BfaylokKI2jxtakQjbW6gnJA0XdAMoia%2F8cdnjyx1yNwWEfgziWwNDPPWrvWjq%2FT7aqwfIW0nvG4JfuDgSmj6i2p6eqEpEVKImvPTgy2uJjJDrlMS7pTzMQoL7yT%2F4uJTEpaI2nOP%2BVA1nwvMrS23T4BooBgWa1eoCMVXdNtzSt0qV2iAx80kRm%2F7FrqM9fICCgJ8OZyhyVIjN%2FdtC%2B%2B3tIyuC5rxO8m%2FLj2R%2FZNQQaRF%2BxFIVBzHMMaTsoht3FfANsRaNQprn85H7WlIQLhqJDqv78v3MsNIwmheFNympirKSoPyoOD4aDzXf9vq67lLlwTF2T7P67Bo2LkZ6BqPA28Jv7L6CiRcHj00g20U1Q0GtkwMDSdLFNtWwpZjFuixAPpPGnoDp1BzByqfiP8B8k78xNEvoGHEINlmpbGPdS2sEoird7n2IoDZ9KDdyNWBjPQVgcAUGYqOyza4FYy2M7I%2BwgeEp9ZBRfX9g%2F3EyIkd56tWwhA%2FBhxrgIwFZi5aYkfUjBEpI4z9ZFCiEN8OQHDb7b2ItmrdGPgMIatqdMGOqUBWeZ3cPRoDiV57bgCQ3LnJcj%2BgMBG5d%2FfOD6%2BrWLNWfnmONj%2BKJ8rt6Xz305KzGQHoXEHM1yqC7jUQPN9ZvqETKyeM7NXlLNlzTF6I3cUxtYv%2F34dpAeJWLQJiHUdKf7G3lRGfQlvIPavHpHyn4J9wfJL25lhStGlVBsIc7Nb%2Bd%2Fa%2FhTcnUPFeOQWK%2Bf8B9U%2F6lvRhbf2BetvyS2qxhvBM17cGYA1&X-Amz-Signature=01436c028d97b9cf512641e12cca55d01a52e9765128dc9728134cdf9d1eb4a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
