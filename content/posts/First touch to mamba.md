---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HNUMNHR%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T225158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCa3vWxf4UKAIUXcGkNSJ9TIh07f26O4GzD%2FUgwrC%2BuNwIgIizErkvaqb%2FOqL1QAcRW1DaGOkRcm%2Fzql51QLsLia7IqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDANH1tcCDEXZf2FdLircAxrBaj2GitZlIsTCgxARU25Bdeg5YxgGnhs6gqaw6u8RzJs%2BdeGj%2FaQMVV0wnQ%2FyQmMySPNyvgUQq0TEPrzAT12zWuQi9J0xqPqGXG0%2FVaxC0oPUu0ru0j8bHwf0jFsr6gNm3sCBeRO5FbegZbFp1CWGo9Q%2BDJ5VopSjILnsQRFXeFKIxVusTYHWSjIXsdjcDWqKQIaNtv2YT%2BcvV6XBQ%2FFbXCx8aGBPGoavKDGUwQ4T%2BFopWg3V5QgPfk1A%2FTPuc5wf66YDLQSMZ%2BjIUO9VtlKpfUEvvzaWMwYnSD%2FeThZ5efxlIhXayRTrX1JdHWQL4KkeV5V76GX4FAqCFwyP4GrtVZvayyIKBxTqbcQAgPzBjvqVoA%2FTstM%2BbzbvJkBOrsNaHp2DQd9%2FLUDEDaHQWQHH8jSKL7g%2Fy33GqRkfoe0viV10xA5kUnRV8hyfS0EIRjP0dHJEe0O5R2%2BcVJmurqScL3WlaiMmR6CQnh6F4lY5TKJcjjbXcmEPWll8qw2PJMetpJ8p3Rwwykld6U24RbhiLLsQ1et5OdKDucNj%2F7aYvSPsm%2BEo8CG77VlxYYRJiTz0pukLtZn6lO9BB2dzLNXv%2FNFqhjhTyTytjR3lPjJv4aCgRfTL24itt%2BN%2FMJy%2FhNMGOqUBnHoypYS0QaGRAOFPvGhn4yYFUgaJEONPG0Ato%2B%2Fm0yv7FlIi0IXstKQ4p0ueGxZCrDALmpY3tRPOjZP%2FzuiEewVAxF4J0DbuZkv13yKqeMfaPiDDiSTfWds%2B5TrD81UrkE1sJoDSihzUQEWbXGHrXIN94qbI7cazDV7HPNVsIHjYvrrA877F6mWyVJxGkiUtreiCic3QFs4vXU9aLMuZ46v1KMml&X-Amz-Signature=54ba8dcf86efde4874e4d37ec50bbffd29edff13c4eae6657c57f6f7d8727825&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
