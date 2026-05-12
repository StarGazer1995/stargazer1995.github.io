---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWXPLLW5%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T053054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQDVYJ2mTyaNqawYQGn8Tb1JhuPQYRN65o9U%2FahgoZbKkwIgejtX5noymPFBjRA5ulARzbRi7vNYUBsUu02OxzBSMSAq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDNRg3oOVExcHvmFuJyrcAyKjz8vyXaUc4S1SPJfrhoSZ%2BFbGrEJqQIAj4wAnn1%2BTlYopiTe8bGPz4Uup631BY3Gx6xQpJNu9J1oKa%2BOYNT5J1ZW%2BakaWKoCenhMt6w7xf7lFyuKkynJpN%2BZZ1xVHLDWXNumpukd9qAg63gjk7f3c5CEgWkwtXqPDar9koTiR%2FqupsFVALpNCFc40KtvUuEUcHgIM3U3p%2FKx9dYVy3cs8Cgisgf5sARGVDcW348HwIkkMxouGnfp6%2FHKxfdE55nAm7mxgvsDy%2BcMJ%2BaTNBA51wzgnBeCY4kCJBbHOsseIA4NcuB7odVUAKwVaAjo07qwriH09XZeY0LN51OTmcXh5nnpvgHI8iC5aHM%2BC%2BYQZSs%2BJa8lj%2F3qvZ8%2BGl6w895xPW6SMtQcPX8%2FsdZHLY%2Fp6k3rj8oshTRCof%2BtYIH7xXK6r%2Fo1guTk4Yakoo0VyCp7lSusLYOhPBWry8u79KrNs5INNTBGnUyNbMg8tAogAuFG3MDv5nIEBgYhnHMPqeeid%2FSXUwv%2FLhqpu5o7ySD2uI4aRM%2BAAKuGt2G3%2FjOrZdIyq1sZgpklR9W1p7yX2Cca5RapATTIBY7DyAWPadmJIZ4iEJ2slNw8C2H%2FJR%2F%2BG%2BvMR9eIJ0w7x50KNMPukitAGOqUB30XzJ9G5qU8UoB85PQrOlx0l53zWwUyXcvffC%2BAIDsmG%2BHGpbL1E%2BWvUtdJmxYdoFvDMtMUUYYfPil22R0WJ173vi%2Fp%2FCPrf7Z8cqoz2K8SWXdxEmzFy93ap4NkcfV02o4Kfh2s%2BhFvRwl5DD59kxpBBmShXaunFcA66EeBwRepJNWheSAV%2F2xDP%2FrkzHP6XCKbGs%2FmfMd6czVSyX%2BmNEbwN9CcU&X-Amz-Signature=40382bc7986f60ff3c8443e30d91f5c1eade087f8d8cdd07589908e202c99ac1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
