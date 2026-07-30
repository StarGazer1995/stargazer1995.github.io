---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQT6YG56%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T132319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFmxGuGBR74OTEK0qQ3v%2Fz%2FDh5YecX8CdG%2FyQ3UMZQLAiAt3sctYbL4MhMpTZQvebYeQ8OLWOZDU2tmGQd5I1c0OiqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMD9WOdh3uAdoLw1x6KtwDp6XsvWSSAnD%2Bov2OgJG%2BmLMfJfeNSIZjbLGZXRAOFfEIWANQLyTxRrTDzfvX4j4837ByeFha6tWd%2FdngLz0n0shlTLfvoWqZOQmW%2F1qFgETmVfdAyFPqOmNQO8mllW96%2B6DbVtpPX%2BXiCpNSZIIF1zrGFv1OHQtxGfZt1Tn%2BMDACWj6BmkDN9%2BSwCbhI41yQm7jfXBnlEFDC5RwwtIKWKWbxIwkXbVtW0I1au5FzwHLxslbM9lk5s3wSLmzvhYwcPe0J8eHh6yQO%2F5L4WTb1xAf4t7ZoMauV%2FkuYIqZTEUnE7D9nclCOIQU%2BrGQS%2B78R3pyxdAhkC6ic%2FuRBoipnU23f2%2FzWHAeSgLj4XEGLEG3UO5YtH4DSjTgBbmENm5xoqWzLt5fNA8fXQVXrprVqj8lzgJArYFx0j4nnig2Ro10lDwQqooK%2FmAwanGwofx8ZaTBIcoF3stDhHbkZnN2BqtjUrN6L75u%2B2Jn9jmxATq5DxdLPUS%2FUN4alm%2Bfr7f1gcZ5oUurFM7NX7mDXSw7RoQWEQpsA2WOPw8DYTkWQvuo5n9YOq4fbynGkFa54kDrQECVQcTSSsA7VAI9emUDFuXNu%2FMC66U%2Fy8nlR5Fo5bHB6A3xUN66u2KEiNK8w9Jyt0wY6pgHhsr7lijHphsUbJQAHC0DoHuFdC%2BUWivTkdYmxOMYCzz8i8%2B7uHimOo2Uhc%2BA8FBjCrhE00ZX6LJrbzfr5BG5M72fKgLTH2H9xo0xRNGJ6syafwSRPzu94SWXSqN4Bgmz42ZYYJCN9X6qk0D28SFngEELfBcxW%2BHGN5z6nvFVMwIYBv%2BHyf1x%2FWILWQG608NVYItkFx3ERcDGJWs1LPEzV484%2Bfhfn&X-Amz-Signature=cd18cea2a93c3e5cf43f0168b46436da89abee50f4724d773931bf44bd2461f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
