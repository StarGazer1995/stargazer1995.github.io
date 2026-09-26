---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LEWNGZI%2F20260926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260926T021738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIG2sagpEUPzyQzGeiaHBU4eojo3LsbLXMsaDKfx19qbSAiEAlh5y18%2BrGgQlgb71LNo271%2B%2BbDAkoF82BV1Llrz0ux4qiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDJwZuY%2B3zuuLt8NuircA8dn0A6a1dEnWXyk3SD3DZbH%2BC%2FJRpKU7LAT%2B%2BzZhob4m%2BaSFihig2lF83Fi%2BsHe26hn0yHtsqjfk3aDFAB16TKWJI4%2BWSwtJxIyhsi9XMETNO8FVnJloQoSasXF5yvnzKA50c6ElExcN7B1sio2HaxUnsCZXsebBGODE79Pa%2F6T0WCLHLE%2FhcRI5WhfPry%2Fja2XiasguR87dCtVtte2epcFjVCBk0rLDNqHIhMPEbWoMOCLTiJlvZX5F12nf6lA7oCRfuRCb%2FMkIiuI8AXuzNSzpK55yYmJh6ZeeGHcEO%2FVwwdt8Mh3a90LRmg3jj1OhrhBIVoOzXc9IFIItwfsHa9ncaSzyIDcm0uUTFq3jNsvzvt8qI8qVVOpXezaFySDIbGjGDoXAMue%2BOYQ0B1TpClifote7%2F%2FOYl%2F8xAA99H7Rt13CXJ3H9gGwrmP%2BUDO%2F05t0ix56bQselen%2BzPG8ZsXEUDaj4R7SDS%2B4QBG8vZJ3A4S1QpfzbjZo%2BtdhJDkPaEBTCGvRex1BuilzcIdKJv0OYzrAQaiqO%2BlocMjuacOqMjTQbbOwbSOxBceUOqB4FBiCvNdSZFkooDKHqVB5FvWIn%2BZtv65u%2Fd5HrUQN28mCHG3xH8USUwGkPoAqMLrL3NUGOqUBb3Xg2QAS6EppTZrbXVAAuXaRdkCtUomfrgE%2BWaefgrqipAZ8F0oGfSxmf0BrkYogK48Js%2BgPGnWAMRteebmINr7E7gKzmYU%2FAkOO5WJeNcmn6DqKkS0EcY1MfgEeAuuwxMBcho%2FNKpQN8PZ%2Bdbz8TnyXSEM6nZlQO1P5CcDkDrYbrTO4iME0ifJRDSRNuALl0J8pofrnmyogbc7dLJJZTApgnlIi&X-Amz-Signature=0d05109c6a6f4d0a8001a88f2851531f604c2eba405df5b24810994700ad36a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
