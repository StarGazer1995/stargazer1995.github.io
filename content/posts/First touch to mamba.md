---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIJCJ3DB%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T205010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJGMEQCIE3AxjVBjDaI3szCfLMjsn2fuKgl9FhJzxoZvSjwrKUjAiBDrGN6za%2BhQNPMcGb5lGP1rU9I5UA609CgsMwlSBsbiyqIBAj0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfHwateLOuFCPanmzKtwDJs2pxwOX%2B%2Fc49d%2BaQ2IvNeT4nnfg9aAlm0rOpQHrGR8GIOUWLlwgs93AIu%2BbuMXfylfcSDn6GgRzx2lLL6mO76qT%2B4%2Be%2FcqgLGTU6l5ZZTnFgbulJjKM6H5XoWNZEWHucvDJM%2BgLsJ0fDe2tNMUnV3ygs5QJYQqsTeOF1tkReOronTdFO6cRHvKQ9Gvp36zlfwKqy%2F2QNXLFImEYCss32Wt0yK63AlL7yrAG1FPSSNPbpgu%2F0AjK32opxxyU6BWhk2Fl5a%2BYWw8p8eDTDrngkkED0NfO8C3Eo1iypfWdynoP1lFZb%2B19jD%2Bpuk%2Fcc5u7HWCC38z%2FFReE9FMkmuv1yMjQmf7%2Bg9YNl4nHz4%2BdrtJnkAwGPzPf%2BzNjFYURK%2Bd63y0Z%2BITXmCqePdJzEENfFk3Mocxo3x4j0zg86W2h%2FtVbw68d4K0NOkWpwWbaZpbjusueE1xZ%2Bf1ICQ2IjpUAWOWQ%2BI8QsdpKW66VrFbCrC78LGl9eXX7B68FGBIOoCHVaMJirDCFOo04tWxg7gU654O239VSIDiwjGh3nFPTKqOI5U8sRRZHcEcZUsw5QC4YemtsSIYLyi8Np3n9YOoAKw5ZigZA9U5dkogT1d0U9%2FIdI7Y9h3RgVqYW%2FnQw69SJ0wY6pgF3yzCKtVGM0ypPz5Dt4RHmexICyPYZBDK06baeP9YpOJtQFhkWGQV0zjHir2Keq%2FyNvKaLeE1KphocAx8iDJQRvXUByb6G7Tb8GszHHeHbQfG%2BqVSd4SUlr3WYleYT5sRkR7%2FWQY9mGMvAuVIxCD30eLifWreg%2BMiqjgByp0RjQekQxCf8FnenesAZeb7W8T1xXbGLzneILGZJDlCxiM1U6vMnuu2O&X-Amz-Signature=d593e385003048e7c29e746d6d194b617c264b0da7f9985aaaa8355b6b19c268&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
