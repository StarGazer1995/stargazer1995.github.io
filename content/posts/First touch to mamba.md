---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPS4SVEC%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T090437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQCAc7WRpnC1XO9VR%2BUPFaWN5fZx%2Fyx7Jc8cfuQgJTdgvQIhAJBQlKrdW%2BbzJjufaWpv%2BjRSOsV%2FsdtFr6iHaFTQMWQnKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzaPwNOg%2F%2B7d3vNyuUq3AMLcNBmA%2FgsbdR4645zJSVryqOiU6wDLTBoiff0addMTKzwYaCAz%2Flm4NMzTnMXnu7zOYZpc730L31yqxWuEJsTxxl2Sbgs%2FlXQjfGR8FfmqaPqqQKrln%2FL1kiw0KD6d2%2B%2BJH8ckmCl4YvFxU7JzoIXRsRN4dDS%2Bxw%2Btryy7AlLWNTtSiVQMzDsAUzOxuvbWAu6Ox0KIR%2BgmwXoySkTor2Hd9fLPLbVSQHVekKNTAU%2B26YO%2FJQBzL0DEiU6zgKdwCWSHAAVB9tmU5744%2FedbQSSLgBEp1Jv%2BRvqM9rgMWgtod11dapbkNw7TKSRKtU1QklLZ880IY%2BHvjR0vNDmrelKlOkybPpCWcOCQZmZx%2BhGm2%2BN%2FELuYdEWtSMDTtAl%2Bl8MNvFMSrgrygywWB2G%2B81CUrm2Ma8UnMMxPP7IH6Z5HJ8k8bDVDB65m84YMtr5Rw4GLCto%2BpjIWg%2FBOz5UW8Jhs7wtwMuAsmIdTIRo81KGf%2Bvqf4wHBXPGdD%2FHU%2FNOzVeWAkiOtYtkg6TlRdM94mRnpmrE0qBuCJcmQkOXrYzlSNR7mKuEmniWYqMGrH%2FCNgLXByG%2BjQSLuNJS02DIYE1JZSyDIGoKQvYNsK6%2F4l%2FToJ9lMGIWdHx%2FooZ%2BOzDLyfbPBjqkAc706UsH6KyKfvoqXU4c8vfj4vnGZZmG%2F5i7s87ppGcfxb7t2nmsA1M2RHsF394geql1uZBx6F1XmnRUJ5snY72BcWOw%2F%2FXRXzjLGZoQyUBoTV5Lvc3eIXOsWaexTp8S8jK9t%2FC6WduojSK5PoxlROaIBE%2B4tUwa1EWV8tazTidXEH1HDuAS6Ck908jN0Hdla2c0Fetn0BKNqfr5eFbblEmYRKnE&X-Amz-Signature=dcab98f5413d49fb6435f1673bebfb0946a6ccef62c529c64b6232399ee0c510&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
