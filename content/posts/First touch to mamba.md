---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFL2BRAJ%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T223632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQCE0lV3lS5TqqP5mcrsYqLBLIRkFsY3iA%2B%2FmPoP2XeFogIgNHQKGn4uZUv3blODRA3d2ssJfvSFAmFZ31B6NS21mZ0q%2FwMIBxAAGgw2Mzc0MjMxODM4MDUiDAqwLlghoCbM1IeRQSrcA5jFEO1HwOoRbCDlmLotic%2Brnd02z%2F7Zf2mHgt3EQguYmqbUqS4ypT2mWfTlm2YjTUAHY1HV%2FX%2FNs6KnEnYfyip1cVGpL%2BcAt4%2Fi2DbZ9Ib%2FaWX2g5z%2F%2Baol1xBo%2FvlfGGlIDvlI3U5vvYudX9%2BMk%2F54OGGlC0pOxCuZBy7Cc1FRzKNGg804SB5%2BdgSQh96FydOS%2Fkj6NsLLGA6GT7BgYhYwCP%2FMkkg6irkk8DJCLcPWKWO9QTaCNJQ%2F6y0fljJi30U2EpO49gbyQdJ50%2BvOtKlebg9l%2BUuRTZAz2debBbhzrkKoX7Nl%2FejyVTwMhk4Q0LbFXAovFyp%2BCAyMxRO6bOCUxEC%2Bw284P9h%2FcW53NdNniBPE%2FwzIK6e4W8dVXMhdAS1V2pHErUDekH4%2BazWE6pZmUE9R81nEjVD3m4iQAbR0xBeQdX1dfgTsv9vktFxLH4FpVQdt0TW%2B93l%2B93ZTmaVxloDDG7YNz34Qk0JkElk5iqtZQYNpd0w%2FeSFUiD0l4rsD3qs4UbFHGxpLwTIodeJ7Clvn0hO5e9KiW5lFbwHWdGTdYWOVEF%2BuS4ZB6chLqdpvMDVKnahgyoPlXAFBy6k3PDQA13TrpUX5kIgqhYgZGR%2FHavDSJTKfcSeWMMr0g9AGOqUBSYoo%2FfUtbcxVCO57a%2BGt4PfpERXD2twggtHhlaSWgIfFHjtLYuwaPjXbGvUzD2wufpOolDBr2ikqLWjlIvtkcy0w86iw938qtHwu9kQnvK9MGCQkImZJdekBwOEb%2BYqHBkV866oDSMtBIL6CAziQfmh10zwmqlq9a%2FCBwzKQr23zgfTO2TxIZl98DwnS7LBFuufKbhyQz2Py11KIwrGSXZiex14H&X-Amz-Signature=ed6c1b42a35934ba2370f96b5ed69a6c5712fa33e5a1c40702197953e81cb677&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
