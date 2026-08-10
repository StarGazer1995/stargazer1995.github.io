---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DQBFSS7%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T034304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCS5WdSZcgKPEUmVh0uAMaYK093vtrNQ8lPgE0SgRtjFgIhAPrSiAAsn3sR4jnFu6FL3BnDmsJJPkeiIJvlTPIV9XOdKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcrQJ8eGMiom37f%2BQq3APcXmB2imE2kNYE43VIjuaxSF5tia7EO4gspQhqhq9yw5DeGJkdzvAp%2B0K7OU0J5pbUig3MyubKy9pm%2BiCwDnn2vlVBNNviUBxcS4IgvJlwo23Y5uC%2BukaRgGGknE%2BR96MRBis9rkq00PC%2FH%2FJeJID6%2B9M9odi9WnA1f3x6yWWxfEzxsMyejqCSu4SGxKKCY1COSk6lvEaeBlPxgLo3VD8ryopUTf%2B3V%2FEBaMWFqdB0OWO9USWyWP02QIFUoGR32frHZl%2FK4Ge%2BFlJh0gcuAxElj85XXEpbweKve2mVY%2BJAoyAMViYhJ4pbq2h%2FMa5L0ujdzf9dPPJzDYzE8aG2oyQTwxypySCwCpfDcR2WWiH%2BduWU6ubv3WlL9lDikL%2BtU4dolJJeFPGIiPZEOYMzxa1U8jf8kWfw6gsicANjfHuyAfABPO2BSLNbxLmj2Fipfphq0UZkQfQ2a1oRLANUogxJ8VxS2DfaWXxsG8a6Cki8oDifZVGncBskg%2FGwwRL%2Fu0wNidh7tluJXGrfFar5v%2BIOR9ChnBPQxRuOzp3PLclxyxJw%2BP7gWpG%2Fquzsn8cDX4h0edcy31itmJlf8CtKu4BeGQa63whiZw10xHeXkuAIynX0w%2Ba%2FgFew1BFvDzDu4%2BTTBjqkAbxVvLaeKIs2kKgUzWq1AZ5HzJDTaf8%2Fzv3eYXdnNKAj9RRJwiHr7RytLNR0%2Bqh5mGcbk5vanaKsQVWcyEkAmWqzAUOf%2BaZOy7OqWDkAeBsR4Mc162zyEyx2f%2FhRlHy0DPdMAfnNikCXV%2BE36dfYDFjzWr3dYOXELdnpMI%2BM%2BxTWNRmWedLdesynYTTmvx1DAiPXur2RK5pW49%2F9HbasXW5bLkXH&X-Amz-Signature=de8cd62a5875fcd71142b425523edf3747f1365181c80eac15b511d3dbc6375d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
