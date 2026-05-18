---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPSBSGH3%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T224720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCEdgdHbM%2BXmooM9uwwziYtVK7%2B3oAJQiS3zA%2F1KbebbAIhAJDTGfuVJSJi6bVBGnvJnqR0QYnmHw%2FvwuOrUIBi9YIsKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXsKWF0RzO%2F8baMMAq3APc%2B7T3%2FX%2FKxIHJRYITvZ1g0ND4ki%2BMAIbwsCocfpSvkaZSVAsaJHfp895Dk%2BlgJo9SUCfRv5GNNeCn23RBLp8ud2Fetp3AySW6q4Yl3LEfsuYE2%2FdmL6OH8p2G0zShGzM7HIWH3pV6ZxYvZjVCXZHq%2BtAtUa7KsplMd1UObSNYQypFnnrbwdnpElELLkQ9TioCzaGW0npsPFQx2m%2BsD9lb7gu9T0hsy0NqvHswkgEYM%2Bn795U%2Ft%2FzRk%2F%2F3p9wMyFHE7v2t0nXTBqgd%2BKMK%2BpYE3krJTH1%2FDysR2OvrmsOo%2B1bZZ1CkA%2FiJpAduRSX5YG%2B9%2BfR%2F6tdNx3%2FfYHuwUsdVvnVcgB33IovSOZ2JLmX85XY3J%2FnPCGSLEP9gxsLBM9T7Rbhinj%2F36cxATb3u9WyiIVikRLTCFkEDMbKx0%2Ff4VWwFqYk2pQzfZE7LKmnOgpZvlqpGZJA8Zop2VC6BhxpSLX4fnPnOgGss%2Fh2HXF6VTKe6PeK0M1djURJAtam1SOhX%2F2IO1nduPL8KnsaZYMyXz1bnzYHJ%2FnNX8srJMgU7YLBSczOJDKPbvbeY9mueqETaDN6U1Uqk3qh1IgpvfhG2msi18qBtQjL3%2BtGn6vR%2FHvkp3zuuL6N2ULTwuTCWhK7QBjqkATLxFkcu%2BVoUUp2W1CJ78Pd2BUx8FqgVO6%2FYz16Z8z5YjHitHOHlnRyfiE9qnOzRhSC4ouq0ZxeYTHr1TMZZHZ9DN6PPFm4E%2BJOqxnvCkko0AoLyTg%2FvB%2F%2BkfratiSBuHan6Ox00m76CHS7G7mMBfzOX1q1o%2F4RGYbngb0JZg8pysI48GU%2BSxfOfDxRvK95seSsrcQBckWSZ9GPCXRxZQFA%2F0y9G&X-Amz-Signature=b788111510ccd72d96927792192452d2a9b6fb53b2146261614cffd5e412aa96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
