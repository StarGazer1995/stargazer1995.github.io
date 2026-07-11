---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLNFSXXV%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T105313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQD%2F%2B9Wh7yB%2F96UqorV%2Bz%2FR1R4E1TvDpMm8RRJlUScRYmQIhAJaNpTBo8FNd3HGSkWif6oGLzIiEM%2FmUAPVCELrpTgRGKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztZSx%2BHxTp0xzcKNAq3ANxwMX1w47ZULLhYS9IIIR04I0k7mgzg59tKwf3ELoHJZi60lnMuvPl%2Bzaxw07Ndalm%2BHEQ6oUidUe3Ux7od6Vf%2B%2Fog6w7Qj1%2BPhzTBHTfhjRlgcUUKabqeKEwUgv3Xf6273Nd9znpVntfeYubsi1djCDwqgv3LxXGBtOnfqc%2Bnv3iW4C6dQjyP8HvIKu9lbjtfqPbStiRMe7jAVLfU%2F2QDYNf2Rv2rGswlN3UQehZf3gydVZbRkZCTYsxc0smKwATn%2F40PitLIg923rAzsKz7M9hPLgjX%2BOO80n283olypVPLn0hT%2FzC3ZpkcipoITTjH0bySw0LKB4txdAw615UDjuFGuEjgf9YbV5J017U2M%2BWQKrJF5QS7IKJowqsEKe0lrmxPL6VRYjIPomrXCN7vShHuUr5RBYJvuY65oeuiuetJ8r2KVrUXlpC6zoTxWYJ0N4Az5JkXtNaGJyP1bTmL8mwLe1ZH0dbQa7uXP4n1u2MPPF30x1JsyfgZGplhB6xaGOvCrM4qG98cvSVFM0GmM%2BP6lvXmyWWYB0ZYmNgyIXduEvRxExCeWoVTRjfyJZfzhG1FaxCeQuEcgtJsyyJupMC4uqAFjJpmkQHcnnJG%2Bn62DA9r%2BxMzLGyiWhDDGocjSBjqkAcdexCeLKytKEmaimmWW2BJ%2F0nS81YbT83daAnE%2Feyzl7uEEWBGG4Lbm9PprU1Z7N%2B4lqBLHRbV1irBMid1mZxoywIgCYwT5Qi%2FUQwynxh7V7vaNFO0wMWnTBFr6YqstRyARHLSiSxKSG17HTCd%2Bv1wTAMCZqQn79Vz3WDxrScKns5W%2FapmL1OeTs7n9vzDInDOu4PQMbpZfQV83N1DKzpOOeAiN&X-Amz-Signature=cd8b18e397129d80039317fa13459418afd54f93da93f98c8969dea7d5db7f73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
