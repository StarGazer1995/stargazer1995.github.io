---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HOWUN2S%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T223602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIEKSA02hix%2FG2ElHRHhs%2BIyGShPsETpwv6r9HRUyXellAiEAq0jXLHTaj4Gc9bpq%2FNQYi5vsAHjFliW7M3TGkc0j44YqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0GZ3K3xYdHW88%2B3yrcA5sd5p%2FXaoCSjz9UaWVgE5M6pnqejguOa2TtgeTNIe2aXxBH9YzidG1yLp5UIrPfr%2BqHwVBCuraLxBUYbWMPLZw2b%2B1MMxiZgNq3zTx1AXboWnwGuUWqm6GMQfhrd%2FbjR8JLDizJ5DeBMSA4iDoPK2h6ms1SR5qO0Im3V3wgIwfbu82XEtgOUqGwImVPmWvZTazFqHo9PEMIFs%2F9F8FrxlxVvlsVCLTTuPTqKCQNtD0EhpJJNRr8ifTNW9TZlw0z%2FKZ%2BeM03ZjaEcWrvuqWkWVgjGs3MU9v33QaBFkk%2FVR8UOzlaB62iniNgZhdO9%2FQTqD6LZ9qyDlo356tP%2F70GN%2BzrOLfciKnxuNot3z0ekGWlZcvurZk42DmR1s2zo85KPSPMlRWJwsVKjn6RHbCRKg3AW1MVvhasBCSH0nYHkiXsgqBYJ%2B7sJclUH21heSnjsnSXP66xvObZrtpWolhta75SIT9eknmtgUZwVmYk%2FEtd5H4z3ztgf4Ioa%2F5%2FmZ019alViscDCI6zqdM9HL63oWCnRofBDoNZ4VU6OoU3GXimqoAzuA85P6j80z0ruBpMWPU13azkZ%2FUxHTc8MS1aVi%2F69N2SkEdlcPezv7ItGiVWgFWi6CwS3fZHsNHHMNnqytIGOqUBNsgni1EsC384q35Z8HhUfbx3PTwhKngt9LouC07cRlvua2kQQgQH7%2BCVmKsQZSfxj%2Fl86knt%2FMy9iqIZav0IM%2BXfNKRthBJtNXtMLE87Ybk7B34G%2B2ybxzc2Ae55qELQyjcU%2BAl9PFDHWlNozpNWdu96mN6LENa0nHhVw%2BkJIgmdlyE1mlUriCV2psZrYCBkmI%2FXORR%2FvCK54P9adL3sAADvlanD&X-Amz-Signature=52167866ccaf059c46e713e56a6f9329c0dbddc1b147757d90b4760377e297a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
