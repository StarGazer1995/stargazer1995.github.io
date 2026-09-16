---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGLAEDQ3%2F20260916%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260916T191051Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJGMEQCIGDC4qtbAF2Nu20Ta6jp96QFH3GlAp52Cd4ztee42ztnAiAEFAAK3fCYBbkC69Df29hk2QooguVSd0VlhjpRHLilICr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMWKirgazFk9kfvgTgKtwDFUL9%2BxiwvCEBijcugepXevuE41ptRGHzh07qPsFVwxsyGZMKjzvNFp1q1n8m4JNrgQ%2FnF9jCaLzPrbFz8Mzwkd6OFG1MkUbMSrUnARrj4j5MLSLT2ZqP9i8pStWuUoq8aOnrv4%2Bui71cHSlti1O97aKFwJp4Brbpj9tLTXKSlnUVqJrRPfwoVhb47s1v30BefhP9cY8Z2XijfT35pUE14H6G9oWEVctfnHU0v21nr97X96RxPOnKIvLuQG3NAunRsBNA%2FJGrna2qmAZ15D4k4Lu3I7lTDkyNFIPu58BeIx8sUozZAaabcj9btD3jW2fpb9eTcmYoR%2FrL9so8p40hNNK%2FDwa%2BKe9pw2Fsne6392SgStoQeAB3Z0yy07rbn09wQ1UsTRXq%2FyT%2BEc6h72NtW3%2BoescGskldrQ%2FSri7Xy2e0h0L82hU4C47S2QCH9RD7Xp8hOPQkEIBtTwSZjRIZ9v%2FAPasrkq%2Bx633ufLeAcc3NsfBqkV17FBLDlmexnbI5dxZiM3MOtt0ipKvkgiPLUlyT6UOUOc7JMo0KlkR0fAem5WU92W%2FEEg5CWIFm2x2mLqPVmuCB%2FCCMhvkJgq2Zw%2FmvsnUt8Aexurp%2FO0Cac1dru8qYkutdINHIOUMwkZ6r1QY6pgFf%2BnZvCUcNaNax%2FyA4uzu0Jnq352lmFhfk%2BqR%2FS57O%2Bu1KObitC7QuXimO4%2FFsh7gWRpElx14FlG2%2FM2G33OvGJSMMUYwiLUlyz9m1BgZljDy3ldWC53fxBg3Nd80LtTRB1L5pzrOEU%2BB%2Bkzf1z8WG%2Fg5%2B%2Bg7nxmXucJKigTN4ZYLXqDj5YG58%2BmMyofw%2BUqXSYj%2FlG%2Fzv89ljxFcpsgS9J7O0Fald&X-Amz-Signature=fd61f0514b10d4765980d8411d156185da7e4321b7e786207968a80be1efb2f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
