---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKRHMSE7%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T170544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGZGuNcyDaFh2Ym9of5zS7adMkIX1D8qw0TVTklxh25gIhALytf56%2Fibu1%2Ff%2BieFR3f2x%2BiS2eHtwgVFGB9bm%2Bti1pKv8DCHgQABoMNjM3NDIzMTgzODA1Igyy8SRgoD4lDcFMGwUq3AOY4CtuQ9e4H9s6nG64aaEHRZ6nH7xHMI%2BerU0ycdwcb3XZIUmfHnjIrxiDSuHRF3StRPupk2QITys37DgwHgEes251xEiX4h1G3KATyf2wnuTf1ipWvx2xFVT7x6Ik7OOj8D%2BEjh6BWt0MtxfwtgAvok2qUy5h6GRhod2Px3sRD1%2Bpm3iCWXVLBf6G0fSFQnkmUGQHQUM1RE9ZNlD5w78ijaleSPHmlU8GJAlv%2BlC%2Fbt%2B7iprXyKbxcstOuMz%2BErbSULh98wBk6SLEmCrjVuJ4yl6xc3oaFuLTfm3NDJsBawak9bx0L%2BCRHKyNOmfLz23SACBdR1rsG8jE0xI8DLl2HsmaiEx73xn6gqqccPePP3awaFyvRwcDdJIv7UtZrtrXN6Th65WtbZH4owc9wpT2ujn9f%2B21orvx%2F%2F1edMA1YfPGxQtmrDlYDuQUEQDj0m5wID%2BkkoxCplLG7W8hsIF4Zn9PFlrPrWpPQO9CLntxCn%2BwgnG4DQAzZBj4YBAMadZEDOfxiH2RMvZucxjw9mcWiDL4EPny3FcfIZYounhnAKkyJBTLyWIrXC7WCJyA0DE%2FDhGC50vQ0lNIvgXLNWSPt4JqCsFANP9fOPt%2B1kujW1CASqp2p12jjvfnqjDO57%2FVBjqkAaB7IBh5%2FKcV030BbNeNC0hylWDvwO7Mz9f8KBpom4PrSDzJD9DC3f6DT9nNznNXZBK2%2Bo%2FHrxAkYTB2kAk5TGHCzhfm757OzDKakdbBouYg6sfi6Id%2B2%2BKhYADdOv976WqhIU9agogx9vN8bddm%2Ff9%2F%2FgNFlUdJFvmyAiWLhIRNd61YHiJiS6%2BfP8CiohsRvO%2FwWGMzxuHAAn3HOlLRB6vASSWv&X-Amz-Signature=a16686eb2627f7018bd23f6ee3a0c52909f1fd39e20c66678a43ff37ef931ffb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
