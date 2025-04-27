---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RT4Q74TL%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T064614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAeka4bLwy6kHBGYf3V8FKo29Ekr9ivlaoPPtAVuF%2BtgIhAMFaBWODUNS5B2ps%2Bbpv%2Bt4bwCSYAqAiayizAC1OvHzYKv8DCFYQABoMNjM3NDIzMTgzODA1Igy3KEJkQ%2BE5l6KSrNAq3APERluwQLGft0Z97RiqkIlMq9G1jQ6CHcA2bu%2Byp247%2FkncUr%2Fe%2Bql6qHTgRj8WWYchH%2FIEfmXTLKDllmexq%2FxFAluFiLvw%2B72cNsCbymzKcqdBNmXXaVdqXRmsQch1PO2IeOp8eIlbeZgl90tESjiW2WqxuhWlTr9GwIqm%2BqwNFxyUFbZHsdGNO%2B0bySytJRJ3Hr8R3ErvZcDpq11g2jbosODIGV03aaLLnxjykRWKDRBq23K8YG5SgqJvu76ZK8iMpW3nh44M6uz8ASNIlWcoPxoau2b6WimNHeWoEAGuk2D1%2FFMb2cmY4tk3KhTmh3%2BPHwXGEPu5IE2OSdL9C9JoMdZpO%2FNt%2FWqLoDfdT2bAkUPfsUEA8S%2Fp1eu5FjFZOcA1rg2ElarOKEteVXniPup%2BMJaeI4tM0cVvDBTHYIBqV9ImfhgTDvA19SbJAMpJBuRqXjf7qb5O6YQ5HePgthR54BQ6oHXO%2FL%2BxrPyuvAV%2FprWd8flNn1DCjBdu9Oo51C%2F0vd54Jop0i7v9vDL%2BfeJt%2BfL%2Be19jbavi99ffP2OLYvn8vqDbN3cfrmd2NjG32FgaTgKvA66OmRKo4mJOG03Pik4vJVSiXtrgTIoEngZfF10sPylP7fSfbI%2BsuTD28rbABjqkAUD0sG6HJfLFBeHEc%2BVSQydHxbLHyepJbGIriovu%2BB5yqZj18jgYRtMdmZqreyrQAhBftqF5RvHUeo3w2fXXhpssZ5LTozFMUecZdBsFux19WRsyYyzJirYPUzy4rKXCp4LlkeVeuE7%2FDM%2FiDMCjYz%2FUFVF867t4Kyy9x64LXCuNI8%2BF%2FEcwStxoXkfEFZLr0XIqK5n%2BjujU2nVt2kJ%2BrMUfeLBi&X-Amz-Signature=cb5127ad6c2872364dc9bb6d070a62d58243939f201c52a6b83b1e2dd9f076ec&X-Amz-SignedHeaders=host&x-id=GetObject)

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
