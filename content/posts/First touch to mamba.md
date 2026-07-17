---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UVUYT7T%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T125947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuMkrfU0DHX81r03BTg0UyrLcc7YijI09S%2FcP7ppKnGwIhALwsZCgZml9HdAYfVLNX5DdXVhvsDgIIxbFy2JiM0MqDKv8DCFwQABoMNjM3NDIzMTgzODA1IgzNtD1tzEgvKjzxXqYq3AN6Z4ViEKYEFggasTfrc8HVt%2F8PvFnEctwff9ljcHjOCTjD8t2sQN3OxXw2NwYETiuflhCoXczsy29w6wNpHJRAVATyOD3vR41L3PC2usUYxgOSUFFWVcmx0Ft1Jj9Of%2FaY0FMDZ9MD1k65QEG1TZX0o5S%2FNwtgxUrIpb1KHVr9O6RyVQHHP9UBMwQNapz3h%2Fbs5LM7NLijnVA9rBXHCeGGMVR1xwERNUteJsOGL6ZKIiqysAJbWgFD%2FnhG2o%2Bk98bQm5zaXver4TEOMDQRz3KzFSW4TtlKB6tm38kFJ6K9Xy%2FG0lHjIN4mLw%2FXTaF%2F7bh0vSVYXvSEHCCikzB6BkF5I4wNlo81JVoL%2BADGfGydhnXI35%2B%2BYiHNd8zjZxttvlcMf17N0bGjlXWlxxk2R8nJfTIh6CVytRuIGd1kOY0GGcvyrtEbIIyX8IH7qtBHU%2Bt1gCQmFGr5bhf3tXdz7ZuKybcccDLxq92nrnF8c8SspLc3Fc19QwYT5JXpZqh4skwk2tClMy9XWwdfAZ4U2YZApFubev4kMJ%2BOErY%2BfwHciH9CsdnZvrBdUyPW9cxrKeuJtL9%2Fq96iFyXbkJnUa%2FIxyWJNVXUVuTDEOZjAZVMYYl4QjxSL9DsNXKtTZjCxjOjSBjqkATaBpb%2FclPVsxyGdX95wY%2FORzzL9X2hy3jSFxKrzAkAIx2MyoP8VuSaR8GOxqI1KEebP8Nwv1uygnX11X%2FCI2r36XDOd3FN9HZ6Rl7WXcMW2n5jFstFs3WHyx48qFPqkiqah3wZsAmB2YP51%2BhB60uY7kCRJXfQZTtabSEmwP4b4QsbXbkdyLei%2FykDHLWxoXqAt6aBBHd9oXl5WelqPL6Xu5G0i&X-Amz-Signature=63bbdc2911f424db3cf3dc5e4739aced51ddc78a2af6b4ac6a07329103feb4f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
