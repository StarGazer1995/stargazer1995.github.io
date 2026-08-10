---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFYEEGAB%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T004832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEqDeNn5Z6UAT%2F6Pf8anAUPueADrq9ieCNHzmBlywshOAiEAqFDaYRY5De1kaZbi9rvtE3fithns0hb82QZ%2BJ%2F6cxEAqiAQIkf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAFuciD%2Bwczq%2Btzm%2BircA9sqamLO5Mh%2BtTbWpw9uM4lVlB9I%2BaLlFyWB4sJ5MoK53PjSOPWJgIao4Pueka9cs3WSLnnSkhR56DvGxDcUJCEin6XciCIgEzZBG5dmn3Sh9e82RcWXFDNUB1B6oz7miHbYfSTUXLe%2Fu1lT%2BOlhnmihQQSypuVn0q2F%2B1IGmMucMGH4FVnUqZOGYZa5IBLJruDy6yDbwZTyt85vc6rTP5ds8HnjInlWnDCTlFcBF4gMuTdEIWVC6JXsysfwo2wTGwDSFb%2F%2Fa6CYTWow%2Bc7%2B%2BTnW6vtEtZXdEr8sihigHxMjvwC2oGglfR6DrQE%2FpSk2D3sGbXeI1cF1%2BiL7XYt09GjnF21wl%2Bg50kzfiTlxn8zNeJ%2FG%2B0VibMy94%2FbJPIrPyubOkAvId8qZXwaEHGftZBQcg6ggDlhfPmUTz9AEZ05ql5j7A3D79TBLIFIh0ZuCQ%2BDH4Nr1PkJ2mX%2FF3dVOWQCnuYRL0B9UUCnDXY1zKEHBzpu9xbYmWF10ewzhT19I2kt4carOk0HLQb9Q8gwcpw8VYGeDt%2F4wiMZ5NXlMQCRLvWNSeP0xRM9C40tAJfPB2qnM3ZixcEbtGJuG6OuVg1PJ4XVtrwL7Zii7g7Uj%2BHJqNiQzIVWTko29zV%2BqMLKu5NMGOqUBjQjQ7y0JdFFTXzCZ6qkavSl1QYHnIddBx2Zl%2FIJ3Dcp%2BnpeB7Q9qP8fPu8oQHqewnberS7ZwKEiCH%2FCNGWQkF1Fo00hOSw1o41uOW8LJwImXJFWs%2F8OGem%2BmoospyEwzhHTP98%2BgmxEarhBsfXZ5hO5Nl%2FHpnSXC4%2FSDFjgDoPIqXdYBFcGj4YxBcY8L900ictAgwAP5ad89hbDta5i3zVLMWvqM&X-Amz-Signature=01cebc8e89e260d48ab1e5470e22c85c0510e6d1ec2b53d06b8feac052756fcd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
