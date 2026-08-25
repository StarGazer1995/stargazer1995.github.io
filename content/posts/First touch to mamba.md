---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YO3M2IYM%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T162330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIBRX3yyWx1raPBUqdo2fDnFU%2FYsJpk7OEYici924GKEbAiAtqN9NsVV7R5ElUyzGBNzjZTO7j1rIeyzlW6PVlTEyMCr%2FAwgIEAAaDDYzNzQyMzE4MzgwNSIM37rFYhHdKJHOAHWcKtwDIPF7fJ53B5TTfiTRoszD1fJq%2FQjXQl950M4l5au4gsjw8xlzZKRLOyBa7anrSw1fQFwfGQlqSYw9D38FiTpVGiTatn15ujNGC9obVYM7HIdNyVglZcWrR2JfP4vwETSN89WYUWMU%2ByXhy1OeRZXDHQ4no%2F%2Bh4EGHZMg3%2BLNnQ8DolJJkOalVl1wPsK%2BPMGFvx%2BX22uInUUQyWpQIq6XZ8aE6UOqUcDXtlNbyqCPn4YqKMmTl6VPI60d2vuF%2FiURCAUPQeOz54N1FxLnUKbT56ODx8grpmgokAAy4%2F0VSFdyaVGcvMVsms1qWCwV7rHqCJKZLtFo94CWCol3nXRNZ0eCzcnKk%2FcXevUG18LbdFLG4vZ7mEj2PfE5v%2BDEeHmDHqblqX2XluFwRijuF5ULhYY7J%2FPalJ3Fuj7lQdq9ZAD8O%2Ft8ttE7TpyD54UsHOgjxkTnYOMmtS%2BfC3ABsuHNAQLq2EY74srXr0z9zu7GU76%2B0T%2FYDRpryuf%2BGAdiBEfScSwdtz%2FURd371vfdjMCVLtubxyARpK4EfMJUelYk0YaLdXnmvSHW%2FgfOZsvJp%2B8r0ksQH4TyfWKjP16H77KlfYwSBL9gzuYNbaCNiFE4RYP80vR9fRq1HRHw2sO8w5c%2B21AY6pgG4uE8foWRJOY5MlJ%2BB%2BuvEDkgT2%2FCfOOMA4z9KiRBXb8jS9W4E65lVwItbpQ8RPaKl%2BvU1n7l08sfvDrl1US%2BtpFrrEpcGigMc67NuRnMYZ%2BTvBQSJcP4aMTU4M2s8BSw3ddisGKzYrbgrsw%2B%2FncAo94c%2Fx33HLJdJQboHoJI6Lo1LHaL0P%2Fp%2FuvVeVDz1caVYMzQ0bd0oFNcEmfPc7smid2BxJeqz&X-Amz-Signature=04fdfac9ed2a4e3bc42e0be72f2899e3cb4f3ed443c5950439c4aee84ae9838f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
