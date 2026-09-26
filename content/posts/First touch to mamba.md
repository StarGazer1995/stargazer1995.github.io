---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6ZMR7AD%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T135721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCICp8Tatf7irOCYdi0GuDl5QLS5gYzFXMSLppQ3MF7JTgAiB6I1xHHsX95u167UMUgxjhreVbID1i0peCvrjZz19RsSr%2FAwgGEAAaDDYzNzQyMzE4MzgwNSIMpu%2BXWW6%2FIiqJE%2BAGKtwDA9fn6XgdwuriKk4q%2BU8PPFSyk7q2%2FprO9dptNd5IlDIaEmFZGXfdBlsEmO4KIeF1Fwp%2FwS7eaU8nVwvXWGb3sED4Nz6kLy3Xa0jcYrzDZ4Mxpzev2anxOrWAM6F2UAxOqUSziMwxFiCJjDEelKK2tH3RPMpYBMLXuKTk%2BeIfaN%2BBeAQ4tk%2FumVIVwF9FbHofV4QHOz0nLA6yo2OxTa9A19MTqHS8PT6Qf8tZ7kpsKy8IkXqn45ZxqSUgJPN2ZPqZC2vQWUBveFojWmYH83lzaxilceuNI6WiCYRwJ03CyZW4iAOlnuph5OdcauMVh4LxtJfTzieq%2BFB87r%2Bk4dZgpN2YdYngf5fVUBWmNiooGzltvpyt485EeHCp2s44Uh7xtJ7BQ5ReHsUtnLQZF6yXnYI3GYfpxSa3ljXVS%2FtN%2BLOxhc2H38NlMIPVJJwply8nroBA6o4XcYpRq2G1cMa4%2BcURDSDUhJa%2Fd9eM%2BLL7wRtlw34uh%2B3Wsz6RfXlRP5pUiVqqKptZGM6KjCMb6P06QlVmUZ2Ge8vgGmCrvAYxvF92muEL6dv%2Bj7gBo6M%2FVvVyinN11na%2FV7mZcfk50mHvaEyqkJ5j6tpQyCAqWS7SeYsEO9IPubDZ7PZ2NkQww%2F3e1QY6pgFj8pctFeRipqZIF9N5wJp8s8u7PpCbJIVXt0em8Luk%2B%2BEOReyS3TmFfIgHFcCdSYaHitTU1buZUx3XsWTjQItpyvuXwJTPZdNF4q0Uf8i%2FWZDfOLRXOfJElfwGTQDbxCYWSAOVkaSADfdNtPp8ASsaz3%2BLHYi9zoZ1bnrt6fzZDBaVPauEKP1YeGhSfquotOwmQiBw1rj6YqB8lvgpy1ThKLGp7iIt&X-Amz-Signature=f776f6b49edeb9935e98f8b3296c08b014ddd7eedc7265a59174380a322af98c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
