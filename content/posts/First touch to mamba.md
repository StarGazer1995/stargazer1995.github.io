---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GJL7H64%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T083710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGtyWVQQOnYlCdt8vH%2BV8c3n0CC5Qxs5oCJf3WwWSFpTAiEAz5VFPWAylaL7v09i4And0Gggk2rXCQCFOl9MyeLSje0q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDMnLd1%2Fw0Kx0lCv0uircAxLLVhDAecyuBaUrerhsZxuubW7g6lNs%2BsGyJiE3NnS4hWcanYDcVtQ0TkvWEX7pG9q%2FYISyMGzhNeBMD%2F2zqm3uG%2BZpqP0v4bZIrTbB7UsSe9dlNPcdgqcGnFn2FO9YDr6rrZ3%2FSxQMrvhlybjGFY2aaOt49G6syX%2FlRK81qYcT9VxZOCWCcu1iM7419jj4eOjHy%2BRpygBtIAL7WoOfzFiQLV6oaZJeHY3N6eUnkt3W0HCYyx5xElsl%2BJm5UozV9a8qPIKqYO6oKm75Lfdvr%2FQQvgOGaxa9swGfkXBFfPygkH3iAma9oDN50H%2BmEtirNN2v5k%2Fv6INEiwp%2F7NrS7Gxm7KhXJDsxNvmK5kcMZMrtaa4Gvq1JsuT7WN%2Ba60rR8od03F6riRaBPUD4Nw5U68kavytgvBZK7MAm6R%2FxE982srZTbsA0jL5zF6SiqiHNNCIqvBfc%2FE%2FZDW18og6h%2FbbwFCOIlkEmEzRW%2B4V4gGPZFWJ9uY%2B5FwAhGoYKEdKEIJASTeND7D10H2MozkWCh2ZcuJD3ivxpxZ9QV%2B4449PWeSEjzToKah88j3U47m%2F4IbfLmJ0XN5f6HPiqAbwNjwby9%2B04vN3Qv0RjeE7CqR3NGrs%2F6rlx%2F0otK4SpMP%2BWm9AGOqUBSFMzOckesFbnJunbMygE%2BwkKgr9lXHI1sogpcwhzd1V9HK4eq%2FQyfEVJ%2FbmL2F5O7AibpPrq6px4cZKnTeYTb2TY9x3vBWOP6mKN1mUMeCDdi%2FdctJf8MMvDhXDJYBJT3yH2aP9ne3Ml10vpPpK9NZSbPvdL1SatOJdee309Z7TXBGJaqys1sxE4vEiIKtIyd%2FVt%2FXNZY8nGGeCLirmN9vuI4PmY&X-Amz-Signature=ab9d727f2e191ce988ea50012ca00cd2bd3ac0c7feef85ad521b64a62095c2c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
