---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FIQ2NR5%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T155334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQ4HxBckWGZpcqVApVihbnyHBbVVw7trasjqWFrmijDAIhAJdoXoMIJ8LoWFVYd6UPIpRGXoPRh%2F85S%2Fd6s1fCcD65KogECJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4qAru%2F15Vzd3cwEIq3ANHR9%2BcAOh%2FfzZKipKuLBF7jRRbnNbjP9FYBzO3UqSlD1kdwgWQVAZR7icFBmxRD9b59MM56fjTN177kN%2F3qSUvfl%2BlZbazynW2%2FRqQnzXCfpv%2Bn14esfrSQHVe9ZCiJ3Y1HD8Zl9cDrqYFQiPbesQMvrHNhD%2FuMK7QED4Su4BeKrRXL74QXuWxYDvkEH7hh1Q%2BE70Cbk2nXZFuLHjzyBPplIvvk4kNzfMxajS1QhKbSM6a5ZbTFBmbt7eBDlNoCBWo8gvuKEfvgQki5mxDsdSD5jbTpqEdhix%2BXBs0STw%2FCTRw%2BTzIh7ITHjRFZm0OSMzDBWv0qqSOABzXF6xmBPpW0obBPB2ujkFOphlHWkeEtfznMETL2NcraXKFZwNwILE4Qqm3ho5cotfGx90jiteTWsBa221o5O0kye0YPvIh%2BYidEr9V77mjHoRrjORfUgNSG40KZW282lV6n1jEvdus%2ByPqBcHoz0OlffNfvwWsxw7LeDXaB1LpeIaRu3P%2BRPWZu1HhJPNq1M9VvroTK5XXUscqjKFo6UFN6oHB7eY%2B%2FjRtIWSvFQQLpYJAhToJzmCZYaCN5m%2FO4WuVpBBqeoCo8BqsLeusal6Pd6t83olN4vzyCGbzh3lE4lOZQjC5wq3TBjqkAcDZqu8M%2FhGOLHm2J1FPKsg5Mq6IHO3nGdVfy%2B8632Yqxiqj1JaB7%2FwmquvvQow%2FoUZZdasvw703saBJVIWosTgI1%2Fa1X4IsIJecUdd1O8wG%2FezMmZJPMEDoQOasq38C5hvQnY7fqCX20U2sCmX37tWYABn9tOyE8eVmDX%2FRV3OBFkh98XQ5W3ix7JewC6LESwA9M2HEF8UdYEzAEHr5Y%2FyzULCj&X-Amz-Signature=d947aa644ae5efdddbb5da743b83a07fe5b0d6b8ff289ab9a4503571d95fb993&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
