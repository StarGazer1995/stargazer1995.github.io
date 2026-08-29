---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3H5ZHNY%2F20260829%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260829T220603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF14rfFEDdOJ%2Fpl%2FU2HwyjSVuC5QXJgxdXxlUL8c2snNAiEAoGlsUKUGmpxRLWqZkNaCATSX%2BDoK1XapB8KiUnYyQJkq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDLKw1RFC1xKQLw7DLyrcAyKCmrEnAvhWxkGvqoz13y8vnfoBx3Yg3nuXuYuMn5xw9t2pnFrZYzo7dNYMSboa%2BOLGrvk46CzMJw%2BWoh1%2FZB1YpscWbS1kSqwwVAyC8%2B9iRObV3qsi8HTCjalNZCUbnb8M36Dbw%2FwmeFjFtyScXOimdPG5T9B3O1VPedGNeSiAURb5o8DCG4hYuJMnQ6zjqravix6%2FEuBW8PiLDtlor841LHd7C9PujhBbL52QYByba2lBw6sBcA2j29NG6NAdBlrFuIsOgSqtsJZlHlk9twQ9vYG2zuM7CGZbd%2BLT%2BBg8EzfD6kCRlai1bsI6wpidnDtNgJV6v%2FrlEOMoe8K2p8gM7Fo8TihSeABdj1qWaxWehqhbfy8Dr12fzK7Opw3PbyLFu4oQqxGaFajggxsbRdWv1arCo8gQNmeJtYvPfo6ECYBQh%2BxWPyKJvuI%2FOEPMuofplyXPxfCwQoMaa%2FjF1csY5vBB%2FsSCvxFavqfl35V7DKjF5KwZ53pKzGOXxefqt0QYBTuxicJIGwLm3E7Hex3zYRY66KxSpbKBK2S935bUx%2FF%2FkZKcLD%2BJZBOJQiNix56g5l4liFGToxYdt%2BZXEaFZPKl31QT%2FsubypElEaUpWnCacinPxmPwa6cUPMOD7zNQGOqUBny4p5Jc4TmTZS7V77FitVO0EZpLwnUE6%2FF7sRn8Bn9e95CfUOKfkpfJKeV5IQxyJ%2BK5dRM3in9xchp14MG8E%2Bb%2FDmjKLyND029eA0e%2BTYLPCbqqnnhK7ctNQ0jGCH%2Bho68ZSeVySpq3EKpwY%2FpBkUDpy9hLoCRPpM0YUMeOFAFBG05XjnlGzeI1BwPvcuasmmQgk5yDcJ%2FMdnFj6eC88tqI4eSDQ&X-Amz-Signature=a010fc069581f25bf8b4e1c1faf121e1c93bd46aee0eaa959c8962e59c0fe72c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
