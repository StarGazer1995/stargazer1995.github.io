---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646TWTO7H%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T045457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF4ZAqC9cDj5zDsGTW3Q%2F22p9y35uqhnybiq77YtZ1iuAiEA%2F0u0WzPbxKcj%2BovOLQtVLwdPcihq7ws0l%2FgI6jDEkMcq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDMPfNmPqOHEXlw5JfSrcA%2F5mFrNj%2BhJaCJXK7YHV%2BaF%2BZ2HnHItlt1ANc0EmNV5cXB0SvcHngSdGwwHnZpvkcVztPbXjzzXauPYCR8G50vM2nVnprlaIqycQ6Cb17nJtV%2FNkMk0vr9Ul2mwrO0j49CwrkPFWvev8Lrfkznla%2FT3vGWBnrhrNuODKWL4AdUqD%2BzXO0hQjNk0jYrCv%2FjgsXP4ZKR3AO7%2BkXUlk%2BE6nrwN4qaghgV0CepRsJwoRyUdaezRmBjSd2%2Fubpfn2rT3INLvkJb9LmOVc99ATfOJAc7DbRijurvxkcr0wEqc7jeNoVAX1IyZ4NXDhiQnuwX5OjT7koEHZXPZlv4QAapsXaTw%2BQoq2QxGmk0gR6wWlI0QlWl3HYU1dTAuw2d0ZPSZ8heaKqKzodTJ0WvbDdad%2BKabRQn86NVK4InhTMtvA8cFfBbb5q0%2FKt7SDPFlExah%2FXiplxY%2BTSkkG8vSmhKd91GeukQDLbvf0vVRwqf6Vor%2FZciBniMz75JPpeaXPDJOLBOIgS6egpLsbvwJ5NniM2%2BF7vo1DKcCCswtA%2FuKjQgecMvDUyg4W8xDJXF%2BKAoEYgW8hTNRTO%2FqY55RPBD%2BfetZEI0l%2F84bdn901jO4lB841dg%2F25kKYgsSYvbDiMLPz39MGOqUBPsHCfl2q9Jl0Qv45z0Aql9OQl%2Fu0uYrO0lDPt4ps3LkNsh8a3Ucbup5kotjYefPzLLEJMCmuo4lZ2ead0jYe%2B%2FKqFXSvRDyQAm8KcYVc17B%2FbSbrd5IMI9NgAhldK29s1ioWjO4BdjXkpFfqQitxjY1f%2BrHZugGfroBQfJfYybEbsBbenKnCIKkMt%2BOrfQILI55B4K%2FrzvKGM4IkQXSs%2BTihvPz%2B&X-Amz-Signature=e5f280ee0bfa1c388c334ebb61bea0e623d59ca063a7a0a229758f93f88cf579&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
