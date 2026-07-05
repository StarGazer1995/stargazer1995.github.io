---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KVOOQ2A%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T083835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIDJUOnwDahJrmzlTIDpi9c8dGjmXIMI6N1UCjikgvkWGAiEA8N%2FbUtDv%2Fn2Oork8M8YgNSbBxvHQHdORstaOcY24TQAq%2FwMIOBAAGgw2Mzc0MjMxODM4MDUiDPUsMNjYTJhRF1ekaircA%2FXb7%2Fu64wBLwbmJd8OawgyOlqs4ggFwB%2FuKtnMxX%2BSea6iPRZLae9v7fVDzrb2LMc2xYvsaoIM0Sp%2Fen%2Fq%2F%2BWcNTL0QuWtR0KGegq8dCwPhbWaoa9KtoSMOv6uTbs%2BFuHxLqJz1tueUr4%2FjkDUbHeTuYBdsxKXJAFxLx%2BHSji4YUk%2BBQ96e3qNK4R14lxkg%2FDjGdMoXc7adyNH%2BqvJ9JlOfUrPIcSUvlNVMOR7j1LO2%2BCvOh25xkYFABHA6F0UB%2FIZ8E8S9YHn629i8JY6Vx12wHCUbKt38eeirua6cNqOxKBp8acmAsBeW1oxpaNJ%2FvHfTsDjQdaUQJLM0LRryhvza%2B0iaW9c8ayUfENfFBka44h2b6w15XCrM2zE2I8nzfvn2ptPNFoyMUKoHMuTVgs1fj%2BiSfiJtprQdxV%2BCeudco3Cnsome5K7oxbuvwIFzzpJZxITcgsXvKj%2Bhglxrsxl90scOFbYXSIsL3ud0ITXXOnTWFOBjtTIlO62wvaTdDu7EtOh0iOQfbvDnNewngRLpCBJLkLhNaSteu%2BJTsxm0pVzYL8zFLLi69N1TsCITWmKfy2pr4JD7T2QtRV0Oko8HIgGbjUODmmAf5X01u%2F06R0t4WkIz7d6s1TvfMMD8p9IGOqUBgP%2FeZLd16jtOskTw1jU6%2Bu0JGHbjPFwYpuZdZaPoft8Bn%2FgTPlCRHEyVIzP8dp6jgEQil%2BA0Abgkn0XcGnCgbVbsTclqfZ3OcuS8g8YNxX5x%2FPT8joklmkbHVXozt06kIAjz7WINarlkijZ4c%2B10LA41f688eKXfVvTLOlDD3SaOnQ1c6Qauheu%2BPcwzewBXWykLCFY0ZUKFgtqxrmv1Tt9v2JCY&X-Amz-Signature=cd31a16a5bf4d79198e7ba4772b67e476a607d0642d8756aca634e45a895cabb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
