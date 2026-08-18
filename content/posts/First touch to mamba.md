---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG7HBRT4%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T161807Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGfy%2B1S454EPmQW%2Fx0XgwE3ghBL9IalY6BnTA4Vbk4WQIhAO2ot6mlCsaESBOpMITOf0jLAyzRHpW9Ylf%2BfxsQv%2FeEKv8DCGEQABoMNjM3NDIzMTgzODA1Igz57lRhA2HsQlJYdhsq3APP%2BeQ5KaBde%2FnGRT2K5RsVHpdk5s6ijv8E7eB%2FfmQZOcNSM0iaTq9P1Zxvi1xhwxvpAal8YRUrkXHsqp7MLakVdH%2BdCfhqfJbQYlDoqN9EI0wRGsXQw00aFXuT1sASiltEw6Wefv5bDKMlj6ZEaFuKmA4hKnPoMWCDr4MZ9uwdBg9A%2FTrmLoKuw7XVanlkTQl6qq7GWB2JyBonuIph%2FzVgIkX2oTpOTZ2hSDmilEHocOyAY%2F8v4VzqkL71lyTrSHP1rmUt%2FleAgwG4qvnpqxeCpjRIUnx1n2DEuZSg5WWfTD%2F%2BuwMdEFgQEeh1fQJITqvxhy58c2UhMshY7Chbrs6T5%2FMg4NW0huoNvISwpkrOugQ3zdWlOOhp%2BGDaz%2BwvGzzgrZQkdJum76jnhQgf%2BZljUJEtUkh3YdG6zoqNiy8%2BlxorFa2zZ7kys%2Bb8rOiQj13Kh0jqVdcbE2kt0VF%2Bbf6%2FxMjHAkjzCxRjZhODaVbca7RKJOYYynAXyoQOGWR70I1T2d3jwgKSCJtsnog7x9%2BMXoqFv2phbKxwTFVLlxMrkDlsY0%2FtlzPlyVF%2BmrnCDWXMM58G6Y1q0yk5Z8TYA87xZhYZ8cxfSKPH2FYk%2BRW93inB5R92O6dtJofkojCZ%2BZHUBjqkAcoBvjAQXrkFOKWRDTI8GujbXnZSpHTuDnM05dNho0FO2txV0DCdlDxQkd3yC5b8nvxMpm8oKOP%2Bf8RH9PkzAbF5YD3aMcWWxfaoeMXeWDqT9%2BiUMZSd3oaDvxfl%2F4AGkwNLJhbUUKZgH945RWEukcCWV3ZKBn%2Fie7J2fLVqas%2BDhjWJ0W0vjOHbEpVVGgx%2BhEvlMYfP8HVFkAkTR2mPWYRO1Q67&X-Amz-Signature=b01c3c44e7a332e12d0f0923098417bf54732999edebb3dfd286eb6e5840fd9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
