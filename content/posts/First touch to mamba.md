---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2O64N2Y%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T015038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7tW%2BFgKNCNIHh6GVocPsstA35n%2BNy4jKTi12vv9RDoAIgSFACYJxQ%2BSI9dJcfWc4%2Fr2ZEXYwZiFrjUKqrT4dc3bYqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAEC7mBSCbQVhT4fGyrcA9Z276n4kNQUQ2rqLfGosFHMbb0PgUWxk%2FJGhVj86H%2F8bZZT3k%2BousFUT9Pk3xIIonFGtu67r3iCjHwm%2F5o9NWGYr4BZyIqTXBC7YeeH%2F5VgqaMp2R%2F%2BKSnb1wAPzqqzggqcOGwwEGWm3%2FVB6bAAQLDpIzoFqn2X3gzaxlrGzOmH5sxQbG0W5UiKSe1UQN15HjUwcndbNNfu9BhEr8OEMX49cHD1l1p%2B8TKg6RFP7GhgFa2Ti15TsvOQqI3y%2B14gzhc4BdZwHk8wTjD0qqT6NETDWirNFkGCz0w442LUmMNNPhsIUsuaJRzlIujygp7toPzTXDpQ8e04apX65ntcGkk6uPWFlifu8ATEBky1MJhSx12et9bIgLSPIpiXEcInvwP%2FAeE6gf%2FDfvAKINHub3e75jckDCr2uzYujhay16jfUUNDKJ%2FDwBU6q6MBA28w43B2fJrpVVcF31hnq6QIn7ive5fcJ1MY%2FHOoh%2FyOaJFYPxDKpqt0C2Sw71EAAUO%2BEH%2BQUm45nccaVX4S3gIDsjCuKE55WMvB0M2O5wfOtcqr1JMCqMlTU9gEMQbQqyabJND4%2FYJkpRfSJH%2BQ1CWSEOEEGYBPBcARQ9ggNataSKdS%2B02n4YJ9o8dxplhQMPjk3dAGOqUB75zLBtPpz9zqQa78DGHQS%2FDCuxaxfcJQQ8pYtyRrBQCeDu%2BwMAOzJqJ8REa%2B1khprDGeGFIZWustWhd5ygar7YoFWwvZndD%2Bv6YDteoGhL1MzV8WPLGThmTNATZ%2BK0Fyn1x9MbAE7nVq%2BzJ7Ad1rI256mJ1U47GiISkEL0gdmKB%2FCQkR1%2FfqyKNaN8cOnPMRno5I%2FlM%2FkiTjQko9gbF05676rgf9&X-Amz-Signature=a9b42754538fc2944102d2f3fbae17f784999b6997ddcf836fedb591a0ecee9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
