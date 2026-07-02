---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TP5M7P2J%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T190705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIDZyyXKXJSq7jogFuZIOmJcug64ZKX6P5ciHzdxI0vmJAiEA1LYhYdnaF%2FsjVr0Ld8Vm4vWkBVzDNzqtGkhsKyNYeSYqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDss%2FkDxZl19Xy3QcSrcA1pp%2Fq1yMJN%2FxJFmOTqxret1AhMw3PvPKX6tThTigZeZu29sXVf6bUhUISGzxPuG3OTUw5TtWPwtYO5%2FObAI%2FuGyJqrLfTkmTMgZjnScLIBsjbuF4q%2B2F9FxPj6JOUM7o2xaseUG3Fr1B0hq2nh5fWVuiAjHrpvJEgmFijEZShos%2FYUv6CCNGXf3g%2BiJYY%2Fp5W%2Bn62ezY2aAieWA%2B9dNVSYK%2BZr5jablS6H3btr5PLGfBQ3jHeg2MUS612%2F6b3SIxD3Df2zuoR3siDuyRl0b%2BOOJBt9bBu0Wl%2FSMDQpvDXVj0aWBqMAE9O30dIeyh8BHBNUIVqPMyafcNgUdd9QZONYSG1gLksjZUNohs%2FQWbzRrKMuAp97UPjQMCDCObLeTVXRpn4%2Bze1wsa8otAre1hrS8psXypaVkNDXKvJ%2BMNI06Trz2E27nl2GBCsMTVC%2FUnqbGc6XvMD2ShixC%2BjeXgSDoe6DP5UJ0AEi2TZlpYN60YK4ocuWl4HvrFXBTstr7fidduJe7xrAI0pFk6VzVnCgkzyagLoJH85VMINTXVtQjfwd5bqImlAwWju1NKzEJptxcvm18rm5L54Db0Iukzdh07pUcXDToNCurRFt2iXLn7Yt6P15V5Xm0DK5GMKbDmtIGOqUBBzHh3ZxqJY8WYh8epL4cxO4UbmHuLJTxU%2B18qR%2FpYPTWMwzVNZqJ%2BeKmhHpsCR0d%2BYUCIs1G%2F4Hxmov0Xc9ddhzLBRxgqOC1pO%2B67pgcm7LX8PDOqUmZ2mFRMwoLNaatjq73Bd7VoDHqE%2FXj5G6rDC7tkxs4kCq2bcTfocB7HK2A2%2B2i6%2Bh8zgC8wNkimbmujxQTVLuXMkzLdYc38%2FzyabCOb3Oe&X-Amz-Signature=d98c23eddf01472808f56e67444ea821ba312317b08858c4469cb80c297c864f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
