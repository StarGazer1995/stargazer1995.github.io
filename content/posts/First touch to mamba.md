---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CMOIWDR%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T102009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAN8EGEnnvqQAlJfj4RQB%2BxqyZB3WKl%2BbQLcY%2B18S346AiBzGhSKQqAXbE1dkxO2S0JEMeTylb9WH1d2fIE%2BRgljLCqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf2i3hMseBb%2FCcClWKtwDW%2BIXNGAmOG%2FxK154NYsDYitnjghdVgWKmWa2bMkvIlZuqt5RQ8GTG0%2FLapXPT0CcgszLogP%2BfGcEnS%2FWoMkfbob8nHURyATPdGthM60mZroopBjifFddW4q3DFxHPJcZWG%2FdNUw%2Fj8TGM5EJgbghmwB8lvPiSsGIMnFa3m%2Fo2pv8Y%2BEfQ01F45uaPu%2BjyiqAxi9hUQF7wbkCZWz1A4ZqclzVcadQgQ2Gp3wM7YV3WLkQP2BJOzQxTn%2BTcdtr5ZXcd%2FbZ%2Fm1aLlYYrJFPeSu%2BHu8cynxUg%2BqAodK%2BlFmJEOkIxyMSp%2F7vVWNGLOGhj1DoyTnB4cO0i0nqRETF9%2Fj9MSNdy2%2FO2H4bMdAu8FtVIIFK8%2FYeiybW4i%2FP9zkj5oa8Jf%2FY%2FJdb6GSJciJIol9%2FyLK403NF6rzOTG6FPQLBSW4nfySlk4HnZnj26dBMPAUeJsBywVLQytXFSTISo1YOI5ECV0ulo1kAjGriHRw%2BqUPmgKzqqtfrwNpOxc2QU5hvc3%2BmPNI6%2BKN5hGhFx%2BIeRxT7eTdhoO5PWcO3pxr2HOgE%2BcofA%2Fa8O%2FkrFaSZtgNGme4n%2F3OPlxkU0MIaVkbt%2FhCgiHHHlh8n%2B960RIsgDEHmpzJkUm%2F2WetRp3Qw8tCD0gY6pgFks12%2BFFiaAdglal9ymVEKQMIDgP6jTmKt7URnIvR0ZM13TUGqLthlBxmINIythuznO5vUcE9Lnsu7Zi00ykfHVU%2Bzc9r7wd5SfrK%2FMGfhVf1APoO701kUUOs4REO4ymJfPiqFA%2BwaGlvB%2BoHctMUfB3hnJc5jyEC7qEjBgCWWbTYJwP%2BTrUCre%2B9wYLovKPgkPkZuHAMxYhOCHkWSgcqTR%2F%2BkfV1n&X-Amz-Signature=b246129f665ed1a9b1e251fb36cb398fc45e34862e6deff90de046679876d9ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
