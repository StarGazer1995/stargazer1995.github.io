---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667U52T3BB%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T112959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJGMEQCIGbV1mY3eCNBRdUbJgFCqYMmvxELVbkiVCsRw8awVMt9AiAp%2Fnow3DXII9MpPvN%2BEi%2Fe23K%2Fse5hagqvbr8noSVXyyr%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMPQp4gW6idtec%2FkFXKtwDSgzz%2FXrY%2BJblt4VxwEKg1oLZOtc6VW%2BUzZHdWtjQzCFPmLzmaHZeMba3fRBXRw0oOgNtliQdCPDrPqUAA1UNfxjA48Ov18cw7Q4supYfAgdRH6OGKgtiTi7oruAKrOJEoUpr6Da8%2Bg7FZt3Q0tOqWe0fN6KmpHWWIhPdJpDl3Mx1MaQ7kkinuovt1CG5oawwmj%2F9up5pk1un%2FnkTdS42BD4djh5gYOdZI0NZ0MFg4%2F1WTcGTj1w1typt1Xg1iFOg0badma4%2F8VGg1xc0u7aWPx%2B3tfw3wuVLjCzcgFKvbvEAcLuNw4tcGyg50tGmHie5mjX9%2F7ZtTG5T9Bq60%2BAdlhgCwcrm9GGCUQH8LdwcfaxlmIAdU9Ax25FbZJ1800TBP64JjBIeopv7MCpavGI3U%2B4cOs8ODuSsBFEkA3v4Xl%2FoKch3viN7plPSgAP1Fkaxn2HMGg7lLdwakZ2ZzcgQGTGdHAhhlmhJxzkVTCvzUhocsD54XuJxFubMKeWD6JVRhboTBlYBWb5P44kLy49IYv4JhMXU%2B45sqhKq%2BzQcN0xVmA745vACFZLQJDhu5ghhZBKi4a%2BnZm6USMqEIxGnuQOli%2FksCJyy%2FgnnZTeOLnAhZp6zQhs2zCGM8EAw1eOM0wY6pgGhg02nx0y10SojQudKuTsDru15oRZq0UmEGO7sFNuoGbnyjXlBWvF9YxuxYiTua%2Ffkwcp8zZuWiPZnOR29g%2F57U3yqLAObjpjswjSAs%2FYprk1fPHJit0oh38gamreyBQcSxQvIy0U%2B8KhUz6EVLotUswru80%2BV5jhda7tkBQ09XjwTmxCYGGQsJJGQ5JHUIHkoAkmSfv3lOf7eSeYYkOwap9Okji4m&X-Amz-Signature=5fe73ea4f8dc9934cba0e1828359710407254a6f6269c3ed3ad07e4019ae3b05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
