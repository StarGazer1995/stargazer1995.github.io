---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZODXTTTK%2F20260602%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260602T134741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQCGlwum6ttUwSKaGLHHe36iQYzgOvEF74QYu0SoXuBqogIhAKBTPq1fvwE0t2OBcO7wQdAyzvUrHmFpD9FTG80BbNFmKv8DCCYQABoMNjM3NDIzMTgzODA1Igwjo9%2F00%2F1R7kx0q8Yq3APDSKhk732thZ%2Fd7JNfPTCMU1hw67OcCXkOyF9H0QokHvPeu%2F7zCvnYNLrWXlIf43pnP7KJQTPgGPSlXIkj15tUBYAofCFxcXOjodAYnI%2FBX2tPA67oztzaUFBVcHTlL7bfSbduH61jveGkvPFffmJ6oRkQR1DKW5M7ZEdjmf%2F0rYD5r8eTWMbKnTJV3CP1bziTmPO59plRJUii0GJ48EKdqExk8lZQ8GVD6kN9gei8N312ymA72SLUv8qcWO9eQmUVoKMBiJK31ACAO6kS958fPC16uWX1YOsrl%2Fn72bJXgy6vy0U%2Fv8JUXeuBsNJcXyjhElzuub%2B1hHZh4bggkLK0OFuqj97cblIlKjCLr3F%2FQbvCa%2BdO8AmLojU%2Fq5yB9Dvo%2BfAtzs0iZGHtDFpXpfrK6tie20SY7C2klExnQTzvIQGvt2zrdHbe2p5DK4gO6n7AbnEPrlM4K2kXCGjvPHWV7BCkwPT48uAtZpzSgFv%2FHTMCHbI6M9jzUwzmd8PggaPr03yeuf8OKYpi1w%2BeOO5VMYhmhXZjCm7iaGK9HkmotjPRrjJV%2B9mBuoxAu8Lf1KtNmE89UFA3TZEGBHTRw4p6Zd%2BO0vivOrsHOUlLt7obNsuPX7w692uXlHv2DjCGrfvQBjqkAaxibEFGeVmymxEwX4%2F1FnsWeUne01lNGlsBQ4HsTmohIHL4cKs7gN2mTriywSsiXQ3q6yeNnNED9lNf%2BiNFnigAQJNLt%2BhkIN2bkGEIqblgArErqt6EI9UVwPwdzkKOqXluIRy9v%2BrMPoesirOnuSoXvlYGJOBUwDZISvFgl6uOapre%2FcEbvprlBdkkJqCtE7fakQYSXkhcxXESgkwJPjdwikUM&X-Amz-Signature=5a38fd4ee56808f90a0ff2f34d01c905492278d4c1bc9a9eff564d3d6c297db7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
