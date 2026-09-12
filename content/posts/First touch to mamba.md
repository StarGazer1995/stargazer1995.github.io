---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZ27AUC7%2F20260912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260912T143243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXfGn5bfIRrpOD2MPmvIz16luyopCxOoXdCUWcA2UVLgIhAOVX%2BNH2PUJvhk6gadb7RGJ%2FA5IkUvga0ifutMhg%2FVzSKogECLf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCd0B3AnQSp7gSdpAq3AP5co%2B8TJuvgE9kPekBrY4ITC10oGp2P%2FeKbA%2BwQRoVtK%2BZ39lL11JIQCDCh9AbcOfJf8HFFmnwJ8dnLAVPpjpKkEAtIlt5xmAgVRuRBjEiwSt5j4I4925DvSO5kzW8YlNb9bWqNCPvHnO3nNP7vpgmDUZVHWMRYK6ZzPxF69G46ANI4oFnZvNTRzTvuGRh5%2BpQArNa0SQehJaHf0XuxHf6qiDAqFuJP3tUhApbHbGDOa1qAMPk2G22kvWbCJdpMUNvo4YkF6AWFCFK2OoF5gtgwKZ%2B5DoPjPus75Zs75JSwMzH45WS8Kzc9H4F4coST%2BE42t6jYfXZmVVtVi1tyjCrNMA8oww3gNU4PjEnRRsDrvCXrx4%2B7849Z1nJjdFHIzpzPpjZtKJMBfpD2ei1OPL9p6n2SFFQFIUK98JBsVzEHjo5UGj%2F6xRDlAxNKQ2yQ2WCGs9F0HHy31wbOggRkHeTebRUmwWekc%2BBxzBL16v4vO4igWMpNxgBfzskz%2B2ih3Vg3KUfP2xipYc1obpIATaW4qn6fRJpktQ0cYZMp6vriTiWOLp3btpNTQm%2Fb0JbNIuNNkpxaDJ6mcOSid%2BeudlyxWjQED3hnATkGB1Yb2by3s7yywYZzj0UD860GzCGqZXVBjqkARt3aFJV7F0K3PwusKt6p5rMC20ia5q5VJgl5IF7gHLaNsOip2aYl0%2BrXMa%2Bz5TO6Qg857Bap5Ke%2FRojAE0c%2Bxldk3f8LH3n51as4RJbyr0qaMwSj3mIt0AFCMYcPuvtJObSVt7wQvYznYLEE89o9UNEUaft%2BU0jY5K3IzSAKVEJ6cpLWsoNNU3a6wvvIaiNxENWK0C%2BsGZA%2BdKBua7XpmVeaA9A&X-Amz-Signature=8aabd50c8a46a04d585204a50d52ba96eea80abdcd75ab099d61c4623642b380&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
