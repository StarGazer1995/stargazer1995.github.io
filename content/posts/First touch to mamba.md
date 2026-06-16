---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROQMZQ37%2F20260616%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260616T192722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHLwNJGbJe3Xk8a88DD6jl%2FunaufMjdGhkxq%2BJtd%2BroeAiA2NBMbvZ20S%2FT7YkKt9F8JFpvOxNfgeA2p1x63LsJRsir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMgsI9eZ0NeYJOUDGtKtwDZqm1XabGtQlAOk8ZddtxFOSoowhejANgrhWfc3FZiZ9EJI5%2Bs3FOP%2FgYJHS8BA4rwTFxVKDq%2F7d43uAzZJ06ONK7IC58sr622HF0yifzXzj21CC9tM1Y6WcqHFl0RdiZH5Wt0CDQtjV5fUC3bdq3Afr55s4cwxkzgf6Xp%2F3Q82HvvhV4n7rtybQvjI0JSFZvHhH32vkSGa4KCEm%2FiTpdyDMiSw4vdcOPqwUzYX3uiIUskW5hcfxLlQ5w6iMTgRfsWoksYtlBZvQK%2FXUG0O%2BVNaJ0aB5XUXPKUo4U0RYPdXo1dMPjkYsmW2snb%2F4NMe3bMTImUWoDXvNUngpiaj%2BHDmzxU%2FtL5p5co6opirfKRgUnf%2BbN0%2BLbFty8sfT6OyFezR%2B5WY0Y0vbunTPILNeAmVwe3asC6Q8cah2s%2BTWlrp%2Fw%2FWqS%2BSCtTi7Eza20aMTeUR%2Fc2Nw7jlMzA4xqPoRv2mgj0VjLAn%2BPjdo02fsW1%2B8UvxQ2%2FBQgCYy0j72qWCUPfW4kIjeRw6DDFcFz52BC757f4%2B1ErlFEfqHdDijyn%2FVZGBJNLLAh33Hb%2FiM1%2FxBzIkyvzz%2FCRr4v6y2P3FMaM7vQo0sdvKaWsZBa3cM2o%2BBTfSnXq44QNGPLsQMwmafG0QY6pgHGB1Hnes%2BpiYH7s%2BNYyrhLoW%2FdWQJrG%2BJt3J1MBqA%2BgsMWYAliuC0SP%2BkhAFjeynub%2FELU2ueJJTfJos0cst%2FQI%2BSqsNpQlK60gVomyDRBeOfX5ooNtb4t6VtaDo%2FEfVV18sUaWc%2F1L826L36IsOllpAHJzkN6YB35cKfoIMU2YkunmhwSa93jqGHLH2Wb00AsRtU%2BfaqqaZjIKngmnx73VoNu0%2FZ5&X-Amz-Signature=1d27330706fd60ed0f87ecbb5b8d82a33c32378a1febdd68b4d9d16fc4e0cfd3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
