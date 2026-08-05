---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665E4UQPUK%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T115550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQC8WiTbxFwFPutTlJ7e%2BbufAjE7O2W48BluxnYCKQDnlAIhAIenayRHNrpgLLfrONkKr9nXIGhzFnsHFuqSo6kZo2iVKv8DCCQQABoMNjM3NDIzMTgzODA1IgwCx3yV4E4tEYHhuKkq3AMqXQUc2xEtFo1iC2mY92XPOIBA2%2F9kA4Jj%2FHJ7LsRHeSIVoKcgy9u9HghgNblw39%2F5QgaHKdoRrcfbwcICHv90fR99yhxjI8ayCGXqR%2BX6UnmNSDmXFDoJ3kaEw0R8kEOtVxgYcwvdESmQQTugSgj2B3PPBFO6HXvDXognsD8XQVvbEfMygMCCeq9p0Y%2FdOP4hF6O9DYiRCUZLYYSMtf0JVE%2FIETzoZpF7wf7m%2FvG2UGH3J6tnTou%2FmMHKDmZUlVEbSm4k1Pd1g%2FNsNMxRiKy58eFllp4yQTo1qKijp5SpGl6I7r1%2BBpB%2Fy8o7f9iGYRctBSERsStUMTl4A0LEI6Rs%2FynjpB6wSk77iziioEfTRehuIVTdeGTVJ2b8CfJw5dG4fCCz%2BldhVOhF0QkdLf8oyT%2FiS8%2BiOX2BTvJqLeoN8%2FWqU3f2Ys%2FFbfOL6Ij3ExQGhQrZs3%2BV90y3J4Ld5lXMZJbMFRZtcIrpH6MAQInmTjVXf2MfSTBONTKggXX97EWJ1aSAmYQrZ15mzybXXrP1Zwoi%2BGIwI0IY9fKVpxYQB8CWKnyacRdMdxY%2F3uAAoSUgUNdepuV%2FSrpEk0%2FXiEYc89utSqus6Ue%2B%2FaDBw%2BJZwxnqAQ0Lv8GKcf40CDCquczTBjqkAQN6TMkfdyyzlvbcJfr5e2yfsGLoixievLAlwntD6oJ8XDfZ9mRt%2BdiJ2z6b82hLFwBLMsv%2BP%2FtEnoFCohgPC%2BjJtORdX7lzu7V9w2adrOZ6k2%2Ftdh1v0fS2QkAMzVFdPpVZgxF%2FZP0UucSeIGbmVn4QRdAN8%2Fdt3fBR9i2fZAvDFuxzUMZoDNZMqjF4lrSB3wrHCxGfvQVu6B70l92tlHgd13qK&X-Amz-Signature=4a9d27402d3ca03052f3f05cd4d8eea20ab71ef46c9ecb2d54b04e495b61a429&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
