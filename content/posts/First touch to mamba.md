---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VM2ZQ25I%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T152616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQDHOqDkuYnm6HXZsAi%2FcHncwRG%2Fo83gL2xDIDoGGqDMrAIgAM9V4VVAfkiamOaPGrHDq80XGgGwtxrNFnvOYeT1CdkqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAK%2Ft%2B5JJRi%2BRLOrLCrcA9dz1R8WPWu%2BVz9E2Xn6JUYABX9TnQdCIG9jGljiHlbcNmz%2BXMk63oecrTg6tRkon2RstGzqdyw9mX9J1KN7jxUk4FQ9ICCgn5P%2F8QvlsxonP6qib4YOw6M0Gxp%2BXNQzcFV4q2voc4D6SVKX4PiXRD8Wsmk58L59t2epQaK5wTMS7Q6aV1C2LTSsgDSkEQbF%2F4guMk29be6xLSghpRM3Lxou2VUG%2FA9JO8PtvZwnLdMdoKYmZMhHZ1An%2Bjg%2BsyBNQlQfc2ympxcxAK3n1fxowGcPkzPHIpf6DdUwAc1NrcoOlq9%2FDSxDqahm3d%2F9i3VLyeY9%2FYbWlL4gFmcQtXl0tuU73FgksPEp5gmqRfNuCrjxwG54NuyL1v2oLgmapVBxDjL2pKNSNzReawWc2do243dOUNytpS6%2B4YLc7k06X87zKFy%2BWZthC0cAxVpFlXPuzFIH7CZE1yEzrT3S%2BRd7AfXtIabtH%2FxwCaJpBXfgCWkh4Ga%2B6aDGQJEYZw3RhuA7x8tIepT7hugtCRrNXhRep0T8StYZPrB1e0%2FoL294lk6o%2B7%2Bebut9iookdapJoJ9eUI7hSIRE86lbOOjVIM2r3KpJEy4PrpZqqoEH75pDbbunCT%2F5nkqH0dzBb5a0MOGUg9MGOqUBvqGO6pjj8AZSPLrsqVmV97w9xcmRIHWwrg6zB6YdyYH0VBUTVob4FCImDilrpMawGfr6S%2BZD1TkA8ooUJNlYMUqOiiLj9gp97QVTMWiiA4cKP7QkICQZ0Bz32Nu%2B6qjpXEtNxttIx5Q65y7dSfcki5MYJVifjaL8VAcxR177RIT7yCEQdOLHU%2FaZlINj9%2BynCmrKFRoCFPLZ3jxMNJSoKQOZ%2BXk6&X-Amz-Signature=be605a19744573b7575ce8371aedae68c4e7a8dbeac41dc1aef37c8410c06595&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
