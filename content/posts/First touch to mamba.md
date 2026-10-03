---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2XEDPKP%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T201907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICohHNjNFOrK1hMMCUXF86%2BHxpefz27hvYQ7VY3LYUI3AiB2jPhscE1DiS5UzI69tkf3fb5elPM%2FwldS6SRvnnxiviqIBAi0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiliBYiWwZ0jnHDDvKtwDlirnWnS6janJxSvKaw7u4%2FjvQ%2FKVFboY55UmtnMoMv7F4Yt2QEJAerYIQzt8wUeDYtmVY8N7P4ddowH14xjXME%2F0v6XlyWpakVLLULf1hDq7MRzAKz6X7TieA5D%2BRpbGBiupzf0BEwCSRGuWnPgU0Jb83Bn1zFb4rFaYMUlEyplQGn8hfekpa%2BtJ9lxpkxvglWQOsMWXHr01AAPP7einaYj1SZmmA99Rszl5AQSWZx8jvgvmH6nh0kvISK3wCAT3U0Lu0COyH9QHleUSWDaPZgUjYe167IzSMN0InRlNZhblRfNmdvhbQjSksHgQo2ucn60Utw3Lkt7nk0%2FUP8DpGfp%2BBBaC74XV8floHOGI35qUUvgVT%2Fr%2FlxlYLkKnxQQkrwRG9U2uJGAsjQcmPfu4dNP3fllsNtsbqnTOx5SIsSX775Twlhfp5Qp%2BCEmrlNlJPjvACnJ60KquO1RtAfKc0WKdmycYU5N9%2BAKykBxkNJu%2FEyTyT3rY9bIyPFQ%2Fz32gXVqC6ErmtUYF4vc43JCx%2F%2B080paBJsoi3cwKLkCfql0tlxY%2BB8vHvy6R8rPCibKbozBAGMV%2BOR7I4zBkTeTewtM1TiD%2B5DCCg7Tsn%2FTprJAXvxLkCBJl94P7aucwhrCF1gY6pgFAUsw1wxeyfIPAFZC26m4zN%2BJ1oXYKz4qtyw5FFAHSa2LDdFOHfcpa%2FctJGzSE%2BLDE2oOQcXF69DV7SXbFKSCJ%2FD0IO9FAF%2BMExFDtPucbPl1pdyuABfDnQ6S77L0zmlIFuYK6xTcUAUdI7TOR3XxkUqWvdvzUvR2uXq8FQoMWeDqv3CjAsyN7ldXBp708tcYu5UEhxLQ5Hs32HWV8%2FMR3jRBKyxj%2B&X-Amz-Signature=d2b1312296a1fc357cbe0fe5a99c5a584dedebbff6ac1b4fe9bd8bd033a7831c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
