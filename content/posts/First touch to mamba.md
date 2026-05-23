---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEDKGWXA%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T053233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGUaCXVzLXdlc3QtMiJHMEUCIA6P%2FrQmAUwFlq5Rf0Uydd1YOhCOvqqORxiwchX%2BiXxOAiEAhrA%2Ff6UdJNx0pXaLCs7Y05HZ8jElxsMIzmhhvgQ5SBcq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDGim7eUZPVfH2TtsOCrcA%2BfcVK43OF2cja57qbNDFl%2B%2BYDJ7KZruQ%2Bm6zt2%2BQHZqtUQVH1bh0gWFQEU3IOBNjm1XfFtqBjUV2ZdTjnoGaPGOMekrqHapj3zdmg%2Fs%2FNBq8XizMBdV3sWAfahR7BFBGuzhSxK3ZdOzcsbayMJLOZf7q4ryWrK%2BDBXGnmsM006zETPhQRFWiycf24CHsnGT7tknKBIPGB7voC%2Fh%2B31E7SDz%2FLiS%2Fx%2FP927OXQGcIMrQ92L32BiBW4YHL1U4nGE4gAM32TNzOXunNOpzYNU6xCGggMpVGFFUDOBgfjJ%2FTRuOSU2pxPE0L%2Bk8F2LMqDJzf%2FhA7uxqNzjNrozTy6308FYFdU%2FZ0fmQltLo6%2B6kgSMRUxWB4bjjHSujZ5coq98rSxmT8Eg%2Bb29cdFXESH%2BrEjKMbZRP1Jgln0IHZHhZMjp0ByaQj8DzXPC2asTJnufIOitk8Tz7KYYEfuxF1WBpxzoQf%2BfvX8r7vEdErDPDNsjIfARV0PAnUx%2Bf%2Bq1b%2FiiVeXHYwpQ%2F4BqDWHPZt3Dr76Cn5smzizWXnwTfL5OrN7WJ0Dl7yBoqXVGY0qkXefzhQxTqhYB9gSeuHFBnJnk11fd4rL6yIu0gs0Oup8%2BHRgwEGwVWJECUZkVeT8XwMIzwxNAGOqUBIp7fE4dL0ShinDhdzIns4FDG5DGc%2FoCxtKUobkZw%2FtwDSOMOt8jdlgKM0fJaZcsHp2xkbrqTF361Ki6WuzpiEukcILlsLb20Sxk8%2Bj02VduiVxUJ0WIORS8U2WFbDQLVpj8UyVzA52kjRTP6L3ES5SvqvYcNeEdSnGHyjWBgeuf6rjjHGP196gobHCgX3mFCR9bBR41wa%2BaobBPAuxcqvDP1Se3Z&X-Amz-Signature=5761b5aa5fe2156bbee186ed871b5af4ea352aa983e2ad27a4353b4dcd066b75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
