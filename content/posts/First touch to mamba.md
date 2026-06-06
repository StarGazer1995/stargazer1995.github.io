---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVOKXM3I%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T165752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgDeI5CtjPeYEaCtysqeIh7FAtHQYwfYpM4D8SvpKcsQIgbGefaOEgBJjeZ971uvM%2BbJ6vf66ULgVNF3KX4tf%2BmpMqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFnGTeDI7mOl2dwDoCrcA8AXgDwyT86pB0IKwxB6YMSGCcKpeXUFUNKdJUXKAXdSc348kJ2ecDogzkh%2B4rmpqREi5jp2gfZEg3%2FphkrrV8XuX%2BsHNGK7Im456Az3Wf9Z1sxwWXR%2FgDSUUMiNFW%2B9z8UOAT%2F7ZHLLb9k4rumP2B4N9PHWwOis6WTb5ZFo0d11PtrV69T9%2BGd5JdDBNF0mBUIBqq1s%2BWhdoyJrh8gYSyEutqmaYbb6j1dRQq0hWAmsSwP3liAHGMHzdpoh13HHT%2B1evoEMdtylYx4vk6DnLWaGNGQ7VHEf29bvHngs9N%2B9nmaPEXDe4JMHl%2BZPVxMbjenH5SJCsK%2FIRNbyylNrP78Fu8qmwVhwJvEw4GEEvO7oK2KumV%2FYV0q4iiEIA5DyHUN6eJ5%2Bfqdjpn1mbsCrgUhN0uSNxWzcPRgKndaT%2FOKoC4Sh9TuDNLAO0fhyrG5GuiQ9dd%2BlhXyHvL46o1AUZUwSJyF7%2Fsz5WrsTzFLvAktV0xJC0LDtFX41V0mOQ4rJkuaikaiBO7F0ct59rSgSi0%2F65WIZ9uxhIrR8KXrJ%2Fdy68%2FM8xWn%2BBUDzUC7s%2Bb1PAoUj7O35bmgsCoWkut5CybXP4UcIPhx1%2BoSHiCGkbknNUiGuEAiW9pP7lLlvMJOYkdEGOqUBuDUaihvsH44OL5xWF%2BDAt3lS7aaq7ua03fB0mup%2FrY9oN2K7l8xAh%2FcxjrB74wLSrofejcEeJFdYSOHjU0wh62rmd4HveIvGPBYayDviGW%2Fnt3lXmUTsYVW5anwXXYru93qxbpMRCkweSrmkwM7QA1vD8G%2FL7stwKlD0qco0KZVP6sMCI%2B%2BYMxX93auw9qSemahsXQ43gszqlwSC0jBxUIal7eKC&X-Amz-Signature=96d176082ebd41940f68913d3f2a4fcd48dcc4151b14e8fd03108c4c0ba5452d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
