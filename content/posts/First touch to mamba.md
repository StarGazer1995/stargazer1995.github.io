---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPOQW4ZT%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T081345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDCS7%2BbhRrLt%2FvQyMNogFynxFe3dBAMGLG6H%2BV%2FBPfoIQIgBJiQRmJKzLC4G7wHPcZnf9Gb40eDid36s%2F7qGIGZCH4q%2FwMIIRAAGgw2Mzc0MjMxODM4MDUiDMyo0YL9CfCkeDzzACrcAyUxVTOysToXEbzPbkP1sAXvcc4WeiljBeNzecSgOX%2Bkk2QhfhialgAYhMsHi13NEAl9smvPdtOUWi0M3ApQF9tkl%2FTwpXhadMHtyoskOlVmFxhlgsmD0iijwykHOBfgCGzV6TJ0PMT5U%2B2ajEbzrSCmRu79AruQbsX6pv1UFXgOWJhRFhTnw97SJLi3t45mVeIFWTx37IyTvE44VVo%2B1%2FXrcaYh6M2CEiKSricJGX9Zz58Y0VizAMz4D6BUSdjFshm9QwRBvvX6WaAqmT7KczI7AXx%2FS1lKdvpY0UMAwyChivpbQfHEZ9SrmV7QJGw9Q3vLwN90XK3AFDqs0xvc32%2FSCAgz%2FOAmvRUNuMzhGO4NJnCdYMvakguSrVqrl7nb1MTGO76olhCfpLd7lRNOXXcO%2BiZTFgp1O%2FoqjApy0z%2Bxo%2BfTzyD6x7SZ%2BRVawn%2FCXGJGVGc0%2FTtXG3MvQYZ2bWoxX6qz27pN9roWvEHG3%2F9FLjE26ZRRmwDzGTghKj3HxlfRXl%2FHF5wZiXvWBUlD0MaHDBjhKdMzdSn41ggFPIUt2KZXNrse1cy%2FV5E9aRKAgnWfGhsryStLgbF1KULFdMwkL5j8D57s88CyccHKSb3%2BbjrAv22kReUCtNOiMPbcy9MGOqUBjKR4%2Bq8PJz30IB%2BqUX3wBTZGdz%2FXSpdUJhFFJfbVrrL8iIuHrVDix5FE9mUfEt2ejfHN7RGryVmmE3XJDL%2BoUZ9veeh2b98qGiPfvDKqjS696PVTsoJdyXzj02eCXxWs9cUDxnB48CGP2BaLZ1AFkVyHHqtfHAXJEDKgxEoDXnGNk9PVuqUD0usMaNPGbEwtIJfv3VyZw5OdlCNZXFoIhgotqQHv&X-Amz-Signature=b1fdc708c52b313874b95ca7e057b407fdaa72d4cdd5c07f1e80cfc98fab919f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
