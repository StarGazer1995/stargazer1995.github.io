---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JWKFVTG%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T164220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDYaCXVzLXdlc3QtMiJIMEYCIQDnw62Kg7cSy2eb8mj6i%2F%2B%2F6IlibBjdOtQ1CXy0F5WzBgIhAMpUQjCBGogLcEXWRjpPxUsVT3Bd6tedlvkldWWg%2BLxGKogECP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBiekykUCy8ACvf%2F0q3APQT3KdQf536EwhERBvMXMNiUEjPT0IMaDPgUldNMOg7zpAZs5QNMi57fE9dkT5EXsi7OicxdEHBdLXHfcbBi4fFUBYPa6iT0PX80Wp594O1BBcnUtG7%2FqZDrrdQgPOpUdaJx2%2Fpme1ulTa0lv93NtzVrFVtNv%2FqOQyCmGWbo0J8fHcZfeGRKY0jI%2FE7uJeEBUqoKi8knl77h4ws%2Fm7z9gYHjyYTPsxHSv3Wt3QACyriwwMpVj6k%2BgKz0MmdIc5bXN4IJPv5ECUXTv3F4%2FrNnyEzrWprohaS8by4bnCNh67%2FZGvzUyYb3rMb1G4UXfOBysv4jjTkACZLAT%2BfSHFeWK8If6w4%2F1Num0kbnjzQ6m%2Bpms2VHgjDCFXPZ5SWcnEfPnCX7B6qGT7WzA1FStpiQ4U2E%2BxZ5AAe%2FOnUYaKK2LHZOvQehf7Y2cy3xEhYuu1Xo5swVyiI2STNVZl%2BDL7siGbX2o1wzgHDjfg0rY5w9bpViM5YJ9IkjLxbDMl1sBrBGJJAdLISsYSwY898ypcf2%2FAjfFhmXHHXVs5qMg5BNaU83o70ZZZQ652zSJTY4DdqxaTnDSv1MqCcykBUxX1PT0lDA5xw1Ewa6iBetyibg9AlPyOoTEW%2BHCsGCb3FjCZjoLQBjqkAaXJS%2F26LymzX1GbodG0bol9PjiH6NTTwhIqSeEXnb7sKdpJJE56DinolD2528EPl4nty8wQ7QIrHcM293bHYvP9lEgKUJPoGF%2BbAC45t7wPhd8eFiuZHGTK7DA43akXzoz9ssUYVjYj0CoLUWTWarILlD2EEuN7z%2BX%2FU6kzshmL6T4RW5esSE34VMQCFgwVlsMMN0vPI%2FjgOCtd56jzfVJzAYVG&X-Amz-Signature=e1607b3754c862ef0a545fe8d9f2a2b23c100752c05f640594d5290759e91a66&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
