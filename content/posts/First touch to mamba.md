---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636XMPCKC%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T172348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfRkJavF8vWWQtik2hclPnQungOxmKnO%2BKXG9Q3XOpLAiA3IaaVPYy7PYvGG%2F3jL1DF7CwQIIQuzZgPXAnDNOdwnSqIBAiG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMw9p1k2p7Tc7AcKohKtwD%2BtKpbkUZpfIb%2FJsmNGGWYm4ytEobudN0J562BsVaylKvSebxRGxW85l4Tz7MUxgOeaqtLaTRqJ6KGsGPAzr5yvkTeMHJEbgfa5oIFe3AukC4yjvOktbXaPPBO0TyoH5lnx119dcn2JSolvsFr4ChjycFLizEAL%2BCzCh7hGLwpE7wMrerXLMW0iJNnwnO7orRxLYPbG0DSfxNwkdyH80PNlOTVGC0ghR%2FvuT4vAOYQD%2BwKJaGrazYMITprc8lOQpFzjNJeK2zEyxt76eXMv0AJOWmsrCW7iVOEAq8IY6C9MH%2FGTTs%2FHqxuqYsVgLM%2BMKbePXo%2FrOUoRGDiAAgLdITbH5To3pVdYvKbA0zYZJ9Qa%2B8%2BPfWezdayaLUVIp142skiImeHKYTazQPn0yugJfnUUCkOkxYwU6%2FSj0nVljqhAPkMV3gC1sXxlFeAPe4qXRdekLwttYmNF8tBMpiR9m1Esz2fMLbo4Yd6csNJOBm%2FBbMRWLd2wfhuKhNsdYYuRsRb9xEetNjI81UJ6wkn%2FMeqjylCWLcYZ2%2BSin5nECgJinKc0PHRl3B2bPDl9GxxFWG1Yca94o%2Bgwxd4lQ6b6irTsSJJ8GYCLN4NDnDeBnS8U%2B5RA2G8sXE7JPNSf0w9dqK1QY6pgFxKgG0zkDEBEipLUYBe5Hx8L03MpYtxqFfQ3CvqSrPYmqWWtR3ME9rA3KRbnijZC4svpwyEa%2B9PVmMoqdOkjox%2BO8VOstXSSctQBXL3QI7RL267Vk%2FKIOTvBMZFJdRwJVBUEw4SafovbtVY%2BAdpMToW2HzdCEjUP3yyUuUYz6k0sd4ToFJ9TaeKxc8WHIJI8eIssHHk5VeY7l2BxUPf6PaEdpiC%2FPB&X-Amz-Signature=6d9b31528c0d00b4efb221567f2c27de646bc64f62db60115f9cc16e5cf52f12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
