---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WK2K4KI4%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T042358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1%2B%2BUQQTrG4XxP4dInxf4mhPYsbuvw%2B%2FfjO5P84eqv%2FwIhANOrwd48ZBMhtdr%2B9QEhl%2B2YBTkHS9IAdjAgTWpTyPV3Kv8DCFUQABoMNjM3NDIzMTgzODA1IgwglPKQAXwCT8dxMF8q3AM5W41GC9IRkdPUlucmNE%2B0UYgD9yA86Uv%2BYBcAhiqRYMoxaLTpJzqCPgxD3H%2FZ2U7vj2hD8LSnJ38SLne7yGAs9B1KMoiYvlzN%2FFlPjbMaakUr8LSGh7kvR9TZCQ6PFcZ9dbW7VL4llVjXacYL3juySmN%2Bkq9XBy4l552IXkrteaopw%2BlEE1J9kAPL22LpSEqkvoqu7LI0O8cIDX2LSrMy%2BySggzmeodpCkPB0vUkhYbRckjCuz1%2BGEdLJn0jB%2FAQTd8c6Ro1l%2F7L3wP4JGADtiGikEMxYG0bpNWuVj2rFWNKwsWYALYecRe9wEBRiZtu9eX6y54GxAW4sx3jbLYeKy8cj%2BsdBgNQH0f3m7tJRIvuXN6XD8wAVRzKl6X0mU%2BNhI21nTZW022vcjYkpTkgKfchAhYzK8pOC%2Bnpp1Jhl9dtxwz%2F5tP2AfKuQM44cuh4Dc71nSVSnvzhSq5aGp52UM0wqVPh9%2FRJVVX8HDhgi%2FXezSbh2hDprC0LgA%2FVVxLZKU3NbaCygOOdWenbJt1KJrwyBxqGS5tFHY%2F%2BAe1L6KbTsUKVTvNBcBOe0EerZlzc3khRJk7ukQ3vrWcZjl4p2GpdY7aqebyhP%2FK9PXJfIPT23k5jXh%2BTYx5x53jDLtY%2FUBjqkAXNdJWnsKUcKsfRgw%2BNUP4aHttKAujlH54Fy2uBWKd9GE7VPPEKqUWVmSsabPNU44lFzmrFTeHIO2CYNlOYMBHIC2DUd64UpTqp58XjwAKcZODeSY8CfYVHPxxXc%2BZKw4wcJdrGbvgzdvac8Ykj%2F9fhk7FB0PEcujBawsBYUILjI7almFAxTGMxjPaxXXAwEswM41pMLaIeTtfcNEMrsqxlg%2FMe8&X-Amz-Signature=eca3c280f3eadd4580333d850e5b2c5eb28c136354c08931a6ca7495f79fc603&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
