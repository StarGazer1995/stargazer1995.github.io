---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXYHNHG2%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T180401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID0subI3K2%2BJ8mnK883QQXekdIkUVkH1QKxthuO3NT5hAiEAjhgm%2FqsTl1g7gcemehPItzlfi31A%2BWdDE2aKRbsaWsEq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDCJKlRrk6g7P81vdUyrcAzOFiWMCTJa3HDiaQC4uRhywNxImAvikU%2FHuX3Xli%2Bp35bNXiDP%2B9d9sl28udqDqbDyaNgIFWPpYFsM8029qKxcd3GM1fsG2y0es9fh1hCLx0Ff0lm9lZ9vf9G%2FIoNyhX25zY%2B1xnffMP8LcVwr7nPxKRMw8751wcRd2bAqVBDTgxP3recpQMgOchCDqy66RhOIUtdXR29VZ4NF%2FnfBBz0Imk77gWLeQPkXa5LsJ8hwJPykfE7Xelv4jAv7xzbgpu8kuLGTgL6pg7SZL1Ltqq3toF3OWKSrkvFlx3%2Fy0PNEhS7EQq3hzU%2BT73E9O9rdF63uEFpZAP4%2FuN3wNOssPNN4Hy8paIDHDqPHmrhSAMRzBIkIcJIiMIUfyBwAzU0uifpAJ8R8SnBUc9fRsPQL88dvYkOUEaVmjHBYCsRA2%2Fba7NydMsiJA7zPkomgUWwrb%2FoLIz7tQkqCLmicSVHbba6ojVxRojxwg3Icv3jaI9RWuaqflYPgW7VM7hjBlzQmNsXd%2Fu0naH1CyRdKvqEhl9b77Ac6pe1duPDk09pVGMeCQDYAxmgZnpuLc6AOW%2FAGSOQBarJJ0CaSXGpigpq62kzBSoC2b0vo4Y7xnBB%2FssZ7u911lt1wawQrFyjfLMKe1r9IGOqUBfXDjt3%2BwzNU%2B0Iusj6FSd59IgcDfjPFFddp5nuDToAKgNra3eeU%2FIWnEOmDEzxtoTNfU%2BygtHux2sbs%2By5gbBB1YdeBhBgswopUmaH7omev0ywSQ0U3OqoDyCKv7FH7A6rdJpLd6%2FSjsxDAGtfwo8KNDVK5NrfagAQhGTpXGwvEfh8TVr4h8s5qMpGhlYBCTMpPYf0kvTTOWEezG5XMeqAoNQgR0&X-Amz-Signature=b95fcf0c57a3b13850ec3ce2d8d8d3569ed251f076f7e67567984df0b30dfe11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
