---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDIM7CTR%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T133139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQD8T9NrokRfigeBrhtj40QJoZWvcStrSDYiCmin4TToVAIhANp%2Fghwlb812tOWBXmq8uO5Kt6QsAhyepywQdQfuFzKcKv8DCCYQABoMNjM3NDIzMTgzODA1IgwxNSim9QEocQo3zHgq3APhzIqKM9aOCSvqnXt%2FDB8Jed%2FhX833cNkRR9R%2BSOCT5aw%2F6NMfCKJ8l4%2FmE1JEO7COootfnMF6z%2BB7%2B5oLNqLb2icPYJzHS2LB%2BBmgDqhaF1vxjBY6N07w9nRMN5cEJ2PmsfbLlFvdaGn6SFIuhHZCFMJ92OaBjSsv35wPwKnlcpnkDT6hwOsR9ViaWmhlE23yTvhRgw2E425d5QRPJz%2Brrmc6HfO1aqiR1YkKHrJ5yAfIH%2FSe3YvfgO2X%2BpzRaPsFtbCF0oyYuAKicmYygQ29NsghBvdlwFY256YAYQ0qblkFtOvQPmD08z7awa6x4nVjJ67RmO9BUnmUihTOWNp657gJRiqBBWKoOUedgs%2BuCK%2BrEZScVGvRnfK7XGziviOy4QEfJ0PLv0V9GQNKOMw30gFWUAk0%2BY7Xq4ho8GOIFP7dVWiUkJhMsLAU%2F9hL2sSkmBLNUDOnkKRi%2BYgCmyyKq8%2Ffhbkw7MnshVuNfE3tjlLIdBvfLFWebaREdh3WuckRZZ8Iy1hMyKxcNzKKRt2Q6kZB3nDM9T5ucpKXCS%2B1a6VVmLa%2FfgwkfHDZNcPtxgUpvC1sE8Dxw%2FYH%2FIVs1uo%2FGoDA8lOWwIeNimjjLZPOrUYQIrBRQrTs%2FMqXCjC94czTBjqkAa46Q8dBgqIwov6o4GLV9Af86RG%2F9liIUJz84Fst4vvTeOgGC2sKxasdVZXRZnAhuUOUag99CujMEymMDgB7i%2FvCuJs2rDIhdMBeHl6vC0mw6m4Vn3nJsfs7ya9WCg29h4mdqQwuY6U3RtiTWyr0LxlyAN54KYsYSqie09qOczDJtnISNXg8hOsjYonIaRIGs7OyaRe2Ps7eW3mxqhJeUHIYtpce&X-Amz-Signature=ae702d8cda62590765d3440334855fc7017c10752b992aadd7185a518029f29c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
