---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKYLPSY3%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T011246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQCNFVuWlokczEEDNR40brzKe8P%2FAZAJeljAsEkm9vjzQQIgRTSNaeaIuJDU%2B0QHTkTWDw3bKuArev9DFwLvP9JOn2Aq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDPHG8yTt9Ew%2B58xneCrcA3Lse%2FhYzty%2FAzZYPulqCGtlkO%2BbADTQcK7ykNZvXAGEckFRR%2BeAnKwtjjgkCueyuPGIf%2Fmm6MGvX14govLIBino5Hws62iogv95XYaCMq2M6EF%2B5YIskCXV1%2F7x1K1TgNeGoZyAx%2FCI775SgqTejyCAQ1ybamiooJJgx3XZOhHqyXa8JxKSmdthR8sgdjm%2FrEGHAtwpbEDUJcbqVwpUocV5K%2BM9TOxtwVhzlvC9L%2FOlscPrVIEvYgo89AYOE7czMjMPMKRgUpNZXQnM9PSaxmruYhLkX5hQF%2FIRUkASr4oziP0wFKd1sfSXEyt3XZBYln4NQERIqzp6LLLSMRQhZA1ct04kdEnVBvOcMyD5Bw2NQBQ4QfHWHmYjhcf9BsZhNh2x64NXm2IaxE7LvjAjzfRm%2Bj%2FQjAmdJ8adKi5h8e1cq6ew2GWQUw%2FGvVyCJDh92JbcmHHzF0VhD51JNDs%2FpD5tTGjSHbKAAOYfk8miJRrZt0t6L1i%2FePfnbM6C2cVjuxEW39EL%2BqPSxoJIjEM%2BWJI2%2Fym1CQQvhOA2chbcTkdoSO4EEOIJBxRO5Tj6z19gxTuRhzW%2BjBJDOrEoTFXk9SQ1lMB5mF%2FsARvRsMSpkkGAUxBz5btBza2StmAfMI2H29IGOqUBX1OrxhE4nx3k6ZwSbHR3Uujlc6IrPJkINUQ0wW%2BGZZmtRvLketqPM4qYSCdLEMuKUV32e5XDI90fttLjGmnD3ApmKLSwRa%2FDQwYqTCO4VKIchXcxBu96hD4nWrcR9dI19QaB274cmdG4reG9XmuaYZNn7DrLXNzXZmZvsMM2PuUehyMr5zC6u3b94DhVUHmlLHXxC9Y44EPqknD0YImEMmpvDgJW&X-Amz-Signature=d393f970b3df1d021a4587c9ec6c8c75aa6ff0c50e3e232ae6110bce0c092ebf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
