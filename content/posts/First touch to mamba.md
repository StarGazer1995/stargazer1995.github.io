---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674EPQGQI%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T190102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIGCjjPgn%2BbB4DE694deB4cFiA0AGEisLuysVWxiaAI6lAiABHW12fq2IeiZym6CSCXBhiVHfDPjOOEXXpBTiOdOQ1iqIBAj6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMW3HU5Y3cIpE5jzyyKtwD%2BT0Mhcfb9fahv9PN%2B%2FTos%2FkUsH60utR1GsFk8MA9gnYVyfWEAh7cFehg%2BRe6yW6JkDEZUcJ6PjoqMN1mRTDOOcf5C7xGylfPNaOhSsWLzpvjw8muOT1lJrsv3nz54qogNT%2Fdf2SJWI%2B7RD5KJF9qeU1bHvSKKwh6JXJj3lGM%2BvMKcr%2Ft%2BFc%2FX7vKNKds%2FOK8y1UQEHJHTKOMX9OggTYt1jRBhPwpHqB%2BVT1ThsuJ3CSqna%2BsE5w%2Bjj2y%2BawZ82%2BbaMNbs9HAuR8lS8%2BV%2B1JigoGn1EJmB4TB0tGuSjIki0%2FOGPEXLCPDWDHpOk1lPBU%2BPd%2F%2FMQGSbIKuevLuFxUW3hckdqZUJZZkJtyINQVjePjUsoBTHh64LAelc9ST5KtC%2F2MuhAshO668mNlK6XesU93kpddIJUwzFo6B37MLc27A2QdXKjBSt96KpS9KEyiNmEUWpDMnIUuFDeSzrHGLxqevt1x6vJGldFqJgEdrUMp7tdkSYXus1c0SVcdTAFj5bsNmxdL%2FCXfZLP2hptr2EAm138cvPLAPCAOgGZGi%2BICx%2FRSkRftynBtdp5yhX6lYtKx2Sy5Fmcy3JgYQ%2BM4Fs0DkSqIn37Yy%2FDgnCVNH1tvg19vQ3t5muKhCF%2FUwt9Hx0AY6pgGrpb%2FDlj8ArsXLPWp%2BOZ8YknUvNnGjwSUzJT0g0UayQKLoA9wfyunRNHHXB5LcuWdL7uiGCj7jjZ%2Fx6LcFDnS8DRtNqh5KWrx67hz80wZGgA4xgNx8pnOJ0dVuLx7YxlkxqLXwNrn2kVo80AiK%2BPC%2B6LgmNGlQfL9oZpQGDXsdS9%2BinBSXjFTb7W3jMuGpF6chqXr85hdhdcI6ScxkC7LXQEqfpXAM&X-Amz-Signature=63050ba3deaab9310ef8eca37c5aa7fddb8f20c576adad07c7c6cba5a2136cc6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
