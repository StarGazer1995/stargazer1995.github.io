---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVAKVV75%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T043732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCE5xRsAH8tIXuFNowB1RlgG93IIwXBaN4oWOoX%2F%2FQaVgIgTNBhoEwb8XoZRY452fcn86dVe6zqnLxGasyLEmJnIUMq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDHib8dHshA9b5l7%2FSSrcA%2Fc8KmfKg1gzgbdvvS9YXncP%2BzjSrxEfpW05knNzyxvao2YQBi91hm2NlKrhw9UATreVdLRE3ucdpMKuXXTcD2Lu8B3dn1IqyjSplxHhMP6SxSgLgjvzEFFprE6X1p36eZBk0FWjb0FA7OMndmxYwOI2IdYn1gQTM9Q7aN8zxZSZFBFGlRG89iVJQH8sXR4LyoAAVSQ6FSj%2BGumXtHtBAzHmQ9001RcyOBKfsKDv7c3GdKOtk%2FVgQ1A3MgM8sqK8hYOTAyN7IM%2BkmAOUSht5KyfvTj2md6lKxc20C2BSH04yeRuT97LD3s%2BGuho11VydwJkcSUz0jEGdgmgMnJXEcYAYf6j%2BGMLu0%2BrlR6JVuzK2CpOUyYuYVJfhLS%2FzCd9jIFx9RQJmZSEex5bgqB8HbCh1V0oRnYguu9Ls8Bg6sw197uOS72vss2V9jRNfmNu5R712xDdMpx0go7KWmQ17K1RKtCLz80hPni4wj4oVXTfu20LTmynoiTvYrxsq4UZU7iNpPa4rKJg7xVectjAM04BJ98fGT2CE66aCiSFnAZ6NZzp2AuriC4QHpWoOlfqGyx32BY%2F8%2FrUVA2WpwBQiE5tkjibLp2j85X0FxVPSGWQO4UjStvN44lQlQAMJMJnh69IGOqUBrHKXTrr7k%2FMxa5X6be1LZ3vushoCISE0depg1qhlW43IYWCmpIrc%2BYuL%2B12unx%2BTD4u3hQpCWk1eVHyGIV46%2FDV0ZbjyZF5zhSdLo4I%2BSy8BFRBHrjSrXYeWBBkH%2F6y2%2FonAzOqVJaRoWIOhn4%2Fecnk0oNHE1eyXTnmC3bK9OMx51vqDZslVuNcX%2BkLiRMFk4%2Bs6se5Iw%2Bf6Gnz1Z%2F1nxcvAtpt9&X-Amz-Signature=428ed6eb87d7d8c961f2ba3392e73f21552dd673348ed142dff2c3fd15d8bf29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
