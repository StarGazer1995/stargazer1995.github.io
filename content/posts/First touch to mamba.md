---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXLUS3ML%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T144846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIQCzTW4ocEP377AzmjQPaA90JTSNwb67SbvhX8k7Vfy%2BDgIgGjBaoJ3LMnAOqgowenHION10bUECx0XOL8Sv%2F8P0d10qiAQI5v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI4i61Q2Meoxu36rkSrcA2%2BjnGyagOM%2B6n9rfop5Ll3mgmOiuBsOhmONRaSjbPUezefw7SHl6PRL3tGC2zirWcvd45ggWBvp%2BtHbYI137PLUme%2FEzPgMZnCvmg8P%2FS4FF0RyMN4HFsyBsrLPzrdwlahixrpkfJ0ka03sbB4eElfyMYjh7vBNC3xtJTo2r3ed6gREoIL7bjlVz8TlZsnKVEhgiLgOreAr74%2BLsLIJzYeeTtR7g4Cba2w9lIPqyLY34JP9C4SeVm2x0kRRCGJWH6o1n%2FdDyUBYb%2FU5rDDdrmlP0uC6fsx%2BP%2F6mltvzWlmhpiKOlaDVfn8DGXF9CjWAbrV2ZwsBMaJil8gAI14BZzpnVHqoXIiXruLBqdTaQD%2F1dFanDaZe61ho8Vt9BCCQNrAusnx2RVXGTHDf%2B1d1CP4hzOXPK4jyfx3Ef0GtOXrvEACSNQonrCM9Q6JLtvYRIRLyrQGsoXzsAYnj3HXJ6gfBlLoFhrrQOGu6xSI%2FfjaKx63oXt8BZZygBUioPS75%2FwU7FG%2FurAJ7Mrnl4DEDPBy21SHOTyYYEYij%2BCSiVgTGYqhpsfBkoBqKuIKCMXr%2Bh2ViVw4ceW7fHLp558rX5RGJXYuxIrdzW0wCkKlzaXoSv08MZnHTEFiBArL8MN3CpdEGOqUB6Xg1jc9O%2Bq5uX%2FY5qZ0oB3efPKKAYHmz8tyozvcWxtDMtWDm6unVfyfsQYdk5NzGgpMdkAxcrf5c39HCorSaA0jBT6VTDE8bOh8ND%2Bwg3lMKzKpe2J8%2BjlQDvUqttM47Xg1Qe4MqyShGQl1Ux2XtFA4Kqm6GFiDSP8xq%2FQq08bvLLqDyrjWAcf84VGqQTDbnTM%2FxgJhnMlpPi%2B0jfsH4tlr0edsg&X-Amz-Signature=7835f76fda54b3c56d6389afe86d7052d704a9dc899580c2f6efc67556bf6264&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
