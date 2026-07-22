---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JRZUIHF%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T080603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIELaSOsgKaGokS3DkoChUSql0GfCY3xZjHUylCjGbklvAiEArRruzCvigbiOZp8NBhu2phxCZzgP1XnLw%2FozVjfQPswqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEdejSA9fKwNivPt1CrcA%2F5xbOjDxKqkLXeCD4g1LNepWZrRXObVqrUKJ%2Fsb%2BwqNvkR1E950SnnKEwJwIjpx%2BxgdSJyXWoLSB7bhQs4jyfUfcVSWrXu1b9oUZleo8TmNBbw3tpNl9WkUR4MxT2i9S1NAEbZQK77EU7qKrHPmeALmyiRDNJwvHnUoY9%2FPAB9MQnj7cBFsMOPbyz01SmHvygXN0m5M6e3lAGcuSZpOKbVUZOiCNxfyGBaLmoCh37TSq9JAW14MIyDpRvlQeuTuGHHREWSmiWgE7BY6nf84drXDzcZ3uG%2BswV1bWdrvnOxXkaUvGtf7I7d%2B7SlrHOtXRByiLTLIl0iFr3fjp5PNgTx6vv%2BqBs4TiDAU05Yrj9RCP7lJaWIR04n775V1YdBtmnvGxeVj38SThVM71EOPrjz9oN1HN5scfdczLq04wQZYMlYIf%2FFGfeaULqs57YEzps2QFhnXi%2F24TTW5GDsgQSxfy1b2Sfm6Kaq0kUINhJOXNQanltQTrwcRD7mnHmA8fYiZ7LJ5tQW7OXLEMyiFwQmU%2F65kzdK76OIXwo0iLRgWZ0wHHxSyyMTQdNR14%2F7%2BsZ9ZAWI7n7P1rQC1q9%2FKxuDwcnM00grkD4YG9AaAo6tcFRwsDNNEhel3btLCMPXagdMGOqUB2NB3XiRX5%2BHTdZP6bd9GW3DJy%2FkW%2BzraWhBh2Axt%2F1h0CFParwuqjkKrCNoXKWcwbV8%2BHnfsfrndiBAlmiaPt%2Faf7bVH%2FtemEvziBKfdQSqvjKhq1CGPwBt8SRV%2F1oO6GblbxrIiHYGY1yBabI3wzAx9gH52D49iRREq3VBKFJV22LoxZ%2B7n1IJHbHewYMOUO%2F%2BtSe8wGU4GKjF1ktP7tWEaREUU&X-Amz-Signature=b0b8b2ce3a89f2f27ab135fbaad79921e78ff16c45da1e10547aee3cf641c074&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
