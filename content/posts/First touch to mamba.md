---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUJWQDBB%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T020318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJGMEQCIB40pJZ7B24U8n4JUwbDZVXMrJeZrBTeMqNNDvOZC0fWAiAHHuTkoS%2ByC4hAwBK86pzfiDuUZ7TelWUHI%2FDSAWu7Eir%2FAwhBEAAaDDYzNzQyMzE4MzgwNSIMTOr6XHh1LpfDybilKtwDU0pI1g9CH3%2FkGVtoobO1LTP2kIMOarIn77aaaK9ks8fiWT3HqHSUc%2Fox1RTNALYXA%2F7E0YiMuULoFnbXkam8VCj3br7hyQdYggZ86EoGWAXHK4TgJCR01PaRzN%2B%2Bc9h0jfHpG0a2Na5tp6p3GkwEWQr5YyYdW%2BlRpd8tYQxuNH8PBZPaLgVb9HQ8cK5LOzS1hsbB3dDZwaj%2BeI%2B99bInVT55XX8PiJzY8IAwVZsFsbGkvh3o%2FB3HSbKt694wcgZgdWq0if651IFMXa1mZybEcP2EDkJt5vl%2FdJKjqjNqyJZquX03b9DuKH%2BlA0y8Fk874xKQwZgdO5DVMBi1z8bPds8x8HQgGJSDwr6FuOqLcy%2FkAkOvgkQWNNed%2BKK9rQJjdnB%2F8dzwOyf7DNubKpFgFpdxZ5aTIXxpClPKh5O1ninpp3bULRHHhmqSFl8UkHOKxQGeMY3bqtiD%2FF58dGrVzhnY%2BGpKPx%2FgiqeNRBcViI8xBMGNDU%2FnevFKlNNa77zRKxtXJ2lH5yxT1N7n3QkEMLz3uOwYoF3ejidWvUkz7Ykrd3%2BmP7%2FHBVJiO23i1Z%2FdhBB7RoCvOzM8EwGlGjd3VCExbysFGw8vnM3vZOBcUoNasgiCS40Qbhxd%2Bx8wt9Xx0QY6pgFKn5drgtQ%2B%2FMLONZ2zMSfmyb5naUToog76mZfw%2FGfAc668lhlHWce5xy4tOpb3ONhRf6GotCVxNh5%2F1Q255LJNRUSDX%2Bx8%2Bm3BaSYbITigMq993nyK9Tr%2Bdpe0plLqPUgY3bc16b3PVDaOsYlpZ6dv0jKrAXEUxxMWD3WIvCvD6BX0Hgpw%2FW9vE%2Fk3asl3mILbkJjsiu1QSgWDoRk8vQz7EDxXsvJw&X-Amz-Signature=92066b987aa8e291bd2919a8e1e5dece2116588a1220bd6ecad21ca0c344a361&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
