---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCLBAEJE%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T174832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx58oaRrtRtmQ7FHwYs6eej99FMkdcZ99c%2FSPMRfPnYAIhALXcoDYdjm9zixhlQeGxvItI6YopYsQgpNcz%2BdVWoXxyKogECKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxl%2Fk4QzPv9jW201PMq3AOgK0qF0iqV38o2cWhCAqUV%2FgdxZcQNaGJ%2BphVT%2BZG0PlSTnCPtkuPKVPTDsrhz0pL49BhKewv8UNQCXpt0aUO33LQE7Jp3lLeLL2JIJKJEtBJy31yZhgOv7x5EPR81Xqd4hcy5K8ihY200qyhJnD7b%2BSFKJHQ8Wjp%2FArjeOExrlKTxFyI8ftqDWZhYT4iC2tKbLE%2BvTZSqnBPK32fUPfigiW%2FvgNp0Rxw3Nt2Ivoc%2BkJYX4w%2BNroSOZc0SrZRMwe0q%2BmcogC25p8nK5aeOZcjUbvaIWBMHWp51ONNseo2E9u2iILEijJ3JP7U%2F8EqtwjXFNoWAuSZsG8L3%2BS5isO%2FfGuqf8SXxYdGzGE%2BVT9aOHuDhVpDTw0RwHuPtZ92QxymA%2FZNwETD3M8Zc77WqAh1zg5iCnAGhnCXGyEw1lKFhBkJL9pJqO1hjja6zOouXqBTL21ok7xuoYEJFaPAw%2Fl41ktJhJQ25i8QYBKiq6M7Svr8W7cCrRD8AkUEgd6o3Dm2p79zvw%2B1uXW1dULNXkuwstMYs5dNafljfITNimr7ECSoitHaWI36FTY%2FKYwmsj6uyLUqvI9YDLcz6F4RYBWDdpJO1qz08jpxosZbzZBXSjRBu3M1g9eP093%2BpPDC6iMrVBjqkAbprQ9UAgSeGLuMFdsKfZPkS0XyJD5bYGXtk6KbXVrr5HiaRsZ%2FIxNFI9n4BloLODkaTddWcBXaf6puHn%2FIuoZrxhqQcwOdV%2FuNK4YVQOLhR%2Fo71jp%2FW2NzS5CI6q97YJVqI95PHWDT2fIHULKgryA5QWq3ld%2FncWImHFvcanoarZcW76DaxowjxVXJeim2Y9iodTZK9yI%2B942HGZGaZF8ScJ57%2B&X-Amz-Signature=8d69a1912ecb78c3bc5f43f5a64ef4ecf56e3c37574b8bdbad07d9017e438f5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
