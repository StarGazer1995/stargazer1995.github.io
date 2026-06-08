---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZGNJRVF%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T023003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEHb9IRF1%2Bx0uoafMiyZ9JhV3VAaQl06WbAokWgb181XAiEAiBO%2B3zcf06qHmHWBcDGeSES%2F2MnWVhyQkUFD42OFs60qiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFAM20psfjBXcT0ndyrcA3KOc%2BbobE1rQL7BowvPOWZSbuLGj%2FsaR6YVsrg2nmnPqOGDH6Q1YdnxiXtxqxJj4RVhF3pJPbtBiaQMuyDP3xnsEl6sTXicm3YKxtosM0iIJSWAOCJWWMakqE66bqanx2Z4CqPVD9JyqrMd6NmOTP9qewsttcgwGGiqeUVaC%2Fub9RCPy6GT2iTvLDhL7xntl9QGxLmr1j4VBOK5Eg5qvEVVsu9ANOh2G9JnR0i5pK1u9jylpHJwrthfUlun6UGlM0tz8DWTuq11tWiMfuLJ3SuVrdDSBP1ql25%2BUyXpeEFBh%2FVqWzwN18ZjCLA%2FGKL3oWSnlyyS7kin7r9sb11KwN4fm%2BAMsNJtbL7LfPZCD3h%2FUuLBKk6eYOg1h3Ry6Pfw6%2FcOfpmfRuF8njS36Td18%2FgDDlpQXvkiQywcDL6HtSFKpWlGmizUPUVT6xEsHFYMwoViMHOtRxyBkDVM80ubykCX7EJVvVS07lpTa2np3QsX5WLsdfGJKl1IcegIY9M1iQVrCg0mxGuQLa6V4zc6I0%2FIwUPZVH4oetnuzbEYX4U1Xax6w7hZjbiN4A3A8vWi7QfETReGot%2FK4UT79f%2Brh8s7defB2oTwozgFkT92p1FjbHltSOgejPY17BDmMKfBmNEGOqUBwGgwKEi0MKfzBdS3Dve7B3vZn9F%2BPg4yxSGnCq2jFRg2F1Dr9WvgSkspQ2i0dllVIhYciDy4ZyWx4pBPHcxadrQUpig9r4gbeXg7fSul9woyo7nH4M8kgSGbg6nrjPlmncdOw9%2B1h99S54dLelg%2B7VS6mKAK%2BIXfgpI9ILFw3olPp3cz%2Btjdd%2Bec%2Bs%2Fif7%2FlyYKDOR7V27AxWGhu9Sz7mhe3Fqbn&X-Amz-Signature=54990148dc26e27af61624180d78844e35b2fbf02ebb2bd463b99c53b40b11ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
