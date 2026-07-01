---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6L7TLDO%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T080157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIDbE7hc76uLwQAwCgsrjLwc3PpqFNHq6u1UquEnonDGsAiA8WkZydEvlk4hJatYxc0iMDjLbeF4rX%2BDbwMPhOLLVbiqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaaDxExZiZqlM1wrzKtwD68LqLms%2ByxzQ31zDFDWc1lQ3HObwUUTE2u4zo02KfF4aU2Q0Nv0heG3mV3JEOT5WR0rEYUVWABq1Fe4kFWBaAPSvPuPpKRomKkMVUjEbnNd%2FhuBEAHTvZrAFw2TUZUyZEKVEWeg%2FwoDGI2A%2FzVR5qBCLovWdW3NyZ4yvFRbYtB4KNQkGZyZJrguP%2BDlFCCoC2cPMoEYRYbDa9s4QZpykgLSFf7FBnJKCBqg2NZlm3KIYeIDTGnDFgqx%2FnJV1K9d4bdoDu7hAsyEPOmV6XCnkTasTQjlijX6FX6IJ%2FYMI%2FMXzPKt6n3YQeNfDBgwLBkcipswG2WPNlnPNmsTBPsSZLu7Q9QAhxdsJpv4FulLVdMprO9JAO5yK7ygVRp0RajmoWhxXAYXm140xg%2FdOTKfAUzrQvTjh8q85%2F03BiNQtJEFVo75zhzFUiwa5ImXIZ7YeUL99WlFD2Cxx2pKTTSVzde%2FWCsYEWeTdlaULW3NVyPiJvpEMZH0l7TDcoFWP012oUJMlVxzyzC8fOZmB6kz6svtmCcbrZ%2Fooh6q7riPExeuU2s1psncyI1kDbE3LLltQTr6lxCJDZUG%2FFW2C2hL0RmQ9EmDCsFHTQlK%2FuMGt0D%2FcNNBOeToalSVnCqYwkIyS0gY6pgFjxHNxisTulNxhyV2jYi98b9XCpWJocKG7L%2FAtNoYTmJpvz726SFdbbNEGTub4jlfQoTuLlqnujvAuY1efSvF5sEOZ3QezyMc%2Buy1SqL27hKU0Ic1%2BLvZ4d%2FZIDnbXwAMy9WElDiQh9GWI08SbiU3nCe2Hmduz2rPo%2Be7r2IVfaLJoAhxJ637L%2BKVl%2BApgjQj2%2BeorGUTFwAn3ti1fNf%2FQ2xiidkTS&X-Amz-Signature=96fb195dbd9dfdc779c140f1bcbaec3aef2045818869e090a4c7229e1b72732f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
