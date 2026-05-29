---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2QGXP5J%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T143610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGEUIFVHwx8iX8oPY86mvP6zaeW7qaXPvh9HNXhzPjPfAiEA7x0B6ui2171UYqPl8X%2BJwwRRzvq8H2lCB4kXUBv%2BaCQqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIaKt4gLmobMN5H75SrcA6PIYOVVdL0ClOCutCBH5T7KyoTfLydM2WHxEn%2B%2B6eCC%2BGmBfELmLhbXbYN1%2BKa7Li6jHEJ9LsVoxYW5E%2Buqs5tUo%2BEmqgJE%2BuVgHpQJBRNKxVtisTKeJDSbRJqPNfuZBJ%2BbhiUEF%2F3Wrb37zP2Zsko4cjCy2SsTJkxon7xTFMxkSBxX71xPFHLy3oN2hiCC3OAwjn7ydytjg2N26cDz2y41H%2B6Iscmyqm5GwgvX3Cj5q15lT7WnSmxJFz9WGZzSVY3xMkwNcxRpyFq3A%2FuROoOBA5Jb1gZVHjhZz4Ti7f52lREILCaVADcV0vHxVEVMUCm3ZtT2sxsBbeqL5EHjW01i%2BehxrI%2BeAqlLc8vMaX9A8NM4B9vWB54fD3g%2FSHBd2xdePaiveOn3KAJPWZi6Q4X73A1hqaLlY3m3A7U0LX018onEvmLzJnxWLrEl6Ze4xoQJtjR3ddxmELUSAsmam867jm9J9M5SfxEeA%2BvfbhjVCtZlaLV9ERwt5urblbT60Wwm1YiXwmN%2BVg%2FZAmUG7pbnwJOX2RVnJWYhxC39D5ddWyCAlAJnUyRHL8gFsKt23iVE%2B4KnniGZCqBlFJ1QckS0EV5NDM7WBEl9rNjt4BrN6msE7Z4MF9OiWo6rMIqt5tAGOqUB5FjmVI4wsgLV8GwlEtLaAYSNbidtk1r8LdNAJAng3WP8eq4DqzLog5wf%2Bd9GqPbMtRL%2FamBwQKWkMySDuwCmcOTJhYZLvPoaCIoEWYOEd%2BeBSPF8aL%2BsxkbGnjStrmcAU64X5Vuo2CReNpyH0C2AWmrcHftZXtjEzjq4zqnvo3YhrixWZ1yDXqYzkMRLdFUDgt%2BOVDwyt%2FzbUl67c3hl9gXAtzQe&X-Amz-Signature=67e22e2a4f68eabb730b8e58556a5aa38bb5905f6d80d3ee8d05799e71aad1ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
