---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466276LGMKY%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T062948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDzPO%2BfcBOopX96LBpx5uLhZrdLUquq4Jy4NlJ8VnSygwIgH%2B4OHp8oSumN3%2BMbc5mD0TfEvKrklMMeqoQNcLPkjxoq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDHKV4iN977gutACbFCrcA5HZywP7ZVE%2B%2FDOJWszMhfxaDH%2B%2FaEEF1Wikmb7THkfXXPzEQOfXGUR6kREr8vvP%2Bm6bhmBm%2BAnS%2FlPdMgHKmro%2B7Im%2F4TWJnRye8TBMURCPQFIonS7JdGK2tNPQLD1Oh2iN2iODVbQGaawaDvC5607V5tcoo2Ws7FYUEN1brHqftcQg5rwRsgcQr3u3P1ERTjXyqW3OPDx%2Fw0dfQsQjoUUGTX0cNW1IXZhMe%2F5au72tMadDXsLiUJHyKEEGKrFz3IsMUzCHJpiDdk%2FMTPPtspi4%2FZBOZgwv9U4fI6MbuwLEpifVvVponMt7PYBiW86SJie9ds9Nw4mKLIGHYTgh%2FC%2FsDeqE79xP3whSP6tQiQGQRgg2D1dYJi5J7YtsZfpGJFPMyPpDKun4v5bN%2BiCkdVAFlpBLpEXoS3FYJE%2F%2FPsCYljq8y0iQMU%2BaAkFpmuQHa716jBtOvoSieOegTB9gyQzRNQk2P5jNB8%2FXc9orMZAD%2B2UnmYHvWfdNqk7STuv71gSugcUuqIpQT1pQFvhCdy6uU8zwoYFVihvlWxxN9G4f5HjndO70p%2Blu5gIttGWULGsorzv%2Ba%2FYxJE72qtIEncpvRKdSZ0FqU8Vrmk8n%2By0Ojb74Att5aylWERrKMIbMitQGOqUBKNIiil287CSUynbGYk8XaYPj2Q0irYzszTSer4KOHnpB2Tq0g2pRk36MAXRsMxNlJv%2FVns2cAUSR%2Fqy%2Bnjukd5BqCNyhdK8VDwYGSeJwLp7oINj%2FrayZpJgOVJE8a1mvA6ugFRamHPPNTV%2BJXln%2FFOpPs%2FdyVvyX%2B9GPIkAhmgSf36vN051NT48XYNZOVdhp2Ag30FrWl3TkUiC4T8cvT9PBfF21&X-Amz-Signature=671924e48696a2344f1798d398864d08c061596232131ea9eb2a6efad4e568b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
