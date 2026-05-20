---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKUOOOLS%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T020209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIG3lN0BqqTZKS3AiDl4CDtuBx%2BmaeGPov71oeWw0kTGfAiBp296lWJcEEHmJayd2S1IBllhIin62zpjLD7wAH1A%2BYSqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMj3VV7kn7qjapvXwzKtwDXH%2B7Xpjf7dd1qOBKFXQIFK7JmaDJr1n6zLwgSOx30RcFhuv06FstOLwthLxw%2BJAsoiWOCd8fraCg3Fa3vuEqYP3pF1ZnroRtxuWid6oUJGimjIvlv8BGpwx3LdwstuP%2FvYuOgfkKuPFCQN82lCoy%2Bxn0laHsbnB567DYX62Ey5hJYX3Wgxf7z4V%2FRvWbUmpoRis51KgWyTE6ANqAAFV3ZVh8beqISvQVIjS9kyFu04vheAjUuG51Gu5kT0wNJq0p%2FgpqTqckkKPlx4PutZlvi5p%2BxXa3TMNMA%2Fc%2FHSjfKQ8pgJM4e2F8ri%2Fge%2FnVnAgHcrw1tCDvJXW5NFGxuHEGanua0DR8Ri3A7OgiJyWXz0USa74wf5sag6KS%2BHWLS6lXK7DaGL%2FPy5QnEYuu6dh%2BrFXlpoYCdKlEV1%2BkjN51D1nTfgtuQfRcmB6kT%2F9zj0M6xSMQ3M7JrVL7tkCJm7H9VbNpG28pUvmQOK3gKE5fYs%2BYfKXA8oyNxhBrpax3IWUre2oRs6B0G2rpLVpJBknK%2F1PRy%2BvIwSQbw%2BDBLXTpA3OE%2BYMozlNh97VDdzHlkISTIAk%2FS6rcTiAte3DgeMj3cgjQZFkZV4mW5EDhfO3fd7T3dvJHzeW3%2FH01EJ0wppi00AY6pgHbH1eAE1f%2Bd8FqIn38Src1vrZ7A6UpnlISn5jWsPsux7CEsaTjwIW1%2BcW36Mhq3JucqL8tghcIXn%2B8ylynZoMvggoWC%2FX3rW67EgTcYp3sWTIg2MIdCaZzzgDqWTHzkZOhQQCjg%2BCgqI1wN8PBKfh4ZlKRgQ8QfnqYQL8BXuIRGewWZwczb5XgMMHlOMAizY69fH18j5QChbx8Kc7Ll2RXgj1XA0xV&X-Amz-Signature=7465d9dc3401805d5d6839106ff209560c2cc4c33bd2826ec0a01c5c09a9d544&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
