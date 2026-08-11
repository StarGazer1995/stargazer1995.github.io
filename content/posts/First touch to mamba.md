---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZKWCZSF%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T064425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC4y4pU%2B1DKGg6bja7%2F4wsOjGmrIrIoelyvrCiLX%2FQ5MAiBDG7U4ZAYivXn1giSmWlVWCCEsEupyRBD%2Fb1a%2BG29ZdiqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPm96AsNRbGSzauH0KtwD7AEs0aK2vUw2zJdsNiItZ3De0xQT0NjXgxivW9NO000%2FNd8bgQA8FFsJ%2BN2yf%2BMcJeZmJIkP3DyPNEZxCCXWYrdI7S2Gx8Vbbwg6zyvjIQwD10sm9%2Fe6zK29nR0BJwmAbddBUecYYt7VVDv%2Bd9nGQdJZYfdu6%2BbQKDvuHJ1adAPcXeR1He56cXEVTUZR1uUJKVEIePs2BjKLtkX%2BTrzMD80UAS20LHjtIL4AaGI7JBa%2BRiVCWeD%2F4Suq0VBFGumynuILzujTyR%2FHcHxigXES3ochly%2Bd1MMFAUnBCnftjL9HXw%2B3%2FJf3%2FOdTMOBrxCB65v78WN8%2FNOt4TANbkrWSiJUsU3S0qxknjrMzPZ1hw%2FuMxFlAfSwo48zyOccPYpNMlcAHeVPyYiYEi%2BmsmZDMS76S%2F9C3oY6FatTKOZJleMZHhU3WCEhbkvOdhCvdWPLCIPQ3NJ1%2B4jGjFrHvxWE3DlfwxqXZjbE%2Fnd8IgrFx2KdI1RfpuxLlqSaP1gR0kUo6uBXA%2FMCjiwXOZgWSznZLBUQS4qFKTvFX0xIIUQmh2sN1kuqRVO%2FzMeHBMOc%2F7qYbm9Y4V3PoOP1Bief0wjikK%2BzjlWUTwbCej1rpVDqo45XkUWYe%2FjfZ4muk9kcwsdDq0wY6pgEevv3eYCIFzvyR2X1VVUrPPjcQQ3FPWYGKeUv1JS07MMDJfIEPa4DpWDfc3dK4OvCptxXvzIXoVDLZknZdX9%2Fis6DeWr348%2FzOVOFmdgHaDYJ3aJd7oPn6VcgjPb59tMp3nTrIHLNvakUTJZ83tQHqqfNbRqT0s5mNefZbV8DSX%2BYYWLdl3cYx3SkYBRQCRhlT9iq5OpUl99mQNwdN2sR1tOAgrku5&X-Amz-Signature=6af54134af07a89300d8178bc0219b14ad799b445e15326d296612bed88f4595&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
