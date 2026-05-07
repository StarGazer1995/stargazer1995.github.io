---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YR2IM6HY%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T113248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDm3ueLszbb8GVTNsBv4Jw2LN3P%2Fr4HeGMa%2Fnw1WSg7OgIgKQqIUH%2Fl4iMPSBhfcfNrIRr2ntP%2BFRAcDV3SEmEND%2BkqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEdPTnInh7MtbPyZzircAxInN86WupySwBxkoPYiSRA1oEVcP26zv6bzJin6ye3l5%2BgnTFuzutaozm6XIX6Y47EsdB0ieP%2BXRqFPSToODp0402FUASZERLNMA%2BV7leJP5rsW7Pkj%2BjAZM6jdsLo5WvZlfHaj7Gn7yQmMWLB8YkMwzaW9fjHTe9wbAE%2F8FkTFG9p6ybMdys6bVixcE9roALmQPGl82pUzcoyW3f1erzKXsQzqUycXhhh1zlmaAavqXApV3LEsacdodSPXlSWAZwO8OKWFFRd0m7FQQOqB9RomR9FGCb0886dWSHNPnKfmUbC8nkmQcIQBFRrbKlZpZmPgbdfxfdSDf44KH%2FvCBpb81bWa8s0y04m0G9fInvHgd4Y89u30t%2BL6DpzW2ZC%2FLEEUwfYA%2FGjAvAWl5bhJY%2BcldcC7UyUeVUMczMZPph4vGgT5b%2FmOH4oSqYTfilrt7x0miPyxtK%2BtMmIMHdqdzStnr%2FFtx0fCeTsk6qRmHPKaXWNosIbylRPelANVOIZLT51QaYvMabXocHUvUBdXEGfbOgKkPgrcCR%2BOj1CepLnn41k1CYgqE5Y4Tgfn8SMEVat3B78CxTfhm6Qv9Z82%2BVcPVP5rdDjnOzey0ecn0TMxg1eyATaZVonj5PpqMLbI8c8GOqUBvi65sCA26S3olCx3Pf4mcQshIexBVT7SvNZ%2FL5US2iXLL2zHywreQlMcwHlY8o9Lii4ETPrtOjjcQr45Gtxi4HkElSmthZZvr82oh8QM6Vfi2taz%2FuuslZjWitIZ548hCI9v02DqWiKawrLk%2FjAj4KBoc58SmCmhwQPfYvRxVo7lxqO140o8VYO5kkVLMxCJbIZ88leMc48NR%2BCu7e62oyNTOzVp&X-Amz-Signature=0bc43e2c9f5bbb7ef5d96cece7dc18a80bd958c42de7183d1a6544516a2099b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
