---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFC5UWSG%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T164410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFAemeZrHF8OdNQrF5xZ0OhTBCnLhCEL7x59fCFVx6chAiBBJWw3Yvq9ri2WKyrpc1iEUNJDGSx3TtfXEa8Kpb9coSqIBAiR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdAWbLOJk13pHMydrKtwDOZlQ0nn3uWaeGGrcOMYFm%2B%2Bgk97uBYDpLaGvoa9oqnfbUd7jdP0RyPrsw74nhKcn1MWrh%2B3f3bajI6TWPy9gj940qnxX0AeXhkI3lULMIVcBHWjstdfdc9Lg4Tbwck0y0ILgI4bfM%2BN70Zc0jc55J8fVepA3iBcZjQRZiRDveF8xUZoddFrXknjY%2BdMstIlhxMnPXu66YHs9G%2FD0WhByJqI5son0gd4PLGp82egoG16E060w%2FOdYwH7ND77rW53syYnKQwWKL7VP8XV1531COMvrIQyiRcUlLVqEItIR7goDHaxqc8%2B90ZAHjNdIU3RCcGpWLQ4mJxRDnLnb3vyEVEQFaP0R4NK4%2FuMfU%2Bj45pDmkZppdXVYOObI40Zcj08QKJ6MnE58U7U91mMvS8XK1gvbvlcoF6Qrnh2QcFux5GQkHA0dyJ5aBXXjd8mkVWvX9heEREpVaMob4UBrBxCBZb%2FDzeKjFuUXZGzwUnfAjcTaVci9IOr%2Bt34qXboCiZKjTjIk%2Bqg1eCQgYztx0iLlGJxlwl0vM9hv6E1NUyZPPztuf7kIrm73%2FCWghwiicPAJ3znwQAjZb5Am0NHhgaUgaSjmCweVd1VAgGsGo8dwxE02tEQmTRAIOmgev04wtK2i0AY6pgH0xr0wg86XMpbSKW26picCxL6Hd2pkhnIcCffj0PUgOgxgX0Edr4t%2FfnVSbXItUOv2%2FB6xvk%2FogYvGF666A15fdqtwZxcSdC3oJH7hZ6hubKpazGf0mXflKUEp4kJLl6otSIC0TUP9B5%2Bm5twBwdB1PjByepCWIGVIxV0hFdtMCezcyQVJnMYo2ggGjfMhgXIwZZyGYAJo967V0vJYQxhOHpBxcjGa&X-Amz-Signature=7553099bafcf4f7c9be9dcd39348ed767449b3a1093974f6873a9288ca513a7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
