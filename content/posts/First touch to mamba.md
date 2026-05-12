---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SX2ZUFPJ%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T161237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIDQH%2FQ%2Fi%2B8X31zDMGsMMZBXh36oqoUzsPxKbodqt0ua0AiAs0rT3WmtB7BOWhdhouCagwKxJ1xBQXxK5b7TZoncnhCr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMqGTtyax3Af4Fc%2BP8KtwD2EpxlKzsZlCe2BRX7Oq8QO8lMI5heO0dHF1j2jwBLEzDsbb0cGOw3yznzTj%2Fqa4ELrrzlJKQGFdYD3sUtzkSg9MvR%2FEfNgQB%2Bfkf02Gvxhqbz1Gk5jgK9mc7xkmtNoWvlkPuQpk71ILZlDzepX4epUyNFOYmOHnTWPL6bunxFiBoaWDJc8uuEr4tAHaljo0J%2FwIi%2F24LKnIE2Wm5%2B0Jksb1nv%2BslSeGxg22Ti3jBxkXWwWvXZEUwN7zmOU3DiImyDvfQZd8tuR%2BGIxf0LY1eaomt5NjT%2BF2DAOTSy52lI18tI4m3ErRu5pJG7gaN%2BIIne%2BmdT77tLHzr0vje8RFPi8ikiv5oGAw%2B3ZdR3Qh7VjkvPAefkA438233RKbJerF6ww90z3Vvq88I5%2FxrhfzlVBH0%2FHbyy51XN9mw1%2FnDQvKvx%2BBg6S3U46RGKtj0llz8ikl4sOQtRaYwinjcIEsBkBcrm9axLtRwM7aZL87ylgQ7TzK1LrXItTmgwXeUErko%2B3lr3caRBh7KjewmiaK68Sy5yFn%2F9r9%2FhsB9TmFx1mu%2FZPkttjeBoyZnudHve2BHWnJsh%2BSP0d8i%2Fg%2BttsIhkHQAeU5zqRXe4s7YkjZiUoeQ5eMAOOTFRGzxqe4wy5yN0AY6pgEkCLzQ%2Bvpv%2BVrV%2FDnMxx03DrwR3jmua0Ay9tpXJtWFAPJez6CiG2qsfwWs9ol2RaCT96DQseaBGeLSvHxAvXCMCnDIlRdyRTdjNrMKb6TXU1BMkPKgUTwZCtVT7D8QLj89uBqotxjZm1e2dKc8Vb8qtDchKYPq%2FS81RHD95eDDEFJWd8B0QZXNQay0eSJeDdADDCJF%2BkXqRNFZntSiR85WRpUBJTMD&X-Amz-Signature=e74e6052f38850156525d501be5d5929441f17880d756214fc0bf61172cbe61d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
