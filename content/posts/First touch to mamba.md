---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635LZB6N5%2F20261008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261008T012455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJHMEUCIEW%2B6ksH53jgeXmy5notFzt6Gr8NiMMA7YvYPq2FHSQ%2BAiEAr2u1nbrn1ooARVF1gPo8KeBjNFtmvy9%2Fao1kQmP6ZvQq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDNWXy06w6HbPxiOpKircAwNBpRbW0wc02fnXkI00Q%2Fluktigr2CybykwZa8l39kMFvV9YGAdkW4ZM8Oz201wXgfyb6%2FQ4Sqgx7iVnCcBlACKq6avwNxwu8PFoy%2Bw4eULJwkHZZCa7%2B3azhpeQPl8ynlxOAnXaleOphoTl4MtcT6WT4%2BDRFuz1WTCv2MgHaqb2XtAyDJfKVu2fvbmUxZLD%2F%2Bcutie%2FXdm2d6JToa%2FnSTWpmCItm7GnCQxGEyCKjY68ERRf8JFJp2jJwAWpE5mbxFh9PglOnues8XfPoZblbLsxB%2F4SrwUhnVQI4uf5wBw7wyf25YbO90ilzZTX%2Bvm1Z%2F3rfaSnM5hqfcySXVBgswAnCbEYMXLaPOdcXGM8VOx9YAHN%2B4gWAGjY6G0zp1XtCeCVk%2Bgha6ZiTmtGTMdYYO0SvoTyJmeChMK5asbO6BFxHvP2XXRv%2FA55laWVQcklrQ%2FC3WgZv0sfhkIl14i89KyASiEkIDKSzLYaSSoHEgliSrMLwXt5LOnfOJBFrU1%2BIH9ZA8SgIMXq0GtEGZl77VUlnVk04n8oyYxYHneGqApQzDl3vG3gncUB0NbA2rJITd1pdhGsiTbzo71no816l3r1EmrGmBEf1VwQaixro6J6P6Bs1UYyqoYV%2BbjMNrEm9YGOqUBpfXF7isuyrP7L4P%2B0tgOz1wLiPn1NFkDBEEGHxB81UTXwMNTmqX8NlD0cSfGEeEU3ahSeSDeoYSZLF0Alh%2F3BA6lEy8ZdkbDVgQsqHD3G%2BAXMVjIwZqEnkPTW9WLK%2FDdFbis8MMiW0s5HRgUzQoUVKoVKFro%2Fzy7CVg3%2Br8KpKJF6vHsnRqku1q8LBgJcPHqV3DDEHxYkGLPP2lVTVJq8p38zL0d&X-Amz-Signature=495a14d223908afd891e898dc1deb8403b3b1251f5e305fe41ff3cbfaba0f6c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
