---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674IHXC5J%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T203719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIDlxB%2FCICeVbHs4F5g%2BsfhEaWCYBkKQnLtt194ITfoKaAiEAjBCwg9RD0TSGUzTZuqh8psQD5io9C04tv1cxjpYCnZ4q%2FwMIBhAAGgw2Mzc0MjMxODM4MDUiDCLVKZylv%2Fl7dH%2FdjSrcA%2BfQh%2FmvZFEzNDLpa64rpsZCFJUhOirajmNPd38RY4oc7oGZ1dSOFnXEb3f2%2BblBLj4a%2FRvLtyzW9ASUKRCnzFERrPuFPt23oPwwxeRQDkw0tpIE4LUFTFav73nIG%2B0a2tcYxiAEkrInnBtAEvhzmRrjh6FYBtqq7UwY3Vbk4uqnIqpV3eGaQAP5D6mAThtOklNWDP5qmqkjp4TlUgfjNeTj3SJYTNkJcTZ2l9E7cya%2FTvVSMa8843oyewME47W7g%2B%2BSgVRRh80esLZLbZ%2F2FkXi7wvbAo83yMYbOCROrTjWVVJwXex6xapUUh1MkVSX4fqNRZjyk3zw3zw8dnRuirlU%2FOXIXoULxUT9UdROjAhbXcChA0oIIArNM67RHpFRPS2nKOj61rQwe%2Bo9cXqpRrUbPyTf3Rfk2lIxRHyADu4mXGJ4iQG%2FsKQdTKKuiFTvrASbfo88Yaloh7MM%2BzLozJJvMVu%2FCmg7hvn0Z3aJWlcX0MXaK5MbenHt00%2FVheyWiLyfBvHkBkSZsI3%2B0gu%2BEw2EHmvteDMZU1F2gB%2F8RAfIwiCxjs9sB3DzhXgFg2kVtt7%2FVQDI2f77QRu9kBWfQIVuH3dI9Yjzv7AItwXxrfTTokRHTcEAQUBtomL%2FMILVg9AGOqUBTUsDKbM9bKOZjG9IDC8DL1roklviI7rU7rmJ47WVG8RvDw7p62rss2EYsI84cv9Wj%2Bi3Y4d2xWqBGMpjTG5SZsf8EUFSZp8paDg80xqkzQR%2F%2Bga2eodozmVFaNPj5kjE%2FS0Zgqs%2BCIEFI%2BVrX27nw2QpLXxhOEXiX8%2FUMRINagN%2F8MnT0%2Fk7TLFFA7Z7%2BhmvjXrkT8is4ydRiwwsojNGpILn1cdE&X-Amz-Signature=c705b43c73c19b47f35358c5fcd7401999eec9697b684154df60f58bb30e1c1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
