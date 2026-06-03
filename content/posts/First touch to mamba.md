---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZDL5ATI%2F20260603%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260603T084735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCID51nHbcTbutly1vgEzpwDdr6EZSD5rQQ5YufHUWO%2BrhAiBe3%2Fr6XFr2tuG%2BLzjF%2BZF0ez4MiRtn5la7lX5h7zBS5ir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMRB0HemHVTvWxxkeZKtwDdS9e69pgbDlJ4GuVDyVVJXN6oxWq86pzZA7gwhrUK7fBvi8e4UwV%2F5vpeXxCbnKwKHk74JifwUL32vuIZdhFGBqv1BlzH1lVS0ZjAgvfph2Di5qTEJZMwE%2FL0ON3GbIraLVLsnfYIH32M1eRAUIFpzbpLNV%2BtPna7dcjIcelBrtC0uZmnSeIQ%2FpZImqqpH2qO9bxElrB8hZUC%2F8mT8a4vecEwRHssGGYnT607XRq5YL6EyxWom0G68qPkmUpQbudHMwYEVs%2BTCHoiOFi34BRNefqE3KxbqZ1kX2bjVR6ZbSGtUqx70zAWjJUe39IWlL7jHtSvVZeAF4FXIzOC5eO920WL%2F1yrWYxkk6Ep7AWlxCn2m%2BvFLQMycEhGWO%2BpQxnp%2F1NCi7PAks5pxYdM9tHLGW8bQ20PP%2BDp%2FzGVoMfZIIoaCTNoVr52RIV1%2FHnPHMbUdLD5HbFBL3%2Fz%2BQooMnQBKX7s94bYTsxwqOpu5fNzj%2FOn9k4W3M0oisErOhAaGwLP7y0%2F0puyg6XzylzLo5ChgudeF%2FCuFsQEZ6jyBFQZ%2BNDXoJPls8fJYlr5MTuWht%2Fpynx3B62k%2BlTr2nQvMJSBetnT9Pm6qvQWqph%2BmPrY%2FaZM6DatiNtFWfyq70w%2FcL%2B0AY6pgGxEgkuwzyP4yW54byp9YbOmNzus6%2BvaEZDgfkUM8ANwxboypR38LsE1pOPBUjfJerC1IedYcyVmbj1uWWGHZAaN38aOhvQK9jSx3yIa9qedCL8PX1t27QNjYLeF5HFvTyKpzix3HUAShjCTNjkX%2FMCiF7P563t9WufQjiO0ni6tf61ofrDS%2Fc7ViR5zcpBJle3VFDjxkIQTPxOytTHS%2FhRrjcf9YAk&X-Amz-Signature=54151ed24a52ea9e25f219bb7f43b2c6a8d0ae7cf6cae1a13d198cf249ed64dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
