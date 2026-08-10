---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ICSPEI4%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T144951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAztrvm1P%2F2LZ7CL6P39LvygFASRZD%2BHqKqW1XJD23vPAiAMntJEe1UKsN%2FR8AydMLsJaPyRa1j5PCzmjrJ7YqIoUSqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjQc0ac3cvlelgSJ5KtwDxIe%2BDfMtAZ%2Fc7sr8BxJ2ePmf1KFrPmrsYTZjD66Jbr9zvaTLvt75%2BhwZGR5%2FifpVmZqzbRL5noqVECYGmoVmDKb0%2B3kGXRKpWpjdOJmtSaXpMRJIY%2F%2Brr2WI2E4ZZoi96fwod2T1MjP%2FFCfQhx%2Fzp%2FTNrv80wEFoqsY9MPu%2Fif%2FaBfBWpsbgrAkwbCqagMOLH0JUXEzux5FiTXwXHZA5BfnyHXqvk2uwJwwG%2FrDo4DZWAuSwkcNknUqmW5eDRDAPAWC9b9%2Bw%2FQ%2F6fAGl%2BAjtr0fdO9djlwF7wYmjTX4421X%2BmUQ2JgiLARosVYVR422TsFkPNfmX048HXEtDYhFCuIF5y2O7Yv6CGAKmKYddIQdgS%2FsQAywfxkVhu2G4Dvel2Ff62LaQRllHjKNZP8ADw24EHQX9shuHG30yg%2B%2FeHkOawZI4ecY71w9Q0eCu2pwR%2FKmKiOwWb0ZSc3IoFKxAFZJnGiLsC0XMPNgknJmBrdIAmfMDtR7aGPS5bhjAmW4%2FYShv6wPC0aULequcBR4JCCuLyoZ4ra2bFwlBDkuisb2iIzEPO4t8NzDLwqygBK%2FwyIEelpfxLvLnwsxuMbK7s8Dt6cLKRfw4Bwxa%2BRRdlEAaLNDRCrfYZUguVNwwhrfn0wY6pgFjOSttv%2BTLdYZ%2F8NdcizK66o17n69NvdDu1sJrvH0K1BJQrhrVIi2O4R%2Ba63zrzZCY7INYNm2qPnkAG4jF1z55aq3ycIEFjVxVw034xgQKhCKC6mTo2LlwnDHy2RDoN5VwbVbStZp2kr%2FtHqbcFRmDP1pZyS0kthx6roaNDXWovEk3nC3J0nkVHsRIotZ5ZOG3P09cFj9RY%2BO9gHTchiK0YUFVwolw&X-Amz-Signature=84a005a14a772c0b147d900755bc59437b53bae02721762884ffcf89df21048c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
