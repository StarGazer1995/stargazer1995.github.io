---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6BSPIMW%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T094818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQDyJ2C%2Bmb%2BPzCoobtcf%2FdOXohUud5CV41%2BO8C6Eq4ldWwIhALVw2kCXl8oYZJRcDwDlurrimHOaD8%2BqIepz1ailavabKv8DCCoQABoMNjM3NDIzMTgzODA1IgxLFYfTPG70Ts8X3EUq3AP%2B6AyQbhbRY%2BTwFPdL%2FFOm2GtTh7%2Bcbx1VGobSIufSbfC3UGdGFY9aIblqIQb8ANymRMsvc49iXQo8IAftN5ebnp6NHhAiHUn3EVMsylnHTKmWyi7jeAMHrKiST7fOuUGt7s9Dx63MitRdrJMWWAgZFYv4JwAJfQqeFok2Pkq4KUjvlfEIMjP9bwNYXftlylTuUAkuKyty%2BfLSO3ELT7NUVI%2BHzPFe52j2EutmHBTN655%2FwRlX09uY1Xd%2Bcv3dT8rwVah%2Bd%2Bld%2B19dhUGk4HOTBjq66DsRUXjhoe4i8W4vpuPcdY2v8PVs7lUmiQKWZVbBqqgUMW2Z7rvlJAb41lCHer%2FI%2BaTywIaot9U7gNPLPvj0YHWFqAhcLx%2BF8X44xlAL%2BValwjD5phuYDgi6PVv3yhsHCgONn0oRzi%2F0gcFz7qXQA4C6O3ZqKMCGfzjmtmrbIDJmDo1X1yXzwBbyPEW%2B0TK7X%2FBcwNM4ZnbvpibchEA%2F1iMJJDHkrhAUbA4Rd%2Bj5MVSh%2FwE0NKC%2FGn9517juY9f9eX2jV0z%2B2AR9khYR0WmwgRuzUdhGUS75wLlPuTha1J4wdeq1p793vtbG%2BP82yhFJpE1yqvgTYT5vpmiaWAwsG9bk5NWYJYWYPDCBld3SBjqkAdcCM2qE9x2zgiv6ohAnzNflb6%2FWtErizb2oXaMguvSkRAkH0UKHfd7LaMnHJv3p0NXcsnAriJ9sncDjF%2BVEJEk9mSrp%2B8ZbaETt00TfTZwllOLf4mpmJGv4YBALs%2B9p2W%2F%2FqB%2BKiYRlA%2BkZxla15ulNepG1r9J3lvOTiNrNSkDzn%2F%2FGb5z9596x46V3EUI%2BQefzysxp02eC%2FWd2wCxEW6mG%2F227&X-Amz-Signature=67ee7a3c5e676ddd760890c5592c93c0bfd668e22029087dce4389c0810174fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
