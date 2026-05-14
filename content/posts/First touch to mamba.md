---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDY4TNFP%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T224837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWE7%2Fd45bZrFARAExK%2B6n2PYSTIT2hY4fpU8MWw879DgIhAJK%2BEdTCaLyu%2B9792a8L%2FMHQgfQABgOdeVN05xdpvLmgKv8DCGYQABoMNjM3NDIzMTgzODA1Igw6JAF5RirAqAwktnIq3AMz5K2zmXVS6XBniEEzvAUDPzBhUXIcm%2FUbDggqW7fMly3XTkVZrpfS5mUokloR1a6vedJwN29e3G5%2FasK2xmkgXHoamCJtuK%2FJyQwp4VWW9PzViHYN9o841smTr5CX%2B9T%2BbcdvwE%2Bt86z%2BdkXL4kkNwMFlYIG9R2D1LkM4jvJfiY1HKeH%2Frqrr6xOzHtU5n4s2lmZ4SlSg2Nxf62nTFS3vCaqhfHYbWmT3g4UqEVwVDI%2BHP4Ns2TvFzsjM2oAsPuWfrUY2LaMoZVZFQO3Ao%2B%2Bz0x%2BobOPgkRPP8Sf01eiWVGYcFbz%2BTRrfg8d4bXCLUxEs31jnCcYJRViNlu0GJM2xGL%2FVprKfncuWMaABP0vR6t%2BxceqqNSGkPVdxdGAvAPfsgB8owkgqfgvX9nDDi%2BbuuvI1fzzjH508YSXhL8WxEi1jkxADXgqUQ%2FxQC%2BZc4eirItzqFfRCfJQJNQ1xcZ0%2BGGB%2B3gEh8qnllwdyl2w4tUk%2BvqyR%2FW71D%2Bd7JkqVBlwWPbw7lxmjsO20fnXzbbl9fnmw%2FMFH4gyBbf8M10NIcvIl%2BDBXGfCM0Xg3UchtItR3%2Bz4bvC0ukzY%2FMW9zvs5yeR51Dr9Ws1OvL%2FdonctXPQhz5Ud9lMqBbJfGJzDn7pjQBjqkAVNmrqMbNUgF0kmZw8gtpd%2BNqH7ZFyquqham5aJQ8riXYMNkrP1AqwspV0zRDoEwnc%2BKydM4sDJsQ7yxLShhI%2Bdkxz7xtjPtOGnqUPIL5FUFvg4zrVokpMgDW39h%2BjY5gg5A5cQBKirD3z%2FX%2BWrgeSHGbc4GJ5WB5NOHrxwvp88STmFPdFOL1lSDzFTs6NaQjoTHDysuRKVodsKTz67%2BnlFchY8H&X-Amz-Signature=9bbe8c67cd9c294698da803396d21ce9d85cac18cb4a4ac7f07c497155555ac7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
