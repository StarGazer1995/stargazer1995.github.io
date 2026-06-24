---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP5HOSGJ%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T104000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIQCFxBGsgGAknxe3beO%2BaqLHlFkFZdiS1ryb5tafL7%2FTyAIgUB50YueLWLfLiEPFED6Altl53P64Lv%2BEeYfJow4lh%2FAq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDLzzvadkXklJBQenjSrcA6dKQvQgCpRUewPn6ivAd1aIbO3lCizD6BxdULlWMAKFSSeqL6aOhxUzmMOdwDNLduw5%2FPJG2KGU8zxCyQ0aRRmf4Lhuwx5oBYY5SGOkWhMMRPng5Z7UeEawAvQrp5dQT9gy%2BOZD%2F%2BleVhIYtgbkji8rbO6WacCJgpT0fDC4I9lqywLdRG3rCffTI%2FKSLaVYDPF21k%2FCFuCsihERRCIA9n2C5BPFwEceZAeSwT1ebzO8UgAYzeeTrUWnAx%2FTPPx5IiE7yD3wo6b386f3ZTpYS4rBjbTrkdD89A3FGxH8YQp4TZM6pJ5nXLvFSRonZ7Lm0ZkxG4iG8AnTDPlOPw10HPstC4NrTsFir82%2Bcw0%2FN99BajW33X5VTcq1usE22TQ9cUPBAWuKw11IPkxQQrmSr52PCxqQnwXlwdyKY33bWyTSQ1OPgrNtdO6Z3I03QM8SzeSRd3Ixm4A8UVpSbpdYYwuv91LGzMSLQe3hwAD1pkyMYzPsADUwsQCzKWFoJedGQGtSVTo3S2LE%2FohhuBVXO%2Fvp1MfOQ2jiQxCJv2ByiTPdLz1DdOzQ2EorPcUmS0Y9BUVrLQNPdIuEETpXDiibA1GJ0mIIlX28l9zLg4XLZq9QOgzu8FoyiZRBVLkMMOvB7tEGOqUBIK%2FCWc0RsWeYEV4QfxbBCdhJj3YK8mZLxH5hSjqb3DKs1FKg%2BUH12DEky6l1o37D7wgGwPyaMZi2q30wkHAAPnLcga5Dk%2BhBXEMZZcyXa%2BZgBnKiHuY5jHWaPvRbC23MZF1oY%2FKAHWWeJCjKT1lXdoM4mTREb73I1aAPaMARSLhoF4xAj9S6RDKmmJD56L6Co5BR%2FNghZqUGwV%2B4gfvoLA%2BDBO9s&X-Amz-Signature=8bbf7b7e897bf7f854a49983818e57307bd6d79d4df4a9e23cb9b03025a9dab0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
