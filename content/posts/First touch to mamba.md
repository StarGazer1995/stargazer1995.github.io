---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R6OZKH5%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T003446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsXnTSNiuTY7f6HRFNXJagfJ21bFDv2%2FXWO1ITG69oQQIhAJ52iidtVtK3LUpHmokhNldJWbVGZc4MdRRWHtxwkiEoKogECMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzFfdtxZwUF7VmoWc4q3APsL2MKla3w%2Fp%2B6JpGWdPBHRB0ONb2CNo86F4Uqt8EdcFXDG%2BlRxukxgDydNBV7Sc%2B1jvvXz2F2qEt504wcN%2BA6Whzo7sFAcaNPGgEjuyMtGE5cWxgMMrgQxeI30RYkFz447F37s7MDBldEUO%2FdSQ45%2FQkTrJVCbRZlxa5oKbtHoNTyBdKtCMMTV4BR%2Fsr%2Bb%2BL49Bnc%2Btxz95%2Bt%2BglO8Fnwk8IpmZWRyg3ZuG0D9VK7x2tcGkv9zdfOsX2dl%2BMcEEa2Vc7IvTIqJhbRqgCT5j5EvdHbGqHwrfubwn8tbjulr31SbL%2BwnpHVm40e0NZudZBQOny0LdWSiWqjVMPjerVnYelbk6JrIcL%2BXawBViyluE35YxI5pIpOhvQtjtRmouJdSTcZaJW4lIw8It1rX%2FBcYkRoAXxMxMAatORuQQf2fbBoVvxSaNR8jtxc5UOUdM2zrQDEKIM8YXo4uOYQGeHvjCvtvJ26Tlwn18Kf2C2pO%2BEor4oxYJrLjt15%2F5rb84bQHHcMB3JQkSedzvJG6wmzsPT%2FHCV122jj5F3CR4wXiTLoWoA4tekbBDp3b0ZF9ds7rT33HcgyDTxAlgzYR5NsDKfFbflZ7Y5%2FWRYt9X1Tic9WbRkZMDOatOmSbDCB06jUBjqkAdvtG%2FfHNejuSfJhgiIFJSsiTLMPB%2BKz%2FHX%2FoDV7sDjhufWFC%2BQRRgsHoxOiGqO2p8LcoH8pQ2%2BO74qZu%2BvFvYUnnTRwLZAsWg9kXIk1nUUR%2BCSftwbqAGUilk2Mg4acs3%2Bnh8rrgamw3yeQNgRUd3wNbE0m0KtcITSejmMxXSb2IU%2BkU6IUabRjlDwmjs1m9nexb5ptVKN2tprRwNWi%2BjGRiDMT&X-Amz-Signature=cc08d53c4855599047b4982fdb14468e9011dd9e11805fb5489f37090f780d3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
