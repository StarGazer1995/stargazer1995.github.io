---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMMXLBXM%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T080455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFvJKXvXM9if6PoImI09fQpdXDbsQHCIX8zUlWGXF5ZSAiEA8HdHPK7TkV%2BE%2BwJqb0WqoCV3pQ5t3HhrzehPhwgepr4qiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCnxwKewPPv%2BbhXVoCrcAyywrN1mwXz79ThaY8btsiBsoqn73T18%2FrWc1TlpfVqQi8RxXPkfSzkA39gTNBMbuNPkoFz3eBWmmGrJpT8KuNi%2BicVBlMoMNo5RoEDFhHrES0uekaptCqrSGvCF2jx6mUmLL7%2BPJHxUbegah5UK6mcjVZhDWsAivEKq52WXeCKwnJlWfFFg7z3D3DSWynbW3xQjd3OjOmeKPpcVFJrPiz45G%2FrmENCRb1mwOqoQfTWvcXpfUcqfpDjCUbtVeI9tVPrTAMe6BM70zz2Un0koyRrCGPCyjHcpjIIvY4PT95D8GRRIZzYdOQ%2FmIM5Chh%2FIs8GPy%2BpX7EIYmf3DIyGw1E0syl4dxoTRndjp3Sa0ffJqBpjNOyjCy1xeQrPOXkt52Drnxd6VdBiAtLZ8pxrAibWlX5miW2K1umEk3fSsJZu9ulba5YWs6earAizq1NlNvbtOph45NBik4AVgWbF2PWXdwLp6S6aRprh11cnphOS9Hc2gX4fmmN9FkSkRisOTwqUT8X%2BZovVAKsB9unqEqzPUCSOqN9bYForWkZPFJTeXuxROmNYfM49S4rAyZGf1S2%2B7B6sF3W7%2FSzJar34gxQ7Nfrs1rjlnLN0cpbW4mRsoseMKOshgeOkah053MObe688GOqUBU7kAqooPKbZFNcaDQ7ONsDErYAAB9nD2pYL6vqNYnsR7AcVo9S9vTvyWUR7yIpb2i5XAitOmz2XYJ4TD116IzLnHM71h2O7REBj8jleiO2JnmAkE%2FGm%2B1O%2FXzpDn99eSPgPuW8zawrtkGVhmQtVMf7IWCOdbAH8HGMVWA2TRwYS0uBfcg3t35hDYal%2BHZxWAZnWSRpjvgmLeJXmDxyvpB9v2VtXu&X-Amz-Signature=7b1b1f1535fe77f435e291f10a2697fba8dee104a625a64d148c3a6d35031b46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
