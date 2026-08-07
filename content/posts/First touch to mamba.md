---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS4QCTCN%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T042659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDE%2F9%2Bc3cT4%2F5HZNYTJpKi6TbgQzjubujwCg2CHPJzlrAIgPJa%2BB2TklNwN%2F5NOk7jfsQmRx%2BGmUyrrmX6yzu7%2BXCcq%2FwMITBAAGgw2Mzc0MjMxODM4MDUiDLecGiazBgr22a4MVircAydx%2Fesp5PDVeI45NMQupuvJdRZldQlbOXQ0UUJmwcgvJ4ELqihtCZsu%2FYzmvPVIEA5MSNTEglJReLpp2j3CPIR3r3MT%2F%2BN5LNAxt5c3QbbnO%2BdMuFEY2gt9fUrlyLyBPWBzz6JM85UTBpnuSVq79xvIz9fpY6Op5fbhRsD6QEd%2F8ujtqP0OPKXlSVec2XJjHcVvpbiCJAom0XqOm4DSxNBuiynsidwHu1aBiZIFREXhZM3W6u5qem82bZHHirFJMvHa5FiOP9Jbr3GtMkbuOOlC17id%2Bt1%2BlicPzPPF2Cb%2B2KcxxG8djMvTwoPiFfK%2BuZgDZIy%2FbRkYaOaHWIZtqiNEt7xEPKsFWoxNH9Ep7Oa%2FjQ02BZns6ST0fEwiAAuhqMX6GdMDtj%2FWq%2BarZ7%2FWdRCDowdLEuqKIu8spcM3RfUUz9ws1skVSmIyuuSLm5RqHOZ9cW%2FYfyOrUGpPMsU80jVL%2F%2F4dzoEcHTKzZvuUAV%2FXv4AyEJR8zZhf6LFS3RWtjyr3LXM9ZQ7%2BILmfUe0fVS43VDcUJA6pluw47K6CRPK1zVfH3dxUDt8LSNqVjwc1K%2BdzP5jv6Uv89SubZH2PwQCIUUx40v%2FksY4ddjRJHv0de%2F5ewN672q%2Bn4ZRrMLOV1dMGOqUBeHrQOZPyYJh1xS4roxWJ7UquiVC5CxOW1kgUFDItngmYicV7I%2BUiADgisbz%2F1%2BioXcyM21u%2FxddRJ48k6dWi7ojXAqEfgRba2vJVjoQeCenhojSBmID%2BNbmU%2BXC9tJ9qT%2FfAANtYhOS9cxQ3U1IypZEbpc1FuLjqBgIBQJy2ZlhyLGuacnOEPQOa2wbyxjVwe4qdlGVcu6at6eeO7ref2vZ0pg5r&X-Amz-Signature=da53877fdef35cca15ab9bc48b511e3132b1697d51d81d09d1795b25e5360858&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
