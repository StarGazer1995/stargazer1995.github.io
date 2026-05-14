---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QERJAECY%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T082603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGd%2F9YnUhhtNUiGRNcvWyrnjQ0khStYWlAL6GSNMDH0cAiEAwkd8fv9Gni1g74ma%2F5HOvFIWDCyqUdjLZhUnLG92qqsq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDBsrkrsq49rfKIEB6ircAz09BwWp%2FNDLYftP0phCOJcXL0Mhflu6H3NvJahr7R3xWzfHTJzeqozu2GNgWIk3vsAF9L00TYJjJ6JUBkNj%2FLGrNEWF61y2AH26wHTGH56TKPLmJ%2BRKBniSG9QlGjBoM3BimEaUohwFxAgHBt0FBx4TDSCz1Erv8uMrVlUg2vIq%2BUTyRPxIzhjCVsaD46A4eZce9e9rEogazEbcnRvsZcJ%2BTAT0UkFhBePRHWilGN2WdUCL0%2Bcim8xh%2FMuXdzLl5evhYmSFOXVyZex5RK2oCe%2F1XwoNQI31%2F5ItAYpp1WtzyNFi%2BHHCBmeTp3hM%2B319VgyUrnA6Pq7m1VyaLvYj4v7NmCcPfTvlubvlYmQPE2lSjSe8itPXKnBiaVD2TFf7Dmm8rit0dUiDBong%2Be4W8b5KccMmh1hkuJxO14%2FLVSRP%2F4S1w6b6vv0aZvHCxfGTxU2%2FBPL5UGCa%2FzeOWCzEDdchA9%2BGflYJ6xinAZiqRvNd5CbDX%2Fha9E751qfSSgF4rUjxnqNHwdaFFtDiFjdcHKQZNk1V%2FhzZesA7OjITXajZOi7%2BYGFUTPqViGUhkHL1dc2GGR0DrXwpYr2Zng6g4qyBsZ3MmW8lSlLL%2BMraXkoG0ZxoSYBWSXih%2BkxYMMDRldAGOqUBAjdVWl0zlHXx8nYD1qC9ZE0OPcK%2BIXxaKLYjbRGIctjYtCB75YxxqRzrV39o91ux44kaMclDM%2Ft5pWP14ILjmZ8oOUpKHDhSvtrT9%2FuaKc%2FSEKj6kWxenyt8d0tKpcv%2FAPY5hMGUdYX61V0xmw99b4QkhNmLz%2FCxyDlDNH3jzhTgdJY6XZJYC3vRiTsp6V%2BOMzTqRWS0oPyJA1knU5ixDLfgA%2FbZ&X-Amz-Signature=4ca1d004ee6a9a52937df8204f2e0872e4a1832bc66a9cac3d1e77aa52618feb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
