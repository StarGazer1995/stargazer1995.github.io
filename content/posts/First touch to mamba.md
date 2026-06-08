---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MUBBQX2%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T230721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjQwB%2BAdehxSjjVGA9ereyxUqVevpIKGuybFg3cY2k3wIgWnsKK7E782ogsSS8lL1s0EYNTvQAEA4TRltGvTaPpOgqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAuXvRM3OzdxBmMP%2BCrcA%2Bd92mxX1KSEZx7wXWxvXP6IIArzKh4NalzLbBLXbopZ%2BtMOkH%2B3UFWMLWUUZd5jsPQ5ipkcMlovOgiUfQS7rtBEEv0X1mbNWlgwe9FRt6bCYYwr4rPxjCtRvvyLjh6MMY3RXRvOwUD%2FxYoHh7lClcS4YR3i0Nxk9vugCoBOK89ENNd2LVF3S6haM%2BggTtIzmAoLUv7ArUwjrn6suEWM%2FUaq%2FFetPr8UQggGeR4NEjNF0XaKiGRJh3D%2FxjKj2RWbQU1cC2%2BX%2FbayRIlpLz9%2Bv2qfffREJcNvdysGEmPPi1J12UxdXU%2FHYKTuc3M8b3Edbx7ZGLvj8ASBUdZAx6wh0hx5%2FhHZk%2FpCHjesKy%2Fkc0w2Kr1sJRQPvjlzX2iczBac8qzYPcAha3aRdNOfQOVqxAKpFHRAwJQVocRLFzhuebzUhj13ZMKCGv%2FXtLUZpCklEQG55HUUl8Tv2FSRWAo0DeTyuNLXHshn%2Bas44Fx3904dz491acZRvk%2BYcsLmGOVK7ldF1a7jyiysJbOxp38f4RScRmZsiNcnOFSdjSTGHoxjty6wL6LpWdXdDm53omLnyPt2hcht4RwaIuF1%2F5cc7Yl4xQW%2B722QspJWJbFTlgIaQrHE6SikxI%2BEjmvLMKb7m9EGOqUBiOOjELHPUAuaTM2fOtXH6YMeqKmji0BQAOnhiF6MdUP1iUMrp%2FSbZzfDX%2FRB5%2BpiXBk5FvAPuw34xFZjKH0MRi5bqZ7jFWUj7Bh%2BRrrubIH%2BeAN%2Fy64QFNWxWnX3aXwQytcyuC6gQW3cTXFY8TZoT5PssoPm7r%2BKkU0Z6AnjBgzsdnH3pdE29iLfiwAiJvSxKyXf2Inh11gfqe2PfftE9bsZNswN&X-Amz-Signature=2eb256205774b73c59014632f1de1e87c155b44f684a6622d484542a4be01e1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
